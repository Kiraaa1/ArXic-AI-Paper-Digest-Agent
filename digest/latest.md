---
## 2026-10-04

### 1. Effective Resistance and Graph Neural Network Reliability in Tissue-Specific Interactomes
**Authors:** Jianru Shen
**Link:** https://arxiv.org/abs/2610.02175v1
**Summary:** The paper addresses the challenge of improving protein function annotation by identifying which predictions from models should be distrusted, particularly in tissue-specific interactomes. The authors propose using effective resistance, a concept from graph theory, to analyze the interaction structure of proteins and find that it is heavily influenced by inverse degree. Their key finding is that this residual information can explain additional prediction errors in most networks, thereby offering insights into enhancing model reliability at deeper layers while demonstrating that the influence of degree degeneration limits the potential improvements.

### 2. Every Ablation Is a Dose: Counterweights and the Semblance of Self-Repair
**Authors:** Areeb Ahmad, Pratinav Seth, Vinay Kumar Sankarapu
**Link:** https://arxiv.org/abs/2610.02173v1
**Summary:** The paper investigates the phenomenon of self-repair in language models, where removing a component seems to trigger adjustments in other components. The authors propose that this self-repair is driven by pre-existing gains in the model that can be quantitatively described using a simple mathematical framework. They demonstrate that many model components act as counterweights that adjust signal responses consistently, revealing that self-repair is a structured and predictable process rather than a disorganized one.

### 3. Watch, Infer, Coordinate: Inferring Robot Partner Constraints for Zero-Shot Coordination
**Authors:** Suyu Ye, Zheyuan Zhang, Vaishnav Tadiparthi, Hossein Nourkhiz Mahjoub, Ehsan Moradi Pari, Tianmin Shu, Homanga Bharadhwaj, Nakul Agarwal
**Link:** https://arxiv.org/abs/2610.02170v1
**Summary:** The paper addresses the challenge of having robots coordinate their actions when one partner has unknown physical limitations, which can hinder their ability to work together effectively. The authors propose a method called Watch, Infer, Coordinate, which allows one robot to infer its partner's constraints by observing its behavior while it collaborates with another robot. The results show that this approach significantly improves the accuracy of constraint inference and enhances coordination in new tasks, closely matching performance levels of an ideal system with full knowledge of the partner's capabilities.

### 4. AutoCompact: Learning When to Compact Context in Long-Horizon Coding Agents
**Authors:** Xuan Zhang, Longtao Zheng, Cunxiao Du, Bo An, Xin Dong
**Link:** https://arxiv.org/abs/2610.02163v1
**Summary:** The paper introduces AutoCompact, a method for training coding agents to effectively manage their contextual information during long software engineering tasks, ensuring they know when to compact and what to preserve. By leveraging supervised fine-tuning and reinforcement learning, AutoCompact enhances the agent's decision-making for context compaction, leading to improved task success rates. Experimental results demonstrate a significant increase in performance, with pass rates increasing by up to 9.2% over baseline models.

### 5. DuoMind: Enabling Distributed Multi-Robot Coordination with Semantic Communication
**Authors:** Hanchu Zhou, Dechen Gao, Hang Wang, Brendan Lynch, Boqi Zhao, Qiyao Ma, Raman Goyal, Junshan Zhang
**Link:** https://arxiv.org/abs/2610.02161v1
**Summary:** The paper presents DuoMind, a framework designed to enhance coordination among multiple robots using semantic communication, addressing the challenge of collaborative long-term task execution. It employs a combination of vision-language models for high-level reasoning and action models for low-level tasks, enabling robots to effectively communicate and synchronize their actions. The results demonstrate that DuoMind significantly improves multi-robot performance on complex manipulation tasks, supported by a new benchmark for evaluating such coordination.

### 6. When Do Intrinsic Rewards Lead to Exploration?
**Authors:** Scott W. Viteri, Laura Gomezjurado Gonzalez, Clark Barrett
**Link:** https://arxiv.org/abs/2610.02159v1
**Summary:** This paper addresses the issue that intrinsic rewards in reinforcement learning do not always lead to the most informative exploration experiences. The authors propose a formal criterion based on counterfactual information to compare exploration strategies and show through a constructed environment that certain existing intrinsic reward methods can be inefficient. They also introduce a new objective that better encourages optimal exploration by rewarding improvements in information acquisition.

### 7. Muon meets Tamed Langevin: Momentum Preconditioning beyond Convex and gradient-Lipschitz Potentials
**Authors:** Nikolaos Makras, Sotirios Sabanis
**Link:** https://arxiv.org/abs/2610.02158v1
**Summary:** The paper addresses the challenge of sampling from Gibbs distributions where potential energies are not necessarily convex or have bounded gradients. The authors propose a new underdamped Langevin sampling method that incorporates momentum preconditioning with non-quadratic kinetic energies, ensuring the sampling dynamics remain invariant to the target distribution. A key result is the demonstration of exponential convergence to equilibrium and stability of the sampling algorithm, even in the absence of constraints on the potential energy's gradient.

### 8. From Knowledge Access to Source Learning: Developing Source-Specific Competence
**Authors:** Lucheng Fu, Kejing Xia, Yiyang Wang, Yiqiao Jin, Jinjin He, Xiyuan Yang, Haoxin Liu, Ye Yu, Haibo Jin, Yijia Xiao, Wenke Lee, B. Aditya Prakash, Haohan Wang
**Link:** https://arxiv.org/abs/2610.02150v1
**Summary:** This paper addresses the challenge of enhancing large language model (LLM) agents' understanding of external information sources by developing a method called SourceLearn, which enables these models to learn and improve their knowledge of a specific source over time. SourceLearn combines self-directed learning, which identifies and revisits gaps in understanding, with task-guided learning that uses practical experiences to organize knowledge better. The approach significantly outperforms existing methods in improving performance on various benchmarks, with gains of up to 22.6 points compared to previous techniques.

### 9. Faynt: Scaling and Optimizing Policies for Competitive Melee
**Authors:** Ali Janati, Nikita Kuzmin, Rohit Swamy, Charles Niu
**Link:** https://arxiv.org/abs/2610.02144v1
**Summary:** The paper introduces Faynt, a family of Transformer models designed to play Super Smash Bros. Melee, effectively controlling all characters from a single checkpoint. Through advanced reinforcement learning techniques and architecture optimization, the 10M-parameter model achieves a remarkable 98.4% win rate against various specialized opponents and demonstrates superior gameplay efficiency. The authors provide open access to the model weights and tools for automated matchmaking, promoting continued research and development in competitive AI.

### 10. Keyword Harnesses Fail Open: A Cheap Diagnostic Ladder for Tool-Use Claims in Small Language Models
**Authors:** Juan S. Santillana
**Link:** https://arxiv.org/abs/2610.02142v1
**Summary:** The paper addresses the issue of keyword-matching benchmarks falsely crediting small language models for tool use that they do not genuinely perform. The authors propose a cost-effective diagnostic process to evaluate tool-use capabilities by identifying failures and implementing a targeted supervised fine-tuning (SFT) approach. Their key result shows that this method significantly improves the tool-use performance of the tested models, achieving a notable increase in valid tool emission rates while maintaining the integrity of the original model structure.
