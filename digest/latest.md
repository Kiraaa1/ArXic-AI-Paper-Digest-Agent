---
## 2026-07-29

### 1. Pass the Baton: Trajectory-Relayed On-Policy Distillation
**Authors:** Haolei Xu, Xiaowen Xu, Haiwen Hong, Zixuan Ni, Hongxing Li, Yiwen Qiu, Weiming Lu, Yongliang Shen
**Link:** https://arxiv.org/abs/2607.26057v1
**Summary:** The paper addresses the issue of "prefix failure" in on-policy distillation, where a student's incorrect reasoning leads to unreliable outputs during training. The authors propose a method called Relay On-Policy Distillation (Relay-OPD), which allows the teacher model to briefly intervene and correct the student's path at critical points in their trajectory. This approach significantly improves performance on mathematical reasoning tasks, achieving an average increase of 5.73% over standard methods, while also reducing training trajectory length by over 50%.

### 2. $π\mathbf{R}^2$: Reactive Real-time Flow Policies
**Authors:** Sungjae Park, Shubham Tulsiani
**Link:** https://arxiv.org/abs/2607.26055v1
**Summary:** The paper presents $π\mathbf{R}^2$, a novel approach to enhance the reactivity of generalist manipulation policies that typically rely on slow, open-loop action-chunking methods, making them less effective in dynamic control situations. By utilizing a dual-channel conditioning system and a latency-adaptive flow schedule, $π\mathbf{R}^2$ enables these policies to respond to real-time proprioceptive inputs while managing vision data efficiently, resulting in a significant speed improvement in replanning. The method demonstrates substantial performance gains, achieving up to a 30% increase in success rates for manipulation tasks in real-world applications compared to existing baselines.

### 3. Spend Experts Where You Are Unsure: Confidence-Adaptive Routing for Mixture-of-Experts LoRA
**Authors:** Tom Saliencro, Rohan Desai, Priya Nair, Maya Lindqvist, Daniel Whitmore
**Link:** https://arxiv.org/abs/2607.26052v1
**Summary:** The paper addresses the inefficiency of Mixture-of-Experts (MoE) models that use a fixed number of experts to process tokens, leading to overuse for simple tokens and underuse for complex ones. The authors propose CARE (Confidence-Adaptive Routing of Experts), which dynamically adjusts the number of experts based on the model's confidence in the tokens and their potential disagreement, allowing for more effective allocation of resources. This approach outperforms traditional fixed-expert methods in several benchmarks, achieving similar results while activating fewer experts and enhancing out-of-distribution detection.

### 4. Re-thinking Mammography Transfer Learning: The Dataset-Informed Transfer Learning (DITL) Framework for Breast Cancer Screening and Lesion Diagnosis
**Authors:** Adarsh Bhandary Panambur, Siming Bayer, Andreas Maier
**Link:** https://arxiv.org/abs/2607.26043v1
**Summary:** The paper addresses the challenge of improving mammography classification performance by proposing a new framework called Dataset-Informed Transfer Learning (DITL), which combines dataset-specific difficulty signals with neighborhood-aware supervision. DITL features two adaptive components that enhance learning without the need for meticulous hyperparameter tuning. The key result shows that DITL achieves state-of-the-art performance on a large dataset for breast density classification and significantly improves results on smaller datasets, making it a robust solution for breast cancer screening and diagnosis.

### 5. VetClaw: An Edge-Cloud Multimodal Agentic System for Veterinary Disease Screening
**Authors:** Syed Mhamudul Hasan, Anas AlSobeh, Hussein Zangoti, Abdur R. Shahid
**Link:** https://arxiv.org/abs/2607.26042v1
**Summary:** VetClaw is a system designed to improve early veterinary disease screening by combining edge and cloud computing. It captures images of animals and symptom descriptions, sending them to a sophisticated model for disease classification. The key contribution is its ability to integrate visual evidence and user inputs into a responsive and safety-conscious workflow, significantly enhancing prediction accuracy compared to relying solely on images.

### 6. Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions?
**Authors:** Abhishek Pillai, Samir Kumar Nayak, Yuan Chen
**Link:** https://arxiv.org/abs/2607.26041v1
**Summary:** The paper addresses the challenge of evaluating how effectively computer-use agents (CUAs) can understand and track transitions in desktop graphical user interfaces (GUIs) when performing complex tasks. The authors present Desktop-Delta Bench (DDB), a benchmark consisting of over 2,000 human-verified instances that test CUAs on their ability to verify state changes and track actions across various applications. Key findings indicate that while models struggle with accurately recognizing transitions and actions, the introduction of context-aware tasks can improve performance, highlighting the need for better diagnostic assessment tools in CUA development.

### 7. Reinformed Dreamer: An Asymmetric World Model Efficiently Trained through Latent Guidance
**Authors:** Gaspard Lambrechts, Adrien Bolland, Daniel Ebi, Damien Ernst
**Link:** https://arxiv.org/abs/2607.26040v1
**Summary:** The paper addresses the challenge of improving reinforcement learning algorithms by incorporating additional guidance beyond standard rewards, particularly under both partial and full observability scenarios. The authors introduce a new algorithm called the Reinformed Dreamer, which employs a novel objective for learning representations using latent guidance, enhancing the learning process. Experimental results reveal that the Reinformed Dreamer consistently outperforms the original Dreamer algorithm and previous asymmetric approaches, demonstrating its effectiveness in training better representation models.

### 8. Falling Behind Drives Unsafe Development in an Idealised AI Race Experiment
**Authors:** Elias Fernández Domingos, The Anh Han
**Link:** https://arxiv.org/abs/2607.26034v1
**Summary:** The paper investigates how competitive pressure in AI development may lead to riskier, less safe practices, which could harm progress. Through an experimental setup simulating an AI race, the authors found that decisions to engage in unsafe development are influenced more by opponents' choices and the dynamics of the race rather than individual risk preferences. The study suggests that policies should aim to decrease competitive pressure and encourage cooperation in AI development to mitigate these risks.

### 9. CHARM: A Multimodal Graph Foundation Model with Hierarchical Context Modeling for Zero-Shot Transfer
**Authors:** Ankang Yang, Jitao Zhao, Di Jin, Yuxiao Huang, Dongxiao He
**Link:** https://arxiv.org/abs/2607.26023v1
**Summary:** The paper introduces CHARM, a multimodal graph foundation model designed to enhance zero-shot transfer in graph domains by leveraging hierarchical context modeling to better capture multimodal semantics and cross-modal relations. By replacing isolated node features with hierarchical contexts that map specific node patterns to broader concepts, CHARM enables improved representation of graphs without the need for extensive target-domain adaptation. Experimental results demonstrate significant advancements in performance on various zero-shot multimodal graph tasks.

### 10. UniMem: Complementary Episodic-to-Parametric Memory for Boundary-Agnostic Task Streams
**Authors:** Siyu Xia, Chenheng Zhang, Yanting Wu, Haoxuan Li, Jiajun Chai, Xiaohan Wang, Guojun Yin, Wei Lin, Zhouchen Lin, Haifeng Zhang, Jun Wang
**Link:** https://arxiv.org/abs/2607.26017v1
**Summary:** The paper addresses the challenge of enabling large language model (LLM) agents to effectively learn and adapt to diverse, ongoing task streams without rigid boundaries. The authors introduce UniMem, a memory management framework that combines episodic and parametric memory, using learnable routing tokens to facilitate flexible task handling and memory expansion. Their experiments demonstrate that UniMem significantly improves performance on long task sequences, achieving an average increase of 4.0 exact match points across three different models.
