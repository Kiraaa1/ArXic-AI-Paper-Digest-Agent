---
## 2026-11-08

### 1. Conformal Prediction for Time-Dependent PDEs
**Authors:** Joshua Stiller, Annika Schneider, Eyke Hüllermeier
**Link:** https://arxiv.org/abs/2611.08409v1
**Summary:** The paper addresses the challenge of uncertainty quantification in scientific machine learning, specifically for time-dependent partial differential equations. It highlights that traditional conformal prediction methods can fail to provide accurate coverage guarantees in these settings, due to the complex relationships between distributions at different times. The authors propose a refined approach using weighted conformal prediction, which allows for reliable coverage assurances as time progresses, despite the challenges posed by discretization in simulations.

### 2. Social Humanoid: Socially Responsive Human-Humanoid Interaction
**Authors:** Vongani H. Maluleke, James Ni, Kie Horiuchi, Lea Wilken, Jiahui Lei, Evonne Ng, Roei Herzig, Jitendra Malik, Trevor Darrell, Angjoo Kanazawa
**Link:** https://arxiv.org/abs/2611.08407v1
**Summary:** The paper addresses the challenge of humanoid robots being unable to effectively coordinate with humans due to training as solitary agents. The authors propose a hierarchical system called Social Humanoid that enables responsive, whole-body motion based on human movements, utilizing a novel two-phase adaptive retargeting training method. Their work results in a new benchmark of 260 hours of human-humanoid interactions, demonstrating the robot's ability to execute coordinated and human-aligned behaviors across various interaction scenarios.

### 3. StepBack: Step-Level Error-Localized Resampling for Efficient Test-Time Reasoning
**Authors:** Yang Ouyang, Jung-Eun Kim
**Link:** https://arxiv.org/abs/2611.08403v1
**Summary:** The paper addresses the inefficiency of self-consistency methods in test-time reasoning, which often require extensive sampling of complete reasoning paths. The authors introduce StepBack, a technique that focuses on identifying and resampling only the segments of reasoning trajectories that are likely to contain errors, significantly reducing the number of tokens used in the process. StepBack achieves accuracy comparable to traditional methods while decreasing token usage by up to 41.26%, and it can be integrated with other adaptive inference methods for enhanced efficiency.

### 4. Synthesis of Ovarian Cancer Multi-Omics Datasets: A Biology-Informed Evaluation Framework
**Authors:** Déborah Boyenval, Alina Malyutina, Jaana Oikkonen, Sammeli Liikkanen, Sampsa Hautaniemi
**Link:** https://arxiv.org/abs/2611.08394v1
**Summary:** The paper addresses the challenge of creating synthetic multi-omic datasets for ovarian cancer research, which are often expensive and hard to share. The authors propose a new evaluation framework to assess the quality of synthetic RNA expression and copy-number variation profiles based on their biological relevance. They adapt multiple generative models to produce these profiles and demonstrate that one model outperforms the others in preserving critical biological structure, providing a valuable reference for future synthetic dataset generation efforts.

### 5. Learning a patient world model for health system simulation in intensive care
**Authors:** Yingtai Li, Ruoyan Wang, Yu Li, Shaohua Kevin Zhou
**Link:** https://arxiv.org/abs/2611.08392v1
**Summary:** The paper addresses the challenge of simulating healthcare strategies in intensive care units (ICUs) by proposing a learned patient world model that captures the dynamics of patient states over time using neural networks trained on electronic health records. This model can be applied across various clinical scenarios without needing to redefine state transitions, allowing for efficient evaluation of different care policies. Key results show that this approach effectively predicts ICU demands and outcomes, demonstrating a significant advantage over traditional compact state models by capturing nuanced recovery variations and their impacts on resource allocation.

### 6. Hybrid Machine Learning for Imbalanced Landing-Phase Safety Event Prediction from Flight Data
**Authors:** Taha Asghar, Bilal Mufti, Syed Qasim Zaheer, Luqman Ahmed
**Link:** https://arxiv.org/abs/2611.08386v1
**Summary:** This paper addresses the challenge of predicting rare safety events during the landing phase of flight, which is complicated by imbalanced data across multiple variable types. The authors propose a hybrid framework that combines LSTM autoencoders for detecting behavioral deviations with an XGBoost classifier to predict different types of issues. Their method achieves high detection accuracy, demonstrating the effectiveness of combining statistical features with deep learning techniques, particularly in adapting to varying data availability across different airports.

### 7. FedReason: Large Language Models as Weight-Space Meta-Aggregators for Heterogeneous Federated Learning
**Authors:** Ali Mohammadi Ruzbahani, Abbas Yazdinejad, Hadis Karimipour
**Link:** https://arxiv.org/abs/2611.08383v1
**Summary:** The paper introduces FedReason, a system that utilizes large language models to dynamically select aggregation rules in heterogeneous federated learning without requiring server-side training. By analyzing client model weights and generating aggregation programs in a sandboxed environment, FedReason demonstrates a notable average improvement of 1.26 percentage points over the traditional FedAvg method when tested on CIFAR-10 and CIFAR-100 datasets, while effectively handling issues such as label skew and Byzantine clients.

### 8. Module-Aware Optimization for Graph Neural Networks
**Authors:** Guy Hadad, Haggai Roitman, Moshe Eliasof, Bracha Shapira
**Link:** https://arxiv.org/abs/2611.08379v1
**Summary:** This paper addresses the limitations of existing optimizers for Graph Neural Networks (GNNs), specifically how traditional methods can amplify parameter updates due to the unique structure of graph-propagated features. The authors propose GraphMuon, a graph-aware optimizer that adjusts updates based on the covariance structure of layer inputs, leading to improved performance. Their results show that GraphMuon provides significant speedups in achieving lower validation loss compared to AdamW across various GNN tasks, while also maintaining or improving prediction accuracy.

### 9. Muir: Linear Attention with Sensitivity-Allocated Gating and Matched-Filter Readout
**Authors:** Tushaar Gangavarapu, Gil Tabak, Clemens JS Schaefer
**Link:** https://arxiv.org/abs/2611.08376v1
**Summary:** The paper introduces Muir, a novel linear attention model that enhances the efficiency of context handling in transformer architectures by optimizing the way attention states are updated and read out. By integrating gating mechanisms based on the sensitivity of these updates and employing a parallel training method, Muir improves performance metrics like perplexity, commonsense reasoning accuracy, and recall on various tasks compared to existing models, while also achieving faster training speeds. Overall, Muir demonstrates significant advancements in maintaining model performance during extensive context processing without increasing computational demands.

### 10. MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation
**Authors:** Sateesh Kumar, Arnav Balaji, Arpit Bahety, Skand Peri, Georgios Pavlakos, Roberto Martín-Martín
**Link:** https://arxiv.org/abs/2611.08372v1
**Summary:** The paper addresses the challenge of training robots to perform manipulation tasks from varying camera viewpoints, which is critical in mobile manipulation scenarios where the robot's base pose can change. The authors propose MOMASPLAT, a novel framework that uses advanced techniques to synthesize complete manipulation trajectories by reconstructing both the environment and the manipulated objects in 3D from multi-view observations collected during training. Testing across multiple real-world tasks, MOMASPLAT significantly enhances the robot's success rate in handling unseen base poses, demonstrating its effectiveness in reducing reliance on extensive real-world data collection.
