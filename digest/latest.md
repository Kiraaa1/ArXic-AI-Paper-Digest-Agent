---
## 2026-05-29

### 1. Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
**Authors:** Nhat-Minh Nguyen
**Link:** https://arxiv.org/abs/2605.30353v1
**Summary:** This study investigates the effectiveness of an AI coding agent, supervised by a physicist, in developing a scientific software module for perturbation theory. Over 12 days, the AI was able to autonomously handle many tasks but struggled with critical physics insights and misidentified problems, highlighting that the supervision and design of the collaboration are more crucial than the AI's capabilities alone. The findings suggest that future AI systems need to improve in proposing new solutions rather than just optimizing existing ones to achieve trustworthy scientific results.

### 2. VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion
**Authors:** Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Hoda Eldardiry, Pinar Yanardag
**Link:** https://arxiv.org/abs/2605.30351v1
**Summary:** The paper addresses the high memory and latency demands of long-rollout causal video diffusion by introducing VideoMLA, which replaces traditional per-head key-value (KV) memory with a shared low-rank latent representation. This innovative approach reduces memory usage by 92.7% while maintaining quality, even in scenarios where typical assumptions about the low-rank nature of video attention do not apply. As a result, VideoMLA achieves enhanced performance and 1.23 times higher throughput in streaming video diffusion compared to existing methods.

### 3. DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
**Authors:** Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
**Link:** https://arxiv.org/abs/2605.30350v1
**Summary:** The paper presents DynaFLIP, a new framework aimed at improving robot manipulation by enhancing perception through a dynamics-aware multimodal pre-training process. By utilizing image-language-3D flow triplets from various videos, the approach effectively aligns different modalities to focus on motion understanding, leading to better representations for robotic tasks. The key finding is that this method significantly enhances performance—up to 22.5% in out-of-distribution scenarios—by training visual models to not only recognize static objects but also understand how they change with actions.

### 4. LLMSurgeon: Diagnosing Data Mixture of Large Language Models
**Authors:** Yaxin Luo, Jiacheng Cui, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen
**Link:** https://arxiv.org/abs/2605.30348v1
**Summary:** The paper addresses the challenge of understanding the data composition that shapes the behaviors of Large Language Models (LLMs), which is often undisclosed and difficult to audit. It introduces LLMSurgeon, a framework that estimates the distribution of pretraining data domains by leveraging generated text from the model and uses an innovative method to recover the underlying data mixture. The key contribution is the ability to accurately assess domain mixtures through a verifiable evaluation suite, enhancing post-hoc auditing of foundation models without needing direct access to their training data.

### 5. SchGen: PCB Schematic Generation with Semantic-Grounded Code Representations
**Authors:** Qinpei Luo, Ruichun Ma, Xinyu Zhang, Lili Qiu
**Link:** https://arxiv.org/abs/2605.30345v1
**Summary:** The paper introduces SchGen, the first large language model designed to automatically generate editable PCB schematics from natural language descriptions, addressing the traditionally manual and expertise-heavy process of PCB design. It tackles the challenge of complex schematic representations by utilizing a semantically grounded code format that simplifies the generation task for the AI. The results show that SchGen significantly outperforms existing methods in terms of wire connectivity and functional correctness, emphasizing the importance of effective representation in hardware design automation.

### 6. Tiny but Trusted: Efficient Vision-Language Reasoning for Time-Series Anomaly Detection
**Authors:** Xiaona Zhou, Muntasir Wahed, Tianjiao Yu, Constantin Brif, Ismini Lourentzou
**Link:** https://arxiv.org/abs/2605.30344v1
**Summary:** The paper addresses the challenge of detecting anomalies in time-series data using Vision-Language Models (VLMs), which have struggled with this task due to a lack of interpretability and training data. The authors introduce a new benchmark, VisAnomBench, that includes high-quality anomaly explanations, and develop a parameter-efficient VLM called VisAnomReasoner, which is fine-tuned on this benchmark. Results show that VisAnomReasoner significantly outperforms prior methods in precision and F1 score, indicating improved anomaly localization and generalization across different datasets.

### 7. Unlocking the Working Memory of Large Language Models for Latent Reasoning
**Authors:** Lukas Aichberger, Sepp Hochreiter
**Link:** https://arxiv.org/abs/2605.30343v1
**Summary:** The paper addresses the challenge of enhancing reasoning capabilities in large language models by moving away from the traditional autoregressive generation of reasoning steps. Instead, it introduces a method called Reasoning in Memory (RiM), which utilizes fixed memory blocks to enable efficient internal manipulation of information without externalizing intermediate thoughts. The key finding is that RiM outperforms or matches existing methods in reasoning tasks while requiring significantly less computational effort.

### 8. GPIC: A Giant Permissive Image Corpus for Visual Generation
**Authors:** Keshigeyan Chandrasegaran, Kyle Sargent, Suchir Agarwal, Michael Jang, Michael Poli, Juan Carlos Niebles, Justin Johnson, Jiajun Wu, Li Fei-Fei
**Link:** https://arxiv.org/abs/2605.30341v1
**Summary:** The paper introduces GPIC, a large and accessible image dataset of approximately 28 trillion pixels aimed at advancing visual generative modeling. It includes a diverse collection of internet images, all permissively licensed for various uses, and comes with a benchmarking protocol and a baseline model for evaluating generative methods. GPIC is hosted on Hugging Face and is designed to support research and development in scalable visual generation.

### 9. Efficient Test-Time Finetuning of LLMs via Convex Reconstruction and Gradient Caching
**Authors:** Alaa Khamis, Alaa Maalouf
**Link:** https://arxiv.org/abs/2605.30337v1
**Summary:** The paper addresses the challenge of making test-time finetuning (TTFT) of language models efficient, as existing methods often sacrifice speed for quality. The authors introduce HullFT, a method that uses a geometric approach to select relevant training sequences efficiently and employs techniques to optimize computation time. Their results demonstrate that HullFT provides a better balance between the quality of model adaptation and the speed of processing, leading to improved performance compared to current TTFT methods.

### 10. Fairness-Aware Federated Learning with Trajectory Shapley Value
**Authors:** Daniel Kuznetsov, Ziqi Wang
**Link:** https://arxiv.org/abs/2605.30336v1
**Summary:** The paper addresses the problem of biased and unstable learning in federated learning caused by fixed client contribution weights. The authors propose the Trajectory Shapley Value (TSV) to evaluate each client's influence on the model's optimization process and develop FedTSV, an adaptive aggregation method that adjusts client weights dynamically based on their contributions. Key results show that FedTSV accelerates convergence, enhances robustness, and provides fairer assessments of client contributions, improving the overall fairness of federated optimization.
