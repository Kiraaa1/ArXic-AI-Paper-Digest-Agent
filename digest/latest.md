---
## 2026-11-06

### 1. User Embeddings are Superpositions of Interpretable Behavioral Modes
**Authors:** Jonathan Kozaczuk, Zheng Dong, Noyan Evirgen, Keivan Majidi, Eddie K. H. Ng, Chris Porter, Qi Zhao, Jia Geng, Changmao Li, Brandon R. Feng
**Link:** https://arxiv.org/abs/2611.08487v1
**Summary:** The paper addresses the challenge of interpretability in user embeddings used for recommendation and personalization systems, proposing that these embeddings can be viewed as combinations of clear and interpretable behavioral modes. By using sparse autoencoders to recover these modes, the authors demonstrate that their approach outperforms traditional methods on both synthetic and real-world datasets, allowing for natural language naming and querying of the modes. This offers a model-agnostic framework for better understanding user behavior without needing to change existing embedding systems.

### 2. SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization
**Authors:** Qile Jiang, George Em Karniadakis
**Link:** https://arxiv.org/abs/2611.08483v1
**Summary:** SwarmEvolve addresses the slow process of LLM-guided evolutionary search for solving mathematical and computational problems, which typically relies on generating lengthy text outputs for each iteration. The framework employs hundreds of low-cost agents that collaborate in swarms, reasoning in latent space and sharing information efficiently without text encoding. SwarmEvolve significantly accelerates problem-solving, achieving top results in 3 to 8 minutes, compared to over an hour for existing methods, and often improves upon previously found solutions from leading models.

### 3. Scientist World: Grow a Research World for AI-Scientists
**Authors:** Taiming Lu, Sachin Konan, Zhuang Liu
**Link:** https://arxiv.org/abs/2611.08478v1
**Summary:** The paper addresses the challenge of creating a suitable environment for AI-Scientists to effectively engage with scientific research, as existing literature is inaccessible for execution. The authors developed "Scientist World," an autonomous system that transforms research papers into executable environments, allowing AI-Scientists to interact with and evaluate their methods against human achievements. Remarkably, this platform enabled frontier AI-Scientists to outperform human researchers 74% of the time and has generated extensive research traces to enhance future AI training in scientific ideation.

### 4. XStack: A Benchmark for ML Repo Migration
**Authors:** Linrong Cai, Taiming Lu, Haozhe Chen, Zhuang Liu
**Link:** https://arxiv.org/abs/2611.08472v1
**Summary:** The paper introduces XStack, a benchmark designed to assess the ability of AI agents to migrate machine learning repositories between PyTorch on NVIDIA GPUs and JAX on Google TPUs. The benchmark evaluates how well these agents can convert code from one framework to another, revealing that their migration capabilities are currently unreliable, with performance ranging from 40% to 75% success rates. XStack aims to facilitate easier and more reliable migration of ML code across different ecosystems, ultimately empowering researchers to run their work on their chosen hardware.

### 5. Same Behavior, Different Mechanism: What Finite Experiments Can Certify About Integrated Information
**Authors:** Linqian Wu, Diaoxuan He
**Link:** https://arxiv.org/abs/2611.08469v1
**Summary:** This paper addresses the challenge of identifying integrated information (φ) within neural networks, focusing on how experiments with limited and noisy data can reveal insights about the underlying mechanisms of a system rather than just its outputs. The authors analyze specific stochastic networks to demonstrate that, despite identical input-output behaviors, different network architectures can be distinguished through targeted hypothesis testing, revealing crucial information about their internal structures. Key findings include that these measures are sensitive to slight changes in the network's mechanisms and can ensure reliable lower bounds on φ from finite data, thereby contributing to the field of AI interpretability and understanding machine consciousness.

### 6. Towards interpreting any residual stream direction by scaling activation inversion
**Authors:** Celeste De Schamphelaere, Juan J. Vazquez, Ari Spiesberger, Tomáš Gavenčiak, Gavin Leech, Euan Ong, Jiahai Feng
**Link:** https://arxiv.org/abs/2611.08465v1
**Summary:** The paper addresses the challenge of interpreting specific directions in a language model's residual stream, which traditionally relies on existing text from a corpus. The authors introduce Maximally-Activating Example Metamodels (MAEMs), which generate text that strongly activates these directions using a reinforcement learning strategy. Their findings show that MAEMs are more effective than previous methods in identifying and exemplifying concepts, recovering hidden information, and providing verifiable insights into model behavior.

### 7. Adversarial Training with Large Step Sizes: Implicit Bias, Optimization, and Sharpness
**Authors:** Yi Feng, Andrea Paudice
**Link:** https://arxiv.org/abs/2611.08457v1
**Summary:** This paper investigates the effects of using large constant step sizes in adversarial training (AT) for improving model robustness, contrasting it with traditional approaches that utilize smaller step sizes. By analyzing the dynamics of gradient descent in both linear logistic regression and neural networks, the authors uncover unique behaviors in AT, showing that implicit bias and optimization convergence rates differ significantly from standard training, and revealing that loss sharpness can exhibit two-stage dynamics. These findings enhance our understanding of how large step sizes influence the effectiveness of adversarial training.

### 8. Unpacking the Compute Efficiency of Strong-to-Weak OPD against GRPO
**Authors:** Zeyu Leo Liu, Yang Li, Bo Pang, Emre Can Acikgoz, Xuan-Phi Nguyen, Anurag Koul, Srijan Bansal, Erik Nijkamp, Shafiq Joty, Semih Yavuz
**Link:** https://arxiv.org/abs/2611.08453v1
**Summary:** The paper investigates the compute efficiency of on-policy distillation (OPD) compared to Group Relative Policy Optimization (GRPO) in training AI models, focusing on whether using a teacher's guidance reduces the training resources needed to achieve similar accuracy. The authors found that OPD can be significantly more efficient, especially when the teacher is the student's own GRPO checkpoint, achieving comparable accuracy with much fewer training FLOPs across various tasks. Furthermore, a multi-teacher approach consolidates specialized models into a single student while maintaining high accuracy at a fraction of the training cost, demonstrating substantial resource savings.

### 9. ReproBridge: Building Reproducibility into ML Research Artifacts
**Authors:** Yubo Wang, Rui Meng, Jaehyun Nam, Tomas Pfister, Jinsung Yoon
**Link:** https://arxiv.org/abs/2611.08452v1
**Summary:** The paper addresses the challenge of reproducing machine learning experiments, which often requires piecing together information from various sources. To tackle this, the authors developed ReproBridge, a standardized approach that organizes code, environment setup, and reproduction guidelines into a cohesive workflow. The key finding is that using these refined artifacts significantly boosts reproduction success rates from 76.4% to 92.6% and lowers API costs, demonstrating the importance of preserving procedural knowledge in improving reproducibility.

### 10. A Hidden Markov Preference Model for Online Prediction of Adversary Actions
**Authors:** Angel Daruna, Michael Cogswell, Tixiao Shan, Yi Yao, Han-Pang Chiu, Ajay Divakaran
**Link:** https://arxiv.org/abs/2611.08445v1
**Summary:** The paper addresses the challenge of predicting an attacker's next action in a dynamic environment where their behavior can switch between different regimes. The authors propose a hidden Markov model that leverages a feasibility-masked tree of actions to capture the attacker's regime and adapt predictions based on observed actions. Key results indicate that this approach significantly improves prediction accuracy, achieving a better performance (0.8 nats per step) than traditional recurrent models, with faster loss recovery following regime changes.
