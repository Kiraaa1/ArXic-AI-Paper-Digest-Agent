---
## 2026-06-21

### 1. FreeStyle: Free Control of Style-Content Dual-Reference Generation from Community LoRA Mining
**Authors:** Jinghong Lan, Wei Cheng, Yunuo Chen, Ziqi Ye, Peng Xing, Yixiao Fang, Rui Wang, Yufeng Yang, Xuanyang Zhang, Xianfang Zeng, Difan Zou, Gang Yu, Chi Zhang
**Link:** https://arxiv.org/abs/2606.20506v1
**Summary:** The paper addresses the challenge of generating images that maintain the structure of a content reference while adopting the style of a separate style reference, which is difficult due to potential semantic leakage. The authors introduce FreeStyle, a scalable framework that uses community-generated Low-Rank Adaptations (LoRAs) to create a large dataset of style and content reference triplets, and implement sophisticated mechanisms to prevent content leakage during generation. Their extensive evaluation shows that FreeStyle effectively balances style alignment, content preservation, and leakage suppression, marking an advancement in dual-reference image synthesis.

### 2. Entropy Estimation in Multi-Qutrit Systems via Variational and Classical Neural Networks
**Authors:** Sai Sakunthala Guddanti, Anil Prabhakar, Ria Rushin Joseph
**Link:** https://arxiv.org/abs/2606.20504v1
**Summary:** This paper addresses the challenge of estimating von Neumann entropy in multi-qutrit quantum systems using two methods: variational quantum algorithms and classical convolutional neural networks (CNNs). The authors find that while VQAs are effective for small systems (up to three qutrits), CNNs significantly improve performance and scalability for larger systems (up to five qutrits), achieving high accuracy with fewer measurements. Specifically, the CNN model can provide accurate entropy estimates with only a fraction of the measurements typically needed, demonstrating robustness against noise and generalization to various quantum states.

### 3. Calibration Without Comprehension: Diagnosing the Limits of Fine-Tuning LLMs for Vulnerability Detection in Systems Software
**Authors:** Arastoo Zibaeirad, Marco Vieira
**Link:** https://arxiv.org/abs/2606.20502v1
**Summary:** The paper addresses the reliability of large language models (LLMs) in detecting vulnerabilities in systems software, questioning whether they genuinely understand security concepts or simply match patterns from flawed training data. The authors introduce CWE-Trace, a framework that evaluates various LLMs on their ability to detect vulnerabilities, using a carefully curated dataset and two novel diagnostic metrics. The key finding reveals that while fine-tuning improves detection thresholds, it does not enhance the models' actual understanding of security, as evidenced by significant misclassifications and low overall detection accuracy.

### 4. Contagion Networks: Evaluator Bias Propagation in Multi-Agent LLM Systems
**Authors:** Zewen Liu
**Link:** https://arxiv.org/abs/2606.20493v1
**Summary:** This paper addresses the issue of evaluator biases in multi-agent systems where large language models (LLMs) serve as evaluators, leading to the propagation of these biases among agents. The authors introduce the Contagion Networks framework to measure the spread of biases and conduct experiments that show biases can propagate consistently between agents. A key finding is that increasing the size of the evaluator committee can significantly reduce bias contagion, offering a practical strategy for mitigation.

### 5. Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems
**Authors:** Shu Yao, Yuhua Luo, Qian Long, Jingru Fan, Zhuoyuan Yu, Yuheng Wang, Lin Wu, Yufan Dang, Huatao Li, Chen Qian
**Link:** https://arxiv.org/abs/2606.20487v1
**Summary:** The paper addresses the challenge of efficiently handling task execution failures in multi-device agent systems, which often involve coordinating different applications and devices. The authors propose a framework called H-RePlan that separates local recovery strategies from overall global replanning, allowing devices to dynamically adapt their execution without needing to reevaluate the entire plan. Their experiments show that H-RePlan significantly improves task completion rates and reliability compared to existing methods, highlighting the importance of a hierarchical approach to recovery in such systems.

### 6. Optimal Order of Multi-Agent and General Many-Body Systems
**Authors:** Jake J. Xia
**Link:** https://arxiv.org/abs/2606.20485v1
**Summary:** This paper addresses the challenge of optimizing multi-agent systems by analyzing how individual agent behaviors influence collective outcomes. The authors introduce a framework based on agent power and response functions, revealing a trade-off between productivity and resilience. A key finding is that while synchronization can boost collective performance, it may also heighten systemic fragility, emphasizing that optimal order in these systems is both task-dependent and context-specific.

### 7. Your Mouse and Eyes Secretly Leak Your Preference: LLM Alignment using Implicit Feedback from Users
**Authors:** Haw-Shiuan Chang, Jeffrey Gomez, Mehul Patwari, Aryan Sajith, Hamed Zamani
**Link:** https://arxiv.org/abs/2606.20482v1
**Summary:** The paper addresses the challenge of aligning Large Language Models (LLMs) by moving beyond traditional methods that rely on explicit human feedback, which is often scarce and expensive to gather. It introduces a novel dataset, IFLLM, which includes user mouse movements and eye tracking data as implicit feedback to improve LLM response quality. The key finding is that this implicit feedback significantly enhances the performance of a reward model, increasing accuracy from 55% to 64% and leading to substantial improvements in the quality of LLM responses.

### 8. Scalable Training of Spatially Grounded 2D Vision-Language Models for Radiology
**Authors:** Yusuf Salcan, Simon Ging, Robin Schirrmeister, Philipp Arnold, Elmar Kotter, Behzad Bozorgtabar, Thomas Brox
**Link:** https://arxiv.org/abs/2606.20477v1
**Summary:** The paper addresses the challenge of training vision-language models for radiology without requiring manual spatial annotations. The authors introduce RefRad2D, a large dataset of CT and MR image-text pairs, and develop RadGrounder, a model capable of report generation, visual question answering, and spatial grounding. Key results show that RadGrounder performs competitively with specialized models and that including their dataset improves performance without compromising language quality.

### 9. Marginal Advantage Accumulation for Memory-Driven Agent Self-Evolution
**Authors:** Mingyu Yang, Keye Zheng, Congchao Cheng, Yujie Liu, Xingkang Lu, Fan Jiang, Yefei Zheng
**Link:** https://arxiv.org/abs/2606.20475v1
**Summary:** The paper addresses the issue of inconsistent feedback received by memory operations during batch-style trace distillation, which makes it difficult to identify effective operations. The authors introduce Marginal Advantage Accumulation (MAA), a method that accumulates evidence for operations across batches and enhances comparability of feedback. The key contribution is that MAA significantly outperforms existing methods in most scenarios tested, while also reducing the resources needed for optimization by about 75%.

### 10. UltraQuant: 4-bit KV Caching for Context-Heavy Agents
**Authors:** Inesh Chakrabarti, David Limpus, Aditi Ghai Rana, Bowen Bao, Spandan Tiwari, Thiago Crepaldi, Ashish Sirasao
**Link:** https://arxiv.org/abs/2606.20474v1
**Summary:** The paper addresses the challenge of efficiently managing key-value (KV) caches in context-heavy agent workloads, which often reuse long prefixes and require high concurrency for GPU utilization. The authors propose a novel 4-bit KV caching method called UltraQuant, integrating advanced techniques like codebook quantization and optimized kernel design, resulting in a significant performance improvement. Specifically, UltraQuant reduces the time to first token by 3.47 times in late cache-pressured rounds and increases output throughput by 1.63 times compared to the FP8 KV baseline.
