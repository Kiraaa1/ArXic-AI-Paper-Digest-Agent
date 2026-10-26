---
## 2026-10-26

### 1. The Language of Instruction: Genre and Generative AI
**Authors:** James E. Dobson
**Link:** https://arxiv.org/abs/2610.32982v1
**Summary:** The paper addresses the need to conceptualize instruction-fine-tuned language models as part of a distinct genre called the instructional-conversational genre, which merges language patterns from past interactions between humans and generative models. The authors propose that this genre is shaped by processes like instruction fine-tuning, system prompts, and the use of markup languages with special tokens. The key contribution is the formalization of how these elements come together to enhance communication with AI systems, improving their effectiveness in instructional contexts.

### 2. SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning
**Authors:** Yuhan Liu, Lianhui Qin, Shenji Wan
**Link:** https://arxiv.org/abs/2610.32978v1
**Summary:** SceneBloom addresses the challenge of creating realistic and diverse indoor environments for training embodied agents, which require accurate spatial arrangements for effective learning. The framework combines a hierarchical sampler that generates furniture layouts using visual diffusion models with a compiler that ensures geometric validity through contract-guided fitting. Key results show that SceneBloom produces high-quality, physically stable layouts without collisions, outperforming other methods and enabling better navigation policy training in real-world scenarios.

### 3. RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms
**Authors:** Xi Chen, Fengqi Hu, Zeyu Shen, Jiaying Xu, Shangding Gu, Pan Xu, Anqi Liu, Laixi Shi
**Link:** https://arxiv.org/abs/2610.32971v1
**Summary:** The paper addresses the challenges of deploying robust reinforcement learning (RL) algorithms in real-world scenarios, where policies can fail due to unforeseen disruptions. The authors present RobustRLlib, a unified library that combines 17 different robust RL algorithms with a standardized interface, thus enhancing their reusability and evaluation across a variety of tasks and perturbations. A comprehensive assessment of these algorithms reveals their effectiveness and identifies critical areas where improvements are still needed, contributing to a clearer understanding of robustness in RL.

### 4. DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection
**Authors:** Amber Xie, Jiawei Fu, Xiaofeng Guo, Carmelo Sferrazza, Guanya Shi, Haozhi Qi
**Link:** https://arxiv.org/abs/2610.32969v1
**Summary:** The paper introduces DexPort, a portable interface designed to simplify the collection of high-quality demonstrations for training dexterous robot hands, addressing the challenges of teleoperation and human motion retargeting. By allowing operators to control wrist motions and select predetermined skills without needing to manage each finger joint, DexPort enables efficient data gathering across various real-world tasks. The approach demonstrated significant improvements in task success rates, achieving up to 78% in real-world scenarios using the recorded commands directly.

### 5. Flownomaly: Single-Step Conditional-Mean Recovery for Few-Shot Anomaly Detection
**Authors:** Bernardo Perrone Ribeiro, Erkut Akdag, Egor Bondarev
**Link:** https://arxiv.org/abs/2610.32964v1
**Summary:** The paper addresses the challenge of few-shot anomaly detection in industrial settings, where only a limited number of defect-free images are available for modeling normality. The authors propose "Flownomaly," which uses a novel approach of learning a velocity field in a feature space to recover normal representations from noisy query tokens without relying on stored examples or trajectory integration. Their method achieves state-of-the-art performance in anomaly detection benchmarks, demonstrating impressive AUROC scores, particularly in scenarios with minimal training data.

### 6. Measure Before You Train: Typed Decision Models vs. a Classical Baseline vs. a Generative LLM for Routing a Personal Multilingual Inbox
**Authors:** Federico Lucca
**Link:** https://arxiv.org/abs/2610.32955v1
**Summary:** The paper addresses the challenge of effectively classifying emails in a personal inbox, determining their type, urgency, and whether action is required. The authors introduce Foyer, a measurement protocol that collects ground truth labels before training and compare various classification systems, including decision models and generative LLMs, on real multilingual email data. Key findings reveal that while logistic regression achieves high accuracy, the most accurate systems tend to overlook important emails needing action; a cost-based threshold improves performance, highlighting the complexity of balancing accuracy and practical application in email management.

### 7. Where Rounding Happens Matters: Rounding-Location Alignment Stabilizes LLM Reinforcement Learning
**Authors:** Yijing Ke, Tianle Cai, Ruosong Wang
**Link:** https://arxiv.org/abs/2610.32951v1
**Summary:** This paper addresses the instability in reinforcement learning for large language models caused by differences in rounding between training and inference processes, which can lead to off-policy updates. The authors propose aligning rounding locations in specific components of the model while keeping the overall system intact, maintaining certain computations in higher precision until the end. Their method successfully prevents training collapse and shows that aligning just one component can be sufficient.

### 8. Beyond Discrete Tokens: Preserving Numerical Continuity in Medical Vision-Language Models
**Authors:** Dianye Huang, Jiamei Guo, Yue Zhou, Mingde Li, Yi Xiong, Wei Wang, Nassir Navab, Zhongliang Jiang
**Link:** https://arxiv.org/abs/2610.32948v1
**Summary:** The paper addresses the challenge of accurately predicting continuous numerical measurements in medical imaging, specifically for ultrasound, where traditional models rely on discrete tokens. The authors propose a new model called HAD-VLM, which merges autoregressive text generation with a diffusion process for continuous measurement prediction, showing significant improvements in measurement accuracy for echocardiographic tasks compared to previous methods. This approach enhances quantitative analysis while maintaining the flexibility needed for various medical tasks.

### 9. Monetizing Intelligence: Advertising and Subscription Design on LLM Platforms
**Authors:** Yuhang Ji, Fasheng Xu, Tianjun Feng
**Link:** https://arxiv.org/abs/2610.32945v1
**Summary:** This paper addresses the challenges faced by large language model platforms in balancing advertising and subscription models to optimize revenue while maintaining user satisfaction. The authors analyze how a monopolistic platform can strategically select service quality, advertising intensity, and subscription pricing, finding that a mixed approach can enhance consumer surplus and allow for broader access, even leading to utility disparities among users. They highlight the importance of menu design in their findings, suggesting that advertising-funded options can improve overall service provision and pricing strategies.

### 10. Knowledge Distillation across Item and Code Spaces for Parallel Generative Recommendation
**Authors:** Yixuan Xu, Hailin Liu, Linxiang Peng, Can Yang
**Link:** https://arxiv.org/abs/2610.32943v1
**Summary:** The paper addresses the challenge of improving generative recommendation systems that use discrete semantic codes for items, which currently rely on hard labels from observed item sequences without leveraging the richer distributional knowledge from sequential recommenders. The authors propose two knowledge-distillation techniques, Item Distribution Matching (IDM) and Code Marginal Matching (CMM), to transfer predictive distribution information from a teacher model operating in item space to a student model in code space. Their experiments demonstrate significant improvements in recommendation accuracy, with IDM enhancing Recall@10 by 15.39% and CMM boosting NDCG@10 by 8.28%, thereby showing that these methods can effectively enhance standard supervised learning in recommendation systems.
