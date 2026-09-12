---
## 2026-09-12

### 1. CausalArena: Benchmarking Causal Discovery in the Foundation Model Era
**Authors:** Zi-Rong Li, Si-Yang Liu, Tian-Zuo Wang, Han-Jia Ye
**Link:** https://arxiv.org/abs/2609.11897v1
**Summary:** The paper addresses the challenge of evaluating causal discovery methods amid the variability in existing benchmarks and the introduction of causal discovery foundation models (CDFMs). It presents CausalArena, a comprehensive benchmarking framework that combines various synthetic and real-world datasets to assess causal discovery capabilities under a unified protocol. Key findings indicate that performance can vary significantly across different evaluation setups, highlighting the importance of benchmark diversity and the risk of misleading results when pretraining environments overlap with test scenarios.

### 2. 3D Point Splatting for mmWave Radar Novel View Synthesis
**Authors:** Adnan Armouti, Yixuan Gao, Rajalakshmi Nandakumar
**Link:** https://arxiv.org/abs/2609.11894v1
**Summary:** This paper addresses the challenge of novel view synthesis (NVS) for millimeter-wave radar, which requires a renderer that accurately handles complex data and multiple viewpoints. The authors introduce 3D Point Splatting (3DPS), a differentiable point renderer that uses a physical radar model and efficiently processes complex signals. Their experiments demonstrate that 3DPS significantly outperforms existing optical methods in accuracy while being efficient in training time.

### 3. Nuha-Speech: Building General-Purpose Arabic Speech-LLMs
**Authors:** Yingzhi Wang, Reem Alhazzani, Muhammad Alqurishi
**Link:** https://arxiv.org/abs/2609.11892v1
**Summary:** The paper addresses the lack of Arabic representation in Speech Large Language Models (speech-LLMs) by introducing Nuha-Speech, which includes the creation of a large dataset and an evaluation framework for Arabic speech tasks. The researchers built a comprehensive Arabic Speech Question-Answering corpus with over 1.5 million samples and utilized it to fine-tune model variants of Qwen-Omni across various scales. This initiative aims to establish foundational resources and evaluate performance in the development of general-purpose Arabic speech-LLMs.

### 4. CoRA-NAS: Coarse Ranking and Anchor-Residual Refinement for Neural Architecture Search
**Authors:** Yifan Yang, Zhaoyan Wang, Zheng Gao, Xiaoyu Li, Jiaojiao Jiang
**Link:** https://arxiv.org/abs/2609.11884v1
**Summary:** The paper presents CoRA-NAS, a framework designed to improve the reliability of neural architecture ranking in various search spaces by combining initial static rankings with a low-cost refinement process. It employs a two-step approach that aggregates ranking proxies and uses a machine learning model to adjust early performance predictions based on sample architectures. The method shows strong results, achieving high correlation with fully trained models across different benchmarks and selecting architectures that closely match the best-known accuracies.

### 5. Domain-Specific Hallucination Detection in Large Language Models
**Authors:** Varun Teja Chundru, Debasmita Biswas
**Link:** https://arxiv.org/abs/2609.11878v1
**Summary:** The paper addresses the issue of unfaithful claims, or "hallucination," in large language models by proposing a detection pipeline that combines classification, uncertainty quantification, and calibration techniques. The pipeline achieves high accuracy in detecting hallucinations across various tasks and demonstrates significant improvement in reducing hallucination rates in generated responses when applied to a language model. Additionally, the study shows that fine-tuning models on domain-specific data yields better performance than general-domain training.

### 6. Biology-in-the-loop: Amortized Adaptive Hit Discovery in CRISPR Screens
**Authors:** Carl Edwards, Edward De Brouwer, Xiner Li, Namkyeong Lee, Ehsan Hajiramezanali, Anne Biton, Sara Mostafavi, Gabriele Scalia
**Link:** https://arxiv.org/abs/2609.11877v1
**Summary:** The paper addresses the challenge of efficiently selecting experiments in CRISPR screens when resources are limited, introducing a large benchmark called AssayBench-Loop to aid in adaptive hit discovery. The authors propose a framework, AssayLoop, which leverages a transformer-based model to guide experiment selection based on historical data, enhanced with biological knowledge from language models. The key finding is that AssayLoop significantly outperforms existing methods, achieving a 5.67-fold enrichment in candidate hit selection while requiring only a small fraction of the candidate library to be tested.

### 7. On the Regularization Landscape for the Linear Recommendation Models
**Authors:** Dong Li, Zhenming Liu, Ruoming Jin, Hao Zhou, Zhi Liu, Jing Gao, Bin Ren
**Link:** https://arxiv.org/abs/2609.11876v1
**Summary:** This paper investigates the performance similarities among various linear recommendation models, aiming to determine whether their effectiveness stems from a unified underlying framework. The authors discover that the top-performing models incorporate regularization techniques based on nuclear-norm and Frobenius-norm, leading to two new low-rank solutions that combine the advantages of both methods while addressing their limitations.

### 8. The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement
**Authors:** Yi Duan, Ying Liu, Zirui Tang, Haodong Chen, Jun Zhou, Yumou Liu, Bangrui Xu, Yukai Wu, Sidi Chen, Yuhan Zhou, Haoyu Wang, Xiaoyou Yu, Shaokun Han, Xuzhou Zhu, Le Zhou, Bolin Lu, Wei Zhou, Jiachen Liu, Nuozhou Fang, Jiaxin Tian, Ruoyu Chen, Yuxuan Li, Kai Zuo, Kaiyan Zhang, Jiantao Qiu, Conghui He, Guoliang Li, Bowen Zhou, Zhiyuan Liu, Zhoufutu Wen, Jihua Kang, Xuanhe Zhou, Fan Wu
**Link:** https://arxiv.org/abs/2609.11873v1
**Summary:** The paper addresses the limitations of current AI systems, particularly large language models (LLMs), by proposing a framework for recursive self-improvement (RSI), which allows AI to autonomously enhance both its capabilities and its improvement processes. It outlines a development roadmap that progresses through different levels of autonomy and examines the application of RSI in various fields like scientific discovery and software engineering. The authors connect their theoretical research to practical implementations and identify key challenges that need to be overcome to achieve true RSI in AI systems.

### 9. Evaluating Time-Series Foundation Models and Multimodal Dietary Context for CGM Forecasting
**Authors:** Bowen Zhang, Hsiu-Wen Cheng, Hongyu Yang, Evie L. Shen, Joleen Vansomphone, Yuna Li, Kerry Zhou, Zitian Qu, Suning Zhao, Xiangning Deng, Hua Zhou, Jin J. Zhou
**Link:** https://arxiv.org/abs/2609.11872v1
**Summary:** This paper addresses the challenge of accurately forecasting glucose levels in individuals with diabetes using continuous glucose monitoring (CGM) data. The authors evaluated various time-series models, discovering that while fine-tuning foundation models like Chronos-Bolt significantly improved prediction accuracy (reducing errors by over 6% to 18%), incorporating dietary context through a multimodal framework further enhanced performance, especially during post-meal periods. The findings highlight the necessity of adapting models specifically for CGM data and the importance of integrating dietary information to improve forecasting reliability.

### 10. Augustinian BabyLM: What Ostensive Definition Can and Cannot Teach a Small Language Model
**Authors:** Lisa Bylinina
**Link:** https://arxiv.org/abs/2609.11870v1
**Summary:** The paper explores how word meanings can be learned by small language models through visual grounding, using a method inspired by St. Augustine's idea of ostensive definition. By initializing word embeddings based on their visual representations, the authors found that this approach benefits models in some areas, particularly in recognizing object properties, while having little impact on general grammatical knowledge. Notably, the study reveals that the visual grounding remains significant for specific words throughout training, although standard benchmarks do not detect these improvements.
