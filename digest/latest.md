---
## 2026-08-16

### 1. Sparse Orthogonal Regression Technique: A Spectral Framework for Equation Discovery, Approximation, and Integration
**Authors:** Sabin Roman, Ljupco Todorovski, Saso Dzeroski
**Link:** https://arxiv.org/abs/2608.13504v1
**Summary:** The paper introduces the Sparse Orthogonal Regression Technique (SORT), which addresses the challenge of discovering ordinary differential equations from noisy and unevenly sampled data by learning efficient expansions in orthogonal bases. By using L1-regularized regression to estimate expansion coefficients directly from the data, SORT avoids the pitfalls of traditional approaches reliant on specific libraries or predefined equation structures. The key contribution is the establishment of a flexible framework that enhances model robustness against noise and sampling inconsistencies, while also aiding in the estimation of complex integrals and supporting nonlinear approximation tasks.

### 2. TraVEL: Trajectory-Guided Video Embedding Learning for Driving-Video Retrieval
**Authors:** Yi-Chung Chen, Philip Jacobson, Tom Lampo, Yiren Lu, Jin Yao, David I. Inouye, Jing Gao, Danhua Guo, Burhan Yaman
**Link:** https://arxiv.org/abs/2608.13495v1
**Summary:** The paper addresses the challenge of efficiently retrieving relevant clips from large-scale driving videos, which is crucial for various applications like data curation and safety analysis. The authors propose TraVEL, a motion-aware fine-tuning framework that enhances a general-purpose video embedding model by using ego-trajectory similarity for better motion understanding without requiring expert-defined rules. Their approach demonstrates significant improvements in retrieving motion-centric events, achieving notable gains in retrieval performance across different model scales.

### 3. AlayaWorld: Interactive Long-Horizon World Modeling - Full Technical Report (v1.1)
**Authors:** AlayaWorld Team, Kaipeng Zhang, Chuanhao Li, Yifan Zhan, Yongtao Ge, Yuanyang Yin, Jiaming Tan, Kang He, Liaoyuan Fan, Mingliang Zhai, Ruicong Liu, Xiaojie Xu, Xuangeng Chu, Zhen Li, Zhengyuan Lin, Zhixiang Wang, Zian Meng, Zihui Gao
**Link:** https://arxiv.org/abs/2608.13492v1
**Summary:** The report introduces an enhanced version of AlayaWorld, which improves long-horizon world modeling by refining how conditioning signals—inputs that guide content generation—are represented and integrated. Key innovations include replacing previous memory methods with a streaming 3D point-cache renderer and developing a unified encoding process that closely aligns visual conditions with generated video in both structure and timing. These changes lead to more coherent and contextually relevant outputs in interactive simulations.

### 4. Toward a Gricean Retreat: Probing LLMs for Knowledge Boundaries and Referent Specificity
**Authors:** Dananjay Srinivas, Saksham Khatwani, Maria Pacheco
**Link:** https://arxiv.org/abs/2608.13484v1
**Summary:** This paper explores the tendency of large language models (LLMs) to generate specific details about unknown entities instead of opting for safer, more general claims, which reflects a departure from the Gricean ideal of cooperative conversation. The authors used a benchmark to assess whether LLMs recognize when they lack knowledge about a referent and anticipate the appropriate level of specificity in their responses. They found that while LLMs can identify their knowledge boundaries, they still prefer to produce specific but potentially inaccurate details instead of acknowledging uncertainty, highlighting a gap in their conversational alignment with human communication principles.

### 5. Synthetic Persona Pretraining: Alignment from Token Zero
**Authors:** Julian Minder, Viktor Moskvoretskii, Raghav Singhal, Difan Jiao, Andy Arditi, Shaobo Cui, Yiderigun Borjigin, Kartik Bali, Stefan Krsteski, Harsh Raj, Huu Nguyen, Jannik Brinkmann, Ashton Anderson, Roland Aydin, Robert West
**Link:** https://arxiv.org/abs/2608.13482v1
**Summary:** The paper addresses the challenge of aligning AI language models with human values by introducing a method called Synthetic Persona Pretraining (SPP), which embeds desired personality traits into the model from the very beginning of its training. By annotating training data with reflections that reflect these values and subsequently binding them to the model during post-training, the authors demonstrate that SPP significantly improves the model's adherence to ethical guidelines and reduces instances of misalignment, particularly in moral dilemmas. The results suggest that instilling values early in the training process is crucial for achieving effective alignment.

### 6. MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and Coordination
**Authors:** Saisha Shetty, Satvik Tripathi, Austin Lin, Colin Zhao, Theodore Kim, Don Enwerem, Jacinta Arnold, Shahriar Faghani, Tessa S Cook
**Link:** https://arxiv.org/abs/2608.13476v1
**Summary:** The MARC framework addresses the limitations of traditional large language models (LLMs) in clinical AI by introducing a multi-agent system that orchestrates specialized agents for reasoning and coordination tasks, enhancing interpretability and traceability. It simplifies the prompt generation process using a Decomposer module and allows non-experts to configure the system via YAML, making it user-friendly. The open-source framework is designed for flexible deployment and is accessible to clinical professionals without programming skills.

### 7. AaLLM: An End-to-End Analog Circuit Design Framework from Topology Generation to Sizing Using Large Language Models
**Authors:** Mohammed Ayman Habib, Rylan Hart, Morteza Fayazi
**Link:** https://arxiv.org/abs/2608.13472v1
**Summary:** The paper presents AaLLM, an open-source framework that streamlines the analog circuit design process by automating topology generation and circuit sizing using large language models (LLMs). By implementing a multi-agent system that includes designers, critics, and evaluators, AaLLM significantly reduces the time and effort required for circuit design while producing novel topologies that can outperform traditional methods. Key results show that AaLLM decreases the number of SPICE simulation calls by up to 4.5 times and reduces overall design time by 40 times compared to existing techniques.

### 8. Active-Trace Complexity Bounds for Moreau--Yosida Unadjusted Langevin Sampling
**Authors:** Yuchen Xin, Zhihua Zhang
**Link:** https://arxiv.org/abs/2608.13467v1
**Summary:** This paper investigates the Moreau--Yosida unadjusted Langevin algorithm (MYULA) for sampling from nonsmooth composite distributions, focusing on improving the algorithm's efficiency by controlling the discretization error through the active trace rather than global curvature. The authors demonstrate that the number of iterations required to achieve a specified accuracy is significantly influenced by the active trace, leading to improved accuracy estimates for various structured penalties. Ultimately, they establish end-to-end guarantees for the sampling process, showing that their approach can enhance the algorithm's performance compared to traditional methods.

### 9. Concept Drift Detection and Adaptive Retraining of Malware Classification Models
**Authors:** Christofer Washington Berruz Chungata, Martin Jurecek, Katerina Potika, William B. Andreopoulos, Mark Stamp
**Link:** https://arxiv.org/abs/2608.13465v1
**Summary:** This paper addresses the issue of concept drift in malware classification, where changes in malware patterns over time can degrade model performance. The authors propose and analyze three automated concept drift detection methods, including a novel approach using One-Class Support Vector Machines (OCSVM), and compare their effectiveness across various classification models. The key finding is that drift-aware retraining based on OCSVM yields high classification accuracy while significantly reducing the need for frequent model retraining compared to static or periodic methods.

### 10. MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification
**Authors:** Daniel Perkins, John Squires, Janou Milligan, Chandra Raskoti, Linda Ungerboeck
**Link:** https://arxiv.org/abs/2608.13463v1
**Summary:** The paper addresses the challenge of generalizing image classification models across varied datasets and difficulty levels. The authors present ARMDIL, an Adaptive Router that uses a multimodal large language model to smartly direct images to the most suitable classification backbone, incorporating diverse architectures such as CNNs and vision-language models. Key findings indicate that ARMDIL performs well in cross-dataset classification and enhances adaptability and interpretability by allowing easy updates through prompt changes.
