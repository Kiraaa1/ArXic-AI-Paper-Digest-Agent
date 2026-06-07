---
## 2026-06-07

### 1. MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery
**Authors:** Shangheng Du, Xiangchao Yan, Jinxin Shi, Zongsheng Cao, Shiyang Feng, Zichen Liang, Boyuan Sun, Tianshuo Peng, Yifan Zhou, Xin Li, Jie Zhou, Liang He, Bo Zhang, Lei Bai
**Link:** https://arxiv.org/abs/2606.06473v1
**Summary:** MLEvolve addresses the challenges faced by existing machine learning engineering agents, such as information isolation and lack of memory, which hinder long-term optimization. It introduces a self-evolving multi-agent framework that enhances algorithm discovery by enabling information sharing and adapting its search strategy over time. The framework achieved state-of-the-art results in automated algorithm discovery tasks, significantly outperforming specialized methods like AlphaEvolve within a reduced runtime.

### 2. PC Layer: Polynomial Weight Preconditioning for Improving LLM Pre-Training
**Authors:** Senmiao Wang, Tiantian Fang, Haoran Zhang, Yushun Zhang, Kunxiang Zhao, Alex Schwing, Ruoyu Sun
**Link:** https://arxiv.org/abs/2606.06470v1
**Summary:** The paper addresses the issue of unstable weight conditioning during the pre-training of large language models (LLMs). The authors introduce a PC layer that utilizes a polynomial preconditioning technique to reshape the singular value spectrum of weight matrices, ensuring stability in training without adding inference costs. They demonstrate that this approach improves the training efficiency of models like Llama-1B, significantly enhancing convergence using standard optimizers.

### 3. How abundant are good interpolators?
**Authors:** August Y. Chen, Ahmed El Alaoui
**Link:** https://arxiv.org/abs/2606.06469v1
**Summary:** This paper investigates the abundance and performance of linear classifiers that perfectly classify labeled datasets, focusing on the generalization error of these classifiers under specific data distributions. By analyzing the distribution of points within the set of successful classifiers, the authors establish a large deviation principle that characterizes the generalization performance of these classifiers. The key finding is that, in the overparametrized regime, most interpolating classifiers have similar performance, while gradient descent and a natural linear programming approach significantly outperform the majority of these classifiers, highlighting a beneficial form of overfitting.

### 4. Goedel-Architect: Streamlining Formal Theorem Proving with Blueprint Generation and Refinement
**Authors:** Jui-Hui Chung, Ziyang Cai, Zihao Li, Qishuo Yin, Rohit Agarwal, Simon Park, Rodrigo Porto, Narutatsu Ri, Ziran Yang, Shange Tang, Xingyu Dang, Hongzhou Lin, Mengdi Wang, Danqi Chen, Chi Jin, Liam H Fowl, Sanjeev Arora
**Link:** https://arxiv.org/abs/2606.06468v1
**Summary:** Goedel-Architect addresses the challenges of formal theorem proving by introducing a framework that generates and refines blueprints—a structured dependency graph of definitions and lemmas leading to a theorem. By combining automatic blueprint generation with a Lean prover that closes lemmas in parallel, the framework enhances efficiency compared to traditional methods. The key contribution is achieving state-of-the-art performance on various theorem proving benchmarks, demonstrating a significant improvement while being cost-effective relative to existing solutions.

### 5. You Only Index Once: Cross-Layer Sparse Attention with Shared Routing
**Authors:** Yutao Sun, Yanqi Zhang, Li Dong, Jianyong Wang, Furu Wei
**Link:** https://arxiv.org/abs/2606.06467v1
**Summary:** The paper addresses the challenge of improving the decoding efficiency of large language models (LLMs) during long-context inference, which is often hindered by existing sparse attention methods. It introduces a novel cross-layer sparse attention (CLSA) approach that shares both the key-value cache and the routing index across decoder layers, thus retaining the precision of token selection while reducing overhead. This method significantly enhances inference speed, achieving up to 7.6 times faster decoding and 17.1 times improved overall throughput for long-context tasks.

### 6. Human Adults and LLMs as Scientists: Who Benefits from Active Exploration?
**Authors:** Mandana Samiei, Eunice Yiu, Anthony GX-Chen, Dongyan Lin, Jocelyn Shen, Blake A. Richards, Alison Gopnik, Doina Precup
**Link:** https://arxiv.org/abs/2606.06464v1
**Summary:** This paper investigates whether allowing adults to actively explore can help them better identify complex causal rules (conjunctive rules) compared to passive observation, where they typically struggle. Using a modified task, the authors found that active exploration significantly enhances adults' ability to recognize these rules, although they still require more trials than simpler rules (disjunctive rules). The study also compares human performance to various large language models, revealing that while some models perform well, they tend to use less effective exploration strategies and show similar difficulties with conjunctive rules.

### 7. Benchmark Everything Everywhere All at Once
**Authors:** Shiyun Xiong, Dongming Wu, Peiwen Sun, Yuang Ai, Bokang Yang, Wencheng Han, Xiao-Hui Li, Xiangyu Yue
**Link:** https://arxiv.org/abs/2606.06462v1
**Summary:** The paper addresses the challenges of constructing benchmarks for evaluating large language models (LLMs) and multimodal language models (MLLMs), which are often labor-intensive and quickly become outdated. To tackle this, the authors introduce Benchmark Agent, an autonomous system that automates the entire benchmark creation process. Their experiments show that Benchmark Agent can generate high-quality benchmarks across various evaluation scenarios with minimal human effort, revealing important insights about current model limitations in specific reasoning tasks.

### 8. Will the Agent Recuse Itself? Measuring LLM-Agent Compliance with In-Band Access-Deny Signals
**Authors:** Thamilvendhan Munirathinam
**Link:** https://arxiv.org/abs/2606.06460v1
**Summary:** The paper addresses the challenge of informing autonomous language model (LLM) agents that certain resources are off-limits, proposing a new method called the Recuse Signal. This approach involves implementing a lightweight in-band deny signal that prompts LLM agents to voluntarily withdraw from accessing restricted resources. The key finding from experiments is that when this signal is used, compliant agents demonstrate a 100% rate of recusal, while also revealing that the signal's effectiveness may be influenced by how agents perceive authorization.

### 9. Event Detection for Parameter-to-KPI Dependency Learning for AI-RAN
**Authors:** Christie Djidjev, Nicholas Kaminski
**Link:** https://arxiv.org/abs/2606.06459v1
**Summary:** The paper addresses the challenge of detecting meaningful interactions between control parameters and network performance in AI-integrated wireless networks, where such dependencies are often obscured by noise in telemetry data. The authors propose a machine-learning approach that converts continuous data into binary event indicators, helping to identify which parameters influence network outcomes. Their key finding is that the method can effectively recover these dependencies when the signal strength is adequately distinguishable from background noise, emphasizing the importance of proper threshold calibration for accurate event detection.

### 10. In-Context Multiple Instance Learning
**Authors:** Alexander Möllers, Marvin Sextro, Julius Hense, Gabriel Dernbach, Klaus-Robert Müller
**Link:** https://arxiv.org/abs/2606.06458v1
**Summary:** The paper addresses the challenge of Multiple Instance Learning (MIL) in low-label scenarios, where traditional algorithms struggle to adapt. The authors propose a novel approach using an in-context learner with a Perceiver-style architecture, pretrained on synthetic bag-structured data for improved task generalization. This method achieves superior performance across various MIL benchmarks by effectively combining strengths from different data generators, outperforming typical supervised models that need extensive task-specific training.
