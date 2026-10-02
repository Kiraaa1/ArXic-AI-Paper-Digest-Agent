---
## 2026-10-02

### 1. One Basis to Animate Them All: Gaussian Blendshape Distillation for Real-Time Avatars
**Authors:** Ramazan Fazylov, Stamatis Lefkimmiatis, Ivan Laptev
**Link:** https://arxiv.org/abs/2610.02207v1
**Summary:** The paper addresses the challenge of slow neural inference in real-time animation of 3D Gaussian avatars by introducing a distillation method called GALA, which approximates animation using a linear combination of blendshapes and a shallow neural network. This approach significantly reduces CPU animation costs by up to three orders of magnitude while maintaining high rendering quality and enabling smooth animations of complex characters at frame rates of up to 60fps on mobile devices. The results demonstrate the effectiveness of this method across various avatar models, showing that learned representations share a linear structure suitable for efficient animation.

### 2. KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards
**Authors:** Pengfei Li, Naufal Suryanto, Sicheng Zhang, Muzammal Naseer
**Link:** https://arxiv.org/abs/2610.02206v1
**Summary:** The paper introduces KaliBench, a benchmark designed to evaluate large language models (LLMs) on their ability to generate executable command-line interface (CLI) commands for cybersecurity tools on Kali Linux. It features a dataset of over 8,500 query-command pairs and a robust verification pipeline to ensure both correctness and executability of the commands. The key finding reveals that existing models struggle with exact command accuracy, achieving no more than 42%, but that fine-tuning with incentives from KaliBench can significantly enhance performance, making it competitive with much larger models.

### 3. Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents
**Authors:** Yen-Jen Wang, Haozhe Jiang, Shuying Deng, Haoru Xue, Weirui Ye, Rocky Duan, Nika Haghtalab, S. Shankar Sastry, Pieter Abbeel, Haozhi Qi
**Link:** https://arxiv.org/abs/2610.02204v1
**Summary:** The paper addresses the challenge of improving robot capabilities for diverse tasks without needing to retrain model weights, which typically requires significant human input. The authors introduce the Reconstruct, Practice, Go Real (RPG) framework, which autonomously enhances robot performance by analyzing execution failures, refining skills, and creating new tasks based on offline data. The key result shows that RPG can boost task success rates from 28.6% to 95.0% across 22 manipulation tasks, surpassing existing methods.

### 4. Embedding Prediction Helps Image Generation
**Authors:** Sihan Xu, Ji Xie, Zilin Wang, Hui Shen, Stella X. Yu
**Link:** https://arxiv.org/abs/2610.02203v1
**Summary:** This paper addresses the limitation of using fixed embeddings for conditioning image generation in diffusion transformers by proposing a new method called Next-Embedding Predictive Autoregression (NEPA). NEPA predicts the next embeddings dynamically at each denoising step to better adapt to the current noisy state, resulting in improved image quality. The authors demonstrate that their NEPA-DiT-XL model achieves a competitive FID score of 1.32 while using significantly less training compute compared to existing methods.

### 5. ScholarCatalyst: A Benchmark for Retrieving Papers That Inspire New Research
**Authors:** Sohyeon Kim, Yoonho Lee, Bo Liu, Dayoon Ko, Rulin Shao, Seungone Kim, Graham Neubig, Pang Wei Koh, Aakanksha Chowdhery, Akari Asai, Omar Khattab, Yejin Choi, Gunhee Kim, Chelsea Finn
**Link:** https://arxiv.org/abs/2610.02202v1
**Summary:** The paper presents ScholarCatalyst, a benchmark designed to improve AI's ability to retrieve relevant research papers that can inspire new scientific projects. The authors collected insights from 184 researchers who identified prior works that aided their projects, using this data to create a retrieval task for evaluating AI models. Key findings reveal that current AI retrieval methods, including advanced models, perform inadequately, indicating a need for new strategies that enhance AI's capability to navigate extensive research literature effectively.

### 6. SILSA: Sliding-Window Slice Latents for Topology-Preserving High-Resolution 3D Generation
**Authors:** Tianjiao Yu, Xinzhuo Li, Yifan Shen, Ying Shen, Kiet A. Nguyen, Adheesh Sunil Juvekar, Ismini Lourentzou
**Link:** https://arxiv.org/abs/2610.02201v1
**Summary:** The paper presents SILSA, a novel framework for high-resolution 3D generation that addresses the fragmentation and topological inconsistencies of traditional voxel-based methods. By leveraging compact sliding-window slice latents and a new architecture that maintains structural continuity, SILSA significantly enhances generation efficiency and fidelity. The key contributions include improved structural accuracy, reduced generation costs, and a substantial decrease in memory and inference time compared to existing approaches.

### 7. VISTA: A Visual Harness for Reasoning in an Interactive World
**Authors:** Qiushi Han, Keya Hu, Linlu Qiu, Cathy Wu, Kaiming He
**Link:** https://arxiv.org/abs/2610.02200v1
**Summary:** The paper presents VISTA, a visual harness designed to enhance the reasoning capabilities of multimodal models in interactive environments by enabling them to perceive the environment visually and maintain a detailed memory of past observations. VISTA significantly improves the performance of the Claude Opus 5.0 model on the ARC-AGI-3 benchmark, achieving a perfect efficiency score and using fewer actions than human participants. This approach demonstrates VISTA's effectiveness and versatility in solving tasks across various visual games and puzzles.

### 8. TACO: Ternary Absolute-max Column-wise One-sparse Optimizer for LLM Fine-Tuning
**Authors:** Jichao Jiang, Cristian McGee, El Houcine Bergou, Hanqin Cai, Aritra Dutta
**Link:** https://arxiv.org/abs/2610.02199v1
**Summary:** The paper presents TACO, an optimizer designed to significantly reduce memory overhead when fine-tuning large language models (LLMs) while maintaining performance and efficiency. TACO achieves this by using a novel approach that only retains a small set of low precision gradient components for each column of model weight matrices, which allows it to lower memory usage substantially—by a factor of 174 compared to traditional methods. As a result, TACO enables the fine-tuning of larger models on limited GPU resources without sacrificing accuracy or training speed.

### 9. FERPO: Forward Entropy-Regularized Policy Optimization
**Authors:** Sebastian Sanokowski, Alireza Sarmadi, Majid Khadiv
**Link:** https://arxiv.org/abs/2610.02198v1
**Summary:** The paper introduces FERPO, a new reinforcement learning algorithm designed to improve policy updates without relying on the reliability of the critic's action derivatives. By using a forward-KL objective that regularizes with entropy and keeps the target action distribution close to the rollout policy, FERPO enhances exploration and sample efficiency. Experimental results show that FERPO achieves competitive performance and faster actor updates compared to existing methods.

### 10. Cost-augmented Schrödinger bridges on graphs are exactly solvable: a Feynman-Kac tilt replaces learned control
**Authors:** Akshay Balsubramani
**Link:** https://arxiv.org/abs/2610.02195v1
**Summary:** This paper addresses the problem of optimizing mass transport on graphs while minimizing costs associated with state transitions, using a framework known as the generalized Schrödinger bridge. The authors present an exact solution that avoids traditional learning methods by applying a Feynman-Kac tilt, which streamlines the process to directly compute results through alternation of endpoint rescalings. A significant contribution is its application to problems like protein folding and road networks, demonstrating efficient performance even in large-scale scenarios.
