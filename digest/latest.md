---
## 2026-11-09

### 1. On Agentic Manipulation Policies
**Authors:** Chen Chen, Omid Bagherieh, Naveen Nikamanth Appiah Balaji, Jesse T. Gonzalez, Negin Heravi, Fahad Islam, Xueting Li, Jean-Baptiste Regli, Kejia Ren, Petr Švec, David J. Yoon, Matthias Müller, Vladlen Koltun
**Link:** https://arxiv.org/abs/2611.09892v1
**Summary:** This paper addresses the limitations of specialist policies in robot manipulation by introducing agentic manipulation policies (AMPs), which use a generalist AI model to directly control manipulators without relying on demonstrations or task-specific training. The researchers present AMP1, a versatile framework that achieves significantly higher success rates on manipulation tasks compared to leading models, successfully completing 85.6% of trials in a zero-shot setting, while also demonstrating the ability to learn from experience when equipped with a memory store. Overall, AMPs show greater generality and robustness, advancing the field of robotic manipulation.

### 2. CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse
**Authors:** Peter Belcak, Greg Heinrich, Saurav Muralidharan, Shizhe Diao, Pavlo Molchanov
**Link:** https://arxiv.org/abs/2611.09891v1
**Summary:** The paper addresses the inefficiency of large language models (LLMs) that often solve problems from scratch, leading to redundant computations. The authors propose a method called agentic reasoning caching (ARC), which utilizes reasoning traces from LLMs to create efficient CPU-executable caches for reusing solutions to previously solved tasks. The key result is that ARCs can match the performance of state-of-the-art LLMs on complex mathematical and scientific problems while being significantly cheaper and more robust.

### 3. On the (non-)closedness of the set of ReLU networks
**Authors:** Eloi Martinet, Leon Bungert
**Link:** https://arxiv.org/abs/2611.09887v1
**Summary:** This paper investigates the closedness properties of sets of ReLU neural networks, specifically focusing on one hidden layer networks with a limited number of neurons. The authors demonstrate that this set is weakly closed in a specific function space, which ensures that certain energy minimization problems achieve optima within this set. Additionally, they show that sets of ReLU networks with two hidden layers are not closed, contradicting previous conjectures in the field.

### 4. FlowMoP: Stochastic Multi-Person Motion Prediction
**Authors:** Aadya Agrawal, Ho Kei Cheng, Alexander Schwing
**Link:** https://arxiv.org/abs/2611.09882v1
**Summary:** The paper addresses the challenge of predicting the future motions of multiple people, which is inherently uncertain and influenced by various social interactions. The authors introduce a conditional flow matching framework that generates diverse motion predictions for each agent while considering the movements of neighboring agents. Their method outperforms existing deterministic approaches on benchmark datasets and establishes a new baseline for motion prediction in soccer, showing improved accuracy by efficiently modeling social interactions.

### 5. Graded convolutional networks: scale invariance without the scale and robustness to unknown blur
**Authors:** Tanush Shaska
**Link:** https://arxiv.org/abs/2611.09878v1
**Summary:** This paper addresses the challenge of scale invariance in image processing, particularly under unknown blur conditions. The authors introduce graded convolutional networks that utilize a mathematical framework based on local graded convolutions, allowing for better feature extraction that is robust to variations in scale. They demonstrate that their approach significantly improves classification accuracy on blurred images, with notable performance gains on benchmark datasets like MNIST, outperforming traditional methods.

### 6. On the Reliability of Majority-Vote Pseudo-Labels in Test-Time Reinforcement Learning
**Authors:** Haoyu Wang, Ru Wang, Yuanyuan Wang, Jiaxian Guo, Mingming Gong
**Link:** https://arxiv.org/abs/2611.09872v1
**Summary:** The paper addresses the issue of unreliable pseudo-labels generated during test-time reinforcement learning (TTRL) when adapting pretrained language models to new, unlabeled data. It introduces the Prompt-Conditional Distributionally Robust DPO (PC-Dr.DPO) method, which adjusts the reliability of updates based on observed vote consistency, and incorporates a caching mechanism to minimize forgetting. The key finding is that PC-Dr.DPO performs as well as or better than existing TTRL methods across multiple benchmarks and models, demonstrating improved reliability and adaptation in the learning process.

### 7. CodeQuant2: Enhanced Outlier Mitigation and Adaptive Clustering for Low-Precision LRMs
**Authors:** Xingyu Liu, Xiangyang Yin, Tianhua Xia, Haiyu Wang, Sai Qian Zhang
**Link:** https://arxiv.org/abs/2611.09868v1
**Summary:** The paper addresses the problem of poor performance in low-precision large reasoning models (LRMs) during inference due to significant activation fluctuations, particularly in the early decoding steps. The authors introduce CodeQuant2, a clustering-based look-up table quantization framework that effectively manages activation outliers and optimizes calibration sample selection aligned with reasoning behavior. As a result, CodeQuant2 significantly enhances accuracy on reasoning benchmarks and achieves up to 2.85 times faster performance compared to BF16 quantization.

### 8. GRAC: Graph-Based Retrieval-Augmented Captioning for Surgical Scene Description
**Authors:** Rochak Dhakal, Chen Zhao, Soup Cobb, Xin Qian, Xiaofeng Yang, Weihua Zhou
**Link:** https://arxiv.org/abs/2611.09866v1
**Summary:** The paper presents GRAC, a novel framework that automates the generation of surgical scene descriptions by using graph-based representations to capture the relationships between instruments, actions, and anatomical structures in surgery. By retrieving relevant examples from training data and conditioning on them, GRAC significantly improves the quality and accuracy of generated captions. It outperforms existing methods on benchmark datasets, demonstrating enhanced language quality and factual correctness in surgical documentation.

### 9. Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation
**Authors:** Xun Tu, Minghao Zou, Karthik Desingh
**Link:** https://arxiv.org/abs/2611.09864v1
**Summary:** The paper addresses the challenge of mobile manipulators needing to coordinate movement and manipulation to rearrange large objects, which can be affected by the choice of grasp. The authors introduce Grasp-TAGS, a framework that uses reinforcement learning to select optimal grasps based on task-specific goals, and distill this knowledge into a more efficient utility network. The key result shows that Grasp-TAGS significantly improves rearrangement success rates, achieving 89.84% success compared to 79.87% with traditional single-grasp methods.

### 10. Flow-Guided Target-Space Alignment via Path Consistency
**Authors:** Ruizhi Yuan, Zeqiu Yu, Wei Gao, Wei Chen, Xiwei Tang, Lu Tang
**Link:** https://arxiv.org/abs/2611.09863v1
**Summary:** The paper addresses the challenge of effectively aligning a source modality with a target modality's fixed space for multimodal data analysis, ensuring that both global structure and instance-level correspondence are maintained. The authors introduce FlowAlign, a method that utilizes conditional flow matching to guide the alignment process during training, rather than just at inference. Their experiments show that FlowAlign enhances the accuracy of instance-level correspondences while preserving the overall structure of the target space across various modalities.
