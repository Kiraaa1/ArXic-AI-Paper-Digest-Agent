---
## 2026-07-01

### 1. Introspective Coupling: Self-Explanation Training Tracks Behavioral Change Despite Fixed Supervision
**Authors:** Zifan Carl Guo, Laura Ruis, Jacob Andreas, Belinda Z. Li
**Link:** https://arxiv.org/abs/2606.32038v1
**Summary:** The paper investigates how training language models to explain their predictions can lead to accurate introspection rather than mere imitation. The authors found that using fixed counterfactual explanations—derived from previous versions of the models or similar models—allows the language models to generate explanations that better reflect their current behavior over time, even as their behavior changes. This approach demonstrates that static datasets can effectively enhance models’ self-awareness and adaptability without needing constant updates.

### 2. QVal: Cheaply Evaluating Dense Supervision Signals for Long-Horizon LLM Agents
**Authors:** Sergio Hernández-Gutiérrez, Matteo Merler, Ilze Amanda Auzina, Joschka Strüber, Ameya Prabhu, Matthias Bethge
**Link:** https://arxiv.org/abs/2606.32034v1
**Summary:** The paper addresses the challenge of evaluating dense supervision methods for long-horizon LLM agents, which often lack effective feedback on intermediate actions. The authors introduce QVal, a training-free testbed that assesses how well these supervision signals align with strong reference policy Q-values, allowing for direct comparison of various methods without confounding factors from training processes. Their findings reveal that basic prompting techniques frequently outperform advanced dense supervision approaches, indicating that performance tends to cluster by methodological family across different environments.

### 3. Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs
**Authors:** Gabrielle Kaili-May Liu, Avi Caciularu, Gal Yona, Idan Szpektor, Arman Cohan
**Link:** https://arxiv.org/abs/2606.32032v1
**Summary:** The paper addresses the issue of large language models (LLMs) misrepresenting their uncertainty, which undermines their trustworthiness. The authors propose a new framework called reinforcement learning with metacognitive feedback (RLMF) that helps models better judge their own performance and select valuable training examples. Their experiments demonstrate that RLMF significantly improves the accuracy and reliability of LLMs' uncertainty expression, outperforming traditional reinforcement learning methods.

### 4. When LLMs Read Tables Carelessly: Measuring and Reducing Data Referencing Errors
**Authors:** Yuqing Yang, Qi Zhu, Zhen Han, Boran Han, Zhengyuan Shen, Shuai Wang, Vassilis N. Ioannidis, Huzefa Rangwala
**Link:** https://arxiv.org/abs/2606.32029v1
**Summary:** The paper addresses the problem of data referencing errors (DREs) in large language models (LLMs) when interpreting tables, where models incorrectly reference or omit data values. The authors conducted a systematic evaluation of DREs across various models and tasks and found that these errors persist in all tested LLMs. They introduced a lightweight critic model that enhances answer accuracy by up to 12% through improved data referencing, achieving a notable F1 score of 78.2% in detecting DREs.

### 5. Freeform Preference Learning for Robotic Manipulation
**Authors:** Marcel Torne, Anubha Mahajan, Abhijnya Bhat, Chelsea Finn
**Link:** https://arxiv.org/abs/2606.32027v1
**Summary:** The paper addresses the challenge of designing effective reward signals for robotic manipulation tasks, which often struggle with limited feedback from humans. The authors introduce Freeform Preference Learning (FPL), a method that allows users to specify preferences in natural language along various axes such as speed or safety, and then uses these preferences to train a more nuanced reward model for robots. FPL significantly enhances performance in real-world and simulated tasks, improving outcomes by 38 percentage points compared to traditional methods and enabling flexible behavior adjustments without the need for retraining.

### 6. AdaJEPA: An Adaptive Latent World Model
**Authors:** Ying Wang, Oumayma Bounou, Yann LeCun, Mengye Ren
**Link:** https://arxiv.org/abs/2606.32026v1
**Summary:** AdaJEPA addresses the issue of inaccurate future state predictions in latent world models, which can lead to planning failures, particularly during distribution shifts at test time. The proposed approach involves adaptive updates to the model during planning through model predictive control (MPC), using self-supervised feedback from observed state transitions. The key contribution is that AdaJEPA significantly enhances planning success in goal-reaching tasks with minimal additional computational effort, requiring only one gradient update per replanning step.

### 7. Generative Skill Composition for LLM Agents
**Authors:** Xinyu Zhao, Zhen Tan, Vaishnav Tadiparthi, Nakul Agarwal, Kwonjoon Lee, Ehsan Moradi Pari, Hossein Nourkhiz Mahjoub, Tianlong Chen
**Link:** https://arxiv.org/abs/2606.32025v1
**Summary:** The paper addresses the challenge of efficiently selecting and executing a combination of specialized skills for complex tasks within large language model (LLM) agents. It introduces SkillComposer, a system that predicts a structured skill plan by jointly determining which skills to use, how many, and in what order through a single decoding process. The results show that SkillComposer significantly improves task success rates in coding scenarios, outperforming existing skill retrieval methods and achieving results close to an ideal skill selection approach.

### 8. FLORA: A deep learning approach to predict forest attributes from heterogeneous LiDAR data
**Authors:** Emilie Vautier, Clément Mallet, Cédric Vega
**Link:** https://arxiv.org/abs/2606.32023v1
**Summary:** The paper presents FLORA, a deep learning framework designed to predict important forest attributes from varying LiDAR data that is often affected by different conditions such as season and sensor type. By integrating an octree-based structure with additional ecological and temporal data, FLORA successfully forecasts six key forest metrics across France, demonstrating improved accuracy over traditional models with an rRMSE of about 12.3% for dominant height. This approach provides a robust and scalable method for national forest monitoring, addressing challenges faced with heterogeneous LiDAR data.

### 9. SemRF: A Semantic Reference Frame for Residual-Stream Dynamics in Language Models
**Authors:** Jian Gu, Aldeida Aleti, Chunyang Chen, Hongyu Zhang
**Link:** https://arxiv.org/abs/2606.32022v1
**Summary:** The paper addresses the challenge of analyzing how language models process information at various depths, ensuring that measurements of semantic states are reliable and consistent across different layers. The authors introduce Semantic Reference Frames (SemRF), which create fixed anchors for more accurate semantic measurement, allowing for clearer interpretation of language model dynamics. Key contributions include establishing a framework for stable semantic coordinates and providing insights into the efficiency of language model parameters based on the complexity of semantic trajectories.

### 10. Automated Background Swapping for Robustness against Spurious Backgrounds
**Authors:** Cesar Roder, Kajetan Schweighofer
**Link:** https://arxiv.org/abs/2606.32018v1
**Summary:** The paper addresses the problem of deep learning classifiers failing due to reliance on spurious background correlations in images, which do not generalize well. The proposed solution, Automated Background Swapping (AutoBackSwap), involves using a secondary network to separate foregrounds from backgrounds, synthesizing new backgrounds, and augmenting training data. The key result shows that AutoBackSwap effectively improves classifier robustness against spurious backgrounds, even when no contrasting samples exist in the training set, outperforming previous methods.
