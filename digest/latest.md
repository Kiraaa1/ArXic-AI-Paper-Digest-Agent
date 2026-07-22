---
## 2026-07-22

### 1. Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning
**Authors:** Lizhe Fang, Weizhou Shen, Tianyi Tang, Yisen Wang
**Link:** https://arxiv.org/abs/2607.19345v1
**Summary:** This paper addresses the issue of large language models excessively copying text from their inputs instead of generating effective reasoning in long-context tasks. The authors introduce a novel reinforcement learning method called GEAR, which rewards models for focusing on relevant evidence and penalizes them for using irrelevant information. Their approach significantly improves model accuracy—by up to 4.6 points—and reduces repetitive copying, particularly in longer contexts, highlighting the importance of grounding in relevant evidence for effective reasoning.

### 2. Appearance Pointers -- Multimodal Region Control of Diffusion Transformers
**Authors:** Rahul Sajnani, Yulia Gryaditskaya, Radomír Měch, Srinath Sridhar, Matheus Gadelha
**Link:** https://arxiv.org/abs/2607.19344v1
**Summary:** The paper addresses the challenge of precise regional control in image generation using Diffusion Transformers, which often struggle to effectively translate text and image inputs into desired outputs. The authors propose a method called appearance pointers, which are compact tokens that guide the model to focus on specified areas and cues in the input. Their approach achieves performance that meets or exceeds existing methods while allowing for flexible multimodal control without needing to retrain the underlying model.

### 3. CodeRescue: Budget-Calibrated Recovery Routing for Coding Agents
**Authors:** Qijia He, Jiayi Cheng, Chenqian Le, Rui Wang, Xunmei Liu, Yixian Chen, Jie Mei, Zhihao Wang, Xupeng Chen, Yuhuan Chen, Tao Wang
**Link:** https://arxiv.org/abs/2607.19338v1
**Summary:** The paper presents CodeRescue, a method for optimizing decision-making in coding agents after a failure by determining when to continue using low-cost models and when to escalate to more expensive ones. The approach involves training a router with execution feedback and incorporating a Conformal Risk Control layer to adapt to different budget scenarios. The key contribution is the demonstration that this calibrated strategy can significantly outperform traditional methods in solving coding tasks while reducing costs, achieving a higher solve rate with less expenditure.

### 4. Agents in the Wild: Where Research Meets Deployment
**Authors:** Grace Hui Yang, Pranav N. Venkit, Hooman Sedghamiz, Enrico Santus, Victor Dibia, Ioana Baldini
**Link:** https://arxiv.org/abs/2607.19336v1
**Summary:** The paper addresses the challenges of deploying agentic systems, which are large language model-based architectures that can reason, plan, and coordinate in real-world applications. It combines insights from both research and practical case studies in fields like pharmaceutical discovery and finance to identify successful design patterns and strategies for ensuring robustness and reliability in these systems. The authors provide practical tools such as evaluation checklists and templates to help practitioners implement safe deployments across various industries.

### 5. 1-Lipschitz Neural Networks on Hadamard Manifolds
**Authors:** Davide Murari, Marta Ghirardelli, Ben Adcock, Elena Celledoni, Brynjulf Owren, Carola-Bibiane Schönlieb
**Link:** https://arxiv.org/abs/2607.19335v1
**Summary:** This paper addresses the challenge of designing robust neural networks with a controlled Lipschitz constant, specifically on Hadamard manifolds which differ from standard Euclidean spaces. The authors develop 1-Lipschitz neural networks using Busemann functions and geometry-preserving layers, demonstrating their effectiveness in robust classification on the Poincaré disk and improved covariance reconstruction on symmetric positive definite matrices compared to traditional methods. The results highlight the networks' enhanced stability and robustness under geometric perturbations.

### 6. Fundamental limits of distributed multiclass classification from simple binary decisions
**Authors:** Ioannis Papageorgiou, Srinivas Nomula, Ayalvadi Ganesh, Sidharth Jaggi, Parimal Parag
**Link:** https://arxiv.org/abs/2607.19334v1
**Summary:** The paper addresses the challenge of building a multi-class classifier using a small number of simple binary classifiers, specifically focusing on cases where these classifiers are hyperplanes in a high-dimensional space. By analyzing a scenario in which class centers are independent Gaussian points affected by noise, the authors derive performance limits for this classification approach and validate their findings through simulations. The key contribution lies in providing explicit performance bounds that demonstrate the effectiveness of using binary decisions in constructing complex classifiers.

### 7. Provable diffusion-based posterior sampling for linear inverse problems via DDIM
**Authors:** Yuchen Jiao, Na Li, Changxiao Cai, Yuxin Chen, Gen Li
**Link:** https://arxiv.org/abs/2607.19333v1
**Summary:** The paper addresses the challenge of efficiently sampling from the posterior distribution in linear inverse problems, such as image restoration, using diffusion models. The authors introduce a novel algorithm called \pddim, which modifies the standard Diffusion Denoising Implicit Models (DDIM) to incorporate measurement data seamlessly. Their key contribution is the proof of convergence to the Bayesian posterior, demonstrating that this method outperforms existing approaches while remaining computationally efficient and straightforward to implement.

### 8. ROMS-IMLE: A Minimalist Approach to Competitive Single-Step Generative Modelling
**Authors:** Chirag Vashist, Ke Li
**Link:** https://arxiv.org/abs/2607.19332v1
**Summary:** The paper introduces a streamlined generative modeling approach that challenges the complexity of current models by using a simple training objective and a moderately sized convolutional network. By employing Implicit Maximum Likelihood Estimation (IMLE) and avoiding iterative denoising techniques, the model achieves competitive performance, producing high-quality samples efficiently with an FID score of 2.56 on ImageNet 256. This minimalist strategy highlights that effective generative modeling can be achieved without the intricate methodologies commonly employed in the field.

### 9. ISO: An RLVR-Native Optimization Stack
**Authors:** Hanqing Zhu, Wenyan Cong, Zhizhou Sha, Sagnik Mukherjee, Xinyuan Song, David González-Martínez, Xiaoxia Wu, Yuandong Tian, Shiwei Liu, David Z. Pan, Zhangyang "Atlas" Wang
**Link:** https://arxiv.org/abs/2607.19331v1
**Summary:** The paper addresses the challenge of optimizing reinforcement learning with verifiable rewards (RLVR) by focusing on the often-overlooked optimization layer that translates reward feedback into model updates. The authors propose Isospectral Optimization (ISO), a framework that leverages the existing spectral structure of model weights while allowing for new behaviors through changes in input and output frames. Key results demonstrate that ISO significantly improves model performance with fewer training steps, outperforming traditional optimization methods in terms of accuracy across various tasks.

### 10. Associative Emotional Learning in Convolutional Neural Networks
**Authors:** Seowung Leem, Andreas Keil, Mingzhou Ding, Ruogu Fang
**Link:** https://arxiv.org/abs/2607.19327v1
**Summary:** This paper addresses the challenge of modeling associative emotional learning, which links stimuli to emotional outcomes, using deep neural networks. The authors developed a model that processes visual information and evaluates its emotional significance, successfully replicating key findings from human studies such as association formation and generalization. Their results demonstrate that these deep learning models can effectively mimic the neural and behavioral aspects of how emotions are learned from experiences.
