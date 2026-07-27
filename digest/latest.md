---
## 2026-07-27

### 1. SM4RT: Learning Structured Motion Geometry for 4D Reconstruction
**Authors:** Shing Ho J. Lin, Wenzhao Zheng, Dong Zhuo, Yuqi Wu, Jie Zhou, Jiwen Lu
**Link:** https://arxiv.org/abs/2607.22534v1
**Summary:** The paper presents SM4RT, a model designed to enhance 4D reconstruction by incorporating structured motion geometry, addressing the challenge of understanding dynamic scenes from monocular video. Instead of treating motion as isolated point-wise displacements, SM4RT recognizes that objects typically move collectively according to rigid-body dynamics, and it models this using a framework that captures scene dynamics through a compact set of motion bases. The approach enables accurate reconstruction of both 3D geometry and motion together, yielding strong performance in dynamic scene analysis.

### 2. Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills
**Authors:** Siyuan Huang, Pengyu Cheng, Haotian Liu, Tao Chen, Yihao Liu, Jingwei Ni, Shijie Zhou, Ziyi Yang, Gangwei Jiang, Mengyu Zhou, Yu Cheng, Xiaoxi Jiang, Guanjun Jiang
**Link:** https://arxiv.org/abs/2607.22529v1
**Summary:** The paper addresses the challenge of balancing task diversity and reliable feedback in training large language models (LLMs) by introducing a framework called Skill Self-Play (Skill-SP). This method employs a co-evolutionary process involving a task proposer, a solution solver, and a skill controller, which together facilitate an interactive training loop that expands the model's skill set while ensuring reliable execution. The key finding is that Skill-SP significantly enhances the performance of LLMs, even improving models that initially struggle, thereby pushing the boundaries of their capabilities.

### 3. Explainable Reinforcement Learning for assisting Air Traffic Controllers
**Authors:** Anduel Mehmeti, Gabriella Gigante, Salvatore Venticinque
**Link:** https://arxiv.org/abs/2607.22525v1
**Summary:** The paper addresses the challenge of building trust in AI systems used in critical environments like Air Traffic Control by enhancing the explainability of reinforcement learning algorithms. It employs a saliency map technique to reveal which input features most influence the AI agent's decisions regarding flight routing in a simplified ATC environment. This approach aims to facilitate better human-AI collaboration by making the AI's decision-making process more transparent.

### 4. The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents
**Authors:** Darshan Tank, Baran Nama
**Link:** https://arxiv.org/abs/2607.22520v1
**Summary:** The paper addresses the issue of how adding procedural skills to large language model (LLM) agents can sometimes lead to worse performance, despite average improvements in task success. The authors conducted a comprehensive analysis of nearly 6,000 agent runs across various benchmarks to differentiate between tasks that regress (fail after skills are added) and those that consistently fail. They found that regressions are significant and often arise from factors like skill context influence and improper grounding, suggesting that evaluating skills should focus on both enhancements and regressions to better understand their true impact on performance.

### 5. PinEqualizer: Full Funnel Content Exploration and Debiasing System at Pinterest
**Authors:** Olafur Gudmundsson, Bo Zhao, Huayi Liao, Anna Kiyantseva, Sai Xiao, Heath Vinicombe, Mostafa Keikha, Luke DeLuccia, Zihao Chen, Junpeng Hou, Weijie Jiang, Bhawna Juneja, Andreanne Lemay, Wei-Ting Lin, Keyvan Moghadam, Jiaxing Qu, Zhiqing Rao, Zhihua Zhang
**Link:** https://arxiv.org/abs/2607.22518v1
**Summary:** The paper addresses the cold-start problem in search and recommendation systems by introducing the PinEqualizer, a solution that improves content exploration and reduces bias towards established content. This system covers multiple stages of the user experience and allows for precise model predictions across various content types. Over two years of implementation at Pinterest, it has led to notable enhancements in user engagement and the health of the content ecosystem.

### 6. Quantum Spectral Model: Data Reuploading with Input-Conditioned Frequency Support
**Authors:** Peiyong Wang, Udaya Parampalli, Casey R. Myers
**Link:** https://arxiv.org/abs/2607.22516v1
**Summary:** The paper introduces Quantum Spectral Models (QSMs) to enhance quantum machine learning by directly constructing data-encoding unitaries from matrix-valued inputs, thereby leveraging spectral representations. By evaluating different QSM variants on tasks involving matrix data, the study finds that these models generally outperform other quantum models, with variations excelling in specific tasks. This research underscores the importance of aligning model design with input structure, providing valuable insights for future advancements in quantum machine learning.

### 7. Dysphagia Risk Stratification in Head and Neck Cancer via Two-Stage PRO-Clinical Stacking
**Authors:** Siyuan Zhao, Eric Ababio Anyimadu, Zachary G. Brumm, Yue Ma, Clifton David Fuller, Xinhua Zhang, G. Elisabeta Marai, Guadalupe Canahuate
**Link:** https://arxiv.org/abs/2607.22514v1
**Summary:** This study addresses the challenge of identifying head and neck cancer survivors who are at risk for swallowing difficulties (dysphagia) without needing complex imaging technologies. The authors developed a novel two-stage stacking model that integrates patient-reported outcomes and clinical variables to predict dysphagia risk in a straightforward and interpretable way. Their results highlight that specific patient-reported symptoms provide valuable predictive insights, paving the way for a more accessible and effective dysphagia risk assessment approach in clinical settings.

### 8. Opaque Epistemic Mediation: How LLM Deployment Configurations Shape the Validation of Pseudo-Science
**Authors:** Davide Scarso, Hugo Noronha de Almeida, Joaquim Pina
**Link:** https://arxiv.org/abs/2607.22513v1
**Summary:** The paper addresses the issue of how large language models (LLMs) assess controversial scientific claims, particularly pseudo-scientific assertions linked to ethnonationalism. By testing different LLMs (Claude, Grok, GPT, Gemini) across various configurations and interfaces, the authors found significant discrepancies in how these models rated the credibility of pseudo-scientific content, with Grok showing notably higher scores. The results highlight that the validation of scientific claims by LLMs is not consistent and can be heavily influenced by deployment settings, pointing to the need for better transparency and accountability in their use.

### 9. CausalForge: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference
**Authors:** Jiyuan Tan, Vasilis Syrgkanis
**Link:** https://arxiv.org/abs/2607.22511v1
**Summary:** CausalForge addresses the challenge of automating theoretical research in causal inference by improving the reliability of result evaluation beyond what current large language model reviewers provide. It integrates a foundational proof assistant with a self-improving system that autonomously selects research topics, proposes formal results, constructs proofs, and audits their alignment with intended scientific claims. The key contribution is the establishment of a robust framework that leverages machine-checked proofs and statement audits to enhance the credibility and accuracy of automated research outputs.

### 10. Interpretable EEG biomarkers with bag-of-waves: Spatial and temporal waveform dictionaries for low-data regimes
**Authors:** Athanasios Papastathopoulos-Katsaros, Steven T. Lee, Lin Yao, Ajay Thomas, Junseok Park, Matthew J. McGinley, Zhandong Liu
**Link:** https://arxiv.org/abs/2607.22508v1
**Summary:** The paper addresses the challenge of interpreting EEG data for diagnosing neurological conditions, which typically relies on predefined features or complex deep learning models that require large datasets. The authors propose a method called "bag-of-waves," which learns a small set of EEG waveform templates using an unsupervised approach, allowing for the analysis of EEG signals through simpler classifiers. Key results show that this method not only competes with state-of-the-art deep learning models in performance across various datasets but also provides high interpretability by linking identified waveforms to clinically relevant morphologies, making it particularly effective in low-data scenarios.
