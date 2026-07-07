---
## 2026-07-07

### 1. From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model
**Authors:** Wenhao Li, Xueying Jiang, Quanhao Qian, Deli Zhao, Shijian Lu, Gongjie Zhang, Ran Xu
**Link:** https://arxiv.org/abs/2607.05396v1
**Summary:** The paper addresses the challenge of deploying robots in varying camera setups, which can hinder the performance of existing Vision-Language-Action (VLA) models that require specific camera positioning. To overcome this, the authors introduce CamVLA, a model that enables robots to operate using only a single camera image by predicting actions independent of camera geometry and dynamically determining their relationship with the robot. The results demonstrate that CamVLA significantly enhances the success rate of robot actions across different unseen viewpoints, making it a robust solution for real-world applications.

### 2. Weak-to-Strong Generalization via Direct On-Policy Distillation
**Authors:** Shiyuan Feng, Huan-ang Gao, Haohan Chi, Hanlin Wu, Zhilong Zhang, Zheng Jiang, Bingxiang He, Wei-Ying Ma, Ya-Qin Zhang, Hao Zhou
**Link:** https://arxiv.org/abs/2607.05394v1
**Summary:** The paper addresses the challenge of efficiently improving large language models using reinforcement learning with verifiable rewards (RLVR), which is resource-intensive. It introduces Direct On-Policy Distillation (Direct-OPD), a method that transfers the behavior changes induced by RL from a smaller model to a stronger one without needing traditional reward modeling. The key finding is that this approach significantly enhances the performance of the larger model, as demonstrated by improving the Qwen3-1.7B model's score on the AIME 2024 task from 48.3% to 62.4% within just four hours of training on powerful GPUs.

### 3. Interpretable Human-Label-Free Deep Learning for Real-Bogus Classification with Uncertainty Quantification
**Authors:** Raphaël Bonnet-Guerrini, Bruno Sanchez, Dominique Fouchez, Benjamin Racine, Maya Guy, Mariam Sabalbal, Manal Yassine, Vincenzo Piuri
**Link:** https://arxiv.org/abs/2607.05393v1
**Summary:** This paper addresses the challenge of classifying transient astronomical events as real or bogus without relying on costly human labels. The authors propose a novel deep learning framework that uses simulated data and a dual-network approach to handle different levels of label noise, providing an efficient way to quantify uncertainty in the classifications. The key contribution is a method that effectively performs Real-Bogus classification under conditions of class contamination and achieves strong performance and calibrated uncertainties, making it suitable for future astronomical surveys.

### 4. LLM-as-a-Verifier: A General-Purpose Verification Framework
**Authors:** Jacky Kwok, Shulu Li, Pranav Atreya, Yuejiang Liu, Yixing Jiang, Chelsea Finn, Marco Pavone, Ion Stoica, Azalia Mirhoseini
**Link:** https://arxiv.org/abs/2607.05391v1
**Summary:** The paper introduces LLM-as-a-Verifier, a novel framework that allows large language models (LLMs) to evaluate the correctness of solutions in various tasks by generating continuous scores rather than discrete ratings. This approach improves the granularity and accuracy of the verification process, enabling better distinction between successful and unsuccessful solutions while also enhancing sample efficiency in reinforcement learning scenarios. Key results demonstrate significant performance improvements on multiple benchmarking tasks, positioning LLM-as-a-Verifier as a state-of-the-art tool for both verification and task progress estimation.

### 5. Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in Agentic Visual Generation
**Authors:** Haozhe Wang, Weijia Feng, Jinpeng Yu, Che Liu, Ping Nie, Fangzhen Lin, Jiaming Liu, Ruihua Huang, Jimmy Lin, Wenhu Chen, Cong Wei
**Link:** https://arxiv.org/abs/2607.05382v1
**Summary:** The paper addresses the issue of visual generators confidently creating content beyond their trained knowledge, leading to significant performance drops on new and diverse prompts. The authors introduce a co-training framework that combines training and search tools to enhance generators' ability to adapt to evolving knowledge boundaries. The key contribution is the development of a dataset and methodology that enables these generators to improve over time, effectively meeting user requests that require up-to-date information.

### 6. What Does a Discrete Diffusion Model Learn?
**Authors:** Rodrigo Casado Noguerales, Bernhard Schölkopf, Thomas Hofmann, Aran Raoufi
**Link:** https://arxiv.org/abs/2607.05381v1
**Summary:** The paper investigates what discrete diffusion models learn during their training, specifically whether they act as denoisers, score estimators, or bridge plug-in predictors. By rigorously deriving the continuous-time Markov chain evidence lower bound (ELBO) and establishing the Oracle Distance theorem, the authors show that this bound directly relates to data entropy and provides a unique optimal learning strategy. Their framework clarifies the relationships between various loss functions in the literature and demonstrates how each noise process achieves the same optimal negative ELBO, highlighting nuanced behaviors across different diffusion strategies.

### 7. TabPack: Efficient Hyperparameter Ensembles for Tabular Deep Learning
**Authors:** Yury Gorishniy, Akim Kotelnikov, Ivan Rubachev, Artem Babenko
**Link:** https://arxiv.org/abs/2607.05380v1
**Summary:** TabPack addresses the challenge of hyperparameter tuning in deep learning for tabular data by introducing an ensemble of multilayer perceptrons (MLPs) that can efficiently sample and train with varying hyperparameters during training. This approach eliminates the need for precise tuning by allowing users to specify only ranges for hyperparameters, leading to strong performance without extensive effort. In experiments, TabPack matched the results of highly tuned methods while significantly reducing computation time and resource requirements.

### 8. CompactionRL: Reinforcement Learning with Context Compaction for Long-Horizon Agents
**Authors:** Yujiang Li, Zhenyu Hou, Yi Jing, Jie Tang, Yuxiao Dong
**Link:** https://arxiv.org/abs/2607.05378v1
**Summary:** The paper addresses the challenge of long-horizon tasks in reinforcement learning that exceed context windows of large language models (LLMs). It introduces CompactionRL, a novel training strategy that utilizes context compaction to summarize past interactions, allowing LLMs to learn effectively from extended trajectories. The approach yields significant performance improvements on coding benchmarks, demonstrating its effectiveness in enhancing the capabilities of both GLM-4.5-Air and GLM-4.7-Flash models.

### 9. Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation
**Authors:** Jiaqi Peng, Xiqian Yu, Delin Feng, Yuqiang Yang, Wenzhe Cai, Jing Xiong, Ganlin Yang, Jinliang Zheng, Jiafei Cao, Xueyuan Wei, Jiangmiao Pang, Yuan Shen, Tai Wang
**Link:** https://arxiv.org/abs/2607.05377v1
**Summary:** The paper presents Cortex, a framework designed to improve long-horizon manipulation tasks in embodied agents, which traditional models struggle with due to their limited reliance on current observations. Cortex integrates high-level planning and low-level execution through a set of standardized manipulation skills, allowing it to efficiently annotate extensive video data and train on diverse scenarios. The key contribution is its ability to perform better than existing models on complex tasks, enabling zero-shot execution of real-world multi-stage experiments, demonstrating significant advancements in handling planning and execution gaps.

### 10. Fitted Occupancy-Ratio Evaluation without Bellman Completeness
**Authors:** Lars van der Laan, Nathan Kallus
**Link:** https://arxiv.org/abs/2607.05375v1
**Summary:** This paper addresses the challenge of estimating occupancy ratios in offline reinforcement learning, which are crucial for off-policy evaluation. The authors introduce a new method called Fitted Occupancy-Ratio Evaluation (FORE), which uses a fixed-point approach to efficiently project occupancy ratios onto a specific class of distributions. The key contribution is the establishment of discounted occupancy-ratio realizability as a sufficient condition for effective offline policy evaluation, eliminating the need for traditional completeness assumptions.
