---
## 2026-08-09

### 1. HarnessOpt-Bench: Evaluating LLMs at Harness Optimization
**Authors:** Varun Ursekar, Apaar Shanker, Yash Maurya, Shehab Yasser, Vijay S. Kalmath, Veronica Chatrath, Yuan Xue
**Link:** https://arxiv.org/abs/2608.06301v1
**Summary:** The paper addresses the challenge of optimizing the harnesses (prompts, tools, and orchestration) that surround large language models (LLMs) to enhance their performance in agentic systems. It introduces HarnessOpt-Bench, a benchmarking framework that allows automated optimization of these harnesses through an iterative process guided by evaluation feedback. The key findings indicate that different LLMs can effectively act as optimizers, revealing significant variation in optimization performance across tasks, which highlights substantial potential for improvement in harness optimization methods.

### 2. Bias Analysis of L2 Speaking Assessment Systems Using Concept Activation Vectors
**Authors:** Arya Labroo, Mengjie Qian, Kate Knill
**Link:** https://arxiv.org/abs/2608.06300v1
**Summary:** This paper addresses the challenge of ensuring that automatic speaking assessment systems for second language learners evaluate speaking proficiency accurately, without being biased by irrelevant factors like a speaker's first language or age. The authors extend the use of Concept Activation Vectors (CAVs) to analyze bias in two different neural assessment models, revealing that whether a concept is influential in scoring depends on the model's architecture rather than the concept itself. They find that while sparse autoencoders can enhance the linear recovery of concepts, they also reduce sensitivity to the original activation spaces, underscoring the need for careful bias auditing in these systems.

### 3. On-Policy Self-Distillation without Any Supervision
**Authors:** Yijiang Li, Bingyang Wang, Yijun Liang, Yunjie Tian, Di Fu, Nuno Vasconcelos
**Link:** https://arxiv.org/abs/2608.06296v1
**Summary:** The paper addresses the challenge of on-policy self-distillation in large language models, which traditionally rely on external supervision. It introduces Unsupervised On-Policy Self-Distillation (U-OPSD), a method that utilizes a model's own generated outputs to refine its performance through internal consistency. The key findings demonstrate that U-OPSD significantly improves model accuracy across multiple benchmarks, often exceeding the results of supervised distillation methods.

### 4. QuanTiMedAI: Quantum-Enhanced Time-Series Model guided by Agentic AI for Cardiac Arrest Mortality Prediction
**Authors:** Mutasim Fuad Sarker, Adiba Rahman Namira, Wafa Binte Alam, Md Adnan Arefeen, Mahzabeen Emu, Sumaiya Tabassum Nimi
**Link:** https://arxiv.org/abs/2608.06294v1
**Summary:** The paper presents QuanTiMedAI, a novel framework for improving mortality prediction in cardiac arrest patients by leveraging quantum computing and agentic AI. This approach integrates a language model for feature selection with a quantum recurrent network that effectively accounts for the temporal dynamics of patient data. The key contribution is that QuanTiMedAI achieves a higher predictive accuracy with fewer parameters compared to existing methods, demonstrating the potential of quantum-enhanced modeling in healthcare.

### 5. NeSy-RAG: Neuro-Symbolic RAG for Explainable Question Answering
**Authors:** Jonas Gann, Michael Gertz
**Link:** https://arxiv.org/abs/2608.06292v1
**Summary:** The paper presents NeSy-RAG, a neuro-symbolic framework designed to enhance explainability in retrieval-augmented generation (RAG) for question answering, addressing the challenges of opaque reasoning and incomplete user context. By synthesizing Prolog modules from retrieved text and introducing a mechanism to detect missing user-specific information, the system provides clear, verifiable reasoning steps linked to their sources. NeSy-RAG demonstrated superior performance on the ShARC benchmark, achieving 61.1% accuracy compared to 42.8% by a traditional RAG model, without requiring domain-specific training.

### 6. BaKron: Efficient Quantization with Kronecker-Factored Hessians
**Authors:** Johann Birnick, Rayan Saab
**Link:** https://arxiv.org/abs/2608.06291v1
**Summary:** The paper introduces BaKron, an efficient algorithm for neural network quantization that leverages two-sided Kronecker-factored Hessians to better capture the correlations between output coordinates. By employing a divide-and-conquer strategy with anti-diagonal parallelism, BaKron significantly reduces computational complexity from quadratic to linear in relation to the weight matrix dimensions while maintaining the same scaling as existing methods. The authors provide practical benchmarks and demonstrate the effectiveness of their approach in capturing richer curvature information during the quantization process.

### 7. Surv-IPTB: An Attention-Based Model for Estimating Individual Probability of Treatment Benefit with Survival Data
**Authors:** Lev V. Utkin, Stanislav K. Kogan, Andrei V. Konstantinov
**Link:** https://arxiv.org/abs/2608.06288v1
**Summary:** The paper introduces Surv-IPTB, a novel attention-based model designed to estimate the probability that an individual patient will benefit from treatment in survival analysis, where the goal is to predict extended survival times. The authors reformulate this estimation task into a binary classification problem using pairwise patient comparisons, effectively handling censored data through interval-valued probabilities. They demonstrate that Surv-IPTB outperforms conventional methods in complex scenarios, thus providing a scalable and statistically sound solution for assessing personalized treatment benefits.

### 8. The Tamed Subgradient Unadjusted Langevin Algorithm beyond Convexity
**Authors:** Iosif Lytras, Nikolaos Makras, Sotirios Sabanis
**Link:** https://arxiv.org/abs/2608.06283v1
**Summary:** The paper addresses the challenge of sampling from complex target distributions that are non-smooth and non-convex, which can grow rapidly in certain regions. The authors introduce the Subgradient Tamed Unadjusted Langevin Algorithm (SG-TULA), a novel method that leverages subgradients and taming techniques to ensure stable sampling without the need for smoothing. They demonstrate that SG-TULA achieves improved convergence rates and provide explicit guarantees, also successfully applying it to the pretraining of language models like GPT-2, outperforming traditional optimization methods in terms of theoretical guarantees.

### 9. Stochastic Dynamics on Persistence Diagram Space via Reinforcement Learning
**Authors:** Farzana Nasrin
**Link:** https://arxiv.org/abs/2608.06276v1
**Summary:** This paper addresses the challenge of modeling the dynamic behavior of persistence diagrams, which summarize topological structures, in a probabilistic manner. The authors introduce a reinforcement learning framework that allows persistence diagrams to evolve through topology-aware modifications, establishing a controlled way to model stochastic dynamics in this space. Key findings show that their approach can effectively simplify diagrams while preserving essential topological features, making it a valuable tool for applications like neuroimaging analysis.

### 10. The Illusion of Visual Tool-Use: A Causal Audit of Thinking with Images
**Authors:** Zhiheng Wang, Bo Peng, Lai Wei, Chaochao Lu
**Link:** https://arxiv.org/abs/2608.06270v1
**Summary:** The paper investigates the effectiveness of visual tool-use in multimodal large language models (LLMs) by examining whether visual inputs actually improve answers to questions. Through a causal analysis involving various intervention methods, the authors reveal that visual tool-use often does not cause improvements in accuracy, highlighting two key failure modes where visual inputs are either irrelevant or poorly utilized. The study concludes that despite some aggregate accuracy gains, visual tool-use doesn't consistently enhance model performance across many scenarios, coining this phenomenon the "illusion of visual tool-use."
