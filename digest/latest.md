---
## 2026-06-16

### 1. The Value Axis: Language Models Encode Whether They're on the Right Track
**Authors:** Nick Jiang, Isaac Kauvar, Jack Lindsey
**Link:** https://arxiv.org/abs/2606.17056v1
**Summary:** The paper explores how language models, specifically Qwen3-8B, internally assess the likelihood of achieving their goals while generating responses. By constructing a "value" axis based on reinforcement learning data, the authors discovered that this axis influences the model's confidence and decision-making strategies, including its tendency to self-correct and explore options. A notable finding is that optimizing preferences can enhance the model's confidence in certain behaviors, while the model shows lower confidence in politically sensitive topics after training.

### 2. Context-Aware RL for Agentic and Multimodal LLMs
**Authors:** Peiyang Xu, Bangzheng Li, Sijia Liu, Karthik R. Narasimhan, Pramod Viswanath, Prateek Mittal, Xingyu Fu
**Link:** https://arxiv.org/abs/2606.17053v1
**Summary:** The paper addresses the challenge that large language models (LLMs) face when required to identify critical evidence within lengthy or complex contexts, which can hinder their reasoning and multimodal capabilities. The authors propose a reinforcement learning method called ContextRL, which incentivizes models to choose the most relevant context by rewarding them based on context selection related to specific queries and answers. Key results demonstrate that ContextRL improves performance on long-horizon reasoning and visual question answering benchmarks by significant margins, showing its effectiveness in enhancing model grounding and context understanding.

### 3. Exact Posterior Score Estimation for Solving Linear Inverse Problems
**Authors:** Abbas Mammadov, Ozgur Kara, Kaan Oktay, Iskander Azangulov, Adil Kaan Akan, Hyungjin Chung, James Matthew Rehg, Yee Whye Teh
**Link:** https://arxiv.org/abs/2606.17048v1
**Summary:** This paper addresses the challenge of sampling from the posterior distribution when solving linear inverse problems using denoising models. The authors derive a method called Exact Posterior Score (EPS) that enables effective posterior sampling by maintaining the structure of existing denoisers, allowing for training from scratch or fine-tuning. Their approach demonstrates significant improvements in fidelity and other metrics while requiring substantially fewer evaluations compared to traditional methods.

### 4. Geometric Action Model for Robot Policy Learning
**Authors:** Jisang Han, Seonghu Jeon, Jaewoo Jung, René Zurbrügg, Honggyu An, Tifanny Portela, Marco Hutter, Marc Pollefeys, Seungryong Kim, Sunghwan Hong
**Link:** https://arxiv.org/abs/2606.17046v1
**Summary:** The paper addresses the challenge of teaching robots to understand and manipulate objects in 3D environments based on user instructions. It introduces the Geometric Action Model (GAM), which utilizes a pretrained geometric foundation model to effectively encode observations and predict future actions based on language and historical data. The key contribution is that GAM outperforms existing methods in accuracy, robustness, speed, and efficiency across various manipulation tasks, demonstrating improved performance in both simulation and real-world settings.

### 5. Hierarchical Advantage Weighting for Online RL Fine-Tuning of VLAs from Sparse Episode Outcomes
**Authors:** Tongyan Fang, Siyuan Huang, Naiyu Fang, Ganlong Zhao, Zhongjin Luo, Jianbo Liu, Xiaogang Wang, Ying Dong, Hongsheng Li
**Link:** https://arxiv.org/abs/2606.17043v1
**Summary:** The paper addresses the challenge of fine-tuning pretrained visual language agent (VLA) policies in online reinforcement learning, where episodes yield only binary success or failure outcomes, complicating effective feedback for learning. The authors introduce Hierarchical Advantage-Weighted Behavior Cloning (HABC), which uses separate critics for viability and efficiency, allowing adaptive weighting of feedback based on the current state and improving credit assignment. This method significantly enhances success rates in real-robot tasks, outperforming supervised fine-tuning baselines.

### 6. Benchmarking LLM Agents on Meta-Analysis Articles from Nature Portfolio
**Authors:** Anzhe Xie, Weihang Su, Yujia Zhou, Yiqun Liu, Qingyao Ai
**Link:** https://arxiv.org/abs/2606.17041v1
**Summary:** The paper addresses the challenge of effectively conducting meta-analyses by evaluating how well large language models (LLMs) can handle the literature retrieval and screening processes involved. It introduces a new dataset, MetaSyn, consisting of expert-curated meta-analyses that includes extensive research criteria and retrieval information. The key finding is that while LLMs achieve high recall rates in retrieving relevant literature, they struggle significantly in accurately identifying eligible studies, with a maximum recovery rate of only 52.7%, highlighting a major bottleneck in the meta-analysis pipeline.

### 7. The Importance of Phase in Neural Representations: An Internal Oppenheim-Lim Test of Image Classifiers
**Authors:** Alper Yıldırım
**Link:** https://arxiv.org/abs/2606.17037v1
**Summary:** This paper investigates the role of phase information in neural networks for image classification, inspired by an earlier finding that natural images can be recognized from Fourier phase alone. The authors conducted experiments by swapping the phase of one image with the magnitude of another within different layers of various neural networks. They found that classifiers generally rely more on phase for identity recognition, while the magnitude information is often less critical, revealing that different architectures handle phase and magnitude in distinct ways, particularly highlighting differences between CNNs and attention-based models.

### 8. Your Privacy My Cloak: Backdoor Attacks on Differentially Private Federated Learning
**Authors:** Xiaolin Li, Ning Wang, Ninghui Li, Wenhai Sun
**Link:** https://arxiv.org/abs/2606.17035v1
**Summary:** This paper investigates the vulnerability of differentially private federated learning systems to backdoor attacks, challenging the idea that differential privacy enhances security against such threats. The authors introduce a new attack method called RING, which cleverly exploits the masks created by differential privacy to hide malicious updates while still achieving a significant impact during model aggregation. Their experiments demonstrate that RING can achieve an average attack success rate of 90.3%, highlighting a substantial security gap in differential privacy implementations in federated learning.

### 9. KVEraser: Learning to Steer KV Cache for Efficient Localized Context Erasing
**Authors:** Mufei Li, Shikun Liu, Dongqi Fu, Haoyu Wang, Yinglong Xia, Hong Li, Hong Yan, Pan Li
**Link:** https://arxiv.org/abs/2606.17034v1
**Summary:** The paper addresses the challenge of efficiently erasing specific spans from the KV cache of long-context language models, as traditional methods require significant recomputation of subsequent tokens. KVEraser is introduced as a learned method that replaces only the erased KV states without altering the rest of the cache, utilizing a two-stage training process for effective adaptation. Key results demonstrate that KVEraser achieves nearly the same performance as full recomputation while significantly reducing latency, offering a 3-4x speedup in various tasks.

### 10. DEEPRUBRIC: Evidence-Tree Rubric Supervision for Efficient Reinforcement Learning of Deep Research Agents
**Authors:** Minghang Zhu, Chuyang Wei, Junhao Xu, Yilin Cheng, Zhumin Chen, Jiyan He
**Link:** https://arxiv.org/abs/2606.17029v1
**Summary:** The paper addresses the inefficiency of reinforcement learning (RL) in training deep research agents due to inadequate rubric-based rewards that may not accurately represent the needs of the task. The authors introduce DeepRubric, a framework that generates high-quality query-rubric pairs by first establishing clear evaluation criteria through an evidence tree built from sub-questions. As a result, they created 9,000 training examples, successfully training a model that performs comparably to existing state-of-the-art systems while using significantly fewer computational resources.
