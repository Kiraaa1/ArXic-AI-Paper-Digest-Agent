---
## 2026-08-18

### 1. Don't Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask Exploration and Transition-aware Memory
**Authors:** Bingxin Xu, Yuzhang Shang, Emilio Ferrara
**Link:** https://arxiv.org/abs/2608.16889v1
**Summary:** The paper addresses the challenges of managing long-horizon robot manipulation tasks, where errors can accumulate across multiple subtasks. The authors introduce BATON, an approach that explores each subtask individually and uses a transition-aware memory system to ensure smoother handoffs between them. This method significantly improves both overall task success and cumulative success rates on the RoboMemArena benchmark, outperforming the current state-of-the-art by over 11%.

### 2. Q-based Variational Inverse Reinforcement Learning
**Authors:** Ondrej Bajgar, Peter Tisnikar, Alessandro Abate, Konstantinos Gatsis, Maike Osborne
**Link:** https://arxiv.org/abs/2608.16888v1
**Summary:** The paper addresses the challenge of inferring human preferences for AI behavior, which is often impractical to specify directly. It introduces Q-based Variational Inverse Reinforcement Learning (QVIRL), a Bayesian method that estimates reward functions by learning a distribution over optimal Q-values from expert demonstrations. QVIRL is notable for its scalability, ability to quantify uncertainty, and successful performance across various tasks, including training with raw pixel data, marking a significant advancement in Bayesian inverse reinforcement learning.

### 3. Improving the matrix multiplication exponent with modern optimization and AlphaEvolve
**Authors:** Emilien Dupont, Marvin Eisenberger, Borislav Kozlovskii, Abbas Mehrabian, Francisco J. R. Ruiz, Abigail See, Renfei Zhou, Josh Alman, Virginia Vassilevska Williams, Matej Balog
**Link:** https://arxiv.org/abs/2608.16884v1
**Summary:** The paper addresses the problem of improving the matrix multiplication exponent, denoted as $ω$, which indicates the computational complexity of matrix multiplication. The authors reformulate the related optimization problem, apply novel machine learning techniques, and enhance the optimization process using AlphaEvolve. Their approach successfully lowers the upper bound of $ω$ to less than 2.371177, surpassing the previous best bound of 2.371339.

### 4. Spectral Gaps of Hit-and-Run and Coordinate Hit-and-Run
**Authors:** Yunbum Kook, Santosh S. Vempala
**Link:** https://arxiv.org/abs/2608.16878v1
**Summary:** This paper addresses the spectral gap and convergence rates of the Hit-and-Run and Coordinate Hit-and-Run Markov chains used for sampling from convex bodies. The authors connect the spectral gap to Poincaré constants and improve existing bounds on the mixing time, demonstrating a better convergence rate for nearly isotropic bodies compared to previous results. The key contribution is a refined analysis that reduces the dimension dependence from cubic to nearly quadratic, while employing duality and calculus techniques in the proof.

### 5. AutoSR: Automatic Symbolic Regression by Searching Research States
**Authors:** Kejia Zhang, Youran Sun, Xinyu Ren, Chugang Yi, Haizhao Yang
**Link:** https://arxiv.org/abs/2608.16876v1
**Summary:** The paper presents AutoSR, an automated system for symbolic regression that enhances traditional approaches by retaining the scientific context and reasoning behind candidate equations rather than just focusing on the equations themselves. It utilizes a method called progressive-widening Monte Carlo tree search to systematically explore scientific investigations, incorporating a comprehensive record of motivations and evidence. The key contribution is that AutoSR successfully recovers known algebraic relations from benchmark problems while also providing a structured justification for its findings, marking a shift towards integrating scientific reasoning into symbolic regression.

### 6. An Analytical-Prior Framework for Data-Efficient Prediction of Sound-Reduction Frequencies in Rectangular Side-Branch Helmholtz Resonators
**Authors:** Jiaming Li
**Link:** https://arxiv.org/abs/2608.16873v1
**Summary:** The paper addresses the challenge of accurately predicting sound-reduction frequencies in side-branch Helmholtz resonators when high-fidelity simulation data is limited and costly to generate. It introduces an analytical-prior learning framework that leverages a low-cost analytical model to enhance data efficiency, either by correcting simulation data discrepancies or by distilling the analytical model into a learned prior for calibration. The key findings demonstrate that this approach significantly improves prediction accuracy, with mean absolute errors reduced to as low as 0.371 Hz compared to traditional methods.

### 7. Data-Efficient and Interpretable Classification of Circulating Tumor Cell Phenotypes in Microfluidic Devices via Deep Learning
**Authors:** Serena Su, Yifan Wang, Senwei Liang
**Link:** https://arxiv.org/abs/2608.16870v1
**Summary:** The paper addresses the challenge of accurately classifying circulating tumor cell (CTC) phenotypes using trajectory data from microfluidic devices, which involves complex fluid interactions. The authors present a novel deep learning framework that utilizes a targeted data augmentation strategy called Subsequence to improve learning from localized trajectory segments, leading to enhanced classification accuracy. Key findings indicate that this approach not only boosts performance but also reveals that shorter segments of trajectory data contain critical biophysical information necessary for effective prediction.

### 8. Towards Computational Provenance: Carrying Causal-State Evidence in Generated Text
**Authors:** Benjamin Belay
**Link:** https://arxiv.org/abs/2608.16868v1
**Summary:** The paper addresses the challenge of verifying the internal computations of language models by examining whether generated text can provide evidence of the internal state that influenced its generation. The researchers implemented this idea in two types of neural network architectures, demonstrating that they could authenticate and trace specific internal states through subtle patterns in the output text, despite producing the same answer. The key finding is that, in controlled settings, detectable evidence of these internal states can indeed be encoded in the generated text, establishing a proof of concept for computational provenance in language models.

### 9. Non-Crossing Deep Quantile Regression for Distributional Survival Prediction
**Authors:** Shuai Huang, Zhe Qu, Zhaowei Hua, Guohao Shen, Rui Tang, Hongtu Zhu
**Link:** https://arxiv.org/abs/2608.16864v1
**Summary:** The paper addresses the challenge of accurately predicting survival distributions in situations where the effects of covariates vary over time, which traditional hazard and mean models oversimplify. It introduces a new framework called Censored Non-crossing Quantile (CNQ) that uses deep learning techniques to estimate multiple conditional survival quantiles while ensuring their proper ordering. The approach outperforms existing methods in simulations and real clinical applications by providing more accurate predictions and revealing nuanced covariate effects that might be missed with simpler models.

### 10. The canonical facets of multi-separator polytopes
**Authors:** Bjoern Andres, Silvia Di Gregorio, Jannik Irmai, Lucas Fabian Naumann, Shengxian Zhao
**Link:** https://arxiv.org/abs/2608.16861v1
**Summary:** The paper explores the graph multi-separator problem, which aims to improve image segmentation techniques. The authors develop an integer linear program (ILP) formulation and identify the polyhedral structure of the associated multi-separator polytope, revealing graph-theoretic conditions for its facets. A key contribution is the complete characterization of these facets and a demonstration of the relationships between the multi-separator polytope, the boolean quadric polytope, and the lifted multicut polytope.
