---
## 2026-10-23

### 1. Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success
**Authors:** Yunfei Xie, Howard H. Qian, Shiyi Lan, Kaiyu Hang, Chen Wei
**Link:** https://arxiv.org/abs/2610.31670v1
**Summary:** This paper addresses the challenge of evaluating robotic foundation models without relying on expensive closed-loop testing by introducing a new offline metric called Sensorimotor Alignment ($S^2$). This metric assesses how a model's sensory representations align with the geometry of physical motion, and the authors find that higher $S^2$ scores correlate with better performance in robotics tasks. The key contribution is showing that $S^2$ serves as a useful proxy for model capability, enabling the identification of promising models before extensive fine-tuning is performed.

### 2. Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning
**Authors:** Mahdi Salmani, Adel Javanmard, Devansh Gupta, Meisam Razaviyayn
**Link:** https://arxiv.org/abs/2610.31667v1
**Summary:** This paper addresses the challenge of efficiently pruning candidate solutions in reasoning models during test-time scaling, where the goal is to select the most promising candidates for further computation. The authors propose a new pruning method that optimizes a measure called pass@$k$, which balances the quality and diversity of selected partial solutions to maximize the likelihood of finding at least one correct final answer. Their approach outperforms existing pruning techniques, particularly when a moderate number of candidates are retained, demonstrating the effectiveness of directly balancing quality and diversity in the pruning process.

### 3. Phase Transition from Random Features to Fully Trainable Networks
**Authors:** Xin He, Huan Lao, Xiliang Lu, Shijun Zhang
**Link:** https://arxiv.org/abs/2610.31663v1
**Summary:** This paper investigates the transition from using fixed random features in neural networks to fully trainable representations, addressing the challenge of creating effective approximation spaces in scientific computing. The authors identify a phase transition in approximation accuracy related to varying degrees of trainability and initialization conditions, providing a specific approximation rate for two-layer networks. A key finding is that a small proportion of trainable neurons can significantly reduce approximation errors, with experiments confirming similar behavior in deeper networks.

### 4. Reliable AI-Assisted Decisions via Selective Auditing
**Authors:** Isaac Gibbs, Elise L. Han, Ryan J. Tibshirani, Tijana Zrnic
**Link:** https://arxiv.org/abs/2610.31662v1
**Summary:** This paper addresses the challenge of effectively monitoring AI decision-making by balancing automated approvals and human expert audits. The authors propose a novel online optimization framework that minimizes expert reviews while ensuring that a controlled fraction of AI errors goes unchecked. Their experiments demonstrate that this method significantly reduces the need for human oversight while maintaining reliable error control across various applications, including language model monitoring and data labeling.

### 5. SpectralCanary: Embarrassingly Simple Low-Frequency Traces for T2I Dataset-Use Auditing
**Authors:** Sy-Tuyen Ho, Anirudh Satheesh, Soham Chawathe, Huy Nghiem, Yongkyun Lee, Andrew Adams Schoen, Furong Huang
**Link:** https://arxiv.org/abs/2610.31659v1
**Summary:** The paper addresses the challenge of auditing whether a text-to-image model was fine-tuned on a specific image dataset, as models can incorporate visual traits without reproducing the original images. The authors propose SpectralCanary, which embeds a low-frequency canary image into dataset images while preserving their captions, allowing a lightweight verifier to identify this signal in generated outputs. The results show that SpectralCanary outperforms existing methods in accuracy and preservation of original images, demonstrating that low-frequency signals are effective for dataset auditing.

### 6. Cost-Aware Abstention for LLM-Based IT Ticket Classification
**Authors:** Sachin Gupta
**Link:** https://arxiv.org/abs/2610.31657v1
**Summary:** This paper addresses the issue of costly misrouting of IT support tickets by evaluating a cost-aware abstention approach, where a routing policy is trained under specific cost conditions and then applied to test data. The researchers compared various classification models, including large language models (LLMs), and found that a TF-IDF logistic regression model with a calibrated threshold significantly reduced routing errors and overall costs. The study highlights the importance of cost-sensitive calibration in ticket classification, particularly showing that strategically abstaining from decisions can lead to notable reductions in misclassification rates and expenses.

### 7. METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning
**Authors:** Ali Najar, Hosein Hasani, Amir Kooshan Fattah, Yasamin Rajabi, Mahdieh Soleymani Baghshah
**Link:** https://arxiv.org/abs/2610.31656v1
**Summary:** The paper introduces METTA, a method designed to enhance meta-reinforcement learning agents' ability to quickly adapt to new tasks using memory-based strategies. By splitting adaptation into short-term and long-term memory processes, METTA achieves efficient learning without the heavy computational costs of traditional transformer models. The key findings demonstrate that METTA significantly improves task success rates in complex environments while requiring less training time and offering better exploration strategies.

### 8. EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence
**Authors:** Qijin Zhang, Hanzhen Wang, Yuehan Zhao, Haoyu Dai, Yao Shu, Zhongxiang Dai, Shuang Qiu
**Link:** https://arxiv.org/abs/2610.31650v1
**Summary:** The paper addresses the problem of large language model (LLM) agents executing unsafe actions due to missing safety-critical facts in tool responses. The authors developed EpiSEM-Bench, a benchmark consisting of 300 task pairs that evaluates how well these agents handle evidence omissions and recover necessary information before acting. Key findings reveal significant differences among various models in their ability to detect missing information and adjust their actions accordingly, highlighting the importance of evidence recovery in enhancing safety.

### 9. Low-Bit N-Gram Embeddings for Language Models
**Authors:** Stephen Chung, Wenyu Du
**Link:** https://arxiv.org/abs/2610.31646v1
**Summary:** The paper addresses the high memory demands of n-gram embedding tables used in language models by exploring low-bit quantization techniques to reduce memory usage. The authors demonstrate that storing n-gram embeddings at four bits can significantly cut memory requirements by about 75% while retaining over 99% of the performance gains typically achieved with full-precision tables. Furthermore, this approach allows for reinvestment of saved memory into larger tables, enhancing overall model performance while maintaining efficiency.

### 10. A Fix for Softmax and Cross-Entropy
**Authors:** Jonathan T. Barron, Dan Gnanapragasam, Michael Tschannen
**Link:** https://arxiv.org/abs/2610.31642v1
**Summary:** This paper addresses two numerical issues in the standard implementations of softmax and cross-entropy: "Softmax Collapse," which hampers gradient computation when one logit is much larger, and "Softmax Cancellation," which generates incorrect gradients when logits are nearly equal. The authors propose straightforward implementations that rectify these problems, leading to improved training dynamics and preventing issues like accuracy collapse and undesired network drift. Key contributions include enhanced training stability and clearer bounds on logit growth during the learning process.
