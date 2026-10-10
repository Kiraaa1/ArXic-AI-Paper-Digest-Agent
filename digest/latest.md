---
## 2026-10-10

### 1. Ecology of AI Agents: Collaboration Creates a Population Threshold for Takeoff
**Authors:** Erin Crawley, Hidenori Tanaka
**Link:** https://arxiv.org/abs/2610.12436v1
**Summary:** This paper addresses the risk of uncontrolled population growth of misaligned AI agents capable of conducting cyberattacks. The authors develop an ecological theory modeling the dynamics of AI-agent populations, revealing that collaboration among agents can lower the critical population threshold needed for a population explosion, even if individual agent capabilities remain unchanged. They propose that to ensure safety, larger populations should be deployed gradually in controlled settings while assessing how their collective capabilities scale.

### 2. VioLA: Learning Generalist Humanoid Control Policies from Human Data
**Authors:** Mert Albaba, Jens Beißwenger, Anna Manasyan, Daniel Marta, Michael J. Black, Wieland Brendel, Andreas Krause, Georg Martius, Martin Riedmiller
**Link:** https://arxiv.org/abs/2610.12435v1
**Summary:** The paper presents VioLA, a generalist control policy for humanoid robots that enables them to follow instructions using body and hand motion predictions instead of complex joint commands. By mapping human motion to a common latent space, VioLA leverages a large dataset of human demonstrations, allowing the robot to perform locomotion and manipulation tasks successfully without the need for fine-tuning on specific tasks. The key result shows that VioLA achieves a 100% success rate in locomotion and 88.6% in manipulation tasks on a real robot, outperforming existing methods significantly.

### 3. FAITH: Feasibility-Aware Safety-Filtered RL for High-Dimensional Systems
**Authors:** Songyuan Zhang, Baljeet Singh, Sarthak Ranjeet Kaingade, Chuchu Fan, Bryan Trinh
**Link:** https://arxiv.org/abs/2610.12432v1
**Summary:** The paper presents FAITH, a new approach to safe reinforcement learning that separates safety from performance in a way that avoids conflicts during training. By using a model-free method to predict safety values, FAITH allows for effective policy updates without competing safety objectives and is capable of managing unsafe actions when necessary. In experiments, FAITH demonstrated superior performance in both task returns and safety rates on high-dimensional systems, including humanoid robots, outperforming existing methods.

### 4. Toward Joint Optimization of Circuit Depth and Training Data Size in Adaptively Grown Quantum Classifiers
**Authors:** Saeefa Rubaiyet Nowmi, Md Mahmuduzzaman Kamol, Mohammad Saidur Rahman
**Link:** https://arxiv.org/abs/2610.12428v1
**Summary:** The paper investigates the relationship between circuit depth and training data size in quantum classifiers, aiming to optimize both for better model performance. Using the Q-FLAIR growth mechanism, the authors reimplemented its approach to analyze how circuit size changes with increasing training data on the MNIST dataset. They found no predictable relationship between the circuit depth and the amount of training data, highlighting that while the generalization guarantees hold, they do not effectively predict performance variations, suggesting a need for further exploration in this area.

### 5. FastBench: Can Streaming VLMs Perceive High-Dynamic Real-World Streams?
**Authors:** Yuxuan Hu, Weikang Shi, Yang Bo, Xudong Lu, Xintong Guo, Shuhan Li, Yuyang He, Huankang Guan, Peiwen Sun, Yunqiao Yang, Wenbo Li, Rui Liu, Hongsheng Li
**Link:** https://arxiv.org/abs/2610.12427v1
**Summary:** The paper introduces FastBench, a new benchmark designed to evaluate the ability of Streaming Video Large Language Models (VLMs) to understand high-dynamic real-world video streams, which current benchmarks inadequately address. The approach includes creating question-answer pairs from high-FPS video clips and using a pipeline for filtering and verifying answers, while also providing a baseline method called ProactiveFrame that optimizes frame rate processing. Key findings reveal that even the best-performing models struggle with high-dynamic scenarios, scoring below expectations, highlighting the limitations of current VLMs in perceiving fast events in live video.

### 6. RoboRSI: Stable, efficient, and reusable robot self-evolution in complex real-world environments
**Authors:** Zimo Wen, Yijin Chen, Yuxuan Cao, Wendi Chen, Yanwen Zou, Wenye Yu, Fuhang Kuang, Han Xue, Jun Lv, Chuan Wen, Cewu Lu
**Link:** https://arxiv.org/abs/2610.12424v1
**Summary:** RoboRSI addresses the challenge of enabling robots to self-improve by efficiently organizing and reusing the skills they acquire through experience in complex environments. The system employs a structured approach called Top-Down Skill Refinement, which breaks tasks into manageable skills and manages the learning process using a coordinated team of components. The key result shows that RoboRSI significantly enhances a mobile manipulator's success rate in multi-object household cleanup tasks during extensive trials, outperforming existing methods by up to 11 percentage points.

### 7. Beyond Spatio-Temporal Priors: A Generalizable Approach for Dense Correspondence Matching
**Authors:** Luping Liu, Bingyi Kang, Yifan Wang, Dong Xu
**Link:** https://arxiv.org/abs/2610.12421v1
**Summary:** The paper addresses the limitations of traditional dense correspondence matching methods, which rely on strict assumptions about smooth motion and rigid geometry, and are inadequate for image editing and reference-guided generation tasks. The authors propose a novel framework called FreeMatching that leverages generative and semantic representations along with diverse supervision to enhance correspondence matching across complex image transformations. Key findings indicate that FreeMatching significantly improves correspondence quality in challenging scenarios while also serving as a reliable metric for assessing identity preservation that aligns with human evaluations.

### 8. A Unified Bellman Operator for Safety-Critical Reinforcement Learning
**Authors:** Nishanth Arun Rao, Royina Karegoudra Jayanth, Benjamin Eysenbach, Jaime Fernández Fisac
**Link:** https://arxiv.org/abs/2610.12420v1
**Summary:** This paper addresses the challenge of reinforcement learning in safety-critical environments, where it's essential to balance maximizing performance with adhering to safety constraints. The authors introduce a unified Bellman operator that combines both objectives into a single framework, allowing the learning process to converge to an optimal policy that maximizes task performance without compromising safety. Their approach demonstrates stable convergence and effectively maintains safety during testing, showing near-zero safety violations.

### 9. WOVEN: Weaving Visual World Modeling into Multimodal LLMs
**Authors:** Zheyu Fan, Yue Zhang, Mingkai Deng, Kangrui Wang, Qineng Wang, Canyu Chen, Jie Hao, Xing Fan, Chenlei Guo, Eric P. Xing, Mohit Bansal, Manling Li
**Link:** https://arxiv.org/abs/2610.12417v1
**Summary:** The paper addresses the shortcomings of multimodal large language models (MLLMs) in spatial and physical reasoning by introducing WOVEN, a training source and benchmark for visual transition reasoning. By leveraging a diverse set of visual examples organized by scene, action, and reasoning type, the authors found that training on just a small subset of this data significantly enhances MLLM performance across various tasks. The key contribution is establishing visual transition reasoning as a foundational element for improving the training of MLLMs, leading to substantial performance gains on external benchmarks.

### 10. MAMHOI: Factorizing Scene-Aware Human-Object Interaction through Affordances
**Authors:** Mingyuan Lei, Yoonchang Sung, Tat-Jen Cham
**Link:** https://arxiv.org/abs/2610.12416v1
**Summary:** The paper presents MAMHOI, a new method for generating realistic human-object interactions in complex 3D scenes by addressing the challenges of understanding how interactions can occur in different environments and accurately representing the motion involved. MAMHOI uses a two-step process where it first assesses feasible interaction locations and methods based on the scene, and then generates the corresponding motion for the human-object interaction, all without needing extensive paired data. The results show that MAMHOI produces more realistic interactions while reducing inappropriate object penetration into scenes, enhancing the overall quality and feasibility of the generated interactions.
