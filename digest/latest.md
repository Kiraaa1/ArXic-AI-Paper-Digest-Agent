---
## 2026-06-20

### 1. LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents
**Authors:** Md Nayem Uddin, Amir Saeidi, Eduardo Blanco, Chitta Baral
**Link:** https://arxiv.org/abs/2606.20529v1
**Summary:** The paper presents LedgerAgent, a method for improving tool-calling agents in customer service by explicitly maintaining task states in a separate ledger instead of relying on implicit state management through prompts. This approach helps ensure that agents make decisions based on accurate and up-to-date information while adhering to domain policies. The key finding is that LedgerAgent significantly enhances performance, particularly in consistency across multiple trials, compared to standard prompt-based methods.

### 2. StylisticBias: A Few Human Visual Cues Drive Most Social Biases in MLLMs
**Authors:** Shaghayegh Kolli, Timo Cavelius, Nafiseh Nikeghbal, Samantha Dalal, Jana Diesner
**Link:** https://arxiv.org/abs/2606.20527v1
**Summary:** The paper addresses the challenge of understanding how visual cues influence social biases in multimodal large language models (MLLMs). By creating a benchmark called StylisticBias, the authors generated a dataset of 25,000 images with controlled variations in visual attributes while keeping identity constant, allowing for precise measurement of how these attributes affect model judgments. The key finding is that a small number of visual traits—particularly related to age, body type, and fashion—account for the majority of observed biases, emphasizing the importance of specific cues in shaping MLLM responses.

### 3. DeepSWIP: Quotient-WMC Counterfactuals for Neural Probabilistic Logic Programs
**Authors:** Saimun Habib, Vaishak Belle, Fengxiang He
**Link:** https://arxiv.org/abs/2606.20526v1
**Summary:** The paper presents DeepSWIP, a method that enhances the DeepProbLog framework by enabling counterfactual reasoning through a single-world causal semantics. This is achieved by transforming neural predicates into standard ProbLog choices and applying weighted model counting to compute counterfactuals efficiently. The key contribution is a significant inference speedup demonstrated in experiments, along with improved intervention calibration and reduced bias in estimations, particularly in the context of neural probabilistic logic programs.

### 4. SARLO-80: Worldwide Slant SAR Language Optic Dataset 80cm
**Authors:** Solène Debuysère, Nicolas Trouvé, Nathan Letheule, Elise Colin, Georgia Channing
**Link:** https://arxiv.org/abs/2606.20523v1
**Summary:** The paper introduces SARLO-80, a new dataset designed to enhance multimodal learning by providing high-resolution synthetic aperture radar (SAR) imagery, aligned optical images, and natural language descriptions. The dataset consists of 119,566 triplets derived from 2,500 scenes worldwide, standardized to an 80cm slant-range grid for precise pixel-level alignment. This contribution addresses the lack of high-quality datasets in the SAR domain and enables better cross-modal retrieval and conditional generation, supporting advanced research in SAR-optical relationships.

### 5. Sovereign Execution Brokers: Enforcing Certificate-Bound Authority in Agentic Control Planes
**Authors:** Jun He, Deying Yu
**Link:** https://arxiv.org/abs/2606.20520v1
**Summary:** The paper addresses the challenge of securely managing autonomous agents in cloud environments, ensuring that authority for making changes does not reside with unpredictable reasoning processes. It introduces the Sovereign Execution Broker (SEB), which enforces certified action authority by validating and recording actions against established rules before execution. The key contribution is a prototype implementation that effectively separates the processes of proposing, admitting, and executing actions, enhancing security and auditability in agent-based control systems.

### 6. FlowEdit: Associative Memory for Lifelong Pronunciation Adaptation in Flow-Matching TTS
**Authors:** Harshit Singh, Ayush Pratap Singh, Nityanand Mathur
**Link:** https://arxiv.org/abs/2606.20518v1
**Summary:** The paper presents FlowEdit, a framework designed to address the persistent pronunciation errors in text-to-speech systems, particularly for out-of-vocabulary proper nouns. Instead of retraining the model, FlowEdit learns corrections as latent edits and stores them in a neural memory system, allowing for efficient and adaptive pronunciation adjustments. The approach significantly reduces pronunciation errors by 92.7% while maintaining the overall quality of speech synthesis, with corrections completed in about 15 seconds on a single GPU.

### 7. Multi-LCB: Extending LiveCodeBench to Multiple Programming Languages
**Authors:** Maria Ivanova, Pavel Zadorozhny, Rodion Levichev, Ivan Petrov, Adamenko Pavel, Ivan Lopatin, Alexey Kutalev, Dmitrii Babaev
**Link:** https://arxiv.org/abs/2606.20517v1
**Summary:** The paper introduces Multi-LCB, a new benchmark that extends the LiveCodeBench (LCB) framework for evaluating large language models (LLMs) on code generation tasks across twelve programming languages, addressing LCB's limitation of only supporting Python. By transforming Python tasks into equivalent tasks in other languages while maintaining strict contamination controls, Multi-LCB enables robust cross-language assessments of LLM performance. The evaluation of 24 LLMs revealed issues like Python overfitting and significant performance differences across languages, highlighting gaps in LLM capabilities and establishing Multi-LCB as a valuable tool for multi-language code evaluation.

### 8. Probe-and-Refine Tuning of Repository Guidance for Coding Agents
**Authors:** Asa Shepard, Jeannie Albrecht
**Link:** https://arxiv.org/abs/2606.20512v1
**Summary:** The paper addresses the challenge of providing effective operational guidance for large language model (LLM)-based coding agents, which is crucial for navigating code repositories. The authors propose a novel approach called "probe-and-refine tuning," where synthetic bug-fix probes are used to iteratively improve the guidance files without needing direct agent interaction. Their key finding is that this refined guidance significantly increases the agent's ability to locate relevant files for code changes, achieving a mean resolve rate of 33% compared to lower rates for static or unguided approaches.

### 9. Efficient and Sound Probabilistic Verification for AI Agents
**Authors:** Alaia Solko-Breslin, Pramod Kaushik Mudrakarta, Mihai Christodorescu, Somesh Jha, Krishnamurthy Dj Dvijotham
**Link:** https://arxiv.org/abs/2606.20510v1
**Summary:** The paper addresses the challenge of verifying AI agents' compliance with security policies in uncertain environments, which often involves probabilistic behaviors. The authors introduce a new framework that uses distributionally robust optimization to calculate reliable upper bounds on the likelihood of policy violations without needing to assume independence between various factors. Their approach is shown to outperform existing methods in terms of performance and enhances the balance between security and utility in practical applications.

### 10. What Do Safety-Aligned LLMs Learn From Mixed Compliance Demonstrations?
**Authors:** Sihui Dai, Mann Patel
**Link:** https://arxiv.org/abs/2606.20508v1
**Summary:** The paper investigates how language models interpret and respond to a mix of benign and harmful compliance demonstrations, exploring the effects of demonstration content and ordering on harmful compliance. By testing four different models, the authors find that benign and harmful demonstrations have varied effects on compliance, depending on the model and its training, particularly highlighting the significance of the preference optimization training phase. This research provides insights into the dynamics of how models learn from mixed demonstrations, moving beyond simply showing that harmful behaviors can be triggered to understanding the underlying mechanisms.
