---
## 2026-06-22

### 1. Analyzing Defensive Misdirection Against Model-Guided Automated Attacks on Agentic AI Systems
**Authors:** Reza Soosahabi, Vivek Namsani
**Link:** https://arxiv.org/abs/2606.20470v1
**Summary:** This paper addresses the challenge of defending agentic AI systems from increasingly sophisticated automated attacks, specifically prompt-injection and jailbreak attempts. The authors propose a novel defense strategy called Contextual Misdirection via Progressive Engagement (CMPE), which provides misleading responses to detected malicious interactions, thereby confusing attackers and reducing their success rates. The results demonstrate that CMPE can significantly diminish the effectiveness of these attacks, reducing their success rates by up to 100 times in certain benchmark scenarios.

### 2. Fisher-Geometric Sharpness and the Implicit Bias of SGD toward Flat Minima
**Authors:** Md Sakir Ahmed, Kumaresh Sarmah, Hemen Dutta
**Link:** https://arxiv.org/abs/2606.20469v1
**Summary:** The paper addresses the problem of understanding why stochastic gradient descent (SGD) seems to favor flat minima, which are thought to generalize better in deep learning, by establishing a reparametrization-invariant measure of flatness using Riemannian geometry based on the Fisher Information Matrix (FIM). The authors define a new mathematical concept of Riemannian sharpness and demonstrate that it correlates better with generalization performance than traditional Euclidean sharpness measures. Their findings show that SGD concentrates probability mass around Riemannian-flat minima, providing a rigorous explanation for the observed generalization capabilities of flat minima.

### 3. Agentic Symbolic Search: Characterizing PDEs Beyond Hand-crafted Expressions, Meshes, and Neural Networks
**Authors:** Zongmin Yu, Liu Yang
**Link:** https://arxiv.org/abs/2606.20467v1
**Summary:** The paper addresses the challenge of finding analytical solutions to partial differential equations (PDEs), which are typically derived through manual mathematical analysis or approximated via numerical simulations and neural networks. The authors introduce Agentic Symbolic Search (ASYS), a framework that combines PDE theory and search experience to generate testable symbolic programs, which are refined through a mix of evolutionary search and gradient-based optimization. ASYS successfully produces interpretable mathematical representations for various PDE problems, demonstrating a novel approach for automating the discovery of solutions beyond traditional methods.

### 4. Data Bias Mitigation under Coverage Constraints & The Price of Fairness
**Authors:** Bruno Scarone, Alfredo Viola, Renée J. Miller
**Link:** https://arxiv.org/abs/2606.20461v1
**Summary:** This paper addresses the issue of bias in machine learning models, particularly for individuals with intersecting sensitive attributes like race and gender, which often leads to poor performance and discriminatory outcomes. The authors extend a bias mitigation framework to include coverage constraints ensuring sufficient representation of all groups while maintaining data efficiency, rather than striving for complete bias reduction. Key findings show that their approach maintains predictive accuracy across various classifiers and highlights the importance of coverage constraints in enhancing model performance.

### 5. Context-Aware Hierarchical Bayesian Modeling of IVF Laboratory Environmental Conditions
**Authors:** Zahra Asghari Varzaneh, Reza Khoshkangini, Pia Saldeen, Lars Johansson, Thomas Ebner
**Link:** https://arxiv.org/abs/2606.20459v1
**Summary:** This paper addresses the problem of improving IVF pregnancy rate predictions by incorporating detailed laboratory environmental conditions, which have been largely overlooked. The authors developed advanced temporal features that capture the dynamics of incubator conditions and applied a hierarchical Bayesian Beta regression model to analyze data from clinics in Asia and Northern Europe. The key contribution is a significant reduction in prediction error, achieving a cross-validated error of 1.27% and demonstrating that environmental monitoring can provide valuable insights for IVF success rates.

### 6. Repurposing a Speech Classifier for Guided Diffusion-Based Speech Generation
**Authors:** Rostislav Makarov, Timo Gerkmann
**Link:** https://arxiv.org/abs/2606.20457v1
**Summary:** The paper addresses the issue of needing two separate models for classifier-guided speech generation, which can be inefficient. Instead, the authors propose repurposing an existing speech classifier by adding a lightweight subnetwork for diffusion generation, allowing the combined model to generate high-quality speech. The key contribution is demonstrating that this approach not only reduces memory and computational requirements but also effectively combines discriminative modeling with conditional speech synthesis.

### 7. SSH-Net: A Deep Neural Network for Predicting Failure Time Distribution Functions under Competing Risks with Application to GPU Data
**Authors:** Jie Min, Yueyao Wang, Mengkun Chen
**Link:** https://arxiv.org/abs/2606.20451v1
**Summary:** The paper presents SSH-Net, a deep learning model designed to predict failure times in systems experiencing competing risks, which is critical in engineering applications. By structuring the neural network to accommodate different groups of covariates through separate sub-networks, the model improves prediction accuracy for cause-specific failure outcomes. Validation results demonstrate that SSH-Net effectively predicts failure time distribution functions, particularly using data from Titan GPUs.

### 8. Topological Data Analysis for High-Dimensional Dynamic Process Monitoring
**Authors:** Angan Mukherjee, Tyler A. Soderstrom, Michael J. Kurtz, Victor M. Zavala
**Link:** https://arxiv.org/abs/2606.20443v1
**Summary:** This paper addresses the challenge of real-time monitoring of complex industrial processes using high-dimensional time-series data. The authors propose a novel method that combines topological data analysis with machine learning to represent the data as manifolds and utilize topological descriptors for event detection. Their results demonstrate that this trajectory-based approach effectively identifies a variety of events, outperforming traditional methods like principal component analysis and reconstruction-based models.

### 9. Evolutionary Two-Stage Hyperparameter Optimization Strategies for Physics-Informed Neural Networks
**Authors:** Fedor Buzaev, Dmitry Efremenko, Egor Bugaev, Andrei Ermakov, Denis Derkach, Daria Pugacheva, Fedor Ratnikov
**Link:** https://arxiv.org/abs/2606.20442v1
**Summary:** The paper addresses the challenges of optimizing hyperparameters in Physics-Informed Neural Networks (PINNs), which struggle with convergence and sensitivity to various parameters when solving Partial Differential Equations. The authors propose a novel two-stage hyperparameter optimization strategy that utilizes evolutionary algorithms for initial exploration of configurations, followed by refinement using gradient-based methods. Their approach demonstrates superior performance and lower mean error compared to traditional training methods across multiple PDE problems, all while operating within limited computational resources.

### 10. Interpretable Sperm Morphology Classification via Attention-Guided Deep Learning
**Authors:** Zahra Asghari Varzaneh, Reza Khoshkangini, Thomas Ebner, Lars Johansson
**Link:** https://arxiv.org/abs/2606.20438v1
**Summary:** The paper addresses the issue of male infertility linked to abnormal sperm morphology by developing an attention-guided deep learning model for sperm classification. By integrating EfficientNet-B0 with a Convolutional Block Attention Module, the model not only improves classification accuracy but also enhances interpretability, achieving high accuracy on standard datasets. The key contribution is the model's ability to provide both reliable results and visual explanations of its decision-making process, making it suitable for clinical use in fertility assessments.
