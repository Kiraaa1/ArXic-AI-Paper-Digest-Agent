---
## 2026-07-10

### 1. UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks
**Authors:** Zhekai Chen, Chengqi Duan, Kaiyue Sun, Bohao Li, Yuqing Wang, Manyuan Zhang, Xihui Liu
**Link:** https://arxiv.org/abs/2607.08768v1
**Summary:** The paper introduces UniClawBench, a new benchmark designed to evaluate proactive agents in real-world tasks by focusing on five core capabilities rather than relying on traditional, static testing methods. It proposes a dynamic evaluation setup with 400 bilingual tasks and live assessment in Docker containers, allowing for a more nuanced understanding of agent performance. The benchmark's innovative design helps isolate the effects of model capabilities and framework choices, contributing valuable insights for future research in developing capable proactive agents.

### 2. OpenCoF: Learning to Reason Through Video Generation
**Authors:** Xinyan Chen, Ziyu Guo, Renrui Zhang, Dongzhi Jiang, Hongsheng Li
**Link:** https://arxiv.org/abs/2607.08763v1
**Summary:** The paper presents OpenCoF, a new framework designed to enhance reasoning in video generation models by introducing a dedicated dataset and a fine-tuned model. Unlike traditional reasoning methods, OpenCoF uses temporally connected frames to improve performance in video reasoning tasks. The key contribution is the demonstration that incorporating diverse temporal supervision and specific mechanisms for organizing reasoning significantly boosts the model's reasoning capabilities across various benchmarks.

### 3. Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation
**Authors:** Yifan Zhou, Qihao Yang, Yan Li, Donggang Li, Xiru Hu, Hokin Deng, Ziyang Gong, Xuanyi Zhou, Huacan Wang, Xiangchao Yan, Wanghan Xu, Wenlong Zhang, Shaofeng Zhang, Yue Zhou, Yifan Yang, Zhihang Zhong, Xue Yang
**Link:** https://arxiv.org/abs/2607.08758v1
**Summary:** The paper addresses the challenge of evaluating AI systems' ability to understand and generate scientific ideas based on their historical lineage, akin to biological evolution. The authors introduce IdeaGene-Bench (IG-Bench), a benchmark that models scientific contributions as "Idea Genome" objects, allowing for the assessment of both lineage reasoning and idea generation. Key findings reveal that current large language models struggle with this task, achieving only 27.3% accuracy in lineage reasoning, highlighting limitations in their compositional understanding.

### 4. Score Accuracy Along the Forward Diffusion Does Not Certify Numerical Stability in Diffusion Sampling
**Authors:** Yiwei Zhou
**Link:** https://arxiv.org/abs/2607.08757v1
**Summary:** The paper addresses the issue that achieving low average error in the forward distribution of diffusion models does not guarantee stable sampling in the reverse process, particularly through numerical methods like Euler–Maruyama discretization. The authors construct examples demonstrating that despite small forward errors, the reverse process can still exhibit divergent moments. Additionally, they introduce a method to project learned denoisers onto bounded convex sets to ensure better numerical stability and Wasserstein convergence while maintaining pointwise accuracy.

### 5. MulTTiPop: A Multitrack Transcription Dataset for Pop Music
**Authors:** Nathan Pruyne, Benjamin Stoler, William Chen, Chien-yu Huang, Shinji Watanabe, Chris Donahue
**Link:** https://arxiv.org/abs/2607.08756v1
**Summary:** The paper presents MulTTiPop, a new dataset designed to improve automatic music transcription for pop music by providing 572 audio segments paired with multitrack MIDI recordings. The dataset was created through a meticulous process of matching audio with MIDI, ensuring accurate timing and tempo alignment. Evaluation of existing transcription models on this dataset reveals significant challenges, with the top-performing model achieving only 38% Onset F1, indicating that there is much potential for advancements in this area.

### 6. SLORR: Simple and Efficient In-Training Low-Rank Regularization
**Authors:** David González-Martínez, Shiwei Liu
**Link:** https://arxiv.org/abs/2607.08754v1
**Summary:** The paper presents SLORR, a new framework for low-rank regularization during training of neural networks, addressing issues with existing methods that are complex or require significant changes to the model. SLORR simplifies the process by applying stateless regularization directly to weight matrices using efficient approximations, allowing for better model compressibility with minimal training overhead. The key finding is that SLORR enables compressed models to maintain high performance with significantly less than 1% additional training cost in various neural network settings.

### 7. Using AI-based Learning Assistants in Higher Education: A Large-Scale Descriptive Analysis
**Authors:** Kristina Schaaff, Quintus Stierstorfer, Valerie Heckel
**Link:** https://arxiv.org/abs/2607.08748v1
**Summary:** This study investigates how an AI-based learning assistant, Syntea, is used by a large number of students in higher education, analyzing data from over 77,000 distance learners. Unlike previous research that relied on small sample sizes and self-reports, this analysis provides insights into actual usage patterns based on objective data, revealing significant differences in usage across various demographic and structural factors. The findings highlight the incorporation of AI support into student routines and offer valuable information for enhancing educational chatbot development.

### 8. Dimensionality Reduction Meets Network Science: Sensemaking on UMAP's kNN Graph
**Authors:** Duen Horng Chau, Donghao Ren, Fred Hohman, Dominik Moritz
**Link:** https://arxiv.org/abs/2607.08746v1
**Summary:** The paper addresses the underutilization of UMAP's internal k-nearest-neighbor (kNN) graph in analyzing high-dimensional data. By applying standard graph algorithms to this graph, the authors reveal insights such as representative data points, dense regions, and tightly-knit neighborhoods. Their findings demonstrate that these graph-based methods can effectively enhance data analysis, often matching or complementing existing clustering techniques.

### 9. AUTOPILOT VQA: Benchmarking Vision-Language Models for Incident-Centric Dashcam Understanding
**Authors:** Siddharth Damodharan, Radhika Gupta, Ali Alshami, Ryan Rabinowitz, Jugal Kalita
**Link:** https://arxiv.org/abs/2607.08745v1
**Summary:** The paper introduces AUTOPILOT-VQA, a benchmark designed to evaluate Vision-Language Models in understanding dashcam videos of driving incidents. It addresses the challenge of assessing how well these models can reason about safety-critical scenarios by providing a dataset with structured questions related to real-world driving conditions and incidents. The benchmark enhances the evaluation of autonomous driving systems by shifting focus from simple object recognition to complex, context-aware reasoning about driving safety.

### 10. ARDY: Autoregressive Diffusion with Hybrid Representation for Interactive Human Motion Generation
**Authors:** Kaifeng Zhao, Mathis Petrovich, Haotian Zhang, Tingwu Wang, Siyu Tang, Davis Rempe
**Link:** https://arxiv.org/abs/2607.08741v1
**Summary:** The paper presents ARDY, a new framework for generating realistic 3D human motions in real-time for interactive applications, addressing the limitations of both offline and existing online methods in terms of speed and control. ARDY combines explicit and latent representations to allow for high-fidelity motion generation that can be dynamically controlled using text prompts and kinematic constraints. The key contribution is a two-stage autoregressive transformer that efficiently supports extended context and adaptive goal-setting, leading to impressive motion quality and adherence to user-defined constraints, as demonstrated through extensive evaluations and an interactive demo.
