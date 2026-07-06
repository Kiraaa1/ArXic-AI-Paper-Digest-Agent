---
## 2026-07-06

### 1. Neuron-Aware Active Few-Shot Learning for LLMs
**Authors:** Zhuowei Chen, Liwei Chen, Christian Schunn, Raquel Coelho, Xiang Lorraine Li
**Link:** https://arxiv.org/abs/2607.02423v1
**Summary:** The paper addresses the challenge of efficiently adapting large language models (LLMs) to specialized domains with minimal human annotation by introducing NeuFS, a framework that selects the most informative unlabeled samples based on internal neuron activation patterns instead of relying on external outputs. This new approach enhances diversity in the selected few-shot samples while identifying those that are particularly challenging for the model. Experimental results show that NeuFS outperforms existing methods in reasoning and text classification tasks, highlighting the value of leveraging internal model dynamics for sample selection.

### 2. LIME: Learning Intent-aware Camera Motion from Egocentric Video
**Authors:** Boyang Sun, Jiajie Li, Yung-Hsu Yang, Chenyangguang Zhang, Tim Engelbracht, Sunghwan Hong, Cesar Cadena, Marc Pollefeys, Hermann Blum
**Link:** https://arxiv.org/abs/2607.02417v1
**Summary:** The paper addresses the challenge of generating camera movements for autonomous robots based on user intent expressed in natural language, which is crucial for tasks like object inspection or revealing hidden details. The authors introduce LIME, a novel model that learns from egocentric video footage to predict appropriate camera poses, effectively capturing diverse user intentions. The key contribution is demonstrating that LIME can transform passive video into actionable insights for intent-aware camera motion, enhancing robotic perception and interaction capabilities.

### 3. The Future of NLP may not be at NLP Conferences: Scholarly Migration Patterns in Natural Language Processing
**Authors:** David Jurgens
**Link:** https://arxiv.org/abs/2607.02416v1
**Summary:** The paper investigates whether the center of NLP research is shifting from traditional NLP conferences to broader machine learning venues, an effect amplified by the rise of Large Language Models. Analyzing publication trends between 2010 and 2026, the authors find that established researchers are publishing less in ACL flagship tracks while increasingly favoring newer Findings tracks and general ML venues, which attract more citations. This trend indicates a significant migration of NLP scholarship towards general ML conferences, reflecting a changing landscape in the field.

### 4. Q-GAIN: A Python Package for Machine Learning and Physically Informed Analysis Applications
**Authors:** M. Doris, S. Guo, S. M. Koh, L. Ritter, A. R. Fritsch, S. Mukherjee, I. B. Spielman, J. P. Zwolak
**Link:** https://arxiv.org/abs/2607.02413v1
**Summary:** The Q-GAIN Python package addresses the need for efficient machine learning and physics-informed analysis in cold-atom experiments, particularly for analyzing images of Bose-Einstein condensates. It offers a modular workflow that allows users to seamlessly load data, apply machine learning techniques for feature detection, and utilize traditional analysis methods. Key contributions include its implementation of classification tasks, soliton detection, and an object-detection tool for identifying vortices in BEC images.

### 5. Text-Driven 3D Indoor Scene Synthesis in Non-Manhattan Environments
**Authors:** Xianhui Meng, Zirui Song, Yuchen Zhang, Li Zhang, Yongxuan Lv, Xiuying Chen, Kun Wang, Yan Luo, Kai Chen, Hangjun Ye, Long Chen, Jun Liu, Xiaoshuai Hao
**Link:** https://arxiv.org/abs/2607.02407v1
**Summary:** The paper addresses the challenge of generating realistic 3D indoor scenes in non-Manhattan environments, where traditional methods struggle with object placement and layout accuracy. The authors introduce SPG-Layout, a novel framework that incorporates statistical object distribution and a hierarchical layout strategy to improve scene fidelity. Their extensive evaluation shows that SPG-Layout outperforms existing approaches, effectively balancing semantic realism and physical plausibility in both Manhattan and complex non-Manhattan settings.

### 6. Object-centric LeJEPA
**Authors:** Jakob Geusen, Ender Konukoglu
**Link:** https://arxiv.org/abs/2607.02404v1
**Summary:** The paper addresses the challenge of training image encoders efficiently for downstream tasks by focusing on object-centric representation instead of whole images, which typically require large datasets. The authors utilize object masks from off-the-shelf segmenting algorithms to stabilize the training process and extend the LeJEPA framework to align these object representations. The key contribution is that this object-level approach significantly outperforms the traditional image-level method across multiple tasks, achieving better performance on benchmarks like tracking, classification, segmentation, and re-identification.

### 7. ACID: Action Consistency via Inverse Dynamics for Planning with World Models
**Authors:** Gawon Seo, Dongwon Kim, Suha Kwak
**Link:** https://arxiv.org/abs/2607.02403v1
**Summary:** The paper addresses the issue of ensuring intermediate transitions in decision-time planning with action-conditioned world models are realizable and consistent, rather than just focusing on reaching the goal. The authors introduce a framework called ACID, which incorporates cycle action consistency by comparing actions inferred from predicted transitions to the originally conditioned actions. Their results show that ACID significantly enhances planning effectiveness across various tasks while using less computational resources compared to existing methods.

### 8. Fast Multi-dimensional Refusal Subspaces via RFM-AGOP
**Authors:** Thomas Winninger
**Link:** https://arxiv.org/abs/2607.02396v1
**Summary:** The paper addresses the challenge of identifying multi-dimensional refusal subspaces in Large Language Models (LLMs), which are important for ensuring safety and interpretability but are often difficult to extract due to computational constraints. The authors propose an efficient adaptation of the Recursive Feature Machine (RFM) algorithm, enhanced by a probe-informed initialization, which allows for rapid identification of these subspaces, achieving significant speed improvements while also outperforming other methods in certain tasks. This suggests that RFM could serve as a scalable tool for subspace extraction in LLMs.

### 9. WattGPU: Predicting Inference Power and Latency on Unseen GPUs and LLMs
**Authors:** Mauricio Fadel Argerich, Jonathan Fürst, Marta Patiño-Martínez
**Link:** https://arxiv.org/abs/2607.02391v1
**Summary:** WattGPU addresses the challenge of efficiently matching Large Language Models (LLMs) to GPUs for inference workloads without the need for exhaustive profiling. The tool uses two predictive models based solely on publicly available LLM metadata and GPU specifications, enabling accurate predictions of GPU power draw and latency even for unseen hardware. Key results show that WattGPU significantly reduces prediction error for power and latency in server scenarios, outperforming traditional methods by up to four times.

### 10. DecompRL: Solving Harder Problems by Learning Modular Code Generation
**Authors:** Juliette Decugis, Fabian Gloeckle, Francis Bach, Taco Cohen, Gabriel Synnaeve
**Link:** https://arxiv.org/abs/2607.02390v1
**Summary:** The paper presents DecompRL, a novel reinforcement learning algorithm designed to tackle complex problem-solving tasks by breaking them down into smaller, independently solvable components, which can be recombined for greater efficiency. By shifting the focus from expensive GPU inference to more economical CPU evaluations, DecompRL is able to explore a vast number of potential solutions while significantly reducing costs. The approach demonstrates superior performance on benchmark tasks compared to traditional and diversity-based RL methods, successfully solving problems that were previously beyond reach.
