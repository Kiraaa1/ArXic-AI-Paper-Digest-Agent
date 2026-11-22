---
## 2026-11-22

### 1. The Geometry of Lies: Knowledge and Persona Directions for Detecting Deception in Large Language Models
**Authors:** Md. Abdullah Al Zami, Suraiya Shanaz, Mahdi Hasan, Shoaib Ahmed Dipu, Farig Yousuf Sadeque, Md. Sabbir Ahmed
**Link:** https://arxiv.org/abs/2611.26545v1
**Summary:** The paper investigates how to detect deception in large language models (LLMs) by using persona directions derived from role-playing scenarios. By expanding an existing persona bank to include roles that deny knowledge alongside their honest counterparts, the authors demonstrate that these persona directions can more effectively rank deceptive responses compared to traditional linear probes. The key finding is that while persona directions show promise in distinguishing lies from honest denials, their effectiveness varies across different models and tasks, especially on lies about knowledge where wording similarities complicate detection.

### 2. AURA: AUdio-dRiven streaming Avatar
**Authors:** Nathaniel Cohen, Nicolas Dufour, Amélie Royer, Alasdair Newson, Patrick Pérez
**Link:** https://arxiv.org/abs/2611.26540v1
**Summary:** AURA addresses the challenge of generating realistic talking-head videos for streaming applications, which require low-latency and online generation. It introduces a novel method that allows video to be produced in real-time using a rolling cache of audio, significantly speeding up the process. The key contribution is that AURA's smaller model operates 23 times faster than its teacher model while achieving similar video quality, and both models are available for further research.

### 3. LLM GerryMandering: Separating Interactions from Additive Effects in LLM Audits
**Authors:** George Rahul, Ronit Jahilal, Bhaskara Hanuma Vedula, Ponnurangam Kumaraguru, Pushkar Shukla
**Link:** https://arxiv.org/abs/2611.26538v1
**Summary:** The paper addresses the challenge of accurately auditing intersectional bias in language models, where individuals with multiple marginalized identities may be treated unfairly based on their combined attributes rather than individually. The authors propose a new method called ADDIS, which uses an additive modeling approach to identify genuine interactions between attributes more effectively, significantly reducing false positives in audits. Their results show that while many flagged biases can be attributed to single-attribute effects, ADDIS successfully uncovers a core of true interactions that traditional methods miss.

### 4. Cost-Aware Agentic Feature Optimization System for Fleet-Scale Ranking Models
**Authors:** Chang Yang, Yao Xuan, Wendan Yan, Nhat Le, Jiang Liu, Longhao Jin, Zhen Peggy Yao, Alireza Vahdatpour, Djordje Gligorijevic
**Link:** https://arxiv.org/abs/2611.26531v1
**Summary:** The paper addresses the challenge of optimizing feature selection for large fleets of ranking models used by web platforms, all while adhering to resource constraints such as cost and throughput. The authors developed an end-to-end system that utilizes large language model (LLM) agents to propose feature hypotheses, which are experimentally validated, and employs a combinatorial approach to rank and blend feature selections. The system demonstrated a 0.31% improvement in feature diversity without exceeding budgetary limits, resulting in a 0.20% enhancement in a primary online performance metric during A/B testing.

### 5. Backtracking Agent Applications Security Incidents
**Authors:** Yicheng Cai, Taegyu Kim, Peng Liu
**Link:** https://arxiv.org/abs/2611.26525v1
**Summary:** The paper addresses the challenge of identifying compromise entry points (CEPs) in agent applications after a security incident, where traditional logs often lead to a semantic gap between high-level agent functionalities and low-level code execution. The authors present Origin, a backtracking tool that utilizes a cross-layer dependency graph to connect these layers and identify CEPs more effectively, allowing for targeted queries. Their case studies demonstrate that Origin successfully identifies all CEPs in various agent application scenarios, showcasing its effectiveness over existing tools.

### 6. Deterministic Temporal Embedding for Calcium Imaging Trace Extraction
**Authors:** Qi Gao, Julius Beichert, Miriam Ratliff, Karl Rohr
**Link:** https://arxiv.org/abs/2611.26522v1
**Summary:** The paper addresses the challenge of accurately extracting calcium-dependent fluorescence traces from calcium imaging data by identifying pixels linked to the same cellular activity. It introduces a deterministic temporal embedding framework that creates a low-dimensional representation of the data, enabling the separation of temporally coherent sources into distinct spatial regions. The method shows strong performance in recovering complex, irregular cellular sources from both synthetic and real imaging data without needing explicit prior knowledge about cellular shapes.

### 7. The Window Lever: Longer Observation Windows Outweigh the Observed Effects of Data, Capacity, and Architecture in Customer Behavior Forecasting
**Authors:** Tara Sowrirajan, Yanqiao Wang
**Link:** https://arxiv.org/abs/2611.26521v1
**Summary:** This paper addresses the challenge of accurately forecasting customer behavior over long time horizons. The authors conducted experiments demonstrating that extending the observation window—i.e., the historical data used for predictions—from 8 to 16 weeks significantly improves forecasting accuracy, more so than increasing the amount of data, model capacity, or using newer architectures. The key finding indicates that longer observation windows consistently enhance predictive performance across multiple datasets, underscoring the importance of historical context in forecasting.

### 8. Simple Private Noisy SGD is Minimax-Optimal under Population Strong Convexity
**Authors:** Valentin Roth, Marco Avella Medina
**Link:** https://arxiv.org/abs/2611.26515v1
**Summary:** The paper addresses the question of whether a simple differentially private variant of stochastic gradient descent (SGD), known as Noisy SGD, can achieve optimal performance in estimating parameters for strongly convex losses, a common scenario in machine learning. The authors demonstrate that Noisy SGD can match the best possible error bounds for parameter estimation, particularly in private logistic regression, thus proving its minimax-optimality without the complicating factors present in previous results. This contribution provides a more efficient and theoretically sound approach for ensuring privacy in machine learning applications.

### 9. Hybrid Retrieval for Government Scheme Search in English and Marathi
**Authors:** Aishwarya Gunjal, Kanchan Khemnar, Pawan Poojary, Pranav Kulkarni, Raviraj Joshi, Manish Khodaskar
**Link:** https://arxiv.org/abs/2611.26514v1
**Summary:** The paper addresses the challenge of retrieving government schemes in Maharashtra that match citizens' needs across English and Marathi languages. The authors developed a bilingual search system that combines traditional BM25 retrieval with sentence-embedding similarity to enhance search results. Their evaluation shows that this hybrid approach improves the mean reciprocal rank and precision over dense retrieval methods while maintaining strong recall, demonstrating the effectiveness of integrating both lexical and semantic signals in bilingual information retrieval.

### 10. AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher
**Authors:** Guoxin Chen, Shuang Sun, Fanzhe Meng, Xinyu Tang, Ruihua Song, Wayne Xin Zhao
**Link:** https://arxiv.org/abs/2611.26510v1
**Summary:** The paper addresses the issue of improving the effectiveness of teacher models in reinforcement learning, specifically by refining their behaviors during post-training. The authors introduce AutoMaster, an autonomous system that fine-tunes models using a technique called Skill-Guided Fine-Tuning, which leverages natural-language skills to identify and reinforce desirable behaviors. The key finding is that this approach significantly enhances model performance by 1.42-8.99 percentage points over traditional methods, highlighting the importance of integrating skill context during training.
