---
## 2026-10-08

### 1. Never Look Back: Understanding Persistence in 3D Object Memory from Egocentric Videos
**Authors:** Shravan Chaudhari, William Paul, Suchi Saria, Rama Chellappa, Homanga Bharadhwaj
**Link:** https://arxiv.org/abs/2610.10538v1
**Summary:** The paper addresses the challenge of enabling an embodied assistant to remember the locations and details of objects encountered in everyday activities, even after they are no longer in view. The authors introduce Ledger, a persistent 3D object memory system that utilizes observations from egocentric videos to track and describe objects over time, significantly improving localization accuracy. Key results show Ledger's effectiveness in enhancing memory retrieval and spatial question answering, leading to notable performance improvements in various accuracy metrics compared to previous methods.

### 2. Decoupling Exploration from Optimization in RLVR
**Authors:** Saif Punjwani, Micah Goldblum
**Link:** https://arxiv.org/abs/2610.10536v1
**Summary:** The paper addresses the challenge of improving language models' reasoning strategies through reinforcement learning with verifiable rewards (RLVR), which often struggles with retaining model quality when exploring novel ideas. The authors propose a new approach called Exploration-Distillation (ExpDis), which separates the exploration phase from optimization by training explorer policies with a novelty bonus and then using their filtered trajectories to improve a student policy without that bonus. The results show that ExpDis significantly outperforms previous methods in generating diverse and accurate solutions across multiple benchmarks.

### 3. EngramEdit: Decoupled Knowledge Updates in LLMs through Conditional Memory
**Authors:** Hongru Cai, Ran Wei, Wenjie Wang, Chengfa Wu, Ning Song, Yongqi Li, Wenjie Li
**Link:** https://arxiv.org/abs/2610.10533v1
**Summary:** EngramEdit addresses the challenge of updating factual knowledge in large language models without affecting other knowledge or capabilities. It proposes a method that allows independent updates of knowledge by using conditional memory to compute target memory representations and edit shared embeddings while minimizing disruptions to unrelated information. The key result is that EngramEdit enables successful and accurate knowledge updates that retain the model's overall functionality, achieving significantly higher accuracy in reasoning tasks compared to existing methods.

### 4. Long-WAM: Scaling the Context of World-Action Models
**Authors:** Wei Huang, Bohan Zhang, Chenzhi Liu, Isabella Liu, Shuai Yang, Weian Mao, Luozhou Wang, Yicheng Xiao, Weifeng Lin, Qixin Hu, Bryan Chu, Sifei Liu, Linxi Fan, Xiaojuan Qi, Song Han, Yukang Chen
**Link:** https://arxiv.org/abs/2610.10528v1
**Summary:** The paper addresses the challenge of real-time robot control, which requires processing visual history to make accurate predictions about motion and tasks. The authors introduce Long-WAM, a framework that effectively scales the use of visual context by leveraging pre-trained autoregressive video models, leading to significant improvements in task success rates. Specifically, they demonstrate that increasing the context of visual history from 0 to 19.2 seconds can raise success rates on robot tasks from 63.3% to 78.7%, showcasing its effectiveness in dynamic manipulation scenarios.

### 5. Decentralized SGD under Heavy-Tailed Noise: Optimal Convergence Rates and the Role of Gradient Clipping
**Authors:** Aleksandar Armacki, Haoyuan Cai, Ali H. Sayed
**Link:** https://arxiv.org/abs/2610.10527v1
**Summary:** The paper addresses the challenge of optimizing decentralized stochastic gradient descent (SGD) under heavy-tailed noise, which is common in modern machine learning. The authors propose a method called clipped decentralized SGD (DSGD) that applies gradient clipping to achieve optimal convergence rates, even in the presence of noise. Their key contribution is showing that clipped DSGD achieves efficient optimization without compromising consensus speed, highlighting a critical advantage of clipping over normalization in decentralized settings.

### 6. Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models
**Authors:** Mikey Watts, Yuchen Cui
**Link:** https://arxiv.org/abs/2610.10526v1
**Summary:** The paper addresses the issue of language sensitivity in vision-language-action models, which are significantly affected by the phrasing of instructions. The authors propose a method that generates rephrasing rules using a large language model, allowing the system to rewrite incoming instructions without altering the underlying policy. This approach improves the model's performance by 16 to 27% on various tasks, particularly benefiting out-of-distribution scenarios, and achieves notable gains in success rates without the need for retraining.

### 7. Distilling Graph Geometry: Knowledge Gap from GNNs to MLPs
**Authors:** Zhewei Chen, Hao Zhu, Jiaojiao Jiang, Ahad N. Zehmakan
**Link:** https://arxiv.org/abs/2610.10520v1
**Summary:** The paper addresses the challenge of transferring knowledge from Graph Neural Networks (GNNs) to Multi-Layer Perceptrons (MLPs) while maintaining predictive accuracy, particularly focusing on how to preserve important graph geometry. The authors introduce the Graph Geometry-aware MLP (G^2MLP), which uses an energy-weighted alignment based on Ollivier-Ricci curvature to guide the distillation process. The key finding is that G^2MLP consistently outperforms existing graph-free distillation methods across various benchmarks, demonstrating improved performance without requiring graph data during inference.

### 8. Why Forget-Only Unlearning Needs Memorization
**Authors:** Luka Radić, Vikrant Singhal, Amartya Sanyal
**Link:** https://arxiv.org/abs/2610.10519v1
**Summary:** The paper investigates the challenges of "forget-only" unlearning, where a model must forget specific training examples without access to the original data. The authors demonstrate that the feasibility of this unlearning process is influenced by the learning method employed, revealing that models may need to retain more information than usual to effectively forget examples. Their key finding is that some algorithms could require almost complete memorization of the training data to accurately implement deletions, suggesting that traditional training methods may not suffice for effective forget-only unlearning.

### 9. RoboJEPA: Scaling Robotic Latent World Models
**Authors:** Artem Zholus, Nicolas Beltran-Velez, Jianhao Yuan, Sarath Chandar, Tushar Nagarajan, Daniel Severo, Koustuv Sinha, Michal Drozdzal, Adriana Romero Soriano, Jeannette Bohg, Nicolas Ballas, Mahmoud Assran
**Link:** https://arxiv.org/abs/2610.10515v1
**Summary:** The paper addresses the challenge of understanding how the performance of robotic latent world models scales with increased model size, data, and computational resources. The authors introduce RoboJEPA, a large-scale model based on the Joint Embedding Predictive Architecture (JEPA), which demonstrates that imagination error decreases predictably with increased compute, allowing for improved robotics planning and performance. Notably, RoboJEPA, at 8 billion parameters, is the largest model of its kind to date and provides insights that could help advance robotic capabilities.

### 10. SciExam for ENSO: Can AI Agents Build Climate Models?
**Authors:** Yinling Zhang, Langchen Liu, Dongbin Xiu, Xueyan Zou, Xu Kuang, Mengdi Wang, Shilong Liu
**Link:** https://arxiv.org/abs/2610.10513v1
**Summary:** The paper addresses the challenge of evaluating AI agents' ability to create valid scientific models without predefined answers. The authors introduce the SciExam for ENSO benchmark, where agents develop stochastic models of the El Niño-Southern Oscillation using real climate observations within a limited timeframe. Remarkably, six out of twelve agents produced models that outperformed an established published model, indicating that AI can effectively build competitive climate models that contribute to ongoing scientific debates.
