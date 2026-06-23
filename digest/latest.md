---
## 2026-06-23

### 1. AutoDex: An Automated Real-World System for Dexterous Grasping Data Collection
**Authors:** Mingi Choi, Gunhee Kim, Jisoo Kim, Taeksoo Kim, Taeyun Ha, Jongbin Lim, Hanbyul Joo
**Link:** https://arxiv.org/abs/2606.23689v1
**Summary:** The paper presents AutoDex, an automated system that addresses the challenge of collecting real-world data for dexterous grasping by running an entire data collection loop without human intervention, including perception, execution, and labeling. The system successfully gathered a database of over 3,500 grasp trials on various objects, improving data collection speed by 4.8 times compared to traditional teleoperation methods, and achieved a significantly higher success rate when validating grasps compared to simulation-only methods. The resulting data will be publicly available to support further research.

### 2. Randomized YaRN Improves Length Generalization for Long-Context Reasoning
**Authors:** Manas Mehta, Fangcong Yin, Greg Durrett
**Link:** https://arxiv.org/abs/2606.23687v1
**Summary:** The paper addresses the challenge that large language models have in generalizing to very long sequences beyond their training context. The authors introduce a method called Randomized YaRN, which combines positional encoding with a curriculum that exposes models to a wider range of position representations during training. Their key finding is that this approach significantly enhances reasoning performance on long-context tasks, especially at lengths much longer than those seen during training.

### 3. CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation
**Authors:** Sikai Li, Shuning Li, Zhenyu Wei, Yunchao Yao, Chenran Li, Mingyu Ding
**Link:** https://arxiv.org/abs/2606.23680v1
**Summary:** The paper presents CoorDex, a novel learning framework that enhances humanoid robots' ability to manipulate objects while in motion, moving beyond the traditional stop-and-go method. By utilizing coordinated latent residual control that integrates high-dimensional body movements with dexterous hand manipulation, the system is able to perform complex tasks like grasping and carrying objects continuously. The key contribution is demonstrating that this approach significantly improves the effectiveness of dexterous loco-manipulation compared to previous methods under the same conditions.

### 4. Semantic Browsing: Controllable Diversity for Image Generation
**Authors:** Sara Dorfman, Maya Vishnevsky, Omer Dahary, Or Patashnik, Daniel Cohen-Or
**Link:** https://arxiv.org/abs/2606.23679v1
**Summary:** The paper addresses the lack of diversity in image generation from text prompts, where models often produce similar outputs instead of varied interpretations. The authors propose a new method called Semantic Browsing, which allows users to explore image galleries by systematically varying meaningful aspects of the generated content, leveraging rich textual representations for more controlled output. Their approach results in diverse, interpretable images that align closely with user-defined semantic choices, enhancing creative exploration.

### 5. AIR: Adaptive Interleaved Reasoning with Code in MLLMs
**Authors:** Cong Han, Xiaohan Lan, Haibo Qiu, Yujie Zhong
**Link:** https://arxiv.org/abs/2606.23678v1
**Summary:** The paper addresses the limitations of multimodal large language models (MLLMs) in performing numerical computations during interleaved reasoning with code, which have primarily focused on visual tasks. The authors propose an adaptive interleaved reasoning framework that combines a cold-start data pipeline, effective data filtering for reinforcement learning, and a novel tool-invocation strategy, resulting in a significant performance boost—average accuracy on tasks increased by 6.1 percentage points, with interleaved reasoning accuracy improving by 9.9 percentage points and tool-use success rates above 95%.

### 6. Open Problem: Is AdamW Effective Under Heavy-Tailed Noise?
**Authors:** Dingzhi Yu, Hongyi Tao, Yuanyu Wan, Luo Luo, Lijun Zhang
**Link:** https://arxiv.org/abs/2606.23676v1
**Summary:** The paper addresses whether the AdamW optimizer, commonly used for training large language models, can effectively converge under heavy-tailed noise conditions often encountered in pretraining. The authors propose this as an open problem and establish a positive benchmark for convergence while presenting a lower-bound mechanism that illustrates how the memory component of AdamW's denominator may obscure large gradient effects. This work highlights the need for further theoretical exploration of AdamW's performance in scenarios characterized by heavy-tailed noise.

### 7. PsyBridge: A Hybrid Intelligent Framework for Multi-Dimensional Mental Health Assessment and Decision Support
**Authors:** Sunil Wanjari, Manish Thakre, Aayushi Asole, Sharwari Raut, Kwabena Adu-Duodu, Yinhao Li, Stanly Wilson
**Link:** https://arxiv.org/abs/2606.23673v1
**Summary:** The paper addresses the limitation of traditional mental health assessments, which often rely on isolated indicators and lack comprehensive insights. It introduces PsyBridge, a hybrid framework that integrates various validated assessment tools and personality profiling to improve decision-making in mental healthcare. The key finding is that PsyBridge achieves a high accuracy of 84% in risk classification, outperforming standard assessments while offering greater interpretability and stability in predictions.

### 8. Teaching LLMs String Matching, Backtracking, and Error Recovery to Deduce Bases and Truth Tables for the Combinatorially Exploding Bit Manipulation Puzzles
**Authors:** Prateek Agnihotri, Sanchit Jain, Prabhat Agnihotri, Aditya Prasad, Shubham Jain
**Link:** https://arxiv.org/abs/2606.23672v1
**Summary:** This paper addresses the challenge of using Large Language Models (LLMs) to solve complex Bit Manipulation Puzzles that require deducing a hidden logical rule from binary strings. The authors propose a novel approach that avoids traditional arithmetic logic by focusing on string similarity and structured search, allowing for autonomous error recovery. Their method significantly improved performance, achieving over 96% validation accuracy, the highest in the competition.

### 9. Can LLMs Reliably Self-Report Adversarial Prefills, and How?
**Authors:** Quang Minh Nguyen, Uzair Ahmed, Taegyoon Kim
**Link:** https://arxiv.org/abs/2606.23671v1
**Summary:** This paper investigates whether large language models (LLMs) can reliably recognize when their prior responses have been influenced by adversarial attacks, specifically focusing on safety contexts. The authors tested ten different models and discovered that none could consistently identify their compromised outputs, with an average self-reporting rate of only 27.3%. Additionally, they explored various finetuning methods, which improved some aspects of model introspection but ultimately did not enhance their ability to detect tampering, indicating potential risks in relying on LLM self-reporting for safety.

### 10. Tapered Language Models
**Authors:** Reza Bayat, Ali Behrouz, Aaron Courville
**Link:** https://arxiv.org/abs/2606.23670v1
**Summary:** The paper addresses the inefficiency of uniform parameter allocation across the layers of modern language models, which fails to account for the non-uniform contribution of layers to the output. The authors propose Tapered Language Models (TLMs), which allocate more parameters to earlier layers and fewer to later ones, leading to improved performance. Their experiments show that this tapered approach consistently enhances perplexity and downstream task performance compared to traditional models, without increasing computational costs.
