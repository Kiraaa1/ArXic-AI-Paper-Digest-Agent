---
## 2026-08-25

### 1. How to Train a Critic Stably and Efficiently
**Authors:** Penghui Qi, Xiangxin Zhou, Wee Sun Lee
**Link:** https://arxiv.org/abs/2608.23566v1
**Summary:** The paper addresses the instability of training critics in reinforcement learning, which can hinder their effectiveness compared to group-based methods. The authors propose a new approach called Best-Practice Critic Optimization (BPCO), which integrates various techniques to stabilize critic training. The key result demonstrates that BPCO consistently outperforms traditional critic-based methods and matches or surpasses group-based methods while only requiring one response per prompt.

### 2. ReWorld: An Interactive World Model with Long-Horizon Memory
**Authors:** Zhifei Chen, Luozhou Wang, Guibao Shen, Dongyu Yan, Shuai Yang, Tianshuo Xu, Yihua Du, Wei Wang, Tianyi Gui, Lianghua Huang, Yingcong Chen
**Link:** https://arxiv.org/abs/2608.23565v1
**Summary:** ReWorld addresses the challenge of creating an interactive world model that can remember user interactions over long periods while still delivering real-time performance. The approach involves separating short-term control from long-term memory during training, using a mixed attention mechanism with bounded memory at inference, and combining various high-fidelity video sources. The key achievement is that ReWorld outperforms existing models in terms of control precision and video quality, able to regenerate previous views even after extended interactions without losing memory effectiveness.

### 3. SWE Refactor Bench: Can Coding Agents Complete a Long-Horizon, Whole-Repository Stack Migration?
**Authors:** Deyao Hong, Yizhe Chi, Wenyi Li, Xiaoqiu Wang, Mingju Gao, Kaisen Yang, Bingxiang He, Youjie Zheng, Calvin Xiao, Qinhuai Na
**Link:** https://arxiv.org/abs/2608.23564v1
**Summary:** The paper addresses the challenge of automating long-horizon, whole-repository migrations in software systems that have accrued technical debt, which is typically a manual and costly process. It introduces the SWE Refactor Bench, a benchmark designed to assess coding agents' ability to not only perform migrations but also ensure behavioral correctness through a three-stage evaluation protocol. The key finding indicates that despite various attempts by advanced coding agents, only a small percentage (5.4%) successfully complete both the migration and maintain correctness, highlighting the distinct challenges of migration completeness and behavioral correctness in coding tasks.

### 4. EG-ARSA: An Expert-Grounded Open Model for Visual Road Safety Auditing in Low-Resource Settings
**Authors:** Md Thamed Bin Zaman Chowdhury, Moazzem Hossain
**Link:** https://arxiv.org/abs/2608.23563v1
**Summary:** The paper addresses the challenge of road safety auditing in low-resource countries, which often lack reliable data and qualified auditors. It introduces an innovative AI framework, Expert-Grounded Distillation (EGD), that leverages expert knowledge to train a compact vision-language model for conducting visual road safety audits. The key contribution is the development of the EG-ARSA model, which significantly enhances risk assessment accuracy compared to existing models, making proactive road safety evaluations more feasible in resource-constrained settings.

### 5. Physics-Constrained Deep Learning Model for Contactless Blood Pressure Monitoring from Triaxial Bodyseismography
**Authors:** Yuanyuan Zhang, Yida Zhang, Jiahui Li, Yuyan Wu, Fei Dou, Xiao Yin, Zhenlin An, Hae Young Noh, Wenzhan Song
**Link:** https://arxiv.org/abs/2608.23562v1
**Summary:** The paper addresses the challenge of accurately monitoring blood pressure using ballistocardiography (BCG) signals, which can be affected by variations in body dynamics. The authors propose a novel framework called Phy-BP that leverages triaxial bodyseismography (BSG) combined with an adaptive quality-control algorithm and a physical model of wave propagation to improve the robustness and accuracy of BP estimates. The results show that Phy-BP effectively filters low-quality data and enhances the model's performance even with limited training samples.

### 6. Provably adaptive sampling with uniform and remasking discrete diffusion models
**Authors:** Daniil Dmitriev, Zhihan Huang, Yuting Wei
**Link:** https://arxiv.org/abs/2608.23554v1
**Summary:** The paper addresses the challenge of improving sampling efficiency in discrete diffusion models, which typically struggle with high ambient dimensions. The authors propose a first-order sampler that updates coordinates in parallel and can correct errors during sampling, demonstrating that the number of required discretization steps depends on the distribution's intrinsic structure rather than its dimensionality. Their key result shows that an adaptive sampling strategy can achieve a specified accuracy with significantly fewer steps than previously thought, thereby enhancing the practicality of these models in high-dimensional settings.

### 7. Prime Agent: A Self-Improving RLM Harness
**Authors:** Seth Karten, Alex L. Zhang, Kevin Thomas, Sebastian Müller, Elie Bakouch, Daniel Auras, Mika Senghaas, Fares Obeid, Konstantin Dunas, Johannes Hagemann, Sami Jaghouar
**Link:** https://arxiv.org/abs/2608.23552v1
**Summary:** The Prime Agent framework addresses the limitations of language models in handling long-term tasks by providing a system that allows for external information processing and coordination between subagents. It implements a persistent computing environment and a structured memory system that enhances the model's capabilities, leading to significant improvements in performance, such as raising the ARC-AGI-3 RHAE Best@1 score from 30% to 95.5%. This system also promotes efficient collaboration among subagents, further optimizing tasks like coding and game strategy development.

### 8. ConvergeFlow: Language Flow with Provable Convergence to Token Embeddings
**Authors:** Na Li, Yuchen Jiao, Changxiao Cai, Gen Li
**Link:** https://arxiv.org/abs/2608.23551v1
**Summary:** The paper presents ConvergeFlow, a novel language model that addresses the limitation of existing continuous language models, which struggle to reliably generate valid token embeddings. By constraining the data predictor to the convex hull of token embeddings and using a mean squared error objective for training, the authors demonstrate that their flow-based model can effectively converge to valid outputs without needing a decoder trained with cross-entropy loss. Experiments show that ConvergeFlow performs competitively with both continuous and discrete language models, highlighting its potential in the field.

### 9. Robustness of Anomaly Detection Models for Industrial Control Systems under Training-Time Data Contamination
**Authors:** Mustafa Umut Ozbek, Taiwo Ojo, Pooria Madani, Khalil El-Khatib, Li Yang
**Link:** https://arxiv.org/abs/2608.23547v1
**Summary:** This paper investigates the impact of contaminated training data on machine learning anomaly detection models used in industrial control systems. The authors tested 11 different anomaly detectors using various methods of data contamination, finding that the robustness of these models is highly variable and dependent on the specific algorithm used. Key findings indicate that while some models like PCA and SVM are relatively stable under such conditions, local-density detectors are significantly affected, emphasizing the critical need for ensuring data integrity during training.

### 10. Inertial Manifold Neural Operator for Dissipative Time-Dependent Partial Differential Equations
**Authors:** Xiaoyang Xie, Clarence W. Rowley
**Link:** https://arxiv.org/abs/2608.23546v1
**Summary:** The paper presents the Inertial Manifold Neural Operator (IMNO), a novel approach for solving dissipative time-dependent partial differential equations (PDEs) by exploiting their effective low-dimensional dynamics. IMNO improves on traditional neural operator methods by enhancing physical interpretability and stability during long-term predictions, and includes a shift-equivariant variant to maintain input-output spatial consistency. The results show that IMNO outperforms existing methods in accuracy and efficiency for these types of equations.
