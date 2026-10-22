---
## 2026-10-22

### 1. LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data
**Authors:** Zhennan Wan, Jianfei Chen
**Link:** https://arxiv.org/abs/2610.30132v1
**Summary:** The paper addresses the challenge of improving long-context reasoning in large language models (LLMs) without relying on costly external training data. The authors introduce a method called LongZero, which enables LLMs to generate their own long-context reasoning tasks and evidence without any external input. Experimental results demonstrate that LongZero significantly outperforms existing reinforcement learning approaches, showcasing its effectiveness in enhancing long-context reasoning capabilities.

### 2. Think Harder Where It Matters: Item-Level Adaptive Recursion for Sequential Recommendation
**Authors:** Zhanshuo Cao, Jiakai Tang, Yuqi Zhou, Sunhao Dai, Jun Xu
**Link:** https://arxiv.org/abs/2610.30128v1
**Summary:** This paper addresses the inefficiency of existing sequential recommendation systems that apply a uniform computation depth to all user interaction items, regardless of their significance. The authors propose LoopRec, a new approach that adaptively adjusts the depth of computation for each item based on its individual needs, allowing items that require less processing to exit early while more complex items receive deeper analysis. The key result shows that LoopRec consistently outperforms traditional fixed-depth methods across various benchmarks, demonstrating its effectiveness in optimizing computation and improving recommendation accuracy.

### 3. PhysiCalWorld: In-Context Physics Calibration for World Models
**Authors:** Yunhao Luo, Wentao He, Yinpei Dai, Hyelin Nam, Hongze Fu, Joyce Chai, Nima Fazeli, Jeong Joon Park
**Link:** https://arxiv.org/abs/2610.30125v1
**Summary:** The paper presents PhysiCalWorld, a method designed to enhance world models by calibrating them to the specific physics dynamics of a scene, addressing the issue of poor predictions in novel environments due to a lack of accurate physics understanding. Instead of requiring fine-tuning or detailed physics modeling, PhysiCalWorld uses a compact physics descriptor token, derived from exploratory interactions in the test scene, to improve predictive accuracy without significant computational burden. The results demonstrate that this approach notably increases prediction accuracy and planning success across varied environments while maintaining a structured latent space for better generalization.

### 4. A Quasipolynomial Algorithm for $\ell_\infty$ Contractions
**Authors:** Ashkan Soleymani, Gabriele Farina
**Link:** https://arxiv.org/abs/2610.30122v1
**Summary:** This paper presents a quasipolynomial-time algorithm for finding an approximate fixed point in high-dimensional nonexpansive mappings under the $\ell_\infty$ norm. The method employs a boosting technique to reduce the search space effectively. A significant outcome of this work is the implication that simple stochastic games can now be solved in quasipolynomial time, showcasing the practical relevance of this approach.

### 5. Self-normalized Bernstein Inequalities for Regenerative Processes and Applications to Learning Without Independence
**Authors:** Imon Banerjee, Pierre Alquier
**Link:** https://arxiv.org/abs/2610.30119v1
**Summary:** The paper addresses the challenge of establishing generalization error bounds in machine learning for classification tasks using non-independent, regenerative data. The authors develop a self-normalized Bernstein inequality tailored for regenerative processes, providing empirical bounds that account for cycle lengths while minimizing key error terms. A significant contribution is demonstrating that these bounds are minimax-optimal and can inform the design of agnostic classifiers with oracle-like performance guarantees.

### 6. The role of locality and weight sharing in convolutional neural networks
**Authors:** Francesco Mori, Melanie Weber
**Link:** https://arxiv.org/abs/2610.30118v1
**Summary:** This paper investigates how the properties of locality and weight sharing in convolutional neural networks (CNNs) influence their learning processes, particularly in relation to the spatial correlations present in natural images. Using a teacher-student model with a convolutional teacher, the authors derive mathematical equations to compare the learning dynamics of convolutional vs. locally connected networks. They find that while convolutional networks learn faster when positions are uncorrelated, spatial correlations can diminish the advantages of weight sharing, leading to a more complex interplay between learning rates and network architectures.

### 7. Environment Duels: A Microcosm of LLM Co-Evolution
**Authors:** Shibo Jin, Zhiqiu Xu, Yiling Zou, Shangyu Gong, Mayur Naik
**Link:** https://arxiv.org/abs/2610.30116v1
**Summary:** The paper addresses the problem of understanding how large language models (LLMs) interact and influence each other's capabilities in a competitive environment. The authors introduce a benchmark called Environment Duels, where different LLMs create and solve tasks with hints, revealing that the ability to write challenges differs from the ability to solve them. Key findings show distinct skill sets in authorship and problem-solving, with interactions among models creating stable rankings and demonstrating ways that LLMs can collectively learn and improve.

### 8. The End of Consensus Research?
**Authors:** Clément Burgelin, Rachid Guerraoui, Zicong Hong, Yinan Hu, Anne-Marie Kermarrec, Rafael Pires, Rasmus Moorits Veski, Martijn de Vos
**Link:** https://arxiv.org/abs/2610.30114v1
**Summary:** The paper addresses the longstanding challenge of achieving consensus in distributed computing, specifically for geo-replicated state machines. By using AI to discover a new protocol called A-greement, the authors achieved significant performance improvements over existing solutions, reducing latency for write-heavy and read-heavy workloads. Additionally, the AI tool, AI-greement, not only aided in protocol development but also revealed vulnerabilities in current protocols, highlighting the continuing importance of human expertise in this research area.

### 9. Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research
**Authors:** Houde Qian, Zheng Jiang, Wenyi Li, Chenxi Xu, Xinjie Lin, Yuzhao Peng, Ruoyu Han, Youjie Zheng, Kaisen Yang, Qinhuai Na, You Fu, Calvin Xiao
**Link:** https://arxiv.org/abs/2610.30113v1
**Summary:** The paper presents Quant-Arena, a benchmarking framework designed to evaluate large language models (LLMs) in the context of quantitative trading by testing their ability to generate effective trading strategies based on historical market data. The benchmark involves a competitive assessment where models develop trading strategies, which are then evaluated based on their performance in 2024 after being trained on earlier data. The key finding is that while the top-performing model, GPT-6 Astra, achieved the highest score, none of the models outperformed a simple equal-weighted market strategy in 2024.

### 10. Minimax Optimality of the NPMLE for Gaussian Mixtures in Hellinger Distance
**Authors:** Shayan Hundrieser, Tudor Manole
**Link:** https://arxiv.org/abs/2610.30109v1
**Summary:** This paper addresses the estimation of univariate Gaussian mixture densities using the nonparametric maximum likelihood estimator (NPMLE) from independent samples. The authors demonstrate that the unconstrained NPMLE achieves the best possible rate of convergence in squared Hellinger distance, specifically $\log(n)/n$, when the true mixing distribution is sub-Gaussian, and a slightly improved rate when the mixing measure has compact support. A significant contribution of this work is the development of techniques for analyzing the bracketing entropy of finite Gaussian mixtures, which also finds applications in related Gaussian Empirical Bayes problems.
