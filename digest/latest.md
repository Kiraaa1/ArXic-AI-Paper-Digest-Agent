---
## 2026-08-06

### 1. Reasoning Core: Designing Broad Procedural Data for Completion-Supervised Reasoning Training
**Authors:** Damien Sileo, Valentin Lacombe, Dimitri Kachler
**Link:** https://arxiv.org/abs/2608.05148v1
**Summary:** The paper presents Reasoning Core, a diverse set of 50 procedural problem generators designed to enhance completion-supervised reasoning training for AI models. By comparing this new collection with existing procedural datasets, the authors demonstrate that Reasoning Core yields superior performance on various reasoning benchmarks while highlighting the importance of design factors like compactness and difficulty calibration. The research underscores that simply generating procedural data is insufficient for ensuring model training effectiveness; careful consideration of problem design is crucial.

### 2. Argus: A General-Purpose Agentic Runtime for Long-Horizon Reasoning
**Authors:** Boxiu Li, Zimo Wen, Yijia Fan, Junxiang Lei, Sufeng Guo, Jiaao Wu, Ruize Tang, Mukai Li, Yifei Shen, Xiaoyu Chen, Wanbo Zhang, Runjing Gu, Yifei Gao, Yuheng Wu, Xuyao Huang, Zelong Zhao, Jiachen Zhang, Shibo Hu, Hangxi Guo, Yilin Chen, Yuzhe Zhang, Fan Yang, Chuan Wen, Xian Zhang, Xuanhe Zhou, Zhijie Deng
**Link:** https://arxiv.org/abs/2608.05144v1
**Summary:** The paper presents Argus, a general-purpose agentic runtime designed to enhance long-horizon reasoning by allowing persistent adaptation to new information while maintaining operational goals. Argus features distinct roles that manage project tasks and employ a self-evolving mechanism to improve performance through verified learning. Key results demonstrate that Argus significantly outperforms Direct Copilot in benchmark tests while effectively managing resources and improving task efficiency over time.

### 3. OctoLong: Mid-Training On Cross-Repository Code Contexts Enhances Long-Context Modeling
**Authors:** Indraneil Paul, Falko Helm, Goran Glavaš, Iryna Gurevych
**Link:** https://arxiv.org/abs/2608.05141v1
**Summary:** The paper presents OctoLong, a novel method for enhancing long-context modeling in language models by curating rich code contexts that extend for millions of tokens, addressing the limitations of traditional long-context corpora. By incorporating these dependency-rich code references during mid-training, the authors demonstrate that even a small integration of OctoLong data significantly improves performance in long-range code retrieval and understanding, which benefits various coding tasks and scenarios. The results suggest that OctoLong can effectively augment the capabilities of open-language models in handling complex coding tasks.

### 4. Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training Long-Horizon Reasoning
**Authors:** Yinghui He, Ling Yang, Jiarui Liu, Yongjin Yang, Lechen Zhang, Yingcheng Wu, Zhenfei Yin, Mengdi Wang, Sanjeev Arora
**Link:** https://arxiv.org/abs/2608.05139v1
**Summary:** The paper addresses the challenge of evaluating and training large language models (LLMs) on complex multi-step tasks that require switching between different reasoning skills. It introduces a new measure called Skill Entropy to quantify the difficulty of these transitions and presents the Skill^2-Bench benchmark to assess model performance across 558 skills. Notably, the authors demonstrate that their proposed Skill-Entropy RL training framework significantly improves model accuracy on these challenging tasks, showcasing the effectiveness of skill entropy as a training signal.

### 5. Teaching Nemotron Greek: Mining a Corpus, Adapting Retrieval, and Grounding Generation for Modern Greek across Specialist Domains
**Authors:** Ayoub Kirouane, Christos Petrocheilos
**Link:** https://arxiv.org/abs/2608.05138v1
**Summary:** The paper addresses the lack of Modern Greek support in NVIDIA's retrieval-augmented generation (RAG) models, which is essential for various specialist fields like law and healthcare. The authors develop an end-to-end adaptation of the Nemotron retrieval stack for Modern Greek by mining relevant corpora, training retrieval models, and introducing a new benchmark called HERA. Key results show that their optimized models significantly improve retrieval performance and generation accuracy, indicating a strong foundation for future Greek-language RAG systems.

### 6. The Loss Does Not See the Basis, but Adam Does
**Authors:** Devender Singh
**Link:** https://arxiv.org/abs/2608.05136v1
**Summary:** The paper investigates how different optimization algorithms influence the learning of low-rank solutions in matrix factorization, specifically contrasting the behavior of gradient descent with that of Adam. The authors examine the gauge symmetry of the loss function and show that while gradient descent naturally biases toward low-rank solutions, Adam does not because it lacks gauge equivariance. A key finding is that the choice of optimizer fundamentally affects the recovery of structured solutions, indicating that basis selection is crucial in determining the performance of optimization in learning tasks.

### 7. Predicting Brain Morphometry with MT-GNN: Mesh Evolution in Continuous Time with Graph-Based Metric Tensor Embeddings
**Authors:** Hao Ding, Daniel Semchin, Paul M. Thompson, Boris Gutman
**Link:** https://arxiv.org/abs/2608.05132v1
**Summary:** The paper addresses the challenge of predicting the evolution of subcortical brain structures' shape over time using prior MRI scans, which can aid in medical prognosis and clinical trials. The authors propose a novel graph-based neural network model called MT-GNN that predicts the surface geometry directly in continuous time by utilizing a metric tensor approach, resulting in superior accuracy compared to existing methods. Their model achieved a mean vertex error reduction of 2.29% across 14 different brain structures, outperforming other techniques significantly as the prediction horizon increased.

### 8. OPD-V: Visual On-Policy Self-Distillation with Modality Balance
**Authors:** Aniri, Jinhe Bi, Peng Liao, Zengjie Jin, Volker Tresp, Fei Shen, Yunpu Ma, Tat-Seng Chua
**Link:** https://arxiv.org/abs/2608.05131v1
**Summary:** The paper addresses the issue of Modality Imbalance in multimodal large language models, where an over-reliance on text hinders effective visual reasoning during self-distillation. It proposes a new method called OPD-V, which utilizes Positive and Negative Teachers to improve the balance of modalities during the distillation process. The key contribution is the demonstration that incorporating Modality Balance as privileged information enhances reasoning performance across multiple benchmarks while also lowering training costs.

### 9. SSTQ:Privacy-Preserving Vector Quantization via Subsampled Stochastic TurboQuant
**Authors:** Adel Javanmard, David P. Woodruff, Vahab Mirrokni
**Link:** https://arxiv.org/abs/2608.05127v1
**Summary:** The paper addresses the challenge of achieving local differential privacy in distributed optimization with low communication costs, improving upon existing vector quantization methods that suffer from high variance due to their dimensionality. The authors propose Subsampled Stochastic TurboQuant (SSTQ), which combines advanced mathematical techniques to enhance privacy and efficiency, and demonstrate that it significantly reduces mean squared error (MSE) scaling while requiring fewer bits per client. Empirical evaluations on standard benchmarks show that SSTQ outperforms existing methods in terms of utility and communication efficiency.

### 10. Spoken Function Calling: A New Perspective on Spoken Language Understanding for Large Audio Language Models
**Authors:** Yuezhang Peng, Yuxin Liu, Changfeng Gao, Zhifu Gao, Xiangang Li, Xie Chen
**Link:** https://arxiv.org/abs/2608.05126v1
**Summary:** The paper addresses the limitations of traditional spoken language understanding (SLU) in handling open-domain tasks by introducing a new method called Spoken Function Calling (SFC). This approach involves creating structured rule definitions and a curated dataset to improve semantic understanding in dialogue systems. The key finding is that SFC significantly enhances the accuracy of semantic extraction for both large language models (LLMs) and large audio language models (LALMs) compared to conventional SLU methods.
