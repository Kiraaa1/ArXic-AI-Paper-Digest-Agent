---
## 2026-10-01

### 1. Ranking-Aware Prompt Optimization for Multimodal Clinical Diagnosis
**Authors:** Tian Xia, Minghao Liu, Yiqing Liang, Laixi Shi, Jiayun Wang
**Link:** https://arxiv.org/abs/2609.40361v1
**Summary:** The paper addresses the challenge of adapting multimodal large language models for clinical diagnosis in the presence of class imbalance, where traditional accuracy metrics are misleading. The authors propose a novel prompt optimization method called Ranking-PE, which focuses on ranking capabilities by comparing pairs of instances rather than relying solely on accuracy. Their approach significantly improves AUROC scores by up to 16.2 percentage points compared to conventional methods, demonstrating its efficacy in enhancing multimodal clinical decision-making.

### 2. Semifactual Credit-Augmented Policy Optimization
**Authors:** Junshu Pan, Zhizhang Fu, Shulin Huang, Yiran Ding, Zifan Cheng, Wenqi Shao, Qiaosheng Zhang, Yue Zhang
**Link:** https://arxiv.org/abs/2609.40360v1
**Summary:** The paper addresses the problem of sensitivity in large language models' predictions to irrelevant features in prompts when using reinforcement learning with verifiable rewards. It introduces Semifactual Credit-Augmented Policy Optimization (SCAPO), a novel approach that improves token-level credit assignment by incorporating stability under controlled prompt interventions. The results show that SCAPO significantly enhances reasoning accuracy on mathematics and out-of-distribution benchmarks compared to traditional methods, demonstrating the effectiveness of using semifactual stability in training.

### 3. Removing Timing Shortcuts Improves Non-Invasive Brain-to-Text
**Authors:** Dulhan Jayalath, Oiwi Parker Jones
**Link:** https://arxiv.org/abs/2609.40359v1
**Summary:** This study addresses the issue of decoding words from non-invasive brain recordings, revealing that prior improvements in this area were partly due to leveraging timing information rather than actual brain signals. The authors propose a method called SimpleB2T, which processes each segment of brain data independently, leading to improved performance by focusing on the true neural information associated with words. As a result, their approach achieves a word error rate of 36.6%, nearing the effectiveness of invasive speech decoding methods.

### 4. ViTeX-Bench: Benchmarking High-Fidelity Video Scene Text Editing
**Authors:** Xinghao Chen, Xiangbo Gao, Jiongze Yu, Yuheng Wu, Zhengzhong Tu
**Link:** https://arxiv.org/abs/2609.40356v1
**Summary:** The paper addresses the challenge of editing text in videos while maintaining visual quality and the original scene's dynamics. To tackle this, the authors introduce ViTeX-Bench, a benchmark suite that includes a dataset of real-world videos and a comprehensive evaluation protocol to assess text correctness and editing quality. Their key contribution is the ViTeX-Edit-14B, an advanced video editor that outperforms other methods in accuracy and consistency, providing a foundation for further research in video scene text editing.

### 5. Image Classifiers are Efficient Self-Supervised Video Representation Learners
**Authors:** Owais Iqbal, Sudipta Sarkar, Shyam Marjit, Omprakash Chakraborty, Anirban Chakraborty, Abir Das
**Link:** https://arxiv.org/abs/2609.40347v1
**Summary:** The paper addresses the challenge of efficient self-supervised learning of video representations without relying on complex 3D architectures or reconstruction methods. The authors propose VideoMSN, a framework that uses standard image Vision Transformers to treat video data as grids of frames, applying spatial and temporal masking to learn effective representations. As a result, VideoMSN achieves state-of-the-art performance on benchmark datasets while significantly reducing the necessary pretraining time compared to existing methods.

### 6. EvoDuet: Bilevel Co-Evolution of Web Searching and Task Solving for Scientific Discovery
**Authors:** Young-Jun Lee, Jinheon Baek, Soyeong Jeong, Minki Kang, Seungyeon Jwa, Jonghyun Choi, Seungho Han, Dongyeop Kang
**Link:** https://arxiv.org/abs/2609.40340v1
**Summary:** EvoDuet addresses the challenge of enhancing the performance of large language models in evolutionary searches for scientific discovery, particularly when they encounter knowledge gaps. The approach involves co-evolving search queries and solutions through a bi-level optimization method that utilizes a retrieval mechanism to select relevant documents as needed. The key result shows that EvoDuet significantly improves discovery gains across various optimization tasks, surpassing previous benchmarks in several areas.

### 7. Is Weight Tying Still Beneficial for Decoder-Only LLMs in Private Settings Under DP-SGD?
**Authors:** Razan El Mais, Ali Chehab, Ibrahim Issa, Razane Tajeddine
**Link:** https://arxiv.org/abs/2609.40335v1
**Summary:** This paper explores the effectiveness of weight tying in decoder-only large language models (LLMs) during differentially private fine-tuning with DP-SGD, a method aimed at preserving user privacy. By evaluating the performance of GPT2 and DistilGPT2, the authors demonstrate that using untied embeddings significantly improves accuracy and reduces memory usage, surpassing weight-tied models. The findings suggest that untying embeddings is a more efficient design choice for privacy-preserving training of LLMs, challenging conventional architectural decisions in this context.

### 8. Turbo Harness: Instance-Adaptive Harness Optimization
**Authors:** Tunyu Zhang, Hao Wang, Kai Xu, Dimitris N. Metaxas
**Link:** https://arxiv.org/abs/2609.40330v1
**Summary:** Turbo Harness addresses the challenge of optimizing harnesses for agents that need to self-improve, which traditionally rely on a single, average-performing global harness. The proposed method adapts this global harness for individual tasks by reusing data from the initial optimization process to create a structured playbook, allowing for customized patches. Experimental results demonstrate that Turbo Harness significantly outperforms existing optimization methods across various tasks.

### 9. WorldAuditBench: Interactive 3D World Auditing with Multimodal Agents
**Authors:** Ziyan Jiang, Jingbo Yang, Jiabao Ji, Yujian Liu, Qiucheng Wu, Tommi Jaakkola, Yang Zhang, Shiyu Chang
**Link:** https://arxiv.org/abs/2609.40325v1
**Summary:** The paper addresses the challenge of detecting anomalies in interactive 3D environments, like floating objects or walls that shouldn't exist. The authors introduce WorldAuditBench, a benchmark that evaluates multimodal AI agents—using vision-language and vision-language-action models—across various anomaly detection tasks. Results indicate that current models perform significantly worse than humans, highlighting the need for better integration of action and visual reasoning in these systems.

### 10. Cogentic: Multi-Agent Orchestration for Automated Proof Discovery
**Authors:** Yang Cai, Vineet Gupta, Yanchen Jiang, Christopher Liaw, Aranyak Mehta, Grigoris Velegkas, Di Wang
**Link:** https://arxiv.org/abs/2609.40324v1
**Summary:** Cogentic is a multi-agent system designed to tackle complex open research problems in mathematics and theoretical computer science by automating proof discovery. It employs an iterative approach where an orchestrator directs independent provers to explore various proof directions, verifies their outputs, and maintains a verified ledger of promising results. The key achievement is that Cogentic has successfully produced novel findings on five open problems, which have been validated by experts.
