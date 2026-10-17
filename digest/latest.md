---
## 2026-10-17

### 1. 3DCodeVerse: Exploring 3D Worlds as Code
**Authors:** Yipeng Gao, Ziyao Zeng, Jinfa Huang, Yijiang Li, Haolin Xiong, Wang Qin, Xinlei Yu, Youheng Yao, Jie Zhang, Kun-Yu Lin, Rong Liu, Yinyuan Zhao, Yajie Zhao, Meiqi Guo, Jiebo Luo, Lei Shu, Yunhao Ge, Xinyu Hu, Laurent Itti
**Link:** https://arxiv.org/abs/2610.22341v1
**Summary:** The paper presents 3DCodeVerse, a system designed to enable agents to generate and verify editable 3D content efficiently. It includes a large dataset of executable 3D code and a framework that allows for automated refinement and evaluation of 3D programs. Key findings show that fine-tuning existing models on this dataset dramatically enhances their performance in 3D coding tasks, achieving a notable success rate in human evaluations compared to a competitor.

### 2. Dexterity from Supervised Play
**Authors:** Botao He, Yiming Dou, Yiannis Aloimonos, Jitendra Malik, Akash Sharma, Ruoshi Liu
**Link:** https://arxiv.org/abs/2610.22340v1
**Summary:** The paper addresses the challenge of enabling robots to learn dexterous manipulation by autonomously accumulating the necessary experience. The authors propose a framework called DSP, which leverages behavior cloning from short sessions of human play to generate an initial policy, subsequently allowing the robot to collect extensive interaction data for training a world model. The key contribution is that this method significantly improves success rates in tasks like object manipulation while requiring far less data than traditional reinforcement learning approaches.

### 3. Lean Graph Search for Formal Theorem Proving
**Authors:** Yihan Xu, Jia-Chen Gu, Junyi Zhang, Di Wu, Haikang Deng, Po-Nien Kung, Kai-Wei Chang, Amit Sahai, Wei Wang, Nanyun Peng
**Link:** https://arxiv.org/abs/2610.22339v1
**Summary:** The paper addresses the challenge of retrieving relevant lemmas for formal theorem proving by leveraging multi-hop dependencies among mathematical declarations, instead of relying solely on direct lexical matches. The authors introduce LeanGraphSearch, a graph-based retrieval method for Lean 4 that effectively identifies supporting lemmas through a graph of forward dependencies, improving recall and coverage in mathematical proofs. Key results demonstrate that this approach enhances theorem proving efficiency, achieving up to a 40% improvement in pass rates compared to conventional methods.

### 4. Robust Reinforcement Learning for Dynamic Treatment Regimes under Model and Measurement Uncertainty
**Authors:** Chengze Xie, Xuan Wang, Ying Ding, Hairong Wang, Yan Li
**Link:** https://arxiv.org/abs/2610.22336v1
**Summary:** The paper addresses the challenge of developing adaptive treatment policies for patients that remain effective despite errors in biomarker measurements and changes in disease progression. The authors propose a robust reinforcement learning framework that models patients as hidden contexts, allowing for improved generalization and resilience. Their approach, applied to metastatic prostate cancer treatment, demonstrates significantly better performance and reliability compared to existing methods, showcasing the potential of robust RL for creating trustworthy adaptive therapy strategies.

### 5. Evaluation Awareness Beyond English: Do LLMs Act Differently When Tested in Indic Languages?
**Authors:** Trizal Garg, Sibayan Mitra, Arya Karanjkar, Advait Singh, Jagat Sesh Challa, Yash Sinha, Siddharth Mehrotra, Dhruv Kumar, Pratham Yogish Maliya
**Link:** https://arxiv.org/abs/2610.22333v1
**Summary:** The paper investigates whether large language models (LLMs) display evaluation awareness—altering their behavior when they know they are being tested—specifically in Indic languages. The researchers tested four instruction-tuned models across five Indic languages and English, finding that models were significantly more likely to refuse harmful requests when informed they were being monitored. Notably, the refusal rate for harmful requests increased by 14.4 percentage points in Indic languages, indicating that safety evaluations may not accurately reflect real usage behaviors in these languages.

### 6. KnowGPO: Knowledge-Grouped Policy Optimization for Search Agents
**Authors:** Siqi Chen, Zhengxi Lu, Yuchen Yan, Xingyu Wu, Qipeng Chen, Xin Zhang, Aiting Liu, Chao Deng, Jie Liu, Jin Ma, Weiming Lu, Jun Xiao, Yongliang Shen
**Link:** https://arxiv.org/abs/2610.22331v1
**Summary:** The paper addresses the challenge of assigning credit to individual decisions in deep search agents that rely on long-term interactions to complete knowledge-intensive tasks. It introduces KnowGPO, a reinforcement learning framework that evaluates trajectories based on the knowledge they acquire rather than just surface observations, allowing for more reliable credit assignment. The results show that KnowGPO significantly outperforms existing methods and achieves competitive performance with larger models on various benchmarks.

### 7. Designing Transformers for Continuous Diffusion Language Models
**Authors:** Weijian Luo, Yujian Chen, Hao Jiang, Guang Cheng, Tianyang Hu
**Link:** https://arxiv.org/abs/2610.22330v1
**Summary:** The paper addresses the limitations of existing transformer architectures for continuous diffusion language models (CDLMs) used in language generation. It introduces the Language Diffusion Transformer (LangDiT), which incorporates novel design elements to optimize performance. The key contribution is a significant reduction in generation perplexity, surpassing previous state-of-the-art models, highlighting the importance of architectural design in enhancing CDLM capabilities.

### 8. ACEdit: Stable Multi-Turn Image Editing via Asymmetric Conditioning
**Authors:** Sara Dorfman, Nir Goren, Gal Barak, Daniel Cohen-Or, Or Patashnik
**Link:** https://arxiv.org/abs/2610.22328v1
**Summary:** The paper tackles the problem of image editing quality deteriorating over multiple turns due to cumulative distribution shifts. To address this, the authors propose a training method that uses self-generated outputs for editing while leveraging a teacher model to maintain stability and reliability, known as asymmetric conditioning. Their approach significantly reduces quality loss in multi-turn edits while ensuring adherence to the original editing instructions.

### 9. Twice Upon a Time: Complementary Representations for Time-Series Reasoning
**Authors:** Hedi Zisling, Liran Nochumsohn, Ilan Naiman, Mihir Parmar, Omri Azencot
**Link:** https://arxiv.org/abs/2610.22327v1
**Summary:** The paper addresses the challenge of effectively representing time-series data for language-based reasoning and prediction tasks. The authors propose a dual-view model that uses complementary representations: one that maintains absolute measurements through line plots and another that normalizes data to highlight temporal structure. This approach significantly improves performance on various benchmarks, achieving a TSRBench accuracy of 53.2%, demonstrating the effectiveness of combining these different representations in time-series language models.

### 10. Training Reasoning Models to Generate Diverse Scientific Ideas
**Authors:** Manya Wadhwa, Pranav Narayanan Venkit, Hiroaki Hayashi, Yu Li, Tuhin Chakrabarty, Chien-Sheng Wu
**Link:** https://arxiv.org/abs/2610.22324v1
**Summary:** This paper addresses the challenge of generating diverse and high-quality scientific ideas using Large Language Models (LLMs). The authors propose a novel training approach that employs a set-level reinforcement learning objective to generate multiple distinct and structured idea cards grounded in source documents, while penalizing redundancy. Their trained model demonstrates superior creative utility compared to existing models, achieving a balance between idea diversity and quality without sacrificing the feasibility of executing the generated ideas.
