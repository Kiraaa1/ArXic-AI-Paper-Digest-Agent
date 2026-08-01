---
## 2026-08-01

### 1. MixFrag: Fragility-Guided Mixed-Precision Post-Training Quantization for Vision Transformers
**Authors:** Md. Mehrab Hossain Opi, Robiul Islam Ryad, Md. Umar Faruk
**Link:** https://arxiv.org/abs/2607.28589v1
**Summary:** The paper introduces MixFrag, a new framework for mixed-precision post-training quantization of Vision Transformers (ViTs), addressing the inefficiencies of existing methods that use uniform bit-widths for all model components. By measuring the sensitivity of each component to quantization and optimizing bit allocation as a Multiple-Choice Knapsack Problem, MixFrag achieves better classification performance with lower precision across layers. The key outcome shows MixFrag outperforms previous methods, enhancing performance on tasks like object detection by up to 9.6 AP.

### 2. PAIChecker: Uncovering and Checking PR-Issue Misalignment in SWE-Bench-Like Benchmarks
**Authors:** Manyi Wang, Junjielong Xu, Pinjia He
**Link:** https://arxiv.org/abs/2607.28587v1
**Summary:** The paper addresses the issue of misalignment between Pull Requests (PRs) and their associated issues in software engineering benchmarks, which can undermine the evaluation of large language models (LLMs) for issue resolution. To tackle this, the authors developed PAIChecker, a multi-agent system that systematically identifies misalignments through a three-phase process involving pattern recognition, collaborative labeling, and code validation. Their experiments demonstrate that PAIChecker significantly improves accuracy in detecting these misalignments, achieving over 92% accuracy across multiple LLMs.

### 3. $β$-OPSD: Deriving with Policy Optimization, Training with Self-Distillation
**Authors:** Jiawei Xu, Minghui Liu, Juzheng Zhang, Tom Goldstein, Furong Huang
**Link:** https://arxiv.org/abs/2607.28582v1
**Summary:** The paper addresses the challenges of on-policy self-distillation (OPSD) in training reasoning language models, which often requires significant engineering to work effectively. The authors propose a new method called $β$-OPSD, which introduces a controllable regularization parameter $β$ to balance the guidance from a reference policy and a privileged teacher. Their experiments demonstrate that $β$-OPSD enhances optimization stability and improves performance in mathematical reasoning tasks compared to traditional OPSD, offering a more efficient link between self-distillation and policy optimization.

### 4. DualG-MRAG: Decoupling Macro-Reasoning and Micro-Matching for Multimodal Retrieval-Augmented Generation
**Authors:** Jiacheng Tao, Qingyun Sun, Haonan Yuan, Ziwei Zhang, Jianxin Li
**Link:** https://arxiv.org/abs/2607.28580v1
**Summary:** The paper addresses the challenges of multimodal retrieval-augmented generation (MM-RAG), particularly in complex reasoning tasks, where existing methods struggle to connect information across various modalities. The authors propose a novel framework called DualG-MRAG, which separates global reasoning from detailed matching using two distinct graphs—one for overall structure and another for fine-grained verification. Their approach improves evidence recall and accuracy in complex question answering compared to previous methods.

### 5. Sample More, Reflect Less: Self-Refine and Reflexion Lose to Repeated Sampling at Equal Token Cost, from 1.5B to 7B
**Authors:** Iliya Mirzaei
**Link:** https://arxiv.org/abs/2607.28576v1
**Summary:** The paper examines whether advanced self-reflective methods used in language models, such as planning and critiquing their own answers, improve performance compared to simply repeating a question multiple times and selecting the most frequent answer. Through a designed experimental comparison of seven methods across models with varying parameter sizes, the authors found that these self-inspection approaches generally performed worse than repeated sampling, especially as model size increased. The key contribution is the demonstration that simpler methods outperform more complex self-reflection techniques at a comparable token cost, challenging the effectiveness of self-critique strategies in these models.

### 6. Algorithms for Structured Elections under Thiele Voting Rules
**Authors:** Alexandra Lassota, Krzysztof Sornat
**Link:** https://arxiv.org/abs/2607.28575v1
**Summary:** The paper investigates the computational challenges of determining the winners in approval-based committee elections using Thiele voting rules, which depend on how voter satisfaction is structured. The authors analyze the relationships between candidates based on voter approvals and develop fixed-parameter tractable (FPT) algorithms for specific scenarios, particularly when voters are arranged in intervals. Key contributions include resolving open questions in the literature by offering efficient algorithms for restricted cases of the Proportional Approval Voting problem, even when the situation is NP-hard in general.

### 7. Rethinking Inference-Time Scaling in Local Computer-Use Agents: Failure Modes and Compute Tradeoffs
**Authors:** Woongkyu Lee, Jungwook Choi
**Link:** https://arxiv.org/abs/2607.28573v1
**Summary:** The paper investigates how to enhance the performance of local computer-use agents (CUAs) under hardware constraints by analyzing the effectiveness of various inference-time scaling strategies. Through empirical evaluation of several models, the study finds that adding more computation often leads to diminishing returns and alters the types of failures encountered, suggesting the need for smarter computation allocation and error-aware strategies. Key insights include the limitations of scaling approaches and the recommendation for designing CUAs that align with their specific capabilities and constraints.

### 8. Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering
**Authors:** Junlin Yang, Che Jiang, Yu Fu, Tianwei Luo, Can Ren, Weizhi Wang, Kaikai Zhao, Hongyi Liu, Yuxin Zuo, Yuru Wang, Yuchen Fan, Kai Tian, Zhenzhao Yuan, Xiaojian Lin, Li Sheng, Rushi Qiang, Guoli Jia, Xingtai Lv, Ermo Hua, Dianqiao Lei, Youbang Sun, Ning Ding, Bowen Zhou, Kaiyan Zhang
**Link:** https://arxiv.org/abs/2607.28568v1
**Summary:** The paper addresses the challenge of recursive self-improvement in AI systems by developing OpenMLE, a comprehensive framework for machine learning engineering (MLE). It showcases Frontis-MA1, a 35 billion parameter meta-evolution agent that significantly enhances MLE performance through a combination of specialized program-evolution operators and reinforced learning techniques. The key contribution is the model's ability to improve task performance from 39.39% to 60.61% on a specific benchmark, demonstrating its effectiveness in the AI4AI domain.

### 9. Doubly Robust Functional Representation Learning for Longitudinal Causal Inference with Irregular Histories
**Authors:** Mengfei Ran, Yifeng Shen, Ruijie Guan
**Link:** https://arxiv.org/abs/2607.28567v1
**Summary:** The paper addresses the challenge of performing causal inference in longitudinal studies that collect data in irregular time intervals and formats, such as laboratory results and physiological signals. The authors introduce a novel method called Doubly Robust Functional Representation Learning (DR-FRL) that transforms these irregular histories into structured representations, allowing for more accurate causal estimations. Their simulations demonstrate that this method performs particularly well when dealing with complex data scenarios, and they provide a real-world application showing that existing scalar summaries already contain significant information for certain clinical outcomes.

### 10. APO: Unsupervised Atomic Policy Optimization for 3D Structure Prediction of Atomic Systems
**Authors:** Shentong Mo, Yatao Bian
**Link:** https://arxiv.org/abs/2607.28553v1
**Summary:** The paper addresses the challenge of predicting 3D structures of atomic systems, which is critical for fields like material science and drug discovery, especially when labeled data is scarce. The authors introduce an unsupervised method called Atomic Policy Optimization (APO) that uses a dual-reward mechanism to guide the model in finding physically plausible structures without relying on ground-truth data. The key finding is that APO outperforms traditional supervised methods, achieving higher accuracy in structure prediction while improving inference efficiency through better navigation of probability paths.
