---
## 2026-09-06

### 1. The Natural Language Interaction Protocol and Standard for AI Agents
**Authors:** Luyi Xing, Rasit Onur Topaloglu, Ranjan Sinha, Abhay Ratnaparkhi, Samuel Ndichu, Christopher Nguyen, Anindita Das, Tom Sheffler, Mohamed Rahouti, Zichuan Li, Xiaojing Liao, Sanjay Aiyagari
**Link:** https://arxiv.org/abs/2609.04135v1
**Summary:** The paper addresses the challenge of interoperability among diverse AI agents developed across various frameworks and environments. It introduces the Natural Language Interaction Protocol (NLIP), a standardized application-layer communication protocol that allows these agents to interact more effectively through a lightweight message structure compatible with existing transport methods. The key contribution of NLIP is its ability to enable seamless communication between AI agents and tools, thereby enhancing their collective functionality and impact in social and business contexts.

### 2. Prospective Coding Improves Learning in Deep Continuous-Time Recurrent Networks
**Authors:** Shivang Rawat, Mirko Morello, Flaviano Morone, David J. Heeger
**Link:** https://arxiv.org/abs/2609.04134v1
**Summary:** The paper addresses the problem of gradient attenuation in deep continuous-time recurrent networks caused by delays in bottom-up signals and errors. The authors introduce Recursive Quadrature Filters (RQFs), which implement a new approach to make layer inputs prospective, thereby improving gradient flow. Their key finding is that this method enhances learning performance in various network architectures, demonstrating significant accuracy improvements on tasks such as raw-audio speech recognition.

### 3. Environment Evolution for Terminal Agents
**Authors:** Zhiyuan Fan, Tinghao Yu, Yuanjun Cai, Jiang Zhou, Jiangtao Guan, Jincheng Liu, Yun Yang, Dingxin Hu, Zhuo Han, Xing Wu, Feng Zhang, Lilin Wang
**Link:** https://arxiv.org/abs/2609.04128v1
**Summary:** The paper addresses the challenge of training terminal agents by enhancing the difficulty of their interactive environments as the agents improve. The authors introduce an "environment evolution" method that incrementally adjusts environment complexity off-policy, providing continuous learning signals throughout training. Their approach demonstrates significant improvements in performance, with agents showing up to an 18.0 percentage point increase on benchmark tests.

### 4. Epistemic Warrant for LLM Recommendations: Characterizing the Basis for Reliance When Ground Truth Is Unavailable
**Authors:** Shai Vardi, João Sedoc
**Link:** https://arxiv.org/abs/2609.04127v1
**Summary:** The paper addresses the challenge of assessing the reliability of recommendations made by large language models (LLMs) when there is no clear ground truth. The authors propose a new concept called "epistemic warrant," which categorizes recommendations based on their stability and scope. Their findings indicate that this framework provides a more nuanced understanding of LLM recommendations compared to traditional measures of model reliability or user confidence.

### 5. Constant regret in general games via higher-order optimism
**Authors:** Omar Abbadi, Rida Laraki, Panayotis Mertikopoulos
**Link:** https://arxiv.org/abs/2609.04113v1
**Summary:** This paper addresses the challenge of achieving low regret in general N-player games, proposing a new algorithm called higher-order optimism with discounting (HOOD). This algorithm improves upon existing methods by incorporating a higher-order predictive model and entropic regularization, successfully guaranteeing a regret of \(O(N^3\log^2 K)\) for each player. The key contribution lies in effectively dampening oscillations in player strategies, thereby overcoming significant hurdles faced by previous approaches.

### 6. Sequential Beats Joint: On the Interplay between On-Policy Distillation and RLVR
**Authors:** Boyan Li, Bingsen Chen, Chenghao Yang, Ping Nie, Chen Zhao, Xi Ye
**Link:** https://arxiv.org/abs/2609.04108v1
**Summary:** The paper addresses the challenge of enhancing reasoning capabilities in large language models by effectively combining on-policy distillation (OPD) and reinforcement learning with verifiable rewards (RLVR). The authors propose a two-stage approach where OPD is applied first, followed by RLVR, demonstrating that this sequence significantly outperforms methods that combine both techniques simultaneously. Their findings indicate that OPD helps expand the range of solutions guided by a teacher, while RLVR fine-tunes these solutions, thus providing a practical strategy for improving model performance in reasoning tasks.

### 7. Hardware-Aware FP4 FlashAttention-4
**Authors:** Robert Hu
**Link:** https://arxiv.org/abs/2609.04105v1
**Summary:** The paper addresses the challenge of improving the speed of attention mechanisms in neural networks when using Blackwell's 4-bit floating-point (FP4) tensor cores, which do not inherently accelerate processing due to softmax conversions and dependencies. The authors propose a method called Direct-P that efficiently maps scores to FP4 probabilities for faster inference and a causal path that optimizes backward training with FP8 gradients, achieving up to 2.13 times the throughput compared to bfloat16. This approach leads to significantly faster single-GPU updates for large models, although the authors note that using FP4 in distributed training may lead to divergence in performance.

### 8. Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent Half of a Hybrid 27B LLM
**Authors:** Sergii Kozyrev, Davyd Maiboroda
**Link:** https://arxiv.org/abs/2609.04098v1
**Summary:** The paper addresses the challenge of effectively quantizing the recurrent components of a Hybrid LLM, specifically the Gated DeltaNet, to 4-bit precision without significant performance degradation. The authors introduce Minima, a quantization approach (NVFP4 W4A4) that successfully maintains low perplexity and high performance across multiple tasks while being smaller and faster than previous models. Key findings demonstrate that the quantization of the recurrent state is robust due to several mechanisms, including error localization and effective noise handling in long contexts, leading to superior efficiency in deploying the model.

### 9. Adaptive Vision-Language Grasping via Composable Foundation Priors and Generalizable Grasp Synthesis
**Authors:** Sixu Yan, Shikang Wang, Binhua Huang, Xuanlai Tang, Guohua Fan, Fan Huang, Haoxuan Li, Yongkang Li, Yuhan Li, Bencheng Liao, Zeyu Zhang, Wenyu Liu, Hangxin Liu, Xinggang Wang
**Link:** https://arxiv.org/abs/2609.04096v1
**Summary:** This paper addresses the challenge of adaptable robotic grasping by introducing a framework called AdaRoboVLG, which allows robots to generate and evaluate grasping strategies without needing to retrain their underlying policies for different tasks or hand types. The approach combines a generalizable base policy with specialized foundation models that provide useful context, leading to successful grasping even in complex environments. Key results show that this decoupled method maintains high performance while improving adaptability and learning efficiency across various robotic setups.

### 10. DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training
**Authors:** Shubham Gandhi, Saurabh Goyal, Kiran Kate, Yara Rizk
**Link:** https://arxiv.org/abs/2609.04094v1
**Summary:** The paper addresses the challenge of enabling long-horizon reinforcement learning agents to receive useful feedback when no clear success indicators are available. The authors introduce DRACO, a method that dynamically creates scoring rubrics during training and redistributes the evaluation across the steps that contributed to achieving key milestones, thus enhancing credit assignment. DRACO demonstrates significant performance improvements over existing models, achieving better scores on both in-domain and out-of-domain tasks without relying on traditional verification methods.
