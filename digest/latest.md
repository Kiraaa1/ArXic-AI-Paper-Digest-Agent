---
## 2026-06-29

### 1. DexCompose: Reusing Dexterous Policies for Multi-Task Manipulation with a Single Hand
**Authors:** Dihong Huang, Zhenyu Wei, Zhuxiu Xu, Yunchao Yao, Sikai Li, Mingyu Ding
**Link:** https://arxiv.org/abs/2606.28323v1
**Summary:** The paper addresses the challenge of combining existing dexterous manipulation skills to perform multiple tasks with a single hand without interference between the tasks. The authors introduce DexCompose, a framework that uses role-aware action ownership and trains residual modules to maintain task performance while adapting for new tasks. Their method achieved an average success rate of 77.4% across various complex manipulation tasks, indicating a significant improvement over previous approaches.

### 2. Surprises in Proper Positive-Only Learning
**Authors:** Shai Ben-David, Farnam Mansouri, Anay Mehrotra, Manolis Zampetakis
**Link:** https://arxiv.org/abs/2606.28309v1
**Summary:** The paper addresses the challenge of properly learning binary classifiers using only positive samples, a scenario known as positive-only learning, which has been difficult to characterize. The authors provide a clear criterion for proper learnability based on the finite VC dimension and a new condition called uniform exterior separability. Their findings highlight the complexities of this learning framework, distinguishing it significantly from standard PAC learning and introducing new combinatorial dimensions relevant to the field.

### 3. Which Nash Equilibrium? Solver-Dependent Selection on Zero-Sum Nash Polytopes
**Authors:** Luis Leal
**Link:** https://arxiv.org/abs/2606.28308v1
**Summary:** This paper investigates how different algorithms for solving two-player zero-sum games select specific Nash equilibria from a set, rather than converging to a unique outcome. Through analysis of six games, including Kuhn poker, the authors demonstrate that selection depends on the algorithm used: for instance, regularized methods favor the maximum-entropy equilibrium while regret-averaging methods tend to end up at lower-entropy outcomes. The study reveals significant implications for the performance against non-optimal opponents, highlighting the importance of their findings for algorithmic game theory.

### 4. Second-Order KKT Guarantees for Bregman ADMM in Nonconvex and Non-Lipschitz Optimization
**Authors:** Shuang Li, Zhihui Zhu, Qiuwei Li
**Link:** https://arxiv.org/abs/2606.28307v1
**Summary:** The paper addresses nonconvex optimization problems with linearly constrained variables, specifically in cases where traditional Lipschitz conditions are insufficient. The authors analyze a modified Alternating Direction Method of Multipliers (ADMM) using Bregman divergence, showing that the algorithm effectively converges to second-order stationary points despite the challenges posed by strict saddles. Their results, supported by numerical experiments, extend the application of Bregman methods to distributed optimization scenarios like matrix and tensor factorization.

### 5. VGB for Masked Diffusion Model: Efficient Test-time Scaling for Reward Satisfaction and Sample Editing
**Authors:** Kijung Jeon, Thuy-Duong Vuong, Molei Tao
**Link:** https://arxiv.org/abs/2606.28301v1
**Summary:** The paper addresses the challenge of enhancing generative models, specifically Masked Diffusion Models, to better satisfy structural constraints and optimize rewards during inference. The authors introduce MDM-VGB, a novel discrete diffusion sampler that employs reward-guided remasking within a flexible masked-state graph, allowing for more effective generation and repair of samples. They demonstrate that MDM-VGB achieves efficient performance with quadratic complexity, outperforming traditional methods, particularly in tasks like Sudoku and molecular property prediction.

### 6. Democratic ICAI: Debating Our Way to Steering Principles from Preferences
**Authors:** Kevin Kingslin, Anish Natekar, Ashutosh Ranjan, Vivek Srivastava, Savita Bhat, Shirish Karande
**Link:** https://arxiv.org/abs/2606.28294v1
**Summary:** The paper addresses the challenge of accurately capturing the complex reasoning behind human preferences in decision-making. It introduces Democratic ICAI, a method that utilizes structured debates among competing rationales to better understand and express the factors influencing preferences. The results show that this approach leads to more accurate preference predictions and generates preferred guiding principles compared to existing methods.

### 7. Bridging Ab Initio Symmetries and Global Nuclear Masses with Interpretable Neural Networks
**Authors:** Phong Dang, Evander Espinoza, Xiaoliang Wan, Michela Negro, Jerry P. Draayer, Feng Pan, Tomas Dytrych, Daniel Langr, David Kekejian
**Link:** https://arxiv.org/abs/2606.28287v1
**Summary:** The paper investigates whether established symmetries in nuclear physics, specifically Wigner's SU(4) and Elliott's SU(3), can explain nuclear binding across all nuclei, rather than just in selected cases. The researchers developed three neural network models based on these symmetries to predict nuclear masses, finding that their best-performing model, WINN, significantly reduces prediction errors and highlights important features of nuclear binding, such as the restoration of symmetries near the neutron dripline. This work suggests that these symmetries are fundamental principles governing the entire chart of nuclear masses.

### 8. PAC-Bayesian Certificates for Quadratic Closed-Loop Control
**Authors:** Domagoj Herceg
**Link:** https://arxiv.org/abs/2606.28281v1
**Summary:** The paper addresses the challenge of applying PAC-Bayesian bounds to learning-based closed-loop control systems, where the performance metric is a complex quadratic cost. The authors use System Level Synthesis parameterization to derive PAC-Bayes-Chernoff certificates for these systems, allowing them to provide data-driven guarantees on control responses without relying on strict assumptions. A key contribution is the development of a learning algorithm that reduces sensitivity in closed-loop control while improving performance, validated through experiments on a double integrator system.

### 9. Agentic Hardware Design as Repository-Level Code Evolution
**Authors:** Cunxi Yu, Chenhui Deng, Nathaniel Pinckney, Brucek Khailany
**Link:** https://arxiv.org/abs/2606.28279v1
**Summary:** The paper presents HORIZON, a self-evolving framework that automates hardware design by treating it as a form of code evolution, utilizing a sophisticated agent loop that manages repository operations. By evaluating this approach on various benchmarks, the authors achieved 100% completion across all tests, demonstrating its effectiveness in hardware design tasks. However, they note that this achievement is just a step towards solving the larger and more complex challenges in chip design.

### 10. Towards Automating Scientific Review with Google's Paper Assistant Tool
**Authors:** Rajesh Jayaram, Drew Tyler, David Woodruff, Corinna Cortes, Yossi Matias, Vahab Mirrokni, Vincent Cohen-Addad
**Link:** https://arxiv.org/abs/2606.28277v1
**Summary:** The paper addresses the challenge of traditional peer review keeping pace with the rapid production of AI-assisted scientific research. It introduces the Paper Assistant Tool (PAT), an AI framework that analyzes full scientific manuscripts, identifying errors and suggesting improvements. PAT significantly enhances error detection, improving performance by 34% on mathematical issues and demonstrating effectiveness in pilot implementations as a pre-submission tool for major conferences, ultimately reducing the workload for human reviewers.
