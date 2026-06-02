"""Tuneable configuration for the ArXiv digest bot.

Anything a user might reasonably want to change without touching application
logic lives in this module. Values can also be overridden via environment
variables for ad-hoc local runs.
"""

from __future__ import annotations

import os
from pathlib import Path


def _env_int(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None or raw.strip() == "":
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _env_list(name: str, default: list[str]) -> list[str]:
    raw = os.getenv(name)
    if raw is None or raw.strip() == "":
        return default
    return [item.strip() for item in raw.split(",") if item.strip()]


# ArXiv categories to monitor. See https://arxiv.org/category_taxonomy
CATEGORIES: list[str] = _env_list(
    "ARXIV_CATEGORIES", ["cs.AI", "cs.LG", "cs.CL"]
)

# Cap on summaries written per run; controls cost and noise.
MAX_PAPERS: int = _env_int("MAX_PAPERS", 10)

# How many results to ask ArXiv for. We pull more than MAX_PAPERS so that,
# after deduplication against papers we have already digested, we still
# have a healthy pool to choose from.
ARXIV_PAGE_SIZE: int = _env_int("ARXIV_PAGE_SIZE", 50)

# ArXiv API endpoint. Use https; the http endpoint redirects.
ARXIV_API_URL: str = "https://export.arxiv.org/api/query"

# OpenAI model used for summarisation. gpt-4o-mini is cheap and fast and
# perfectly adequate for 2-3 sentence summaries.
OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# Max output tokens for a single summary.
OPENAI_MAX_TOKENS: int = _env_int("OPENAI_MAX_TOKENS", 300)

# Filesystem layout.
PROJECT_ROOT: Path = Path(__file__).resolve().parent
DIGEST_DIR: Path = PROJECT_ROOT / "digest"
DIGEST_FILE: Path = DIGEST_DIR / "digest.md"
LATEST_FILE: Path = DIGEST_DIR / "latest.md"
# Written by the GitHub Action when ArXiv is rate-limited; triggers the 11:00
# UTC retry run. Contains a single UTC date line (YYYY-MM-DD).
RETRY_PENDING_FILE: Path = DIGEST_DIR / ".arxiv-retry-pending"
