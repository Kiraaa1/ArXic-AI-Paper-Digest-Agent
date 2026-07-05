---
## 2026-07-05

### 1. Neuron-Aware Data Selection for Annotation-Free LLM Self-Distillation
**Authors:** Zhuowei Chen, Xiang Lorraine Li
**Link:** https://arxiv.org/abs/2607.02460v1
**Summary:** The paper addresses the challenge of improving large language models (LLMs) in specialized domains without the need for costly human annotations or real-world feedback. It introduces a novel method called Neuron On-Policy Self-Distillation (Neuron-OPSD), which uses internal neuron activations to select training data and construct a teacher model, enabling self-distillation without relying on ground-truth labels. The key contribution is that Neuron-OPSD enhances performance on specific tasks while maintaining generalization across different domains and reducing calibration errors, outperforming previous annotation-free methods.

### 2. Language Models as Measurement Apparatus for Culture
**Authors:** Kent K. Chang
**Link:** https://arxiv.org/abs/2607.02459v1
**Summary:** The paper addresses the problem of how language models can measure cultural phenomena and argues that these models actively shape the cultural realities they analyze rather than merely reflecting them. It uses the concept of the "agential cut" to explore the influence of model design and data choices on cultural measurement, illustrated through case studies on TV and film dialogue. The key contribution is a proposal for a culturally aware research framework that acknowledges the ethical implications of how language models interact with culture.

### 3. Understanding the Robustness of Distributed Self-Supervised Learning Frameworks Against Non-IID Data
**Authors:** Xuanyu Chen, Nan Yang, Shuai Wang, Dong Yuan
**Link:** https://arxiv.org/abs/2607.02447v1
**Summary:** This paper addresses the challenge of applying distributed self-supervised learning (D-SSL) to non-IID data, which is common in real-world scenarios. Through a theoretical analysis, the authors demonstrate that Masked Image Modeling (MIM) offers better robustness to data heterogeneity compared to Contrastive Learning (CL), and they introduce MAR loss to enhance performance further. Their findings suggest that improving network connectivity in decentralized frameworks can increase robustness, offering valuable insights for future algorithm development.

### 4. Optimal Stabilizer Testing and Learning with Limited Quantum Memory
**Authors:** Srinivasan Arunachalam, Louis Schatzki
**Link:** https://arxiv.org/abs/2607.02444v1
**Summary:** The paper examines stabilizer state testing and learning when limited coherent quantum memory is available, specifically how many copies of an unknown $n$-qubit state can be sampled with a fixed amount of memory ($k$ qubits). The authors establish that under these constraints, the sample complexity for testing stabilizer states is significantly higher ($Θ(n-k)$) compared to learning them, which requires $Θ(n^2/k)$ samples. This highlights that coherent quantum memory is crucial for achieving the typical efficiency distinction between testing and learning stabilizer states, and even with a large fraction of memory available, these tasks become equivalently difficult.

### 5. EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments
**Authors:** Zhilin Wang, Han Song, Runzhe Zhan, Jusen Du, Jiacheng Chen, Tianle Li, Qingyu Yin, Yulun Wu, Zhennan Shen, Tong Zhu, Yanshu Li, Guanjie Chen, Derek F. Wong, Yafu Li, Yu Cheng, Yang Yang
**Link:** https://arxiv.org/abs/2607.02440v1
**Summary:** The paper addresses the challenge of evaluating how autonomous agents improve their decision-making policies through feedback in interactive environments. The authors introduce EvoPolicyGym, a structured benchmarking environment that assesses agents' ability to iteratively enhance their policies while managing a limited interaction budget. The key finding is that the leading agent, GPT-5.5, not only ranks highest across multiple environments but also benefits from detailed trajectory analyses that highlight effective mechanisms for policy refinement.

### 6. Extreme Adaptive Transformer for Time Series Forecasting
**Authors:** Sanjeev Shrestha, Hui Liu, Yifan Zhang
**Link:** https://arxiv.org/abs/2607.02437v1
**Summary:** The paper addresses the challenge of accurately forecasting time series data that includes rare but significant extreme events, particularly in hydrologic contexts like streamflow forecasting. To tackle this, the authors introduce the Extreme-Adaptive Transformer (Exformer), which features a novel attention mechanism that prioritizes both normal and extreme events. The results show that Exformer outperforms existing forecasting models by effectively capturing the impact of rare extreme events on predictions.

### 7. Reasoning effort, not tool access, buys first-try reliability in agentic code generation: an observational study
**Authors:** Achint Mehta
**Link:** https://arxiv.org/abs/2607.02436v1
**Summary:** This study investigates whether additional capabilities in coding assistants, like testing tools and design prompts, actually improve software reliability. By analyzing 90 independent attempts to build an application, the researchers found that enhancing the reasoning effort of the agents significantly improved their first-try success rates, while the testing tool did not provide any functional benefits. The main takeaway is that failures primarily stem from inadequate reasoning, not visible flaws, suggesting that focusing on reasoning quality is more effective than simply adding tools.

### 8. Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach
**Authors:** Manuel Alonso-Carracedo, Ruben Fernandez-Boullon, Pedro Celard, Francisco J. Rodriguez-Martinez, Lorena Otero-Cerdeira
**Link:** https://arxiv.org/abs/2607.02432v1
**Summary:** The paper addresses the challenge of grading Linux/bash command-line exams efficiently, as traditional methods struggle with partial credit and variability in student responses. The authors tested four advanced Large Language Models (LLMs) using a cognitive taxonomy framework to evaluate their grading accuracy against expert evaluations. They found that the Gemini 3.0 Pro model with enhanced prompts had the highest agreement with human graders, revealing that the complexity of exam questions significantly affects LLM performance and establishing a structured approach for effective AI-assisted grading.

### 9. WorldSample: Closed-loop Real-robot RL with World Modelling
**Authors:** Yuquan Xue, Le Xu, Zeyi Liu, Zhenyu Wu, Zhengyi Gu, Xinyang Song, Bofang Jia, Ziwei Wang
**Link:** https://arxiv.org/abs/2607.02431v1
**Summary:** The paper addresses the challenge of high interaction costs in real-robot reinforcement learning (RL) by proposing WorldSample, a data augmentation framework that combines real robot rollouts with synthetic data generation through a world model. This method enhances the training process using a technique called Policy-Paced Learning to optimize sample selection and mitigate noise from synthetic data. The results show a significant improvement in policy success rates and reduced training steps, alongside enhanced fidelity of the generated world models.

### 10. QFedAgent: Quantum-Enhanced Personalized Federated Learning for Multi-Agent Activity Recognition
**Authors:** Quoc Bao Phan, Tuy Tan Nguyen
**Link:** https://arxiv.org/abs/2607.02426v1
**Summary:** The paper addresses the challenge of applying federated learning in multi-agent systems where sensor data is heterogeneous and not identically distributed, which typically hampers performance. To overcome this, the authors introduce QFedAgent, a hybrid quantum-classical framework that utilizes a quantum circuit for data fusion, significantly reducing the number of parameters needed compared to traditional methods. The results show that QFedAgent achieves a high mean test accuracy of 97.7% while maintaining a tenfold parameter reduction, indicating its efficiency and effectiveness in activity recognition tasks.
