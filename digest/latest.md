---
## 2026-06-02

### 1. Transferable Self-Harm Surveillance from Emergency Department Triage Notes Using an Evidence-Augmented Machine Learning Approach
**Authors:** Liuliu Chen, Gowri Rajaram, Eleanor Bailey, Katrina Witt, Michelle Lamblin, Jo Robinson, Mike Conway, Vlada Rozova
**Link:** https://arxiv.org/abs/2606.02545v1
**Summary:** The paper addresses the inadequate surveillance of self-harm rates in public health, which often relies on less sensitive diagnostic codes from hospitals. The authors developed a three-stage machine learning approach that combines traditional methods with large language models to analyze emergency department triage notes for identifying self-harm incidents across multiple hospitals. Notably, their method demonstrated high effectiveness, achieving a precision score of over 88% and accurately identifying the primary method of self-harm with 95% accuracy.

### 2. SimSD: Simple Speculative Decoding in Diffusion Language Models
**Authors:** Junxia Cui, Haotian Ye, Runchu Tian, Hongcan Guo, Jinya Jiang, Haoru Li, Chaojie Ren, Yiming Huang, Kaijie Zhu, Zhongkai Yu, Kun Zhou, Jingbo Shang
**Link:** https://arxiv.org/abs/2606.02544v1
**Summary:** The paper introduces SimSD, a new speculative decoding technique for diffusion language models, which traditionally face challenges with rapid inference due to their masked language modeling approach. By implementing a simple masking strategy that allows these models to perform token-level speculative verification similar to autoregressive models, SimSD enhances decoding efficiency. The key contribution is a significant increase in decoding throughput—up to 7.46 times faster—while also improving the quality of text generation across various benchmarks.

### 3. SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction
**Authors:** Yuting Ning, Zhehao Zhang, Yash Kumar Lal, Boyu Gou, Junyi Li, Weitong Ruan, Chentao Ye, Rahul Gupta, Diyi Yang, Yu Su, Huan Sun
**Link:** https://arxiv.org/abs/2606.02540v1
**Summary:** The paper introduces SkillHarm, a benchmark for evaluating vulnerabilities in agent skills, highlighting the risks of skill-based attacks throughout their lifecycle. It examines two attack methods—Fixed-Payload Poisoning and Self-Mutating Poisoning—while categorizing the associated risks and automating attack generation through a coding pipeline. The results show high success rates for these attacks on current agents, indicating significant security vulnerabilities that existing defenses fail to adequately address.

### 4. Tracking the Behavioral Trajectories of Adapting Agents
**Authors:** Jonah Leshin, Manish Shah, Ian Timmis
**Link:** https://arxiv.org/abs/2606.02536v1
**Summary:** The paper addresses the challenge of tracking how changes to agents' skill files affect their behavior over time. The authors propose a methodology that uses a text embedding model to quantify agent traits as vectors in an embedding space, enabling the evaluation of skill file edits. Their approach yields high accuracy in classifying the propensity of agents to seek sensitive data, achieving 91.2% accuracy and a strong correlation in results, and establishes a protocol for agents to assess each other's skill updates.

### 5. SafeSteer: Localized On-Policy Distillation for Efficient Safety Alignment
**Authors:** Hao Li, Jingkun An, Zijun Song, Pengyu Zhu, Rui Li, Hao Wang, Wendi Feng, Yesheng Liu, Lijun Li, Jin-Ge Yao, Lei Sha
**Link:** https://arxiv.org/abs/2606.02530v1
**Summary:** This paper addresses the challenge of aligning large language models (LLMs) with human safety values without sacrificing their general performance, a phenomenon known as the alignment tax. The authors introduce SafeSteer, a technique that focuses on localized modifications to the model's outputs related to safety tokens, rather than making broad trade-offs. They demonstrate that SafeSteer significantly enhances safety performance on various benchmarks with minimal impact on general capabilities and requires far fewer harmful samples for training than previous methods, effectively reducing alignment costs.

### 6. Auditing Asset-Specific Preferences in Financial Large Language Models: Evidence from Bitcoin Representations and Portfolio Allocation
**Authors:** Wenbin Wu
**Link:** https://arxiv.org/abs/2606.02528v1
**Summary:** This paper investigates whether large language models (LLMs) have inherent biases towards specific financial assets, focusing on Bitcoin. The authors develop a detailed audit protocol that includes behavioral assessments and internal feature analysis, revealing that LLMs show varying preferences for Bitcoin based on context and that specific internal features can significantly influence financial decisions. Key findings indicate that modifying these features can alter Bitcoin's portfolio allocation by measurable amounts, highlighting the importance of understanding these preferences as LLMs take on more autonomous roles in finance.

### 7. Why Not Hyperparameter-Friendly Optimisation? A Monotonic Adaptive Norm Rescaling Approach For Long-Tailed Recognition
**Authors:** Shuo Zhang, Chenqi Li, Tingting Zhu
**Link:** https://arxiv.org/abs/2606.02526v1
**Summary:** The paper addresses the challenge of long-tailed recognition in deep learning, where certain classes have significantly fewer samples, affecting model performance. The authors introduce a novel method called Self-Adaptive Monotonic Normalization (SAMN), which simplifies the adjustment of class weight norms without requiring additional hyperparameters. Their approach not only improves recognition outcomes but also achieves state-of-the-art results on benchmark datasets, making it a user-friendly solution for this problem.

### 8. FigSIM: A Dataset for Fine-grained Suicide Severity and Figurative Language in Suicide Memes
**Authors:** Liuliu Chen, Elise R. Carrotte, Brian E. Chapman, Jo Robinson, Mike Conway
**Link:** https://arxiv.org/abs/2606.02523v1
**Summary:** The paper introduces FigSIM, a dataset of 1049 suicide memes annotated for severity, figurative language, and related content, aimed at improving understanding and moderation of harmful meme content on social media. By benchmarking various models on tasks related to figurative language and suicide severity detection, the researchers highlighted the challenges these memes present, including biases in predicting higher severity levels. The dataset is publicly available to aid in further research and content moderation strategies.

### 9. Moment-Video: Diagnosing Temporal Fidelity of Video MLLMs on Momentary Visual Events
**Authors:** Xiaolin Liu, Yilun Zhu, Xiangyu Zhao, Xuehui Wang, Yan Li, Xin Li, Haoyu Cao, Xing Sun, Shaofeng Zhang, Xu Yang, Zhihang Zhong, Xue Yang
**Link:** https://arxiv.org/abs/2606.02522v1
**Summary:** The paper addresses the challenge of video multimodal large language models (MLLMs) in accurately understanding brief, crucial visual events within videos, which are often overlooked due to frame sampling and compression techniques. The authors introduce a new benchmark called Moment-Video, consisting of 1,000 video-question pairs focused on momentary visual evidence. Their evaluation reveals that even the best models achieve only 39.6% accuracy, highlighting significant limitations in current MLLMs' ability to effectively identify and interpret transient visual information.

### 10. Drifting Preference Optimization for One-Step Generative Models
**Authors:** Zhou Jiang, Yandong Wen, Zhen Liu
**Link:** https://arxiv.org/abs/2606.02521v1
**Summary:** The paper addresses the challenge of fine-tuning one-step text-to-image generators, which typically struggle with standard alignment methods. The authors introduce Drifting Preference Optimization (DrPO), a method that ranks generated candidates based on target rewards and updates the generator using a non-parametric approach, allowing it to work with complex rewards without needing backpropagation. Their results show that DrPO improves alignment and significantly reduces training computation compared to existing methods.
