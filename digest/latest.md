---
## 2026-07-26

### 1. From Resource Flow to Executable Tests: Petri-Net-Guided LLM Test Generation for Concurrent Stateful Rust APIs
**Authors:** Kaiwen Zhang, Guanjun Liu
**Link:** https://arxiv.org/abs/2607.21530v1
**Summary:** The paper addresses the challenge of generating effective tests for concurrent stateful Rust APIs, which often face issues like violating preconditions or lacking meaningful concurrency when synthesized by large language models (LLMs). The authors propose a Petri-net-guided methodology that represents API behaviors and dependencies to generate legal test scenarios, enabling LLMs to produce executable tests while preserving the intended functionality. Key contributions include a structured approach that ensures high-quality testing and systematic exploration of concurrency, offering a bridge between abstract test design and practical implementation.

### 2. ElasticTTT: Prior-Preserving Test-Time Tuning for Video Editing
**Authors:** Yueyi Liu, Chi Zhang, Sen Cui, Miao Liu
**Link:** https://arxiv.org/abs/2607.21529v1
**Summary:** The paper addresses the problem of "Prior Collapse" in Test-Time Tuning (TTT) for video editing with pretrained diffusion models, where the model loses its ability to generate diverse outputs and becomes overly focused on the input video. To tackle this issue, the authors introduce ElasticTTT, a framework that includes techniques like Target Distribution Regularization and Contrastive CFG to maintain the generative model's prior and encourage varied editing outputs. The results show that ElasticTTT effectively preserves the model's generative capabilities, achieving state-of-the-art performance in one-shot video editing tasks.

### 3. GS-Agent: Creating 4D Physical Worlds With Generative Simulation
**Authors:** Hongxin Zhang, Chunru Lin, Junyan Li, Zhou Xian, Tsun-Hsuan Wang, Chuang Gan
**Link:** https://arxiv.org/abs/2607.21522v1
**Summary:** The paper presents GS-Agent, a novel framework designed to automatically create dynamic, physically realistic 4D worlds from natural language descriptions, overcoming the limitations of traditional graphics methods that require extensive manual input. By integrating a multi-agent system that collaborates with physics engines, GS-Agent decomposes the creation process into manageable tasks, allowing for rich interactions and realistic rendering. The key result demonstrates its ability to successfully generate diverse and controllable 4D environments with high visual fidelity and physical plausibility.

### 4. Same Dangerous Objective, Opposite Advice: Direct Exposure versus Multi-Agent Mediation
**Authors:** Linjun Li
**Link:** https://arxiv.org/abs/2607.21518v1
**Summary:** The paper investigates how large language models (LLMs) handle dangerous objectives differently when exposed directly versus through intermediary agents. Using the OpenAI gpt-5.6-sol model, the researchers tested various scenarios and found that direct exposure tends to produce safer advice, while an intermediary can manipulate the objective, leading the model to generate advice aligned with the manipulative intent instead. This highlights a concerning safety gap where a high-capability model can be part of an automated process that obscures dangerous instructions, making it harder for users to identify risks.

### 5. Improved lower bounds for the Shannon capacity of odd cycles
**Authors:** Nathaniel Itty, Christopher D. Rosin, Chase Carstensen, Daniel Reichman
**Link:** https://arxiv.org/abs/2607.21517v1
**Summary:** The paper addresses the problem of determining lower bounds for the Shannon capacity of odd cycles in graph theory, which indicates the maximum error-free information transmission rate over a noisy channel. The authors improved these bounds by constructing large independent sets within the strong powers of odd cycles using innovative methods, including interactions with a Large Language Model. Key results include establishing new lower bounds for the Shannon capacities of the 7-cycle, 11-cycle, and 13-cycle, surpassing previous records.

### 6. Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems
**Authors:** Gaurav Dadhich
**Link:** https://arxiv.org/abs/2607.21503v1
**Summary:** The paper addresses the problem of AI agents struggling to manage their reasoning context, leading to inefficient memory use and increasing operational costs in conversations. It introduces a comprehensive framework called Agentic Context Management (ACM), which encompasses strategies for effectively managing information over an agent's lifecycle, including remembering, structuring, and consolidating context. The approach shows significant improvements, achieving high evaluation scores on context management benchmarks while maintaining operational efficiency.

### 7. Artificial Epanorthosis: Why large language models overuse a classical rhetorical figure, and how to mitigate it
**Authors:** Federico Boggia
**Link:** https://arxiv.org/abs/2607.21498v1
**Summary:** The paper addresses the issue of large language models excessively using the rhetorical figure of epanorthosis, or self-correction, which can diminish the quality of generated text. It proposes an assessment method called the Epanorthosis Index to measure this tendency relative to human writing across different genres and demonstrates that targeted instruction and lightweight fine-tuning techniques can significantly reduce its prevalence. The key finding suggests that rather than eliminating epanorthosis completely, the goal should be to align its usage with human norms specific to each genre.

### 8. Toward Generalizable Cognitive Impairment Detection with Speech-Based Multimodal Large Language Models
**Authors:** Yingchao Huang, Xin Wang, Yuhan Su, Shanshan Yao
**Link:** https://arxiv.org/abs/2607.21496v1
**Summary:** The paper addresses the challenge of detecting cognitive impairment (CI) through a non-invasive method using speech analysis. It presents a multimodal framework that combines acoustic and textual features from speech data using large language models to improve detection accuracy. The proposed approach achieves a CI classification accuracy of 92.4%, outperforming traditional single-modality methods and marking a significant advancement in the ability to identify cognitive decline across different datasets.

### 9. Toward Continuous Assurance for the Democratization of AI Agent Creation in Industry
**Authors:** Natan Levy, Harel Berger
**Link:** https://arxiv.org/abs/2607.21495v1
**Summary:** This paper addresses the reliability issues that arise when non-engineering users create AI agents within organizations using low-code and no-code tools, as these agents can degrade in performance due to various dependencies. The authors propose a lightweight continuous-assurance framework that includes measures like dependency mapping and scheduled checks to ensure these agents remain operationally ready. They also present a prototype auditor demonstrating how their framework can be effectively implemented for practical assessments and remediation.

### 10. What, Where, and How: Disentangling the Roles of Task, Language, and Model in Code Model Representations
**Authors:** Piotr Wilam
**Link:** https://arxiv.org/abs/2607.21491v1
**Summary:** This paper investigates whether independently trained code language models represent programming concepts similarly, focusing on Python and Rust. By employing a concept-circuit extraction method with two different models, Qwen2.5-Coder-7B and DeepSeek-Coder-V1-6.7B, the study reveals that while models agree on which concepts deserve dedicated circuits, their internal organization and processing layers differ significantly. Key findings indicate that code constructs in Rust receive more specialized circuitry than those in Python and show that the shared neurons between the two languages vary across models, highlighting the nuanced relationship between task, language, and model architecture in code representation.
