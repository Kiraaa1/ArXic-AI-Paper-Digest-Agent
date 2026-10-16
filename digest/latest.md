---
## 2026-10-16

### 1. LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation
**Authors:** Zhixu Li, Keqian Tang, Litian Gong, Jingyu Yao, Wenqian Zhang, Tianze Xu, Zehao Wang, Yuping Wang, Junge Zhang, Jiachen Li
**Link:** https://arxiv.org/abs/2610.22372v1
**Summary:** The paper presents LIBERO-PeRM, a benchmark designed to facilitate personalized robotic manipulation (PeRM), which addresses the challenge of adapting robots to individual preferences in household settings. It explores various questions regarding how robots can learn and generalize user preferences from demonstrations across multiple tasks, while introducing a detailed framework and procedural pipeline for generating training scenarios. Key findings reveal that while current policies struggle with zero-shot personalization, mixed training methods can enhance preference retention and performance, although challenges remain in handling generalization and conflicts among preferences.

### 2. Discovering state-of-the-art quantum circuits with large language models
**Authors:** Andi Gu, Alek H. Kemeny, Susanne F. Yelin, Mikhail D. Lukin
**Link:** https://arxiv.org/abs/2610.22367v1
**Summary:** The paper addresses the challenge of optimizing quantum circuits for various computational tasks, which is complicated by the need for reversibility in quantum operations. Researchers developed an evolutionary framework that utilizes large language models to propose and evaluate quantum circuit designs. The study found that this approach significantly improved circuit efficiency in most tasks, including a novel architecture for modular inversion that enhances the viability of a classical algorithm for reversible arithmetic.

### 3. T2-z: Test-Time Optimization of Environment Latents for Robotic World Models
**Authors:** Chenyuan Zhou, Yining Hong, Huang Huang, Yunfan Jiang, Wenlong Huang, David Held, Vitor Campagnolo Guizilini, Yue Wang, Li Fei-Fei, Jiajun Wu, Leonidas Guibas, Yejin Choi
**Link:** https://arxiv.org/abs/2610.22364v1
**Summary:** The paper addresses the challenge of predicting how a robot's actions affect its environment, which often involves unobservable factors. The authors propose T2-Z, a method that optimizes environment-specific latents at test time to improve prediction accuracy without needing prior knowledge of those factors. The results show a significant reduction in prediction error and a notable increase in action success rates across various tasks, demonstrating the effectiveness of the approach in adapting to new environments.

### 4. CoDA: Co-Evolution of Data Engines and Action Policies
**Authors:** Tianjiao Yu, Zhilin Ou, Yifan Shen, Xinzhuo Li, Yuanzhe Liu, Onkar Kishor Susladkar, Fan Wang, Ismini Lourentzou
**Link:** https://arxiv.org/abs/2610.22362v1
**Summary:** The paper addresses the challenge of creating useful simulated environments for robot training that specifically help overcome the policy's failures. The authors present CoDA, a framework that allows a simulation engine and action policy to evolve together by sharing a memory of construction challenges and learning progress, which includes a new approach called Text2potential for effective supervision. The results show significant improvements in the robots' ability to succeed in tasks, with out-of-distribution success rising from 5.3% to 27.6% and varying perturbation scenarios showing substantial gains in performance after multiple training rounds.

### 5. PathFM: Fast Generative Forecasting of Multivariate Trajectories
**Authors:** Jiachen Yao, Xiyuan Zhang, Annan Yu, Boran Han, Abdul Fatir Ansari, Shuai Zhang, Michael Bohlke-Schneider, Bernie Wang
**Link:** https://arxiv.org/abs/2610.22358v1
**Summary:** The paper introduces PathFM, a novel model for forecasting multivariate time series trajectories, addressing the inadequacy of existing models that only predict individual quantiles without considering dependencies between future paths. By utilizing flow matching and a distilled sampler that shares computation across multiple forecasts, PathFM generates complete future trajectories rapidly, achieving competitive accuracy on standard benchmarks and outperforming existing methods in capturing complex variability. Its design enhances the practicality of generative forecasting for a variety of applications.

### 6. OmniVerifier-C1: Decomposed Graded Verifier for Rule-Governed Generative World Modeling
**Authors:** Bowei Liu, Xinchen Zhang, Xuhuan Li, Tianlin Zhang, Kaian Jiang, Jingwei Liu, Congyang Zhao, Yifei Qian, Junhong Liu, Zhiheng Li, Yujiu Yang, Yang Cai, Ling Yang
**Link:** https://arxiv.org/abs/2610.22355v1
**Summary:** The paper presents a novel verifier called OmniVerifier-C1 that enhances the assessment of multimodal generative models by breaking down complex prompts into detailed components and providing continuous scores rather than simple True/False judgments. This approach, which utilizes a Decoupled Reinforcement Learning strategy, improves the verifier's generalization abilities across various tasks. The key finding reveals that using pointwise graded evaluations leads to better performance in rule-governed world modeling scenarios compared to traditional binary assessments, underscoring the importance of accurate grading mechanisms in advanced generative systems.

### 7. Rethinking Routing Exploration in Modern Mixture-of-Experts
**Authors:** Bingcong Li, Hao Ma, Michael Muehlebach, Niao He, Yi Ma
**Link:** https://arxiv.org/abs/2610.22353v1
**Summary:** The paper addresses the challenge of effective routing in modern Mixture-of-Experts (MoE) models, which combine fine-grained segmentation and shared experts, leading to less exploratory routing. The authors propose MirrorMoE, which optimizes the routing process by adaptively suppressing unnecessary experts to enhance exploration. This approach consistently improves model performance across different scales by better utilizing the combinatorial potential of fine-grained expert segmentation.

### 8. FDE-Gym: The Last Mile of AI Delivery
**Authors:** Dongxu Yang, Hongda Yan, Renxin Wang, Baoli Zhang, Haojia Zuo, Ying Zhao, Youmin Chen, Xiaojian Liao, Congming Gao, Tianyang Jiang, Yixiao Chen, Qing Wang, Zhiguo Yu, Xiaqing Li, Yuhao Zhang, Jiawen Sun, Renzhe Xu, De Mi, Tiancheng Wu, Xianya Fu, Xuanlu Zhao, Bo Feng, Meixuan Ren, Guanming Lin, Ziheng Zhou, Xinhua Wang
**Link:** https://arxiv.org/abs/2610.22350v1
**Summary:** The paper addresses the challenge of delivering AI solutions in real-world scenarios where customer requirements are often ambiguous and unstated. It introduces FDE-Gym, a benchmark consisting of 95 delivery tasks from diverse sectors that allows agents to interact with scripted stakeholders within simulated environments. The key finding reveals that while the best-performing model achieved a score of 0.56, it only successfully resolved 14 out of the 95 tasks, highlighting the significant difficulties in uncovering unstated constraints and the complexities of meeting real customer needs effectively.

### 9. MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering
**Authors:** Shangheng Du, Jinxin Shi, Shuaiyu Zhang, Yiming Wu, Junpeng Zhao, Shiyang Feng, Xin Li, Liang He, Xiangchao Yan, Bo Zhang
**Link:** https://arxiv.org/abs/2610.22344v1
**Summary:** The paper presents MLExpert, a 35B Mixture-of-Experts model designed to autonomously enhance machine learning engineering (MLE) processes by optimizing long-horizon experimentation through effective feedback management. By utilizing a novel post-training method and a hierarchical outcome-guided supervision framework, MLExpert significantly improves the efficiency of model-directed experiments, demonstrating a medal rate increase from 37.9% to 72.7% on the MLE-Bench Lite, outperforming existing models. This approach shows promise not only in MLE but also in generalizing optimization capabilities across various tasks.

### 10. GeoState: Learning View-Decoupled Geometry States for 3D World Modeling
**Authors:** Hongchang Liu, Jian Liu, Yujuan Ding, Liang Peng, Xun Jiang, Fei Ma, Xing Xu, Yi Bin
**Link:** https://arxiv.org/abs/2610.22343v1
**Summary:** The paper addresses the challenge of predicting 3D world states without the complications introduced by camera perspective, which can obscure scene dynamics. The authors propose a method called GeoState, which uses a scene tokenizer to create a view-independent representation of the environment, allowing future scene states to be predicted without influence from camera movements. Their approach outperforms existing 3D models and maintains geometric consistency across different views while also demonstrating strong generalization capabilities.
