---
## 2026-11-16

### 1. Pairing AIS with RF: Analysis of a Markovian Approach for Maritime Data Fusion
**Authors:** Daniel Grimm, Kyra Jongman, Renato Cordeiro Ferreira, Giuseppe Cascavilla, Alfredo Cuzzocrea, Willem-Jan Van Den Heuvel
**Link:** https://arxiv.org/abs/2611.18563v1
**Summary:** The study addresses the challenge of accurately monitoring maritime activities by combining Automatic Identification System (AIS) data with independent radio frequency (RF) observations, which lack vessel identification capability. Using a Pair Hidden Markov Model (PHMM), researchers aligned RF detections with AIS trajectories by incorporating temporal and spatial factors while accommodating for noise and discrepancies. The key finding indicates that while the PHMM provides significant improvements in precision and area under the curve (AUC) for detecting dark vessels, a simpler time-weighted nearest-neighbor method still outperforms it.

### 2. FETTUCCINE: Fast and efficient brain-to-text decoding on mobile devices
**Authors:** Jonathan D. McCart, Pranav I. Deevi, Mehdi Azabou, Nanda H. Krishna, Caleb A. McKinney, Nicholas S. Card, Sergey D. Stavisky, Chethan Pandarinath
**Link:** https://arxiv.org/abs/2611.18561v1
**Summary:** FETTUCCINE addresses the challenge of decoding neural signals from individuals who are unable to speak, which typically requires complex and slow language models that make real-time communication difficult. The authors developed a lightweight brain-to-text framework that utilizes automatic speech recognition techniques, resulting in a significant improvement in decoding speed and accuracy, achieving as low as 4.39% word error rates. Notably, this system can operate on a mobile device with impressive real-time throughput, enabling more practical use of speech neuroprostheses for communication.

### 3. Training Reasoning Models in Simulation to Natively Use Real Robots
**Authors:** Jiaming Tang, Zhuoyang Zhang, Junxian Guo, Fangzhou Zhao, Yilong Zhao, Zekai Li, Xingyang Li, Yuyang Zhao, Song Bian, Zhijian Liu, Song Han
**Link:** https://arxiv.org/abs/2611.18562v1
**Summary:** The paper addresses the challenge of training open-weight reasoning models to effectively control real robots without prior demonstrations. The authors developed a training method called robot-use reinforcement learning (RURL) that allows a 27B parameter model to learn entirely in simulation, achieving significant improvements in task performance on real robots. Key results include a notable increase in success rates on various tasks, where the trained model outperformed baseline models and showed strong generalization to unseen robots and instructions.

### 4. BAL: Bidirectional Autoregression in Latent Space for Learning Human Movement Representations
**Authors:** Genki Kinoshita, Ko Nishino
**Link:** https://arxiv.org/abs/2611.18559v1
**Summary:** The paper presents BAL, a self-supervised framework designed to learn meaningful representations of human movements from 3D pose sequences by leveraging the natural ordering of behaviors rather than relying on heuristic assumptions. BAL uses a bidirectional autoregressive prediction in a latent space to anticipate movements, incorporating both past and future context to enhance representation learning. The key contribution is that BAL effectively prevents representation collapse while achieving superior performance in motion-related tasks such as captioning and forecasting compared to existing methods.

### 5. WeightBench: Evaluating Language Models as Weight-Space Programmers
**Authors:** Aayush Marasini, Barsat Khadka, Nick Rahimi
**Link:** https://arxiv.org/abs/2611.18553v1
**Summary:** The paper introduces WeightBench, a benchmark designed to systematically evaluate the ability of large language models to perform Weight-Space Programming (WSP), which involves manipulating the parameters of neural networks without gradient descent. The benchmark encompasses 42 tasks across various categories, demonstrating that while advanced models can read and write small networks effectively, they struggle with more complex edits and compressing larger models. Notably, the results show that Claude Opus 5.5 outperformed several other models in this context, achieving a macro score of 0.535 on the evaluated tasks.

### 6. Imitation Bootstrapped Multi-Agent Reinforcement Learning
**Authors:** Tony H. Zhang, Connor Mattson, Daniel S. Brown
**Link:** https://arxiv.org/abs/2611.18543v1
**Summary:** The paper addresses the challenge of using demonstrations to improve multi-agent reinforcement learning (MARL), where a single demonstrator can only control one agent at a time. The authors introduce Imitation Bootstrapped Multi-Agent Reinforcement Learning (IBMARL), which combines behavior cloning with reinforcement learning to select optimal actions from both approaches at each time step. The key finding is that IBMARL significantly outperforms traditional imitation learning methods, achieving faster learning and even surpassing the performance of human demonstrators on several benchmarks.

### 7. Elliptic Sampling: Optimal Interpolant Schedules for Gaussians and Beyond
**Authors:** Cole Becker, Taylan Kargin, Kimia Hassibi, Asuman Ozdaglar, Pablo A. Parrilo
**Link:** https://arxiv.org/abs/2611.18542v1
**Summary:** This paper addresses the challenge of efficient generative modeling by developing a new framework for designing optimal interpolant schedules and discretization methods for sampling from target distributions. The authors introduce "Zoloflow," a sampling algorithm that utilizes variance-preserving elliptic schedules based on Jacobi elliptic functions, which significantly enhances sampling efficiency for Gaussian targets and allows for effective sampling from broader classes of distributions. Key results demonstrate that Zoloflow achieves optimal performance with fewer score evaluations compared to existing methods, while also providing empirical validation across various target distributions.

### 8. Why Finite Intelligence Works in an Infinite World: A Mathematical Theory
**Authors:** Mojtaba Soltanalian
**Link:** https://arxiv.org/abs/2611.18538v1
**Summary:** This paper addresses the challenge of how finite representations of information can effectively function in infinitely complex environments, particularly when dealing with tasks that share common structures. The authors introduce a mathematical framework called future-task information to quantify the minimal information necessary for making decisions based on available evidence. A key contribution is the identification of boundaries for preserving relevant information through structured representations, demonstrating that collective task characteristics can dictate the necessary information requirements beyond individual task complexity.

### 9. ModHarness-RL: Recasting Harnesses as Learnable and Evolving Programs for Agentic RL
**Authors:** Zelin He, Siyu Zhu, Jacob Helwig, Yujian Liu, Li An, Rohit Jain, Shiyu Chang, Alborz Geramifard
**Link:** https://arxiv.org/abs/2611.18533v1
**Summary:** The paper addresses the limitation of fixed harnesses in agentic reinforcement learning (RL), which do not adapt to changing model behaviors. The authors introduce ModHarness-RL, a method that treats the harness as adaptable programs that evolve by learning from the model's interactions over time. Their approach demonstrates improved performance in various tasks compared to traditional fixed harnesses, indicating that dynamic and learned harnesses can better support RL models.

### 10. Alignment by Socialization: Learning Tradeoffs Under Selection
**Authors:** Thomas Brennan, Andrew W. Lo, Chaoyi Zhao
**Link:** https://arxiv.org/abs/2611.18531v1
**Summary:** The paper addresses the challenge of aligning AI agents' behavior with human values, particularly when their task objectives conflict with social conduct rules. The authors developed a model to study how evolutionary selection impacts agents' decision-making, demonstrating that policies allowing agents to learn from their environment (referred to as "socialization") lead to better alignment with human judgments. The key finding is that accumulated experience from socialization helps reinforce desirable behaviors, making them more resilient to later changes in training emphasis, although there are nuances related to memory and the impact of mistakes.
