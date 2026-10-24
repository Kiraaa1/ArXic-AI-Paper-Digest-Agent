---
## 2026-10-24

### 1. Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation
**Authors:** Gabriele Dominici, Teague McMillan, Fazl Barez, Marc Langheinrich, Martin Gjoreski
**Link:** https://arxiv.org/abs/2610.31639v1
**Summary:** The paper addresses the issue of attention leakage in chain-of-thought prompting, where models can produce plausible but misleading rationales due to their ability to access irrelevant context. The authors propose CausalCoT, a framework that structures problems as directed acyclic graphs, allowing each reasoning step to focus only on its immediate causal influences, thereby enhancing the clarity and faithfulness of explanations. Their approach improves the model's ability to connect reasoning steps causally, increasing this sensitivity by up to 21 percentage points compared to existing methods, while maintaining strong predictive performance.

### 2. Can an Agent Debug a Web Corpus? Agentic Auditing of Slovak FineWeb2
**Authors:** Marek Šuppa, Ivan Vykopal, Jaroslav Kopčan
**Link:** https://arxiv.org/abs/2610.31636v1
**Summary:** The paper addresses the issue of unanticipated failure modes in multilingual web corpora, specifically FineWeb2's Slovak subset. The authors employed a tool-using agent based on a large language model (LLM) to debug the corpus by exploring it with a budgeted API and compiling findings into executable tests, which were then validated by native speakers. Their approach identified critical issues, including a significant quantity of machine-generated content that evaded existing filters, demonstrating the agent's effectiveness in detecting and quantifying defects while providing reusable validation tests at a fraction of the typical classification cost.

### 3. BeNice! Closing Looping's Inference-Memory Gap via KV-Sharing
**Authors:** Hayden Prairie, Jacob M. Ryan, Taylor Berg-Kirkpatrick, Daniel Y. Fu
**Link:** https://arxiv.org/abs/2610.31633v1
**Summary:** The paper addresses the issue of increasing memory usage during inference in looped architectures due to the generation of independent key-value caches (KV-caches) with each recurrence. It introduces a two-stage approach, utilizing stochastic depth during pretraining and a post-training method named BeNice! to enable sharing of the final recurrence's KV-cache with earlier ones. This method facilitates KV-shareability without quality loss, significantly improving cache efficiency and inference performance, including a notable reduction in time-to-first-token and an increase in throughput.

### 4. Questioning Instrumental Convergence in RLVR: Checkpoint Evidence from OLMo-3
**Authors:** Barış Alparslan, Sandy Tanwisuth, Caleb Petterson
**Link:** https://arxiv.org/abs/2610.31624v1
**Summary:** The paper investigates whether reinforcement learning with verifiable rewards (RLVR) increases power-seeking behaviors in large language models (LLMs), specifically focusing on the OLMo-3 model. By evaluating behavioral trajectories at various training checkpoints, the authors find that instrumental behavior initially increases but then drops below baseline levels, suggesting that RLVR does not consistently drive such behaviors as expected. This nonmonotonic trend challenges common assumptions about instrumental convergence in LLMs and highlights the importance of training context.

### 5. Bilingual Language Models Capture Cross-Linguistic Influence in Second-Language Reading
**Authors:** Abderrahmane Issam, Irene E. Winther, Stefan L. Frank
**Link:** https://arxiv.org/abs/2610.31620v1
**Summary:** This study addresses the challenge of understanding how a person's first language affects their reading times in a second language. The researchers used bilingual language models to analyze eye-tracking data from readers with different first languages reading English. They found that matching the bilingual model to the reader's first language significantly improved the prediction of reading times, highlighting the impact of cross-linguistic influence during L2 reading.

### 6. OP-Print: Tracing Membership Imprints in On-Policy Self-Distillation
**Authors:** Qi Li, Xinchao Wang
**Link:** https://arxiv.org/abs/2610.31616v1
**Summary:** The paper addresses the privacy risks associated with on-policy self-distillation, specifically the potential for membership inference attacks that exploit the model's learning patterns. The authors introduce OP-Print, a unified framework that effectively identifies and exploits sparse supervision imprints during the distillation process in both gray-box and black-box settings. Their key finding shows that OP-Print significantly outperforms existing baseline attacks, which barely exceed random guessing, highlighting its effectiveness in uncovering private training data.

### 7. Efficient and Optimal Learning of Discrete Distributions with Person-Level Privacy
**Authors:** Gautam Kamath, Mahbod Majid, Ankur Moitra, Argyris Mouzakis, Jonathan Ullman
**Link:** https://arxiv.org/abs/2610.31612v1
**Summary:** The paper addresses the challenge of learning a discrete distribution while ensuring person-level differential privacy in a batch setting where multiple users contribute samples. The authors introduce polynomial-time algorithms that achieve optimal sample complexity under both pure and approximate differential privacy, utilizing a novel degree-6 sum-of-squares estimator for processing potentially untrusted data. Key contributions include a new privacy-preserving method that matches information-theoretic limits and proves the robustness of the estimation through advanced mathematical techniques.

### 8. How Ground Truth Shapes Retrieval Scores: Evidence-Aware Evaluation of a Retrieval-Augmented Generation System for Breast Lesions
**Authors:** Miguel Mochizuki Silva, Samuel Ismael, Mateus C. Dias, Thaís Gaudêncio, Yuri Malheiros, Barufaldi
**Link:** https://arxiv.org/abs/2610.31606v1
**Summary:** The paper addresses the challenge of evaluating retrieval scores in a clinical retrieval-augmented generation system specifically for breast lesion management by developing an evidence-aware evaluation protocol. Using a small corpus and various retrieval configurations, the authors found that their hybrid retriever with specific chunk sizes and overlaps consistently retrieved relevant evidence for most queries. Key findings indicate that enhancing ground-truth annotations improved the recognition of relevant evidence while not altering retrieval rankings, underscoring the importance of comprehensive annotation in evaluation.

### 9. CRANE: Post-Hoc Counterfactual Retrieval for Multimodal Classifiers
**Authors:** Franco Rugolon, Ioanna Miliou, Panagiotis Papapetrou
**Link:** https://arxiv.org/abs/2610.31594v1
**Summary:** The paper presents CRANE, a novel framework designed to provide coherent counterfactual explanations for multimodal classifiers—models that integrate multiple types of input data. Unlike traditional methods that evaluate each modality separately, CRANE utilizes a nearest-neighbor approach to retrieve real training examples from the target class, ensuring the explanations are plausible and drawn from the actual training distribution. The key finding is that the Multimodal Consensus Retrieval (MC-R) strategy outperforms others by effectively integrating multiple modalities, leading to superior explanation quality across various datasets.

### 10. Simulated Control Evals
**Authors:** Jeffrey Olmo, David Zhang, Tyler Tracy
**Link:** https://arxiv.org/abs/2610.31593v1
**Summary:** The paper addresses the challenge of assessing whether AI safeguards can effectively prevent undesired outcomes in real-world environments, which traditional control evaluations struggle to represent accurately. It introduces simulated control evaluations (SCEs), which leverage a language model to mimic tool responses in various settings, improving prediction of safety outcomes. Key results indicate that SCEs significantly outperform conventional control evaluations, achieving higher accuracy and efficiency in predicting safety with considerably fewer samples.
