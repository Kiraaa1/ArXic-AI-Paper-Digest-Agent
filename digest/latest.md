---
## 2026-07-09

### 1. Accurate, Interdisciplinary and Transparent Structure-property Understanding with Deep Native Structural Reasoning
**Authors:** Chen Tang, Yizhou Wang, Jianyu Wu, Lintao Wang, Shixiang Tang, Pengze Li, Encheng Su, Jun Yao, Jiabei Xiao, Yuqi Shi, Jielan Li, Hongxia Hao, Zhangyang Gao, Fang Wu, Ben Fei, Xiangyu Yue, Pan Tan, Bozitao Zhong, Jinouwen Zhang, Aoran Wang, Yan Lu, Jiaheng Liu, Xinzhu Ma, Liang Hong, Mingyue Zheng, Phil Torr, Bowen Zhou, Wanli Ouyang, Lei Bai
**Link:** https://arxiv.org/abs/2607.07708v1
**Summary:** The paper addresses the challenge of understanding structure-property relationships in scientific fields by introducing SciReasoner, a multimodal AI model that maintains native structural information during reasoning. SciReasoner improves predictions in protein annotation, chemical retrosynthesis, and materials science by converting structural data into a unified format that enhances interpretability and accuracy. The model achieves state-of-the-art results across 86 benchmarks, demonstrating that it provides both accurate predictions and interpretable reasoning, thus bridging the gap between AI applications and scientific inference.

### 2. Co-LMLM: Continuous-Query Limited Memory Language Models
**Authors:** Yair Feldman, Linxi Zhao, Nathan Godey, Dongyoung Go, Yilun Hua, Kilian Q. Weinberger, Jennifer J. Sun, Yoav Artzi
**Link:** https://arxiv.org/abs/2607.07707v1
**Summary:** The paper presents Co-LMLM, a novel approach to limited memory language models that enhances knowledge retrieval by using continuous vector queries instead of traditional relational databases. This method allows the model to efficiently access and incorporate factual information from various text sources, surpassing previous models in both perplexity and factual accuracy. Notably, Co-LMLM at 360M parameters outperforms larger models trained on significantly more data, achieving competitive performance comparable to leading systems like GPT-4o-mini.

### 3. The Key to Going Linear: Analysis-Driven Transformer Linearization
**Authors:** Anna Kuzina, Paul N. Whatmough, Babak Ehteshami Bejnordi
**Link:** https://arxiv.org/abs/2607.07706v1
**Summary:** This paper addresses the challenge of computationally expensive causal self-attention in transformers when processing long-context inputs. The authors analyze the impact of different state update designs and propose structural modifications, such as sink tokens and short convolutions, to enhance performance. Their linearization method significantly improves efficiency in LLaMA and Qwen models, outperforming previous approaches while maintaining strong retrieval capabilities for long contexts.

### 4. From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal Extraction for Agent Optimization
**Authors:** Ying Chang, Jiahang Xu, Xuan Feng, Chenyuan Yang, Peng Cheng, Yuqing Yang
**Link:** https://arxiv.org/abs/2607.07702v1
**Summary:** The paper addresses the challenge of optimizing long-horizon agents using execution traces, which are often noisy and inefficient due to redundancy and irrelevant steps. The authors propose STRACE, a framework that improves optimization by identifying and focusing on crucial failure patterns and causal relationships within the traces. Their approach significantly enhances optimization performance, achieving a 1.4 times increase in success rates for agents tested on a formal verification task.

### 5. Breaking Database Lock-in: Agentic Regeneration of High Performance Storage Readers for Database Bypass
**Authors:** Victor Giannakouris, Immanuel Trummer
**Link:** https://arxiv.org/abs/2607.07696v1
**Summary:** The paper addresses the issue of slow data access in analytical workloads that rely on external database systems, which are hampered by traditional database drivers. The authors present Jailbreak, a method that uses Large Language Models (LLMs) to directly read data files and create efficient in-memory columnar buffers, bypassing the database engine entirely. The key contribution is demonstrating that this LLM-assisted approach can significantly enhance analytical performance, achieving up to 27 times faster throughput compared to conventional JDBC/ODBC methods.

### 6. Institutional Red-Teaming: Deployment Rules, Not Just Models, Causally Shape Multi-Agent AI Safety
**Authors:** Yujiao Chen
**Link:** https://arxiv.org/abs/2607.07695v1
**Summary:** The paper addresses the challenge of ensuring safety in multi-agent AI systems by evaluating how different deployment rules influence collective behavior. The authors introduce "institutional red-teaming," a method that systematically tests these rules across various scenarios and models, revealing that specific rules can significantly impact collective safety, with no universally safe choice available. Key findings indicate that identity-targeting rules are particularly harmful, often leading to targeted agent elimination, emphasizing the need for careful selection and monitoring of deployment rules to mitigate risks.

### 7. Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF
**Authors:** Eric Zhu, Abhinav Shrivastava, Soumik Mukhopadhyay
**Link:** https://arxiv.org/abs/2607.07693v1
**Summary:** This paper addresses the inefficiency of reinforcement learning from human feedback (RLHF) when applied to diffusion models, which often require excessive human evaluations. The authors propose two strategies: selective weighting of denoising timesteps during optimization and a replay mechanism that prioritizes informative trajectories. Their approach enhances feedback efficiency significantly, achieving up to a 6-fold improvement in sample efficiency compared to standard diffusion RLHF methods.

### 8. Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning
**Authors:** Vladislav Beliaev
**Link:** https://arxiv.org/abs/2607.07690v1
**Summary:** The paper introduces Agon, a new approach to reinforcement learning that uses two competing models to implicitly evaluate each other's reasoning while solving problems, rather than only focusing on the final answers. By alternating roles—one model drafting a solution and the other reading it—the models are trained to out-reason each other, leading to improved performance. The key result shows that this method significantly increases the accuracy of problem-solving, achieving notable gains on complex tasks compared to existing models.

### 9. ECGLight: Compute-Light Framework For Paper ECG Digitization and Myocardial Infarction Screening
**Authors:** Shreyasvi Natraj, Cyrus Achtari, Felice Gragnano, Andrea Milzi, Marco Valgimigli, Diego Paez-Granados
**Link:** https://arxiv.org/abs/2607.07683v1
**Summary:** The paper addresses the challenge of digitizing paper electrocardiograms (ECGs) in remote clinics, where limited connectivity and computing power hinder access to advanced AI diagnostics. The authors introduced ECGLight, a lightweight framework that converts images of paper ECGs into calibrated digital signals and screens for myocardial infarction (MI) using efficient on-device processing. The system achieves high accuracy rates, detecting MI with 95.51% accuracy on one dataset and 88.89% on another, demonstrating its potential to improve cardiac care in resource-limited settings.

### 10. Neural Operator-enabled Topology-informed Evolutionary Strategy for PDE-Constrained Optimization
**Authors:** Xiangming Huang, Guannan Zhang, Lu Lu, Raphaël Pestourie
**Link:** https://arxiv.org/abs/2607.07682v1
**Summary:** The paper addresses the challenging problem of inverse design for physical systems described by partial differential equations, which are often complex and high-dimensional. The authors propose a new method called Neural Operator-enabled Topology-informed Evolutionary Strategy (NOTES), which combines advanced learning techniques and evolutionary optimization to efficiently explore design spaces. Their approach significantly reduces the dimensionality of designs while achieving high performance, demonstrating superior efficiency compared to traditional methods in applications like nanophotonic beam deflectors and structural optimization.
