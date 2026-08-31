---
## 2026-08-31

### 1. QGPINNs: A Physics-Informed Neural Network Framework for Nonlocal Differential Equations on Quantum Graphs
**Authors:** Vaibhav Mehandiratta, Saket Ramchandra
**Link:** https://arxiv.org/abs/2608.28589v1
**Summary:** The paper presents QGPINNs, a framework utilizing physics-informed neural networks to solve nonlocal differential equations on quantum graphs, enhancing the computational approach by integrating specific boundary and vertex conditions. The framework effectively combines local neural network approximations across graph edges into a cohesive global solution while applying advanced learning strategies for improved accuracy and stability. It has been validated against benchmark structures and real-world networks, demonstrating its effectiveness in solving complex equations and identifying parameters from noisy data.

### 2. Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning
**Authors:** Nan Wang, Mohit Yadav, Jonathan Wulff, Aidan Rosenbaum, Kezhou Chen, Yuvan Sharma, Xu Dong, Yiwei Tao
**Link:** https://arxiv.org/abs/2608.28578v1
**Summary:** The paper addresses the challenge of simulating and controlling tendon-driven robotic hands, which are often more affordable but difficult to learn and operate compared to traditional direct-drive hands. The authors introduce Aero Hand Open, a simulation-ready anthropomorphic hand, providing a detailed simulation model, an actuation mapping for motor commands, and a reinforcement learning training package. This allows effective training and deployment of manipulation policies in simulation without the need for additional fine-tuning on the actual hand.

### 3. Learning a Size-Weight Frontier for Synthetic-Augmented Inference
**Authors:** Chengpiao Huang, Kaizheng Wang
**Link:** https://arxiv.org/abs/2608.28576v1
**Summary:** This paper addresses the challenge of using synthetic data to improve statistical inference when real data is limited, as improperly integrating synthetic samples can introduce bias. The authors propose a framework that defines a size-weight frontier to optimally select the size and weight of synthetic samples to maintain accurate inference across related tasks. Their approach, tested with responses from large language models augmenting opinion survey data, successfully achieves target coverage while significantly reducing confidence intervals.

### 4. On two proofs of $d^2$ mixing of weighted Dikin walks
**Authors:** Yuansi Chen, Yunbum Kook
**Link:** https://arxiv.org/abs/2608.28566v1
**Summary:** The paper addresses the mixing time of weighted Dikin walks, which are used for sampling from exponential distributions within polytopes and truncated positive-semidefinite cones. The authors develop a new method to analyze mixing by focusing on acceptance probabilities in high-probability regions, leading to improved mixing bounds of $\widetilde O(d^2)$ for both polytopes and a specific metric. Additionally, they establish stronger guarantees using a novel bootstrap condition, further enhancing the mixing bound for a particular metric to $\widetilde O(d^2)$ from a previous $\widetilde O(d^{9/4})$.

### 5. Learning between the peaks: sharp asymptotics for kernel ridge regression under power-law anisotropy
**Authors:** Lorenzo Rizzi, Arie Wortsman Zurich, Bruno Loureiro
**Link:** https://arxiv.org/abs/2608.28564v1
**Summary:** This paper investigates kernel ridge regression in the context of anisotropic Gaussian data, focusing on how the input covariance's power-law decay affects learning dynamics. The authors derive precise asymptotic expressions for the kernel spectrum and generalization error, revealing that weak anisotropy retains some isotropic characteristics, while strong anisotropy changes the effective dimension and alters bias behavior significantly. These findings enhance the understanding of how input geometry influences kernel methods and their generalization capabilities.

### 6. A Formal Limitation on Learning Human Language From Textual Corpora
**Authors:** Emily Cheng, Ryan Cotterell
**Link:** https://arxiv.org/abs/2608.28560v1
**Summary:** The paper addresses the challenge of whether a listener can accurately infer a speaker's intended meaning solely from the form of their utterance. The authors apply an information-theoretic framework to establish upper limits on this inference capability, revealing that certain aspects of meaning can only be clarified through extralinguistic context, not through the utterance itself. Their findings suggest that inherent limitations in language mean that no model can fully overcome these bounds, as demonstrated through experiments with various language tasks.

### 7. Blog: Survey of Optimizers
**Authors:** Ruoran Xu
**Link:** https://arxiv.org/abs/2608.28557v1
**Summary:** This survey paper explores advancements in neural network optimization techniques beyond traditional Adam variants, focusing on a diverse range of methods that account for matrices, training dynamics, and system representations. It categorizes optimizers along four axes, highlighting various approaches, including matrix-aware methods and memory-efficient optimizers, while emphasizing that no single method universally outperforms AdamW across different scenarios. The key takeaway is the need for a more nuanced, context-dependent evaluation of optimizers that considers multiple factors like model scale and training settings.

### 8. Logos: An Agent Harness on a Cross-Process Bus
**Authors:** Hanzhang Jia, Liheng Zeng, Hao Cheng, Yi Gao, Bo Ma
**Link:** https://arxiv.org/abs/2608.28553v1
**Summary:** This paper addresses the limitations of traditional agent systems that rely on single processes, where faults can disrupt all components simultaneously. The authors present Logos, a cross-process agent harness that treats each plugin as a separate process, minimizing the impact of failures. Their key contribution is demonstrating that this approach allows multiple sessions to resume seamlessly after failures, significantly improving resilience compared to conventional systems.

### 9. Advancing Interaction-Sensitive Feature Selection: Novel Relief-Based Algorithms, Expanded Comparisons, and Recommendations for Biomedical Data Mining
**Authors:** Kia Kazemi-Nia, Harsh Bandhey, Philip J. Freda, Ryan J. Urbanowicz
**Link:** https://arxiv.org/abs/2608.28552v1
**Summary:** This paper addresses the challenge of effective feature selection in high-dimensional biomedical data, where traditional methods often overlook interactions between features or incur high computational costs. The authors present optimized and new variants of Relief-based algorithms in the scikit-rebate Python package, demonstrating that these methods effectively detect feature interactions while achieving significant reductions in runtime. Key findings reveal that certain RBAs excel in identifying both main effects and interactions, making them valuable tools for improving model performance in genomic data analysis.

### 10. Video Generative Models as Geometry Learner
**Authors:** Haosen Yang, Jifei Song, Zhensong Zhang, Xiatian Zhu, Jiankang Deng
**Link:** https://arxiv.org/abs/2608.28549v1
**Summary:** The paper addresses the challenge of geometry estimation, specifically for depth and surface normal assessment, by utilizing pretrained video generative models instead of traditional image-based methods. The proposed method, GeoNeXt, reformulates the problem as predicting subsequent frames in a video, allowing for more efficient learning by leveraging structured knowledge from video data to model both images and their geometric properties. The results show that GeoNeXt significantly outperforms existing models while using far less training data, even competing with advanced methods trained on much larger datasets.
