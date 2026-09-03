---
## 2026-09-03

### 1. A Common Measure of Communication for Speech Brain-Computer Interfaces
**Authors:** Dulhan Jayalath, Benjamin Ballyk, Oiwi Parker Jones
**Link:** https://arxiv.org/abs/2609.02887v1
**Summary:** The paper addresses the challenge of comparing different speech brain-computer interface (BCI) systems, which currently suffer from inconsistent metrics due to variations in datasets and vocabularies. The authors propose a new measure called open-vocabulary mutual information (OVMI) that quantifies the information a speech BCI can convey relative to the intended vocabulary. They show that using OVMI can enhance the accuracy of speech BCIs by up to 16.3% and provides a standardized way for the community to evaluate and improve these systems.

### 2. Discriminative World Models for Web Agents
**Authors:** Kelvin Li, Dhruv Pendharkar, Anish Pahilajani, Chuyi Shang, Leon Oks, Leonid Karlinsky, Rogerio Feris, Trevor Darrell, Roei Herzig
**Link:** https://arxiv.org/abs/2609.02885v1
**Summary:** The paper addresses the misalignment between world models used by web agents for action selection and the ranking of predicted outcomes. The authors propose a new training objective called predicted-state matching, which focuses on distinguishing the true resulting state from alternatives. Their experiments demonstrate that this approach significantly improves action ranking and task success compared to traditional methods, showcasing the effectiveness of their discriminative training strategy.

### 3. Graph Machine: Towards Better Pretraining via Edges
**Authors:** Lintai Hou
**Link:** https://arxiv.org/abs/2609.02881v1
**Summary:** The paper presents the Graph Machine (GM), a new architecture designed to improve pretraining efficiency by using sparse, dynamic routing while maintaining an \(O(n)\) state size. GM replaces most dense layers in a Transformer model with its sparse layers, employing a referral mechanism for dynamically updated edges. The key finding is that even with significantly reduced token retrieval in the sparse layers, the model maintains robust performance, with one configuration showing a slight improvement in loss.

### 4. GRADSOLVE: fast exact gradients for ODE ensembles on GPUs
**Authors:** Alessio Spurio Mancini
**Link:** https://arxiv.org/abs/2609.02876v1
**Summary:** The paper presents GRADSOLVE, an open-source library that enables fast and exact computation of gradients for ensembles of ordinary differential equations (ODEs) on NVIDIA GPUs. It addresses the challenge of efficiently differentiating ODE solutions by combining a reverse-mode differentiation approach with adaptive solvers, achieving significant speed improvements. The key contribution is that GRADSOLVE computes gradients much faster than existing methods, offering up to 14.1 times the efficiency for gradient calculations while maintaining accuracy, especially beneficial for large ensembles.

### 5. Towards Trustworthy Autonomous Robots: An Explainable AI-Based Decision Framework
**Authors:** Cagri Temel
**Link:** https://arxiv.org/abs/2609.02861v1
**Summary:** The paper addresses the challenge of understanding and auditing decisions made by deep learning-based autonomous robots, which often lack transparency during incidents. It proposes a decision framework called TRACE, which organizes decision-making into four structured layers that allow actions to be traced back to specific sensor evidence. The experimental results show that TRACE achieves high levels of traceability, continuity, and reconstructability in decision-making, thereby enhancing the transparency required for compliance with regulations like the EU AI Act.

### 6. User Feedback Provides a Unique Signal that LLMs Can not Detect
**Authors:** Shachar Don-Yehiya, Leshem Choshen, Omri Abend
**Link:** https://arxiv.org/abs/2609.02859v1
**Summary:** This paper addresses the challenge of effectively utilizing user feedback to improve Large Language Models (LLMs), which is often seen as noisy and ineffective. The authors demonstrate that user feedback is a valuable signal for model enhancement by constructing both synthetic and real-world datasets to compare model revisions made with and without feedback. Their key finding reveals that feedback-informed revisions significantly outperform baseline revisions, highlighting a bias in current evaluation methods that often overlook successful corrections prompted by user feedback.

### 7. Improved Gradient Descent Lower Bounds Beyond Nesterov
**Authors:** Yuhan Ye, Kaizhao Liu
**Link:** https://arxiv.org/abs/2609.02855v1
**Summary:** This paper explores the limits of acceleration in gradient descent methods for smooth convex optimization, presenting improved lower bounds on convergence rates with predetermined stepsizes. The authors establish new non-anytime and anytime lower bounds that surpass previous results, highlighting a significant difference in achievable convergence rates depending on whether an algorithm is allowed to use the solution at each iteration or not. These findings clarify the performance capabilities of gradient descent under specific conditions, revealing tighter constraints on its efficiency.

### 8. The Implications of Linguistic Illegibility for LLM Security
**Authors:** James Mickens
**Link:** https://arxiv.org/abs/2609.02852v1
**Summary:** The paper addresses the issue of "linguistic illegibility" in large language models (LLMs), where the external language outputs do not accurately reflect the internal computations of the models. The authors propose that reliance on linguistic self-reporting for security measures is flawed and advocate for taint tracking as a more robust sandboxing method that defines what system states should remain unaffected by model outputs. This approach, along with additional sandboxing mechanisms, aims to ensure greater security and prevent potential exploits in LLMs.

### 9. Post-Training Language Models for Gold-Medal Performance in Coding Competitions
**Authors:** Aleksander Ficek, Sean Narenthiran, Mehrzad Samadi, Somshubra Majumdar, Boris Ginsburg
**Link:** https://arxiv.org/abs/2609.02849v1
**Summary:** This paper addresses the challenge of competitive programming by developing specialized language models that excel in coding competitions. The authors create Nemotron-3 models using a combination of large problem curation, supervised fine-tuning, and reinforcement learning strategies, along with a novel feedback-driven method called GenCorrect to optimize solution generation. Their key finding is that their models outperform both human contestants and previous benchmarks, achieving record scores in the International Olympiad in Informatics (IOI) competitions.

### 10. UE5M3 FP4 Block Scaling for Stable Language Model Pretraining
**Authors:** Robert Hu, Carlo Luschi, Paul Balanca
**Link:** https://arxiv.org/abs/2609.02846v1
**Summary:** The paper addresses the challenges of stable pretraining for 4-bit floating-point language models, specifically focusing on the limitations of current tensor scaling methods. The authors propose a new approach that combines E5M3 block scales with selective stochastic rounding and forgoes some complex techniques, achieving better training performance. Their results show improved training and validation losses compared to existing methods, highlighting the benefits of a simpler pretraining strategy.
