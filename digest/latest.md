---
## 2026-09-10

### 1. IdeaAMBIG: Benchmarking Implementation-Critical Gaps in Research-Idea Specifications
**Authors:** Yiling Ma, Yilun Zhao, Sihong Wu, Manasi Patwardhan, Arman Cohan
**Link:** https://arxiv.org/abs/2609.10539v1
**Summary:** The paper addresses the issue of inadequately specified research methods that hinder their successful implementation in practice. The authors developed IdeaAMBIG, a benchmark consisting of 660 instances that highlight gaps in implementation specifications, combining real-world examples and synthetic cases. Key findings indicate that while the best-performing model only recovered 9.6% of defects from specifications alone, its success rate improved significantly to 80.6% when given more context, underscoring the challenges in defect localization.

### 2. Likelihood-free inference with nuisance parameters through normalizing flows
**Authors:** Phil Assheton
**Link:** https://arxiv.org/abs/2609.10534v1
**Summary:** The paper addresses the challenge of performing likelihood-free inference when nuisance parameters are present, which complicates traditional statistical methods. The authors propose a novel approach using normalizing flows to uncover a near-pivotal statistic based solely on sample generation, and demonstrate its effectiveness by showing it can accurately identify familiar statistical tests while outperforming existing methods in terms of size and power, particularly for smaller sample sizes.

### 3. A positive resolution of the gap-entropy conjecture
**Authors:** P. M. Aronow, Nathan Kallus, Patrick Lopatto
**Link:** https://arxiv.org/abs/2609.10529v1
**Summary:** The paper addresses the gap-entropy conjecture in the context of identifying the best arm in a bandit problem with independent Gaussian distributions. The authors establish a bound on the expected number of samples required to reliably identify the optimal arm, showing it is directly related to the gaps between the optimal and suboptimal arms and the entropy of their distributions. Additionally, they present a uniform algorithm that operates efficiently across different problem instances, achieving performance close to this optimal sample complexity.

### 4. Characterizing Language Generation in the Limit: Finite Witnesses and a Separation-Width Hierarch
**Authors:** Xiaoyu Li, Andi Han, Jiaojiao Jiang, Junbin Gao
**Link:** https://arxiv.org/abs/2609.10525v1
**Summary:** The paper addresses the challenge of language generation in the limit, which involves generating valid unseen elements from an infinite language given finite samples. The authors develop a framework for characterizing when this is possible, based on the existence of finite positive witnesses that ensure an infinite overlap among activated targets. A key contribution is the introduction of a separation-width hierarchy to categorize the sizes of these witnesses, demonstrating the complexities and requirements of generating language effectively.

### 5. Show-Harness: Just a VLM Agent Can Play Robots
**Authors:** Yanzhe Chen, Zechen Bai, Zhijun Cao, Wenzheng Zeng, Kevin Qinghong Lin, Yiqi Lin, Guoqiang Liang, Kevin Yuchen Ma, Qiming Huang, Mike Zheng Shou
**Link:** https://arxiv.org/abs/2609.10522v1
**Summary:** The paper presents Show-Harness, a system that allows vision-language models (VLMs) to control robots by connecting their intent to specific actions through a semantic interface. This approach effectively enables both closed-source and small-scale open-source VLMs to perform robot control tasks with minimal fine-tuning. The key finding is that this method significantly enhances the capabilities of VLM agents, allowing them to generalize effectively across different tasks and robotic platforms without the need for extensive training.

### 6. Optimal Low-Rank Quantum State Tomography with Bounded-Sample Joint Measurements
**Authors:** Ashwin Nayak, Xingyu Zhou
**Link:** https://arxiv.org/abs/2609.10514v1
**Summary:** This paper addresses the challenge of low-rank quantum state tomography, specifically determining how many samples are needed to accurately estimate a quantum state while allowing measurements to act on multiple samples at once. The authors establish that the optimal number of samples required depends on both the rank of the state and the number of samples used in each joint measurement, showing an improvement of up to a factor of √t compared to single-sample measurements. A key finding is that when measuring groups of samples, a specific sample complexity formula can be applied, enhancing the efficiency of state estimation.

### 7. Quantum Feature Engineering for Credit Default Prediction: When and Why IQP Circuits Help Linear Classifiers
**Authors:** Menachem Finkelstein, Diana Legziel Levy, Zohar Yakhini, Sarel Cohen
**Link:** https://arxiv.org/abs/2609.10505v1
**Summary:** The paper investigates whether Instantaneous Quantum Polynomial-time (IQP) circuits can enhance credit default prediction by generating features that improve the performance of linear classifiers over traditional methods like Kernel PCA. Using a dataset of financial attributes, the authors found that integrating features derived from an 8-qubit IQP circuit significantly increased the F1 score of a Logistic Regression model, surpassing the results obtained from other classifiers and feature extraction techniques. This suggests that IQP circuits can effectively amplify valuable information in the data when appropriately selected.

### 8. Cross-Model Agreement as a Deployment-Time Reliability Signal for Automatic Polyp Segmentation
**Authors:** Siddharth Gupta, Jitin Singla
**Link:** https://arxiv.org/abs/2609.10495v1
**Summary:** The paper addresses the challenge of ensuring reliability in automatic polyp segmentation during real-time colonoscopy, where ground-truth annotations are not available. It introduces a framework called Referee-Based Quality Estimation (RBQE), which measures the agreement between a primary segmentation model and an independent referee model. The key finding is that this agreement can serve as a strong reliability signal, with the best-performing referee achieving a ROC-AUC of 0.960, thus enabling more reliable predictions and allowing for selective rejection of uncertain cases.

### 9. IBIB: A Protocol for Measuring Enterprise AI Systems by Serving Route, Not Model Identifier
**Authors:** Blake Stenstrom, Charangan Vasantharajan, Brian Sathianathan
**Link:** https://arxiv.org/abs/2609.10494v1
**Summary:** The paper presents the IBIB protocol to improve the measurement of enterprise AI systems, focusing on the actual serving routes instead of just model identifiers, which often lead to measurement errors. The approach involves a structured verification process to ensure reliable evaluations of AI capabilities under real-world conditions. Key findings indicate that AI system performance can vary significantly based on serving routes, with important implications for understanding and reporting AI capabilities in enterprise settings.

### 10. Learning with Covariance Matrices: Principal Component Analysis Meets Learning with Graphs
**Authors:** Saurabh Sihag, Andrea Cavallo, Elvin Isufi, Gonzalo Mateos, Alejandro Ribeiro
**Link:** https://arxiv.org/abs/2609.10490v1
**Summary:** This paper introduces variance neural networks (VNNs), a type of graph neural network that operates on covariance matrices, which represent pairwise statistical dependencies commonly found in data. The authors provide theoretical insights linking VNNs to principal component analysis (PCA) and demonstrate their stability and transferability across various datasets. A key contribution is the potential of VNNs to improve learning methods in fields like computational neuroscience, particularly in analyzing neuroimaging data related to brain aging and neurodegenerative conditions.
