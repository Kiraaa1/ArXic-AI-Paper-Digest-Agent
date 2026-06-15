---
## 2026-06-15

### 1. Gaze Heads: How VLMs Look at What They Describe
**Authors:** Rohit Gandikota, David Bau
**Link:** https://arxiv.org/abs/2606.14703v1
**Summary:** This paper investigates how vision-language models (VLMs) effectively describe images, introducing the concept of "gaze heads," specific attention heads that track the image regions being described. By analyzing these heads using comic strips as a controlled environment, the authors demonstrate that manipulating gaze heads allows for precise control of the model's focus and can redirect its descriptive output with high accuracy. This approach highlights a new method for steering VLM behavior in real-time without the need for retraining, and the findings are applicable across different model sizes and architectures.

### 2. ClinHallu: A Benchmark for Diagnosing Stage-Wise Hallucinations in Medical MLLM Reasoning
**Authors:** Sicheng Yang, Hangjie Yuan, Wenjun Zhang, Jinwang Wang, Yichen Qian, Weihua Chen, Fan Wang, Lei Zhu
**Link:** https://arxiv.org/abs/2606.14697v1
**Summary:** The paper introduces ClinHallu, a benchmark aimed at diagnosing and addressing stage-wise hallucinations in medical multimodal large language models (MLLMs), which are critical for clinical decision-making. By analyzing the sources of hallucinations—such as visual misrecognition and flawed reasoning—the benchmark comprises 7,031 validated instances with structured reasoning traces. The study demonstrates that using these traces for fine-tuning significantly reduces hallucinations, offering a valuable tool for improving the reliability of medical MLLMs.

### 3. Persona-Pruner: Sculpting Lightweight Models for Role-Playing
**Authors:** Jinsu Kim, Jihoon Tack, Noah Lee, Jongheon Jeong
**Link:** https://arxiv.org/abs/2606.14695v1
**Summary:** The paper addresses the inefficiency of using full language models for role-playing applications, where multiple non-playable characters (NPCs) are needed. The authors introduce Persona-Pruner, a framework that identifies and isolates the parts of a model needed for specific personas, allowing for the creation of lighter models without significantly sacrificing performance. Their approach demonstrates a notable reduction in performance degradation—up to 93.8% less compared to existing pruning methods—while still retaining the general capabilities of the language model.

### 4. AdaSR: Adaptive Streaming Reasoning with Hierarchical Relative Policy Optimization
**Authors:** Junlong Tong, Wenqi Xu, Yingqi Fan, Anhao Zhao, Xuan Lu, Yang Tan, Xiaoyu Shen
**Link:** https://arxiv.org/abs/2606.14694v1
**Summary:** The paper presents AdaSR, a framework designed to improve reasoning in dynamic environments, such as audio and video streams, by enabling models to reason and adapt their computation while processing incoming data. It introduces Hierarchical Relative Policy Optimization (HRPO), which allows for a more nuanced approach to policy optimization across different reasoning phases. The key contribution is that AdaSR demonstrates improved reasoning accuracy and computational efficiency compared to traditional supervised methods, particularly in terms of managing processing latency.

### 5. Learning Coordinated Preference for Multi-Objective Multi-Agent Reinforcement Learning
**Authors:** Pengxin Wang, Lihao Guo, Yi Xie, Bo Liu, Siyang Cao, Jingdi Chen
**Link:** https://arxiv.org/abs/2606.14693v1
**Summary:** The paper addresses the challenge of coordinating decision-making among multiple agents in environments with conflicting objectives. It introduces a method called Preference Coordinated Multi-agent Policy Optimization (PCMA), which enables agents to learn specific preferences that enhance their collaboration. The findings demonstrate that PCMA not only improves overall performance in multi-objective scenarios but also facilitates better trade-off coordination among agents.

### 6. CORA: Analyzing and bridging thinking-answer gap in Multimodal RLVR via Consistency-Oriented Reasoning Alignment
**Authors:** Jiayue Cao, Zhicong Lu, Xuehan Sun, Wei Jia, Hongling Zheng, Changyuan Tian, Zichuan Lin, Wenqian Lv, Nayu Liu
**Link:** https://arxiv.org/abs/2606.14691v1
**Summary:** The paper addresses the problem of inconsistency between the reasoning process and final answers in reinforcement learning with verifiable rewards (RLVR) for large vision-language models. It introduces a new method called Consistency-Oriented Reasoning Alignment (CORA), which enhances semantic consistency in reasoning by integrating a consistency reward model and a Hybrid Reward Advantage Splitting technique. The key result shows that CORA significantly improves task performance and reduces inconsistencies in reasoning outputs across various multimodal reasoning benchmarks.

### 7. A Complexity Measure for Active Learning in Multi-group Mean Estimation
**Authors:** Abdellah Aznag, Rachel Cummings, Adam N. Elmachtoub
**Link:** https://arxiv.org/abs/2606.14690v1
**Summary:** This paper addresses the challenge of optimizing sample allocation in active learning for multi-group mean estimation, specifically minimizing the worst-case uncertainty across different groups. The authors establish a new lower bound on this problem that considers factors like budget, uncertainty distribution, and a novel measure called Variance Local Curvature (VLC), which assesses information gained from variance changes. Their results demonstrate that this framework achieves near-optimal performance in many scenarios and highlights significant gaps in instances with high variance disparity among groups.

### 8. Flood and Harvest: The Provable Necessity of Trivia for Generating Valuable Mathematics via the Lens of Language Generation in the Limit
**Authors:** Xiaoyu Li, Andi Han, Dai Shi, Zheng Gao, Jiaojiao Jiang, Junbin Gao
**Link:** https://arxiv.org/abs/2606.14688v1
**Summary:** The paper addresses the challenge of generating valuable mathematical statements using AI systems paired with proof assistants, emphasizing the gap between what can be verified and what is deemed valuable by mathematicians. It proposes a model for understanding this generation as a nested language process, revealing that while finite trivia leads to optimal coverage of valuable content, allowing for infinite trivia results in a significant increase in coverage. The key contribution is demonstrating that a constant stream of trivial statements is essential for capturing unrecorded valuable mathematics, highlighting a fundamental aspect of AI-driven mathematical generation.

### 9. CottonLeafVision: An Explainable and Robust Deep Learning Framework for Cotton Leaf Disease Classification
**Authors:** Rafi Ahamed, Md. Abir Rahman, Tasnia Tarannum Roza, Munaia Jannat Easha, Md. Asif Khan, Sudeepta Mandal
**Link:** https://arxiv.org/abs/2606.14686v1
**Summary:** The paper presents "CottonLeafVision," a deep learning framework aimed at accurately classifying cotton leaf diseases to support the textile industry's economic stability. By evaluating several pretrained neural networks, the authors achieved a high classification accuracy of 98% using DenseNet201 and enhanced the model's reliability and interpretability through various techniques like Grad-CAM and adversarial training. The result is a robust tool for real-world cotton disease management.

### 10. HumP-KD: A Hybrid Uncertainty-Aware Multi-Stage Progressive Knowledge Distillation Framework for Efficient Fire Classification
**Authors:** Mohammed Arif Mainuddin, Najifa Tabassum, Omar Ibne Shahid, Riasat Khan
**Link:** https://arxiv.org/abs/2606.14684v1
**Summary:** The paper presents HumP-KD, a novel framework for fire classification that improves model efficiency and accuracy while being suitable for deployment on resource-constrained devices. It employs a hybrid approach of knowledge distillation from two transformer models into a lightweight MobileViT-S, utilizing hierarchical and multi-stage strategies for optimal learning. The resulting model achieves a mean F1 score of 0.9876, significantly surpassing the baseline and demonstrating effective generalization and robustness in various conditions, all while maintaining a compact size suitable for real-time applications.
