---
## 2026-10-14

### 1. ChunkAct: Action Chunking for Agentic Robotics
**Authors:** Bingxin Xu, Wenrui Bao, Xinxin Liu, Jiawei Zhou, Yuzhang Shang, Emilio Ferrara
**Link:** https://arxiv.org/abs/2610.18874v1
**Summary:** The paper introduces ChunkAct, a novel method for improving efficiency in agentic robotics, where a large language model controls robot actions. By implementing action chunking, which allows groups of actions to be executed autonomously and without constant LLM reasoning during execution, the approach significantly reduces the computational load. The key result shows that ChunkAct enhances task success rates by 5% while drastically decreasing the number of LLM calls and tokens used during operation.

### 2. Cepheid: Decoupling Scale from Structure for Cross-Family Motion Completion
**Authors:** Chih-Hai Su, Tsung-Wei Ke, Yu-Lun Liu
**Link:** https://arxiv.org/abs/2610.18871v1
**Summary:** The paper addresses the challenge of completing dense motion details from sparse data across different geometric families, which traditional methods struggle with due to variations in motion scaling. The authors introduce a novel approach that decouples the structure of the motion from its physical scale by learning a dimensionless prior, allowing for more effective motion prediction. Their method outperforms conventional techniques in various scenarios, including previously unseen shapes, and can be applied to real-world recordings without the need for retraining.

### 3. What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study
**Authors:** Mingxuan Yan, Litian Gong, Dihong Huang, Zhixu Li, Tianyu Zhang, Wenqian Zhang, Hefeifei Jiang, Peihao Li, Jian Zhang, Mengfei Zhao, Yikai Tang, Hai Zhai, Zehao Wang, Ruijian Liang, Yanjia Huang, Lin Shao, Changliu Liu, Kaiyu Hang, Zhiwen Fan, Masayoshi Tomizuka, Jianfei Yang, Jiachen Li
**Link:** https://arxiv.org/abs/2610.18869v1
**Summary:** The paper investigates how to effectively use the quality of demonstrations during vision-language-action (VLA) pretraining to enhance performance in subsequent fine-tuning tasks. By comparing different methods of using demonstration quality—such as weighting and filtering—across various tasks and data conditions, the authors show that approach-aware episode conditioning significantly boosts success rates over traditional methods. Their introduction of AXIS-Bench provides a useful framework for these experiments, leading to a real-world improvement in task success from 9.6% to 31.7%.

### 4. Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards
**Authors:** Wenbo Hu, Shraman Pramanick, Krishna Kumar Singh, Nanyun Peng, Kai-Wei Chang, Yong Jae Lee
**Link:** https://arxiv.org/abs/2610.18868v1
**Summary:** The paper addresses the challenge of training long-horizon agents for complex tasks that require months of autonomy, which is hindered by sparse rewards and insufficient data. The authors introduce Tev-Gym, a dataset featuring 1,170 verified tasks with dense, progressive rewards, allowing for better training through a new method called progress-potential reward shaping (PPRS). As a key result, their model Tev-27B achieves impressive performance benchmarks in computing and math tasks, rivaling leading models despite being trained exclusively on a specific dataset.

### 5. Data Free Training of Diffusion Models for Lattice Field Theories
**Authors:** Dennis Grinwald, Ankur Singha, Khaled Kahouli, Karl Jansen, Shinichi Nakajima
**Link:** https://arxiv.org/abs/2610.18863v1
**Summary:** The paper addresses the challenge of sampling equilibrium configurations in lattice field theories, which is crucial for computational efficiency. It proposes a novel method to train diffusion models using their own generated samples, leveraging the target score identity and importance-weighted approaches. The key finding is that this data-free training strategy can achieve performance similar to traditional methods that rely on reference data from Hamiltonian Monte Carlo simulations.

### 6. DoubtLess: Training-Free Contrastive Decoding for Efficient Reasoning
**Authors:** Minghao Luo, Liang Chen
**Link:** https://arxiv.org/abs/2610.18862v1
**Summary:** The paper presents DoubtLess, a novel method for enhancing the efficiency of reasoning models by reducing the length of chains of thought (CoT) without requiring additional training. By utilizing a smaller reasoning model to guide a larger one in generating more concise outputs, DoubtLess achieved a 31% reduction in CoT while maintaining accuracy across various benchmarks. This method also decreased the number of tokens used in a self-debugging coding agent by 20%, demonstrating its effectiveness and generalizability.

### 7. AesCode: Aesthetic Code Generation with Decoupled Cross-Modal Rewards
**Authors:** Xin Gao, Yifan Yang, Xin Li, Pan Wang, Yan Li, Muzhao Tian, Mingxi Cheng, Bei Liu, Kai Qiu, Qi Dai, Dong Chen, Yue Dong, Leandros Tassiulas, Rex Ying, Ji Li, Chong Luo
**Link:** https://arxiv.org/abs/2610.18860v1
**Summary:** The paper presents AesCode, a system designed to generate aesthetic code for visual artifacts like slides and dashboards by integrating content and visual guidance. By utilizing a design graph and decoupled cross-modal rewards from both deterministic verifiers and a visual language model, AesCode optimizes for spatial planning, aesthetic quality, and correctness through reinforcement learning. The results show that AesCode significantly improves visual quality compared to existing models, achieving performance similar to advanced closed-source models.

### 8. Hybrid Reasoning Agents
**Authors:** Jiaru Zou, Yunzhe Qi, Sirui Chen, Federico Bianchi, Shang Zhu, Pan Lu, Jingrui He, James Zou
**Link:** https://arxiv.org/abs/2610.18861v1
**Summary:** The paper addresses the challenge of creating an AI agent that can efficiently reason beyond human language while still communicating through it. The authors introduce Hybrid Reasoning Agents (HybridAgents), which integrate latent reasoning with text-based interaction, using a novel architecture that allows seamless transitions and maintains context. Their approach outperforms existing AI models across various benchmarks, demonstrating significant improvements in performance, inference speed, and cost efficiency.

### 9. Exact Topological Compliance: Generating Persistence-Equivalent Graphs
**Authors:** Mattie Ji, Indradyumna Roy, Vikas Garg
**Link:** https://arxiv.org/abs/2610.18856v1
**Summary:** The paper addresses the challenge of generating graphs that exactly match specified topological features, represented as persistence diagrams (PDs). It proposes two methods: a local approach that iteratively builds graphs while ensuring they match the target PD, and a global constraint satisfaction approach that leverages modern solvers for more efficient generation. Both methods successfully achieve exact compliance with target PDs, marking a significant advancement in topology-aware graph generation.

### 10. Two Clocks: Why Larger Rollout Batches Learn Slower but Fail on Schedule in Reinforcement Learning with Verifiable Rewards
**Authors:** Yuante Li, Junwei Quan, Kai Qiu, Kate Zhang, Yicheng Tao
**Link:** https://arxiv.org/abs/2610.18853v1
**Summary:** The paper investigates why larger rollout batches in reinforcement learning with verifiable rewards (RLVR) lead to slower learning and increased failure risk. The authors introduce a "two-clock" framework to differentiate between the samples that contribute to learning progress and those that lead to performance collapse, showing that larger batches can result in less efficient learning despite maintaining first-order improvements. They validate their findings through experiments and propose a scheduling method for RLVR that involves starting with smaller batches before transitioning to larger ones to optimize performance while minimizing failure.
