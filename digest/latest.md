---
## 2026-09-27

### 1. ExplorationBench: Measuring AI Systems' Exploration in Verifiable Alien Worlds
**Authors:** Ming Zhang, Zhenghao Xiang, Peizhong Gao, Yujiong Shen, Yuhui Wang, Zhonghan Yue, Shihan Dou, Zhangyue Yin, Junjie Ye, Shichun Liu, Weihuang Zheng, Jiahao Chen, Jiayi Chen, Hongzhang Liu, Jiaqi Shao, Tao Gui, Qi Zhang, Xuanjing Huang, Suncong Zheng, Maxm Pan
**Link:** https://arxiv.org/abs/2609.30199v1
**Summary:** The paper addresses the challenge of evaluating AI systems' ability to explore and discover new knowledge rather than just recalling pre-existing information. It introduces ExplorationBench, a framework built on verifiable simulated environments called Alien Worlds, which allows for the assessment of AI systems through structured tasks and feedback. The results show that while some AI systems can effectively learn and apply new rules in these environments, their performance can vary significantly, indicating both potential and challenges in their exploratory capabilities.

### 2. Beyond Compression: Training Latent Representations for Stable Long-Horizon Rollout in Neural Surrogate Solvers
**Authors:** Andreas E. Robertson, Ashley T. Lenau, John D. Shimanek, Benjamin A. Jasperson, Vivek Oommen, David L. Damm, Krishna Garikipati, Remi Dingreville
**Link:** https://arxiv.org/abs/2609.30198v1
**Summary:** This paper addresses the issue of instability in long-horizon predictions made by neural surrogate solvers, which compress physical system simulations into a latent space. The authors enhance the training of these models by employing techniques like Koopman operator learning and noise injection to better align the latent representations with long-term forecasting. As a result, their approach reduces long-rollout errors by about 40% while being significantly more efficient in computational resources compared to full-resolution models, demonstrating that compression should also focus on enabling stable dynamic evolution.

### 3. SAGE: Mitigating Long-Horizon Reasoning Biases via Topological Guidance
**Authors:** Xinyue Zeng, Jiawei Zhang, Yujun Yan, Dawei Zhou
**Link:** https://arxiv.org/abs/2609.30192v1
**Summary:** The paper addresses the challenges large language models face with long-horizon reasoning, particularly due to exploration and compounding biases that arise in complex reasoning tasks. To tackle this, the authors introduce SAGE (Structural Admissibility-Guided Exploration), a framework that uses structural guidance methods to improve model performance on these tasks. The key contribution is that SAGE significantly outperforms existing techniques, achieving up to an eightfold improvement on a complex reasoning problem known as the Andrews-Curtis problem.

### 4. Jev-Mobile: Jev as an Executor for Mobile GUI Agents
**Authors:** Linghua Zhang
**Link:** https://arxiv.org/abs/2609.30186v1
**Summary:** The paper addresses the inefficiencies of existing mobile GUI agents that rely heavily on vision-language models (VLMs) for both planning and executing tasks, which leads to high latency and operational costs. The authors propose Jev-Mobile, which separates high-level goal planning using a VLM from low-level action execution through a fast decision model, enabling quicker actions while still adhering to the VLM's goals. The key finding is that Jev-Mobile significantly reduces execution time and costs, achieving competitive task success rates compared to earlier models.

### 5. Intrinsic-Extrinsic Coupling in Learning Dynamics
**Authors:** Qinyou Wang
**Link:** https://arxiv.org/abs/2609.30185v1
**Summary:** The paper addresses the challenge of how a learner can respond to new training data while considering both its internal state and external inputs, particularly in class-incremental learning scenarios. The authors develop a framework to analyze intrinsic-extrinsic coupling through mathematical concepts and executable interventions, demonstrating that interventions can have non-additive effects and that positive interactions between intrinsic mechanisms and external training scenarios are not guaranteed. A key contribution is the identification of how these interactions can affect learning dynamics, emphasizing the importance of distinguishing between local interventions and overall training performance.

### 6. ARGUS: Role-Aware Event Knowledge Graphs for U.S. Employment-Discrimination Complaints
**Authors:** Sriram Kannan, Swetha Saseendran, Vishnu Vardhan Reddy Kandi, Leslie Barrett, Madhavan Seshadri, Enrico Santus
**Link:** https://arxiv.org/abs/2609.30184v1
**Summary:** The paper introduces ARGUS, a system designed to create Event Knowledge Graphs from U.S. employment-discrimination complaints, which capture complex event sequences better than traditional methods. By combining a structured schema and advanced models, ARGUS builds detailed graph representations that improve the classification of claims and the quality of legal question answering. The key finding is that these graph representations enhance document understanding and reasoning, particularly when integrated with relevant retrieved information.

### 7. Search-Aware Reinforcement Learning for Multi-Component Query Understanding in Roblox Game Search
**Authors:** Nayoung Choi, Shengjian Chen, Xiaokai Wei, Wenzheng Zhang, Daiyao Yi, Rachit Pareek, Vincent Su, Michelle Gong, Jinho D. Choi
**Link:** https://arxiv.org/abs/2609.30177v1
**Summary:** The paper addresses the challenge of improving query understanding (QU) in search systems, specifically for Roblox, by using a reinforcement learning (RL) approach that focuses on optimizing individual components of the QU process. The researchers employ a two-step method that starts with teacher-student supervised fine-tuning followed by component-specific RL optimization based on real-time interactions with the search engine. Their findings demonstrate that this method significantly enhances both the effectiveness of each QU component and the overall search quality, achieving a notable increase in search ranking metrics.

### 8. GridSFM: A Foundation Model for Solving AC Optimal Power Flow
**Authors:** Luke Bhan, Weiwei Yang, Margaret Capetz, Baosen Zhang
**Link:** https://arxiv.org/abs/2609.30173v1
**Summary:** The paper presents GridSFM, a novel framework designed to effectively solve the AC Optimal Power Flow (AC-OPF) problem, which involves optimizing the flow of electricity across complex power grid networks. It leverages a large pretrained graph neural network model, refined with physics-informed fine-tuning techniques, to adapt to various grid configurations quickly and accurately. Key results indicate that GridSFM significantly outperforms traditional single-topology models in terms of cost and computational efficiency, while maintaining effectiveness even as the system size increases.

### 9. Do Audio Language Models Hear and Read Distinctive Features Alike?
**Authors:** Yuanhao Chen, Peter Chin
**Link:** https://arxiv.org/abs/2609.30167v1
**Summary:** The paper investigates whether audio language models process distinctive phonetic features similarly when hearing versus reading phonemes. By analyzing the representations of minimal pairs of phonemes in six different models across multiple languages, the authors measure the similarity in the models' interpretation of these features. They find that only one model shows consistent alignment in voicing across languages, suggesting that the model type, rather than its size, influences how phonetic features are represented in audio and text.

### 10. A Training Criterion with Token-Level Tolerance to Transcription Ambiguity for Automatic Speech Recognition
**Authors:** Saurabh Kumar, Diptiman Mohanta, Prasanta Kumar Ghosh
**Link:** https://arxiv.org/abs/2609.30160v1
**Summary:** The paper addresses the challenge of transcription ambiguity in automatic speech recognition (ASR) by proposing a new training criterion that leverages token-level wildcard arcs in addition to traditional word-level arcs. This approach allows for more precise handling of unsupported tokens while maintaining supervision for the rest of the word, leading to improved accuracy across multiple languages and datasets. The key result is a reduction in mean word error rate by 9.45% compared to conventional methods, demonstrating that this token-level tolerance effectively targets localized discrepancies in transcripts.
