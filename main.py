"""Daily ArXiv digest orchestrator.

Run from the GitHub Action (or locally) to:
  1. Fetch the most recent ArXiv submissions in the configured categories.
  2. Drop any papers we have already digested on a previous day.
  3. Summarise up to MAX_PAPERS of the remainder with OpenAI.
  4. Append the result to digest/digest.md and overwrite digest/latest.md.

Exit codes:
  0 - success, or a benign skip (no new papers)
  1 - unexpected fatal error
  2 - ArXiv temporarily unavailable; the GitHub Action queues an automatic
      retry two hours later
"""

from __future__ import annotations

import logging
import os
import sys
from datetime import datetime, timezone

from dotenv import load_dotenv
from openai import OpenAI

import config
from src.fetcher import ArxivUnavailableError, fetch_recent_papers
from src.models import Digest
from src.summariser import summarise_papers
from src.writer import append_to_digest, read_seen_arxiv_ids, render_digest, write_latest

logger = logging.getLogger("arxiv_digest")


def _configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
    )


def _require_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Add it as a GitHub Actions secret "
            "or to your local .env file."
        )
    return api_key


def run() -> int:
    """Main entry point. Returns the desired process exit code."""
    load_dotenv()
    _configure_logging()

    api_key = _require_api_key()

    now = datetime.now(timezone.utc)
    logger.info("Starting digest run at %s", now.isoformat())

    try:
        fetched = fetch_recent_papers(
            categories=config.CATEGORIES,
            page_size=config.ARXIV_PAGE_SIZE,
            api_url=config.ARXIV_API_URL,
        )
    except ArxivUnavailableError as exc:
        logger.warning(
            "ArXiv is temporarily unavailable (%s); exiting with code 2 so "
            "the GitHub Action can queue an automatic retry.",
            exc,
        )
        return 2

    if not fetched:
        logger.info(
            "ArXiv returned no parsable papers for categories %s, exiting "
            "cleanly without writing.",
            config.CATEGORIES,
        )
        return 0

    seen_ids = read_seen_arxiv_ids(config.DIGEST_FILE)
    fresh = [p for p in fetched if p.arxiv_id not in seen_ids]
    logger.info(
        "Filtered %d fetched papers against %d already-digested ids -> %d new",
        len(fetched),
        len(seen_ids),
        len(fresh),
    )

    if not fresh:
        logger.info(
            "All %d most-recent ArXiv papers have already been digested, "
            "exiting cleanly without writing.",
            len(fetched),
        )
        return 0

    papers = fresh[: config.MAX_PAPERS]
    logger.info("Summarising %d papers with model %s", len(papers), config.OPENAI_MODEL)

    client = OpenAI(api_key=api_key)
    entries = summarise_papers(
        papers,
        client=client,
        model=config.OPENAI_MODEL,
        max_tokens=config.OPENAI_MAX_TOKENS,
    )

    if not entries:
        logger.warning(
            "All %d papers failed to summarise, exiting without writing.",
            len(papers),
        )
        return 0

    digest = Digest(digest_date=now.date(), entries=entries)
    rendered = render_digest(digest)

    append_to_digest(config.DIGEST_FILE, rendered)
    write_latest(config.LATEST_FILE, rendered)

    logger.info(
        "Digest complete: %d/%d papers summarised for %s",
        len(entries),
        len(papers),
        digest.digest_date.isoformat(),
    )
    return 0


def main() -> None:
    try:
        sys.exit(run())
    except Exception:
        logger.exception("Fatal error during digest run")
        sys.exit(1)


if __name__ == "__main__":
    main()
