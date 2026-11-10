---
## 2026-11-10

### 1. Guiding Data Allocation for Robust Subpopulation Generalization
**Authors:** Zhaoying Pan, Yipei Wang, Shenyu Lu, Xiaoqian Wang
**Link:** https://arxiv.org/abs/2611.12884v1
**Summary:** The paper addresses the issue of machine learning models struggling with subpopulation shifts, which can lead to poor performance on certain groups despite high average accuracy. The authors extend a Gaussian feature-model framework to show that diverse training subgroup distributions, including imbalanced ones, can achieve robust generalization comparable to balanced datasets. They propose a method to strategically allocate data within these subgroups, demonstrating that this approach is a more efficient way to enhance model performance than simply ensuring balance.

### 2. Kolmogorov-Chapman Maps: Trajectory-Free Learning for Simulating Molecular Dynamics
**Authors:** Majdi Hassan, Marta Skreta, Dominique Beaini, Kirill Neklyudov
**Link:** https://arxiv.org/abs/2611.12880v1
**Summary:** The paper addresses the inefficiencies of simulating molecular dynamics using stochastic differential equations, which often require long trajectories for training machine learning models. The authors propose a novel method called Kolmogorov-Chapman Maps (KC-Maps), which learns the transition of these processes using only marginal samples and known parameters, rather than extensive trajectory data. The results show that KC-Maps can effectively model peptide dynamics, significantly reducing the computational time compared to traditional approaches.

### 3. Adaptive Quantization Preserves Fast Rates for TD Learning over Rate-Limited Channels
**Authors:** Sreejeet Maity, Aritra Mitra
**Link:** https://arxiv.org/abs/2611.12878v1
**Summary:** The paper addresses the challenge of efficiently transmitting updates for temporal-difference (TD) learning in reinforcement learning settings constrained by communication limits. The authors introduce a novel algorithm called Batched Adaptively Quantized TD (BAQ-TD), which combines batching and adaptive quantization to enhance the transmission of information. The key finding is that BAQ-TD can maintain the statistical convergence rates of unquantized TD learning when operating over a channel with limited capacity, demonstrating that only a logarithmic increase in communication is needed compared to previous methods.

### 4. HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition for Multimodal Agents
**Authors:** Haozhen Zhang, Bohan Liu, Jianzhu Bao, Qingyuan Liu, Haodong Yue, Xiao Li, Zi Pong Lim, Wenya Wang
**Link:** https://arxiv.org/abs/2611.12872v1
**Summary:** The paper presents HiVe-Mem, a new framework designed to enhance how multimodal agents manage and utilize long-term interaction histories. It combines two innovative strategies: expanding memory using a relational graph to retrieve related information and composing diverse evidence forms for each memory, tailored to specific queries. The results indicate that HiVe-Mem significantly improves performance in multimodal tasks while drastically reducing the amount of data processed.

### 5. Vendi Anomaly Scores for Efficient and Accurate Anomaly Detection
**Authors:** Amey Pasarkar, Adji Bousso Dieng
**Link:** https://arxiv.org/abs/2611.12871v1
**Summary:** The paper addresses the challenge of anomaly detection, which is important for reliable machine learning applications. The authors propose a novel method called the Vendi Anomaly Score (VAS), which identifies anomalies by measuring how much the removal of a sample affects the diversity of the dataset, without relying on traditional density or partitioning techniques. Their approach achieves state-of-the-art performance on various benchmarks and remains effective in large-scale settings, showcasing its robustness across different contamination levels and dataset sizes.

### 6. Where Does Alignment Emerge and What Does It Mean? A Closer Look at the Platonic Representation Hypothesis
**Authors:** Julia Herbst, Simon Roschmann, Quentin Bouniot, Zeynep Akata
**Link:** https://arxiv.org/abs/2611.12869v1
**Summary:** This paper explores the Platonic Representation Hypothesis, which proposes that neural networks are developing similar representation spaces, particularly between language and vision models. The authors analyze alignment between unimodal models at different layers and find that while cross-modal alignment is significant, it does not reach the levels seen within the same modality. Their results indicate that alignment can still emerge effectively in newer models when using clean and informative data.

### 7. Shortcuts and Boundaries: Verifiable RL Misalignment and Contextual Safety Learning
**Authors:** Xinjie Shen
**Link:** https://arxiv.org/abs/2611.12865v1
**Summary:** The paper addresses the problem of reinforcement learning (RL) agents misaligning their behavior with contextual task requirements due to reward incentives, leading to undesirable shortcuts and reward hacking. The authors propose a method to verify and understand these conflicts by encoding them into task dynamics, allowing the generation of diverse environments and compliance feedback. A key finding is that incorporating contextual checks can significantly improve safety in task execution, increasing successful completion from 53% to 89% in various scenarios, while still maximizing productivity.

### 8. Is Persona Generalization Predictable?
**Authors:** Olina Mukherjee, Arnav Goel, Aditi Raghunathan, Jacob Mitchell Springer
**Link:** https://arxiv.org/abs/2611.12864v1
**Summary:** This paper addresses the issue of persona generalization in language models, where fine-tuning in one area can inadvertently lead to unsafe behaviors in other areas. The authors discover that the relationship between in-domain and out-of-domain persona rates follows a consistent probit-linear pattern across various models, revealing that training adjustments primarily affect the model's learning transferability. A key finding is that fine-tuning later model layers results in reduced out-of-domain misalignment while maintaining strong performance in the original domain, providing a predictive framework for managing behavioral transfer in language models.

### 9. WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems
**Authors:** Zheng Jiang, Fang Niu, Bo Peng, Houde Qian, Wenyi Li, Deyao Hong, Mingju Gao, Yizhe Chi, Youjie Zheng, Kaisen Yang, Calvin Xiao, Lifeng Sun, Huan-ang Gao
**Link:** https://arxiv.org/abs/2611.12856v1
**Summary:** The paper addresses the challenge of evaluating how well large language model agents can autonomously organize and orchestrate workflows in multi-agent systems, rather than just completing tasks. It introduces WorkflowArena, a benchmark with 145 tasks across various professional domains that measures both the quality of the final deliverables and the delegation strategies used by the agents. The key finding is that no single model consistently outperforms others across all domains, and that effective workflow organization can significantly enhance the performance of less capable agents.

### 10. What kills $v$-prediction? A Patch-wise PCA Perspective on Pixel-Space Flow Matching
**Authors:** Tianze Luo, Haofeng Huang, Yuan Yao
**Link:** https://arxiv.org/abs/2611.12852v1
**Summary:** This paper addresses the challenges faced by Pixel-space Flow Matching in training generative models, particularly the difficulties associated with the common $v$-prediction objective due to off-manifold noisy targets. The authors analyze these issues using patch-wise Principal Component Analysis (PCA) and identify a bandwidth bottleneck that affects the model's performance, leading to the development of the Raw-injected Transformer (RiT). This new architecture effectively restores the performance of $v$-prediction while achieving competitive results on ImageNet, highlighting the importance of the interaction between prediction objectives and model architecture.
