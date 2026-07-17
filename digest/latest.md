---
## 2026-07-17

### 1. Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models
**Authors:** Patrik Wolf, Thomas Kleine Buening, Andreas Krause, Celestine Mendler-Dünner
**Link:** https://arxiv.org/abs/2607.15277v1
**Summary:** The paper investigates how well large language models (LLMs) adhere to the principle of statistical self-consistency, which suggests that their predictions should align when considering different subpopulations of data. Using binary trees to partition populations and analyzing LLM responses, the authors found that models often produce inconsistent estimates, with finer subpopulation guesses providing better alignment with human data than direct population-level responses. This indicates that while models have knowledge of subpopulations, they struggle to effectively integrate this knowledge into overall estimates, suggesting a need for improved evaluation methods for LLMs.

### 2. RoboTTT: Context Scaling for Robot Policies
**Authors:** Yunfan Jiang, Yevgen Chebotar, Ruijie Zheng, Fengyuan Hu, Yunhao Ge, Jimmy Wu, Tianyuan Dai, Scott Reed, Li Fei-Fei, Yuke Zhu, Linxi "Jim" Fan
**Link:** https://arxiv.org/abs/2607.15275v1
**Summary:** The paper presents RoboTTT, a novel robot training method that significantly increases the amount of visuomotor context used during robot policy training to 8,000 timesteps, which is three times longer than existing methods. By integrating Test-Time Training with advanced sequence modeling, RoboTTT allows robots to perform complex tasks more effectively, achieving an 87% performance improvement on manipulation tasks compared to models using only single-step context. This breakthrough demonstrates that longer context lengths can enhance the capabilities of robot foundation models, enabling one-shot imitation and robust performance in challenging environments.

### 3. MeanFlowNFT: Bringing Forward-Process RL to Average-Velocity Generators
**Authors:** Yushi Huang, Xiangxin Zhou, Jun Zhang, Liefeng Bo, Tianyu Pang
**Link:** https://arxiv.org/abs/2607.15273v1
**Summary:** The paper addresses the challenge of efficiently generating samples using MeanFlow generators by applying reinforcement learning (RL) techniques from the DiffusionNFT framework. It introduces MeanFlowNFT, which optimizes instantaneous velocities while maintaining the fast sampling characteristics of MeanFlow that rely on average velocities. The key contribution is that MeanFlowNFT outperforms previous state-of-the-art methods, achieving better performance with significantly fewer sampling steps in tasks such as image and video generation.

### 4. SciDiagramEdit: Learning to Edit Scientific Diagrams from Paper Revisions
**Authors:** Yasheng Sun, Zezi Zeng, Yifan Yang, Chong Luo, Wenyi Wang, Ziwei Liu, Jürgen Schmidhuber
**Link:** https://arxiv.org/abs/2607.15272v1
**Summary:** The paper introduces SciDiagramEdit, a framework designed to automate the editing of scientific diagrams based on natural-language instructions, addressing the often tedious task of revising figures in research papers. It utilizes a benchmark that analyzes revisions from arXiv to learn editing skills, refining its editing capabilities through agentic learning methods. The key contribution is demonstrating that leveraging actual manuscript revisions can significantly enhance the accuracy of figure editing instructions.

### 5. Online Neural Space Time Memory for Dynamic Novel View Synthesis
**Authors:** Baback Elmieh, Lynn Tsai, Zeman Li, Srinivas Kaza, Tiancheng Sun, Gabor Csapo, Ali Behrouz, Yuan Deng, Stephen Lombardi, Steven M. Seitz, Xuan Luo
**Link:** https://arxiv.org/abs/2607.15271v1
**Summary:** The paper addresses the challenge of synthesizing new views from streaming videos in real-time, particularly in dynamic scenes with occlusions. The authors propose a novel method that decouples the processes of memory updates and application, allowing for periodic updates while still applying the memory frame by frame. This approach, which includes a Memory Loss mechanism and a Memory Caching strategy, achieves state-of-the-art performance in real-time view synthesis, especially in scenes involving dynamic human motion.

### 6. Pretraining Data Can Be Poisoned through Computational Propaganda
**Authors:** Victoria Graf, Hannaneh Hajishirzi, Noah A. Smith, David Kohlbrenner, Kyle Lo
**Link:** https://arxiv.org/abs/2607.15267v1
**Summary:** The paper addresses the vulnerability of language models (LMs) to harmful behaviors introduced through poisoned pretraining data, particularly focusing on large-scale data sources. It presents a new method, called HalfLife, for analyzing and estimating the inclusion of malicious content in web-crawled training data from public discussion platforms. The key finding highlights that public interfaces can serve as a vector for effective attacks on language model pretraining, emphasizing the need for better detection mechanisms in data curation processes.

### 7. SceneBind: Binding What and Where Across Vision, Audio and Language
**Authors:** Mingfei Chen, Zijun Cui, Ruoke Zhang, Hyeonggon Ryu, Eli Shlizerman
**Link:** https://arxiv.org/abs/2607.15265v1
**Summary:** SceneBind addresses the limitation of existing multi-modal models that effectively identify objects but lack explicit spatial relationships in scenes. It introduces a novel representation that combines semantic embeddings with spatial attributes, allowing for better alignment and retrieval of visual, audio, and language information. The key contribution is its state-of-the-art performance in scene and spatial retrieval, along with successful application to tasks like audio-visual localization, supported by a new real-world dataset and training protocol.

### 8. Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents
**Authors:** Paul Kassianik, Blaine Nelson, Yaron Singer
**Link:** https://arxiv.org/abs/2607.15263v1
**Summary:** The paper addresses the limitation of traditional evaluations of security agents, which often focus solely on their peak performance without considering the operational costs involved. The authors propose a cost-aware evaluation framework that assesses both offensive and defensive security agents based on their performance relative to budget constraints. Key findings reveal that while offensive capabilities improve with additional resources, defensive capabilities rely more on strategic tool usage and decision-making, highlighting the need for evaluations that reflect practical operational efficiency.

### 9. Decoding Market Emotion from Blockchain Activity: A Data-Driven Sentiment Classifier
**Authors:** Arthur G. Bubolz, Abreu Quevedo, Giancarlo Lucca, Rafael A. Berri, Eduardo Borges, Bruno L. Dalmazo
**Link:** https://arxiv.org/abs/2607.15258v1
**Summary:** This study addresses the challenge of understanding Bitcoin market sentiment by analyzing blockchain activity, financial data, and social media content, rather than solely focusing on price predictions. The researchers developed a sentiment classifier using various machine learning techniques, with XGBoost proving to be the most effective, achieving an average F1-score of around 0.84. They also employed SHAP for model interpretability, demonstrating that combining these data sources can provide valuable insights into cryptocurrency market behavior.

### 10. SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration
**Authors:** Yuyao Zhang, Junjie Gao, Zhengxian Wu, Jiaming Fan, Jin Zhang, Shihan Ma, Yao Yao, Weiran Qi, Chuyan Jin, Guiyu Ma, Xingzhong Xu, Kai Yang, Ji-Rong Wen, Zhicheng Dou
**Link:** https://arxiv.org/abs/2607.15257v1
**Summary:** The paper addresses the challenge of information-seeking agents becoming ineffective due to repetitive search loops when they fail to find useful information. To tackle this, the authors develop SearchOS, a multi-agent framework that maintains a clear and shared record of search progress through a structured context management system. The key contribution is that SearchOS outperforms existing systems, improving the efficiency and effectiveness of information retrieval by dynamically managing tasks and evidence throughout the search process.
