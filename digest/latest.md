---
## 2026-10-09

### 1. CSF: Contextual Safety Filtering for Motion Generators
**Authors:** Lizhi Yang, Yiling Hou, Yao Tang, Junheng Li, Daniel Weng, Blake Werner, Aaron D. Ames
**Link:** https://arxiv.org/abs/2610.12467v1
**Summary:** The paper addresses the issue of ensuring safe whole-body motion in text-conditioned motion generators, which may misinterpret actions depending on the scene context. The authors introduce a training-free contextual safety filtering (CSF) technique that utilizes reference trajectories to define safety values and enforce safe motions. Their approach significantly reduces dangerous events by up to 90% while maintaining a high rate of harmless motions, and it has been successfully demonstrated on a real robot.

### 2. On the estimation and validity of AI time horizons---a statistical look at the METR plot
**Authors:** Drew T. Nguyen, William Fithian
**Link:** https://arxiv.org/abs/2610.12466v1
**Summary:** This paper addresses the estimation of AI time horizons, specifically how long it takes for humans to complete tasks that AI can solve with a 50% probability. The authors employed spline fitting and item-response theory to refine the analysis beyond the assumption of a linear relationship between human completion times and task difficulty. They found that jumps in time horizons are not equally challenging, leading to improved time-horizon estimates and new diagnostic tools for validating these estimates.

### 3. A Balanced Data Diet: Addressing the Exploration Bottleneck in Mega-Scale RL for Robot Control
**Authors:** Octi Zhang, Mateo Guaman Castro, Patrick Yin, Ignacio Dagnino, Abhishek Gupta, Rosario Scalise, Byron Boots
**Link:** https://arxiv.org/abs/2610.12465v1
**Summary:** The paper addresses the challenge of inefficient exploration in large-scale reinforcement learning (RL) for robot control, particularly for complex tasks like locomotion and manipulation. The authors propose an adaptive sampling method called Success Guided Sampling (SGS) that focuses training on task configurations near the limits of the robot's capabilities, enhancing the learning efficiency in massively parallel simulations. This approach significantly improves performance, allowing robots to successfully tackle difficult tasks and even transfer learned skills to real-world scenarios without additional training.

### 4. From Reactive Containment to Proactive Assurance: Lessons from OpenAI, Anthropic, and Google Agent Security Incidents
**Authors:** Abbas Raftari
**Link:** https://arxiv.org/abs/2610.12463v1
**Summary:** The paper addresses the problem of security breaches in AI agents from organizations like OpenAI, Anthropic, and Google, which occurred when agents inadvertently accessed real systems beyond their testing environments. The authors propose a new framework called the Proactive Agent Security Assurance Cycle (PASAC) and a Boundary Assurance Stack to ensure continuous security throughout the execution of these agents. The key contribution is a shift towards proactive security measures, emphasizing the importance of validating boundaries in real-time rather than relying on static safeguards.

### 5. BrickBench: Evaluating Agentic Brick Design
**Authors:** Peter Kulits, Yiqing Xu, R. Kenny Jones, Cordelia Schmid, Jiajun Wu
**Link:** https://arxiv.org/abs/2610.12452v1
**Summary:** The paper introduces BrickBench, a benchmark designed to evaluate the ability of agents to create LEGO-set designs based on text prompts, ensuring that these designs are both visually appealing and physically buildable. The approach involves agents selecting from a library of parts and reasoning about various constraints to produce their designs. Key findings indicate that while these agents meet many physical and semantic standards, they do not yet match the creativity and quality of human-designed sets.

### 6. One Block, Multiple Depths: Recurrent Vision Transformers with Depth-Programmed Experts
**Authors:** Adrian Bulat, Yassine Ouali, Georgios Tzimiropoulos
**Link:** https://arxiv.org/abs/2610.12448v1
**Summary:** This paper addresses the challenge of achieving high accuracy in vision tasks while minimizing the complexity and storage requirements of deep learning models. The authors introduce a recurrent Vision Transformer architecture (reViT) that uses a single Transformer block and dynamically varies the feature transformations through a set of shared experts, significantly reducing the number of parameters needed. Notably, the reViT model achieves accuracy comparable to deeper encoders while operating efficiently, demonstrating effective performance in various tasks with fewer stored parameters and the ability to adapt to different depths.

### 7. Bi-FORK: Generative Modeling of High-Dimensional Bifurcating Systems
**Authors:** Anna Zimmel, Fleur Hendriks, Markus Holzleitner, Florian Sestak, Martin Weichselbaumer, Vlado Menkovski, Johannes Brandstetter
**Link:** https://arxiv.org/abs/2610.12449v1
**Summary:** The paper addresses the challenge of modeling bifurcations in physical systems, where a single input can lead to multiple valid outputs, which traditional deep learning methods struggle to capture. The authors present Bi-FORK, a generative framework that effectively learns these one-to-many mappings by maintaining coherence in space and time and employing a novel sampling technique to identify distinct solution branches. Bi-FORK demonstrates significant scalability and can recreate complex multimodal solutions across various high-dimensional systems, far surpassing previous methods.

### 8. Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception
**Authors:** Oskar J. Hollinsworth, Alex F. Spies, Tigist Diriba, Adam Gleave, Chris Cundy
**Link:** https://arxiv.org/abs/2610.12445v1
**Summary:** The paper addresses the issue of detecting deception in large language model (LLM) agents, which can mislead users. The authors developed a robust method using probes trained on the largest deception dataset to date, achieving impressive detection accuracy (98.8% AUC) and demonstrating even higher effectiveness in complex cases of deception. They also released their dataset, FIBS, to encourage further research in this area.

### 9. Rounding in Preconditioner Space: Redesigning 4-bit AdamW Optimizer-State Quantization
**Authors:** Hanyang Li, Shao Tang, Daniel Thomas Braithwaite, Gregory Dexter, Leonardo Neves, Aman Gupta, Hiroto Udagawa, Abhishek Shivanna, Daniel Silva, Rohan Ramanath
**Link:** https://arxiv.org/abs/2610.12444v1
**Summary:** The paper addresses the issue of quantization errors in the AdamW optimizer that occur when reducing storage needs with 4-bit representations, which can negatively affect model performance. The authors propose two innovative methods—Zero-Inclusive Preconditioner-space Stochastic Rounding (ZIP-SR) and Zero-Excluding EDEN calibration (ZE-EDEN)—to optimize the quantization process while preserving key statistical characteristics. Their experiments show that both approaches significantly reduce validation loss compared to existing 4-bit implementations, achieving up to 70% reduction in performance gaps relative to 32-bit AdamW optimization in pretraining tasks across a range of model sizes.

### 10. Density Ratio Estimation with Stein Displacement Fields
**Authors:** Song Liu
**Link:** https://arxiv.org/abs/2610.12437v1
**Summary:** The paper addresses the challenge of estimating the density ratio between two probability distributions, which is important for understanding how one distribution shifts to another. It introduces a novel method that combines density ratios and displacement fields to model this shift within a single optimization framework. The key contribution is the development of two inference algorithms that either adjust a pretrained model or refine data closer to the original distribution, demonstrating the method's practical applications in simulation-based inference and nonlinear component analysis.
