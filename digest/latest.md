---
## 2026-07-04

### 1. Towards Robustness against Typographic Attack with Training-free Concept Localization
**Authors:** Bohan Liu, Wenqian Ye, Guangzhi Xiong, Zhenghao He, Sanchit Sinha, Aidong Zhang
**Link:** https://arxiv.org/abs/2607.02494v1
**Summary:** The paper addresses the vulnerability of CLIP-based vision models to Typographic Attacks, where irrelevant text in images distorts their visual understanding, posing risks in critical applications like autonomous driving. The authors propose a novel, training-free method for interpreting and improving model robustness by identifying and modifying specific components in the Vision Transformer architecture that misinterpret lexical information. Their approach significantly enhances classification accuracy in the presence of such attacks, outperforming existing defense strategies.

### 2. G-RRM: Guiding Symbolic Solvers with Recurrent Reasoning Models
**Authors:** Timo Bertram, Sidhant Bhavnani, Richard Freinschlag, Erich Kobler, Andreas Mayr, Günter Klambauer
**Link:** https://arxiv.org/abs/2607.02491v1
**Summary:** The paper introduces G-RRM, a method that enhances symbolic solvers for constraint satisfaction problems by integrating them with a new type of neural model called SE-RRMs. This neuro-symbolic approach improves the efficiency of symbolic solvers, especially when the problem size is large and the solver can adapt its decisions based on neural suggestions. The key finding is that when the conditions are right, such as in expansive combinatorial search spaces, G-RRM can significantly speed up solvers like backtracking and Glucose 4.1, achieving notable performance improvements, whereas other solvers like CaDiCaL do not benefit from the neural guidance.

### 3. Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning
**Authors:** Liyan Tang, Fangcong Yin, Greg Durrett
**Link:** https://arxiv.org/abs/2607.02490v1
**Summary:** This paper addresses the issue of large vision-language models' inability to properly reflect on and correct past mistakes while using visual inputs, particularly with out-of-distribution images. The authors introduce a reinforcement learning framework called VRRL that enhances self-reflection through techniques like masked trajectory prefixes and experience replay buffers to train the model on diverse corrections. The key result is a significant improvement in out-of-distribution accuracy on visual grounding tasks compared to standard models and previous training methods.

### 4. Combating Textual Noise and Redundancy: Entropy-Aware Dense Visual Token Pruning
**Authors:** Xuehui Wang, Xuankun Yang, Wei Shen
**Link:** https://arxiv.org/abs/2607.02484v1
**Summary:** This paper addresses the challenge of efficiently pruning visual tokens in vision-language models (VLMs) without losing important information, particularly in complex tasks with dense instructions. The authors introduce the Entropy-Aware Dense Pruning (EADP) method, which quantifies and mitigates textual noise and optimizes token selection using a novel submodular maximization approach. Their experiments show that EADP significantly enhances the accuracy and efficiency of VLMs while preserving essential visual details under strict constraints on the number of tokens.

### 5. Audio-Based Understanding of Audiobook Narration Appeal
**Authors:** Shahar Elisha, Mariano Beguerisse-Díaz, Emmanouil Benetos
**Link:** https://arxiv.org/abs/2607.02473v1
**Summary:** This study investigates how various qualities of audiobook narration impact listener appeal, considering factors like genre and specific titles. The researchers extracted vocal and acoustic features from audiobooks and analyzed their correlation with listener engagement data. The key finding reveals that particular acoustic characteristics are strongly associated with audiobook appeal, suggesting that understanding these factors can enhance audiobook personalization and narrator selection.

### 6. TestEvo-Bench: An Executable and Live Benchmark for Test and Code Co-Evolution
**Authors:** Jiale Amber Wang, Kaiyuan Wang, Pengyu Nie
**Link:** https://arxiv.org/abs/2607.02469v1
**Summary:** The paper presents TestEvo-Bench, a new benchmark designed to assess how well software testing agents can evolve alongside code changes by generating and updating tests based on real commit histories from open-source projects. By providing executable tasks and live updates to the benchmark, it ensures tasks are relevant and reduces the risk of data leakage in evaluations. The study found that while state-of-the-art agents performed relatively well overall—achieving up to a 77.5% success rate in test generation—they struggled with the most recent tasks, particularly when constrained by limited resources.

### 7. Human Capital, Not Model Benchmarks, Predicts Hybrid Intelligence in Forecasting
**Authors:** Vivienne Ming
**Link:** https://arxiv.org/abs/2607.02467v1
**Summary:** This study investigates how human-AI collaboration affects the accuracy of predictions in a real-money prediction market. By analyzing individual forecasters, the researchers found that the effectiveness of collaboration depends more on specific human qualities—such as perspective-taking and intellectual humility—rather than just cognitive ability or model benchmarks. The key finding is that while many forecasters either matched AI performance or performed worse, a minority successfully combined their reasoning with AI, achieving superior accuracy.

### 8. Learning to Move Before Learning to Do: Task-Agnostic pretraining for VLAs
**Authors:** Junhao Shi, Siyin Wang, Xiaopeng Yu, Li Ji, Jingjing Gong, Xipeng Qiu
**Link:** https://arxiv.org/abs/2607.02466v1
**Summary:** The paper addresses the challenge of limited expert demonstrations in training Vision-Language-Action (VLA) models by separating the learning of physical skills (how to move) from understanding tasks (what to do). The authors introduce a two-stage framework called Task-Agnostic Pretraining (TAP), which first learns movement skills from inexpensive, unlabeled data before grounding these skills with minimal expert input. Their approach outperforms traditional methods, achieving significant improvements in performance and robustness with far less labeled data required.

### 9. Will Scaling Improve Social Simulation with LLMs?
**Authors:** Caleb Ziems, William Held, Su Doga Karaca, David Grusky, Tatsunori Hashimoto, Diyi Yang
**Link:** https://arxiv.org/abs/2607.02464v1
**Summary:** This paper examines whether increasing the size of Large Language Models (LLMs) will enhance their ability to perform social simulations effectively. The authors conducted experiments with various LLMs to analyze how scaling influences the accuracy of simulating opinions, behaviors, and forecasting over time. Their findings suggest that while larger models generally improve simulation outcomes, challenges remain for less-represented topics and specific tasks, indicating that scaling alone may not suffice in all scenarios.

### 10. OrbitQuant: Data-Agnostic Quantization for Image and Video Diffusion Transformers
**Authors:** Donghyun Lee, Jitesh Chavan, Duy Nguyen, Sam Huang, Liming Jiang, Priyadarshini Panda, Timo Mertens, Saurabh Shukla
**Link:** https://arxiv.org/abs/2607.02461v1
**Summary:** The paper introduces OrbitQuant, a novel approach to quantizing diffusion transformers (DiTs) for image and video generation, addressing the high computational cost of inference due to shifting activations. By using a data-agnostic method that normalizes and rotates activations, OrbitQuant allows for consistent quantization across various inputs without the need for recalibration for different settings. The key contribution is achieving state-of-the-art post-training quantization performance at low-bit rates, optimizing DiTs' efficiency without sacrificing generation quality.
