---
## 2026-09-11

### 1. GPU-CFR: 80x Faster Counterfactual Regret Minimization by Compiling the Game to Static Dataflow and CUDA Graph Replay
**Authors:** Boning Li, Longbo Huang
**Link:** https://arxiv.org/abs/2609.11923v1
**Summary:** The paper addresses the inefficiencies of existing GPU implementations of Counterfactual Regret Minimization (CFR), which traditionally perform worse than optimized CPU code despite the computational potential of GPUs. The authors introduce GPU-CFR, a compiler and runtime that optimizes the CFR process by compiling game data into a static structure and minimizing runtime overhead through techniques like static chance folding and CUDA Graph Replay. As a result, GPU-CFR achieves a remarkable performance improvement, running 29.8 to 80.4 times faster than previous GPU methods and significantly outpacing the fastest CPU implementations for various games.

### 2. General Quantification of Covariate and Concept Shifts
**Authors:** Hongbo Chen, Li Charlie Xia
**Link:** https://arxiv.org/abs/2609.11918v1
**Summary:** The paper addresses the challenge of generalizing machine learning models when faced with changes in data distribution, a problem that traditional theoretical bounds struggle to handle effectively. The authors introduce a new definition of concept shifts, termed $γ^{*}\!$-concept shifts, and develop a general error bound that encompasses both covariate and $γ^{*}\!$-concept shifts. They also present a tool called DataShifts that quantifies these distribution shifts and provides reliable error estimates for a wide range of applications.

### 3. Data Scarcity and Model Sparsity: Mixtures-of-Experts Overfit More to Repeated Data
**Authors:** Atindra Jha, Margaret Li, Jure Leskovec, Percy Liang, Luke Zettlemoyer
**Link:** https://arxiv.org/abs/2609.11917v1
**Summary:** This paper investigates how data repetition negatively affects the performance of Mixture-of-Experts (MoE) models compared to dense transformers, particularly under conditions of data scarcity. The authors experiment with varying data repetition and apply regularization techniques to combat overfitting. They find that while MoEs deteriorate more quickly with repeated data, certain regularization strategies—especially strong masking—can help them maintain better performance than dense models, highlighting the need for methods to minimize over-specialization in MoEs.

### 4. Can Edge-Deployable Vision-Language Models Identify Species?
**Authors:** William Zhou, Mayukha Siripuram, Xiao Yan, Ziqi Liu, Yi Ding
**Link:** https://arxiv.org/abs/2609.11916v1
**Summary:** The paper investigates whether small, locally-deployable vision-language models (VLMs) can effectively identify animal species from camera trap images, which often suffer from poorer quality compared to standard photographs. Four VLMs were compared against a specialist model, BioCLIP, across various species and image types, revealing that while all models performed better than chance, they struggled with field images due to quality issues rather than model weaknesses. Ultimately, BioCLIP, despite having fewer parameters, significantly outperformed the VLMs, indicating that specialized training data is crucial for better identification in real-world applications.

### 5. Generative Marketing Mix Modeling: A Causal Inference Framework Linking GEO and GEM to Business Impact
**Authors:** Masahiro Kato, Daiki Honma, Taka Kato
**Link:** https://arxiv.org/abs/2609.11915v1
**Summary:** The paper addresses the challenge of measuring the impact of Generative Engine Optimization (GEO) and Generative Engine Marketing (GEM) on business outcomes, as conventional marketing data fail to capture user engagement with generated content. The authors introduce Generative Marketing Mix Modeling (GMMM), a framework that combines various data sources to estimate causal effects more accurately. Key contributions include establishing conditions for identifying these effects and demonstrating the method's effectiveness through simulations involving product recommendations in English and Japanese.

### 6. Distance generalization in transformers: why bother with positional encoding?
**Authors:** Daniel Henrik Nevermann, Claudius Gros
**Link:** https://arxiv.org/abs/2609.11913v1
**Summary:** This paper investigates how transformers handle distance generalization, which refers to the model's ability to perform tasks when the distances between tokens differ from what it encountered during training. The authors developed synthetic tasks to examine the impacts of various positional encoding schemes and data diversity on performance with unseen distances. They found that understanding the underlying mechanisms of distance generalization is crucial, and explored how different factors like positional encodings can influence the outcome.

### 7. Artificial Id: Drive and Persistent Alignment in Agentic AI
**Authors:** Yakov Pyotr Shkolnikov
**Link:** https://arxiv.org/abs/2609.11911v1
**Summary:** The paper addresses the challenge of managing Agentic AI systems that operate beyond specific tasks while adapting over time. The authors introduce the concept of an "artificial id," an internal mechanism that helps the AI determine when to continue, stop, or change its behavior without relying on explicitly defined objectives. Their experiments demonstrate that this adaptive persistence can facilitate beneficial behavior, but also pose risks of misalignment and unintended actions across different tasks, highlighting the need for robust control mechanisms in such systems.

### 8. From Protocols to Evidence: Bounded Claims for AI in Service of the Common Good
**Authors:** Nitesh V. Chawla, Paulo Benanti
**Link:** https://arxiv.org/abs/2609.11910v1
**Summary:** The paper addresses the challenges posed by AI in the context of existing institutional failures related to responsiveness and accountability. It proposes a framework for evaluating AI through protocols that emphasize responsible deployment and evidence-based claims, linking technological interventions to ethical considerations based on human dignity. The key contribution is the development of a "rupture test" that connects institutional shortcomings with AI system evaluations, ensuring that deployment claims remain grounded in verified evidence.

### 9. TART: A Modular Tool for Technique-Aware Audio-to-Tablature Guitar Transcription
**Authors:** Akshaj Gupta, Hwi Joo Park, Andrea Guzman, Shamak Gowda, Samhita Konduri, Jiachen Lian, Robin Netzorg, Gopala Anumanchipalli
**Link:** https://arxiv.org/abs/2609.11904v1
**Summary:** The paper presents TART, a new system designed to improve automatic transcription of guitar audio into tablature, specifically addressing challenges like capturing expressive techniques and correct note assignments. TART uses a modular approach with four main components, leading to significant performance improvements over previous methods across several benchmarks. Notably, it is the first framework capable of generating guitar tablature that includes both fingering and expressive technique details directly from audio.

### 10. MindTopo: Can Foundation Models Reason in Topological Space?
**Authors:** Yunfei Ge, Anbang Liu, Qineng Wang, Johnalbert Garnica, Jianwen Lyu, Zihan Wang, Reuben Tan, Jianfeng Gao, Ruohan Zhang, Yining Hong, Jiajun Wu, Manling Li
**Link:** https://arxiv.org/abs/2609.11900v1
**Summary:** The paper presents MindTopo, a new benchmark designed to assess the topological reasoning abilities of foundation models, as spatial reasoning involves understanding both metric and topological relationships. This benchmark evaluates models on their ability to reason about and plan in topological spaces through various cognitively grounded properties. Key findings indicate that while models perform better at reasoning tasks compared to planning, they still lag significantly behind human capabilities, even after fine-tuning and reinforcement learning.
