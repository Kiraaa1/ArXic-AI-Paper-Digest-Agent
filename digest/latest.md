---
## 2026-08-08

### 1. RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual Reasoning Transfer
**Authors:** Xinye Wang, Junxiao Liu, Shujian Huang
**Link:** https://arxiv.org/abs/2608.06347v1
**Summary:** The paper addresses the challenge of improving multilingual reasoning abilities in large language models, especially for languages with fewer resources. It introduces RP-OPSD, a method that enhances on-policy self-distillation by focusing on critical reasoning decisions, referred to as reasoning pivots, to guide the learning process. The key finding is that this approach significantly outperforms existing multilingual reasoning methods across various languages and difficulty levels, effectively prioritizing important reasoning signals over mere text generation.

### 2. TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajectories
**Authors:** Yunjia Qi, Zehua Yin, Xintong Shi, Hao Peng, Songyuanyi Lu, Yixian Liu, Richeng Xuan, Yuhong Liu, Zhichao Hu, Xiaozhi Wang, Lei Hou, Bin Xu, Juanzi Li
**Link:** https://arxiv.org/abs/2608.06346v1
**Summary:** The paper addresses the challenge of identifying the root causes of failures in long trajectories of Large Language Model (LLM)-based agents, which often suffer from cascading errors. The authors present TrajDebug, a framework that uses a multi-granular approach to trace errors and their impacts effectively. Their experiments show that TrajDebug outperforms existing methods in error detection, providing valuable insights for improving agent performance.

### 3. Scalable estimation of VARMA models
**Authors:** Daniel Paulin, Victor Elvira
**Link:** https://arxiv.org/abs/2608.06340v1
**Summary:** This paper addresses the challenges of estimating vector autoregressive moving-average (VARMA) models, which are typically impractical for large datasets due to computational barriers and complex likelihood evaluations. The authors introduce a new estimation framework that reparametrizes the model to ensure stability and relies on fixed-size statistics for efficient optimization, enabling faster calculations regardless of dataset size. Their empirical results show that this approach yields accurate forecasts comparable to traditional methods, making VARMA viable for larger applications where previously only simpler models were used.

### 4. Optimal Rates for Learning with Monotone Adversaries
**Authors:** Anay Mehrotra
**Link:** https://arxiv.org/abs/2608.06337v1
**Summary:** This paper investigates the impact of monotone adversaries on the learning performance of machine learning models when they introduce additional labeled examples based on a clean sample. The authors demonstrate that, contrary to classical expectations, the incorporation of these examples can increase the expected error by a logarithmic factor for classes with VC dimension greater than one. Their findings reveal that the optimal learning rates are inherently affected by the adversarial context, particularly exhibiting a more complex behavior than traditional PAC learning.

### 5. Tytan: Interactive Neurosymbolic Construction of Analytic Semantic Schemas from Relational Data
**Authors:** Donna Hooshmand, Shubham Shahi, Cameron Barrie, Abhratanu Dutta, Marko Sterbentz, Harper Pack, Kristian J. Hammond
**Link:** https://arxiv.org/abs/2608.06331v1
**Summary:** The paper introduces TYTAN, a system that automates the creation of analytic semantic schemas from relational databases, addressing the challenges of manual schema construction that can hinder data analysis scalability. TYTAN merges symbolic data analysis with language model-based inference to accurately propose entities and roles, asking users clarifying questions when needed. The key result demonstrates that TYTAN achieves 100% coverage of important schema elements, correct retrieval execution, and high accuracy in semantic role assignment across tested databases.

### 6. Benchmarking the Benchmarks: Evaluating Benchmarks for Conversational Agents
**Authors:** Noam Koren, Roy Bar-Haim, Abigail Goldsteen
**Link:** https://arxiv.org/abs/2608.06329v1
**Summary:** The paper addresses the issue of inconsistent and low-quality benchmarks used to evaluate task-oriented conversational agents. The authors propose a framework that utilizes large language model (LLM) judges to assess various aspects of benchmark quality, such as consistency and complexity. Their key finding is that this framework effectively distinguishes between different levels of benchmark quality, providing valuable diagnostics and enhancing the evaluation process for both synthetic and manually curated benchmarks.

### 7. Benchmarking and Enhancing LLMs for Rule-Intensive Review of National Standard Documents
**Authors:** Tao Wang, Qihao Yang, Rongjiao Liang, Lianghong Lin, Haitao Wang, Xinyu Cao, Tianyong Hao
**Link:** https://arxiv.org/abs/2608.06312v1
**Summary:** The paper addresses the challenge of using large language models (LLMs) for the structured review of national standard documents, which are complex and governed by specific rules. To tackle this, the authors developed GB/T-Bench, a benchmark for evaluating LLM performance in this context, along with GB/T-Reviewer, a multi-agent system that enhances review effectiveness by coordinating specialized skills. The results show that while LLMs lag behind human experts in this task, the application of structured coordination significantly improves their performance.

### 8. Does FLAIR super-resolution erase or hallucinate small white-matter lesions?
**Authors:** Zahra Khodakarami, Yue Li, Pulkit Khandelwal, John Detre, Sandhitsu Das, Christopher Brown, David Wolk, Paul Yushkevich
**Link:** https://arxiv.org/abs/2608.06311v1
**Summary:** The study investigates how super-resolution (SR) techniques affect the detection of small white matter lesions in brain scans, specifically whether they erase existing lesions or create false ones. Using high-resolution FLAIR scans and simulating degraded versions, the researchers compared various SR methods to assess their impact on lesion segmentation accuracy. The key finding is that SR primarily erases small real lesions rather than hallucinating new ones, with the degree of erasure increasing with lower-quality scans, though all methods improved lesion detection compared to unprocessed thick slices.

### 9. RRC: Unlocking Generative Reward Models in LLM Reinforcement Learning via Ranking-Based Reward Construction
**Authors:** Chenglong Wang, Ziming Zhu, Yifu Huo, Bei Li, Qiaozhi He, Yan Ding, Xiaoyang Hao, Yuxin Gao, Tianhua Zhou, Xiaojia Chang, Tongran Liu, Jingbo Zhu
**Link:** https://arxiv.org/abs/2608.06310v1
**Summary:** The paper addresses the challenge of effectively integrating generative reward models into reinforcement learning (RL), as traditional RL methods rely on scalar rewards while generative models operate on relative preferences. To solve this, the authors propose a Ranking-based Reward Construction (RRC) approach that utilizes two strategies—self-competitive and anchor-guided ranking—to derive rewards from comparative rankings. Their experiments show that RRC significantly enhances RL performance with generative reward models, outperforming existing reward construction methods in various benchmarks.

### 10. Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations
**Authors:** Sagar Tamang, Ayush Vyas, Tabarakul Hazarika
**Link:** https://arxiv.org/abs/2608.06305v1
**Summary:** The paper addresses the inadequacies of traditional top-k retrieval methods for processing complex documents, such as financial statements, where chunking can lead to significant errors in interpreting numeric data. The authors propose a novel method called READ, which uses three deterministic operations on the raw document rather than relying on embeddings, resulting in a much higher accuracy rate of 58.8% in answering specific questions, compared to only 15.7% for dense retrieval methods. This approach highlights the advantages of embedding-free retrieval techniques over conventional methods in handling structured data.
