---
## 2026-11-02

### 1. Latent Reasoning in Continuous Space for Unified Multimodal Models
**Authors:** Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee, Minsu Cho, Jinwoo Shin
**Link:** https://arxiv.org/abs/2610.42149v1
**Summary:** The paper addresses the challenge of integrating language-based reasoning into image generation within Unified Multimodal Models, which typically struggle due to a mismatch between discrete token reasoning and continuous image generation. To overcome this, the authors propose a Latent Reasoning framework in Continuous space (LARC) that transitions reasoning from discrete tokens to continuous hidden states through a two-stage training process. The key contribution is that LARC significantly enhances image generation quality and compositional fidelity, achieving state-of-the-art results on benchmarks while demonstrating improved adaptability during testing.

### 2. Flide: Accelerating Decision Inference with Exact State Forking
**Authors:** Bobo Li, Jiajia Song, Hao Fei, Wynne Hsu, Mong Li Lee
**Link:** https://arxiv.org/abs/2610.42148v1
**Summary:** Flide addresses the inefficiencies of existing inference engines in decision models used by LLM agent systems, which struggle with computational overhead and unreliable output. It introduces a novel execution method that separates the logical structure of decision requests from their physical processing, using a technique called ForkAttention to efficiently handle dependencies. The key outcome is that Flide significantly speeds up query responses—up to 9.5 times faster than current models—while maintaining high accuracy in results, thereby enhancing the scalability of decision-making in intelligent agent systems.

### 3. Latent Sparse Attention: Towards Subquadratic Ultra-Long Context Attention
**Authors:** Ales Kubicek, Andrea Caciolai, Liangzu Peng, Sukrit Sumant, Benjamin Hoover, Fraser Greenlee, Ruairidh M. Battleday, Radim Urban, Torsten Hoefler, James C. R. Whittington
**Link:** https://arxiv.org/abs/2610.42147v1
**Summary:** The paper addresses the challenge of efficiently processing ultra-long contexts (over 1 million tokens) in attention-based models, which typically struggle with quadratic computational costs. The authors present Latent Sparse Attention (LSA), which utilizes a learned hierarchical clustering of keys to significantly reduce computation while maintaining accuracy. Their method shows remarkable speed improvements in attention operations, achieving up to 72.4 times faster performance in prefill tasks with similar accuracy compared to conventional sparse and full attention methods.

### 4. Hierarchical World Models with Implicit Dynamics
**Authors:** Gaoyue Zhou, Yvonne Wu, Zichen Jeff Cui, Nicolas Ballas, Mido Assran, Lerrel Pinto, Yann LeCun
**Link:** https://arxiv.org/abs/2610.42146v1
**Summary:** The paper addresses the challenge of effective long-horizon planning for embodied agents, which often struggle with errors and complexity when using traditional methods. The authors propose a new hierarchical framework called ID-WM (Implicit Dynamics World Models) that separates high-level decision-making from low-level execution, allowing agents to generate more accurate and flexible plans. This approach demonstrates a 38.5% performance improvement over existing methods in various tasks, significantly reducing errors and enhancing performance in complex scenarios.

### 5. RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory
**Authors:** Shengguang Wu, Suning Huang, Cherie Ho, Ria Doshi, Hao Zhu, Serena Yeung-Levy
**Link:** https://arxiv.org/abs/2610.42141v1
**Summary:** The paper addresses the challenge of designing control frameworks for robotic agents, which are typically handcrafted for each new setup. It introduces RoboArchitect, an automated system that observes a robot's performance, identifies issues, and iteratively improves the control harness around a fixed policy. Key results show that this approach significantly boosts the robot's success rates on unseen tasks and scenes, indicating that optimizing the harness could yield substantial improvements in robotic manipulation without altering the underlying model.

### 6. Counting on Dummies: Privacy Amplification with Observable Counts and Truncated Batches
**Authors:** Vitaly Feldman, Audra McMillan, Kunal Talwar
**Link:** https://arxiv.org/abs/2610.42139v1
**Summary:** The paper addresses the challenge of maintaining privacy in Differentially Private Stochastic Gradient Descent (DP-SGD) when using varying batch sizes that may be revealed during processing, particularly in the context of truncated batches. The authors propose a mechanism that incorporates random dummy points to obscure the visible batch sizes, thereby preserving privacy even when batch truncation occurs. Their results show that this approach achieves improved privacy efficiency compared to existing methods, demonstrating its practical effectiveness in distributed settings.

### 7. A Better Critic Matters for Distribution Matching Distillation
**Authors:** Zongze Wu, Xianbang Wang, Zhengyang Geng, Mingdeng Cao, Zhoutong Zhang, Richard Zhang, Eli Shechtman, Ruiming Cao
**Link:** https://arxiv.org/abs/2610.42135v1
**Summary:** The paper addresses the challenge of improving the effectiveness of Distribution Matching Distillation (DMD) in training student models by examining the role of the critic in this process. The authors propose two enhancements: scaling the critic's capacity alongside the teacher's and introducing a step-aware critic (STAC) that provides tailored feedback based on the student's generation step. These improvements lead to better performance in various model generation tasks, mitigating training collapse and enhancing student quality.

### 8. Instance-dependent sequential limits as an exact information ledger
**Authors:** Akshay Balsubramani
**Link:** https://arxiv.org/abs/2610.42133v1
**Summary:** This paper addresses the challenge of establishing precise instance-dependent limits for various decision-making problems, including bandit regret and Markov decision processes. The authors present a unified approach that employs a chain of statistical techniques to derive these limits as an exact information ledger. A key contribution is the identification of differences between standard algorithms and classical limits across various applications, which enhances our understanding of their performance in practice.

### 9. DecisionRank: On-Policy Distillation for Decision-Model Rerankers
**Authors:** Yanran Wu, Dian Yu, Chongyang Bai, Jieyi Zhang, Rui Liu, Tianyi Chen, Shike Mei, Hang Cui, Frank Shyu, Sandeep Pandey, Luke Simon, Chunwei Liu, Xi Liu
**Link:** https://arxiv.org/abs/2610.42128v1
**Summary:** The paper addresses the challenge of transferring ranking knowledge from a generative language model (LLM) to a decision model for structured tasks, aiming to improve retrieval efficiency without the latency of autoregressive methods. The authors propose a novel training technique called DecisionRank, which employs on-policy distillation in item-space to enhance the decision model's ranking through direct feedback from the LLM. The significant outcome is that DecisionRank outperforms larger generative models while being significantly faster, achieving state-of-the-art results on various retrieval benchmarks.

### 10. Physiological Trajectories and Observation Patterns in ICU Mortality Prediction: Transportability Under Changing Measurement Conditions
**Authors:** Benjamin T. Pike
**Link:** https://arxiv.org/abs/2610.42126v1
**Summary:** The study investigates how well physiological data and observation patterns predict mortality in ICU patients, specifically examining the impact of timing and measurement conditions on prediction accuracy. By analyzing data from multiple hospital databases, the researchers found that physiological trajectories consistently improved prediction performance, while the benefits of observation patterns varied significantly with timing and availability of measurements. The key takeaway is that clinical prediction models should be tested not just on different patient groups but also under the specific conditions in which their data was collected.
