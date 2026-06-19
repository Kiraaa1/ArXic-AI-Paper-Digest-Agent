---
## 2026-06-19

### 1. How Transparent is DiffusionGemma?
**Authors:** Joshua Engels, Callum McDougall, Bilal Chughtai, Janos Kramar, Senthoran Rajamanoharan, Cindy Wu, Arthur Conmy, Asic Q Chen, Jean Tarbouriech, Min Ma, Brendan O'Donoghue, João Gabriel Lopes de Oliveira, Rohin Shah, Neel Nanda
**Link:** https://arxiv.org/abs/2606.20560v1
**Summary:** This paper investigates the transparency of the DiffusionGemma model compared to the autoregressive Gemma 4, focusing on how well we can understand its reasoning processes. The authors analyze variable and algorithmic transparency, finding that while DiffusionGemma initially seems opaque, it can achieve better interpretability by mapping intermediate states through a token bottleneck without sacrificing performance. The study reveals new phenomena unique to diffusion models and concludes that DiffusionGemma's outputs are comparable in monitorability to those of Gemma 4.

### 2. UNIEGO: Proxies as Mediators for Unified Egocentric Video Representation Learning
**Authors:** Wenhao Chi, Arkaprava Sinha, Dominick Reilly, Hieu Le, Srijan Das
**Link:** https://arxiv.org/abs/2606.20559v1
**Summary:** The paper addresses the challenge of egocentric video understanding, which is limited by the single viewpoint of wearable cameras. It introduces UNIEGO, a novel framework that uses hierarchical multi-teacher distillation with proxy models to integrate knowledge across different perspectives and modalities, enhancing the representation learned from egocentric videos. The key contribution is that UNIEGO achieves state-of-the-art performance in action recognition, video retrieval, and action segmentation by effectively managing and distilling diverse, yet complementary, teacher knowledge.

### 3. Optimal Deterministic Multicalibration and Omniprediction
**Authors:** Georgy Noarov, Aaron Roth
**Link:** https://arxiv.org/abs/2606.20557v1
**Summary:** The paper addresses the problem of achieving multicalibration in machine learning models, which requires that these models remain unbiased not only overall but also when considering specific groups. The authors present a deterministic algorithm that achieves the optimal sample complexity previously only attainable by randomized algorithms, thereby solving an open question in the field. Additionally, they extend this approach to create optimal deterministic predictors that satisfy outcome indistinguishability, contributing to advances in omniprediction and panprediction.

### 4. Structuring and Tokenizing Distributed User Interest Context for Generative Recommendation
**Authors:** Ruizhong Qiu, Yinglong Xia, Dongqi Fu, Hanqing Zeng, Ren Chen, Xiangjun Fan, Hong Li, Hong Yan, Hanghang Tong
**Link:** https://arxiv.org/abs/2606.20554v1
**Summary:** The paper addresses the challenge of integrating complex user behaviors and item semantics in generative recommendation systems, which often struggle with scalability and representation accuracy. The authors propose G2Rec, a scalable framework that combines holistic graph-based user co-engagement modeling with semantic tokenization, allowing for improved modeling of user interests without needing explicit ground-truth data. The results show that G2Rec outperforms existing methods in generating more comprehensive and accurate recommendations in real-world applications.

### 5. The Token Is a Group Element: On Lie-Algebra Attention over Matrix Lie Groups
**Authors:** Przemyslaw Musialski
**Link:** https://arxiv.org/abs/2606.20547v1
**Summary:** This paper introduces a novel attention mechanism called Lie-Algebra Attention, where the tokens are elements of matrix Lie groups, providing a mathematical framework to process transformations without relying on traditional representation-theoretic approaches. The authors demonstrate that this method achieves an intrinsic, canonical measure of similarity between group elements using a closed-form formula, significantly enhancing performance in sequence-completion tasks on various group types while using far fewer parameters than existing vector-token methods. By effectively addressing the limitations of prior attention mechanisms, this work expands the applicability of attention models to complex group structures, including non-compact affine groups.

### 6. Predictability as a Fine-Grained Measure for Privacy
**Authors:** Linda Lu, Karthik Sridharan
**Link:** https://arxiv.org/abs/2606.20546v1
**Summary:** The paper addresses the challenge of balancing individual privacy and data accuracy in differential privacy (DP) by introducing a new framework called "privacy via predictability." This framework measures privacy leakage based on the attacker's knowledge and the data they have while also being specifically tailored to different types of sensitive information and attacker models. A key contribution is the development of a predictability-calibrated output perturbation scheme, which offers a finer-grained privacy measure that can complement traditional DP methods.

### 7. Toward Calibrated Mixture-of-Experts Under Distribution Shift
**Authors:** Gina Wong, Drew Prinster, Suchi Saria, Rama Chellappa, Anqi Liu
**Link:** https://arxiv.org/abs/2606.20544v1
**Summary:** This paper addresses the challenge of ensuring that mixture-of-experts models remain well-calibrated when faced with changes in data distributions. The authors analyze how different routing strategies affect the calibration of these models and propose a new method that penalizes calibration errors in the overall model. Their key finding is that this adversarial reweighting approach significantly enhances the balance between accuracy and calibration performance, especially in difficult scenarios.

### 8. Multi-Task Bayesian In-Context Learning
**Authors:** Qingyang Zhu, Eric Karl Oermann, Kyunghyun Cho
**Link:** https://arxiv.org/abs/2606.20538v1
**Summary:** The paper addresses the challenge of making Bayesian predictive inference more efficient and adaptable, especially when dealing with shifting data distributions. The authors propose a multi-task in-context learning framework using a transformer that learns to incorporate prior information directly into its predictions. This approach achieves performance comparable to traditional Bayesian methods while being significantly faster, demonstrating its effectiveness on complex tasks like spatiotemporal temperature prediction.

### 9. Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving
**Authors:** Liang Su
**Link:** https://arxiv.org/abs/2606.20537v1
**Summary:** The paper addresses the challenge of low-latency, small-batch serving of large language models (LLMs) on devices, which is crucial for interactive applications like speech systems and robotics that require quick responsiveness. The authors propose a novel approach called execution-state capsules, which allow for complete restoration of the entire execution state at designated checkpoints, facilitating efficient state management. Key results show that this method achieves sub-millisecond snapshot and restore times on GPUs, significantly improving performance over traditional key-value cache methods, especially as input sizes increase.

### 10. How Do Instructions Shape Speech? Cross-Attention Attribution for Style-Captioned Text-to-Speech
**Authors:** Nityanand Mathur, Hamees Sayed, Wasim Madha, Apoorv Singh, Sameer Khurana, Akshat Mandloi, Sudarshan Kamath
**Link:** https://arxiv.org/abs/2606.20532v1
**Summary:** The paper addresses the challenge of understanding how specific words in style-captioned text influence the acoustic output in text-to-speech (TTS) systems. The authors introduce a novel method called cross-attention attribution, tailored for speech diffusion models, which analyzes the impact of style and content tokens on voice characteristics. Key findings reveal that style tokens significantly shape the waveform and are most influential early in the generation process, providing insights into improving TTS controllability.
