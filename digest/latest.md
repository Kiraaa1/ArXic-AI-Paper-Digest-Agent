---
## 2026-06-13

### 1. Before You Think: System 0, AI-Mediated Cognition and Cognitive Colonization
**Authors:** Marianna Bergamaschi Ganapini, Massimo Chiriatti, Enrico Panai, Giuseppe Riva
**Link:** https://arxiv.org/abs/2606.13658v1
**Summary:** This paper investigates how artificial intelligence affects human thinking and knowledge through three frameworks, emphasizing the unique perspective of System 0. It introduces the idea of "cognitive colonization," where AI systems subtly embed external influences in users' thought processes. The authors argue that recognizing and understanding these hidden impacts is crucial, especially as AI becomes increasingly integrated into daily life.

### 2. Dense Supervision, Sparse Updates: On the Sparsity and Geometry of On-Policy Distillation
**Authors:** Guo Yu, Wenlin Liu, Yulan Hu, Hao-Xuan Ma, Jun-Peng Jiang, Han-Jia Ye
**Link:** https://arxiv.org/abs/2606.13657v1
**Summary:** The paper investigates how on-policy distillation (OPD) affects model parameter updates in language and vision-language models, revealing that these updates are small and sparsely distributed across layers, primarily affecting feedforward networks. The authors find that training on just the identified sparse subnetworks achieves nearly the same performance as using the full OPD, but note that the effectiveness of different optimization methods varies, with dense teacher supervision enabling particular geometric characteristics in the updates. This work highlights that OPD maintains specific properties of on-policy training rather than merely rewriting parameters.

### 3. Operadic consistency: a label-free signal for compositional reasoning failures in LLMs
**Authors:** Nathaniel Bottman, Yinhong Liu, Kyle Richardson
**Link:** https://arxiv.org/abs/2606.13649v1
**Summary:** The paper addresses the challenge of detecting reasoning failures in large language models (LLMs) during inference without relying on ground-truth labels. The authors introduce "operadic consistency" (OC), a method that checks whether a model's direct answer to a question aligns with the answer derived from a composed breakdown of the same question. Their findings show that OC is a strong predictor of accuracy across various data sets, outperforming existing confidence indicators and leading to improved selective prediction in LLMs.

### 4. SkMTEB: Slovak Massive Text Embedding Benchmark and Model Adaptation
**Authors:** Marek Šuppa, Andrej Ridzik, Daniel Hládek, Natália Kňažeková, Viktória Ondrejová
**Link:** https://arxiv.org/abs/2606.13647v1
**Summary:** The paper presents SkMTEB, the first extensive benchmark for text embeddings in Slovak, addressing the lack of resources for this low-resource language by evaluating 31 datasets across various tasks. The authors developed two efficient Slovak embedding models, \texttt{e5-sk-small} and \texttt{e5-sk-large}, which are competitively effective while being locally deployable, thus providing tools for semantic search and generation tasks. The project aims to set a precedent for developing similar resources for other under-resourced languages.

### 5. Recursive Agent Harnesses
**Authors:** Elias Lumer, Sahil Sen, Kevin Paul, Vamse Kumar Subbiah
**Link:** https://arxiv.org/abs/2606.13643v1
**Summary:** The paper introduces the Recursive Agent Harness (RAH), a new approach that enhances long-context reasoning in coding agents by utilizing full agent harnesses instead of just recursive model calls. By enabling a parent agent to generate and execute scripts that spawn subagents for more granular tasks, RAH significantly improves performance in coding tasks, achieving an increase from 71.75% to 81.36% accuracy over the Codex baseline, and reaching 89.77% with a more powerful model. The study highlights how this harness recursion strategy effectively enhances task execution and reasoning capabilities in AI coding agents.

### 6. The Stable Recovery Manifold: Geometric Principles Governing Recoverability in Continual Learning
**Authors:** Ayushman Trivedi, Bhavika Melwani
**Link:** https://arxiv.org/abs/2606.13637v1
**Summary:** The paper addresses the issue of catastrophic forgetting in continual learning, where previously learned knowledge can be lost during training on new tasks. The authors investigate the geometric aspects of recoverability by analyzing how knowledge can be retained and recovered despite significant changes in representation, using a model based on a ResNet-18 trained on Split CIFAR-100. They find that the dimensionality required for effective recovery remains stable, indicating that the underlying knowledge is still accessible, despite changes in the representational space, suggesting forgetting is more about access issues rather than a loss of information.

### 7. Operads for compositional reasoning in LLMs
**Authors:** Nathaniel Bottman, Kyle Richardson
**Link:** https://arxiv.org/abs/2606.13634v1
**Summary:** The paper addresses the challenge of effectively breaking down complex queries into simpler parts for large language models (LLMs) to enhance their reasoning abilities. It introduces operads, a mathematical framework that models these decompositions, allowing for a formal understanding of how sub-answers can be combined. A key finding is the introduction of operadic consistency, which correlates with higher accuracy in answering multi-step questions across various LLMs, suggesting operads can improve the reliability of reasoning in AI systems.

### 8. Aerial Wildfire Suppression Planning with a Hybrid CNN-Cellular Automata Fire Model
**Authors:** Ion Matei, Maksym Zhenirovskyy, Takuya Kurihana, Rohit Vupala, Anthony Wong
**Link:** https://arxiv.org/abs/2606.13633v1
**Summary:** The paper addresses the challenge of planning aerial strategies for wildfire suppression, which involves anticipating fire spread and determining effective intervention actions in uncertain conditions. The authors developed a combined model using a hybrid neural network and cellular automaton to predict fire behavior and optimize aerial drop strategies for water and retardants. Their approach demonstrated the ability to create effective suppression plans that reduce the area affected by wildfires while accounting for various uncertainties, as illustrated in a case study on the 2020 Bear Fire.

### 9. From Tokens to Faces: Investigating Discrete Speech Representations for 3D Facial Animation
**Authors:** Pedro Correa, Olivier Perrotin, Samir Sadok, Paula Costa, Thomas Hueber
**Link:** https://arxiv.org/abs/2606.13630v1
**Summary:** This paper investigates how different types of speech representations impact the quality of 3D facial animations driven by speech input. The authors evaluate four representation methods and find that those encoding phonetic classes improve the accuracy of facial animations. They also propose a new Audio Visual Text-to-Speech (AVTTS) pipeline that uses shared discrete representations for decoding both speech and facial motions.

### 10. Valid Inference with Synthetic Data via Task Exchangeability
**Authors:** Lezhi Tan, Tijana Zrnic
**Link:** https://arxiv.org/abs/2606.13629v1
**Summary:** This paper addresses the challenges of using synthetic data in scientific research, which can often be biased or inaccurately represent real-world scenarios. The authors introduce a concept called "task exchangeability," which allows researchers to validate the use of synthetic data by ensuring it is mathematically comparable to historically relevant real data. They provide methods for making valid inferences from synthetic data, demonstrating their approach through applications in public opinion surveys and AI evaluations.
