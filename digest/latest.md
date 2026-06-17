---
## 2026-06-17

### 1. Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement
**Authors:** Mingtong Zhang, Dhruv Shah
**Link:** https://arxiv.org/abs/2606.18247v1
**Summary:** The paper addresses the challenge of enabling robots to learn and improve their policies in real-time while operating in the real world. The authors introduce a framework called VERITAS, which combines a pre-trained robot policy with a visual verifier to enhance decision-making during inference and facilitate self-improvement without additional training. The key finding is that this approach not only improves policy performance during operation but also allows for effective offline policy refinement using verified self-generated data, achieving results comparable to those obtained from expert demonstrations without needing human intervention.

### 2. Variable-Width Transformers
**Authors:** Zhaofeng Wu, Oliver Sieberling, Shawn Tan, Rameswar Panda, Yury Polyanskiy, Yoon Kim
**Link:** https://arxiv.org/abs/2606.18246v1
**Summary:** The paper addresses the inefficiencies in transformer architectures that maintain a uniform layer width, despite different layers serving varied computational roles. The authors propose a novel architecture, termed > <former, which employs a variable-width design, featuring wider layers at the beginning and end while narrowing the middle layers. Their findings reveal that this nonuniform width allocation leads to improved language modeling performance and reduced computational costs, demonstrating a more efficient way to scale language models.

### 3. ReproRepo: Scaling Reproducibility Audits with GitHub Repository Issues
**Authors:** Shanda Li, Qiuhong Anna Wei, Jingwu Tang, Valerie Chen, Nihar B Shah, Tim Dettmers, Yiming Yang, Ameet Talwalkar
**Link:** https://arxiv.org/abs/2606.18237v1
**Summary:** The paper introduces ReproRepo, a scalable framework for evaluating the reproducibility of research results by utilizing GitHub issues to identify common reproduction challenges in machine learning papers. By analyzing 1,149 papers, the authors demonstrate that large language model (LLM) agents, particularly Codex with GPT-5.5, can effectively identify reproducibility issues reported by humans, achieving a success rate of about 90% in linking problems to relevant publications. This approach provides a more efficient method for conducting reproducibility audits in the scientific community.

### 4. Sign-Rank, Index, and List Replicability: Connections and Separations
**Authors:** Ari Blondal, Hamed Hatami, Pooya Hatami, Chavdar Lalov, Sivan Tretiak
**Link:** https://arxiv.org/abs/2606.18236v1
**Summary:** This paper addresses the challenge of establishing lower bounds on the sign rank of binary concept classes, which is crucial in learning theory. The authors link the sign rank to two more manageable measures: the \(\mathbb{Z}_2\)-index and list replicability, demonstrating that the \(\mathbb{Z}_2\)-index is bounded by a linear function of the list replicability number. A significant outcome is a clear separation between sign rank and the \(\mathbb{Z}_2\)-index, along with new upper bounds and composition results for list replicability, which enhance our understanding of these complexity measures.

### 5. EvolveNav: Proactive Preflection and Self-Evolving Memory for Zero-Shot Object Goal Navigation
**Authors:** Qi Chai, Wenhao Shen, Nanjie Yao, Yue Xia, Kaiyong Zhao, Jie Ma, Guosheng Lin, Hao Wang
**Link:** https://arxiv.org/abs/2606.18235v1
**Summary:** The paper addresses the challenge of Zero-Shot Object-Goal Navigation, where agents must find objects without prior training. It introduces EvolveNav, a framework that allows agents to continually improve by learning from past experiences and selecting effective navigation strategies, along with a module that predicts action outcomes. The approach significantly enhances performance, achieving a 10.1% increase in success rates while minimizing unnecessary exploration steps.

### 6. Adaptive Volumetric Mechanical Property Fields Invariant to Resolution
**Authors:** Rishit Dagli, Donglai Xiang, Vismay Modi, Xuning Yang, Gavriel State, David I. W. Levin, Maria Shugrina
**Link:** https://arxiv.org/abs/2606.18231v1
**Summary:** The paper addresses the challenge of accurately predicting the mechanical properties of 3D objects, like Young's modulus and density, which are often missing in digital assets. The authors introduce AdaVoMP, a novel method that utilizes a sparse voxel structure and a transformer model to generate precise material properties at a much higher resolution than previous techniques. Their approach not only enhances the accuracy of these predictions but also reduces computational requirements, enabling the creation of realistic simulations for complex 3D models.

### 7. Learning Red Agent Policy from Observations for Neurosymbolic Autonomous Cyber Agents
**Authors:** Ankita Samaddar, Sandeep Neema, Daniel Balasubramanian, Xenofon Koutsoukos
**Link:** https://arxiv.org/abs/2606.18223v1
**Summary:** The paper addresses the challenge of predicting the actions of cyber-attackers in partially observable environments, which complicates the training of autonomous cyber-defense agents. The authors propose a Policy Learning Technique that uses imitation learning to derive policies from network observations and defender actions. This method, integrated into a neurosymbolic cyber-defense agent, successfully predicts attacker actions with high accuracy in various simulated scenarios.

### 8. Darshana Graph: A Parallel Commentary Corpus for Comparative Indian Philosophy, with Stylometric and Exploratory Graph Analyses
**Authors:** Joy Bose
**Link:** https://arxiv.org/abs/2606.18222v1
**Summary:** The paper presents the Darshana Graph, a comprehensive corpus of over 125,000 philosophical texts from Hindu, Buddhist, and Jain traditions, with a unique focus on aligning 8,500 records from various commentators on the same source verses for comparative analysis. The authors employ stylometric and large language model techniques to analyze argumentative styles and extract philosophical relationships, finding notable patterns and disagreements among different schools. This resource is valuable for researchers examining interpretative differences in Indian philosophy and is publicly available for further exploration.

### 9. Finite-Time Queue Peak Laws in Stochastic Networks: Logarithmic Scaling After Geometric Thresholds
**Authors:** Hao Liang, Cheng Tang, Yunzong Xu
**Link:** https://arxiv.org/abs/2606.18218v1
**Summary:** The paper investigates how the peaks in queue lengths behave over a finite time horizon in stochastic networks where multiple queues share limited service resources. By examining scheduling policies like MaxWeight under conditions of uniform load, the authors demonstrate that queue peaks grow logarithmically after surpassing a specific geometric threshold, deviating from traditional square-root growth patterns. This work highlights the influence of network geometry on finite-time queue dynamics and offers refined bounds and insights for managing queues in complex network configurations.

### 10. Zone of Proximal Policy Optimization: Teacher in Prompts, Not Gradients
**Authors:** Byung-Kwan Lee, Ximing Lu, Shizhe Diao, Minki Kang, Saurav Muralidharan, Karan Sapra, Andrew Tao, Pavlo Molchanov, Yejin Choi, Yu-Chiang Frank Wang, Ryo Hachiuma
**Link:** https://arxiv.org/abs/2606.18216v1
**Summary:** The paper addresses the challenge of knowledge distillation in reinforcement learning, where small models (students) struggle to learn effectively from larger models (teachers) when forced to imitate their output. To overcome this, the authors propose Zone of Proximal Policy Optimization (ZPPO), which focuses on integrating teacher guidance into prompts rather than directly affecting the student's policy gradient. The key result shows that ZPPO significantly improves performance in small student models across various benchmarks compared to traditional distillation methods.
