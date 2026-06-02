---
## 2026-06-02

### 1. Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge via Perceptual Perturbation and Reward Modeling
**Authors:** Seojeong Park, Jiho Choi, Junyong Kang, Seonho Lee, Jaeyo Shin, Hyunjung Shim
**Link:** https://arxiv.org/abs/2606.02578v1
**Summary:** The paper addresses the issue of Perceptual Judgment Bias in multimodal large language models (MLLMs), where these models often favor plausible narratives over correct visual information when there's a conflict between text and images. To combat this, the authors introduce a Perceptually Perturbed Judgment Dataset that helps isolate perceptual errors and develop a training framework that improves the consistency and accuracy of MLLM evaluations. Their experiments demonstrate that this approach significantly enhances the models' reliability and alignment with human judgments.

### 2. ProtoAda: Prototype-Guided Adaptive Adapter Expansion and Geometric Consolidation for Multimodal Continual Instruction Tuning
**Authors:** Yu-Cheng Shi, Zhen-Hao Xie, Jun-Tao Tang, Da-Wei Zhou
**Link:** https://arxiv.org/abs/2606.02576v1
**Summary:** The paper addresses the challenge of Multimodal Continual Instruction Tuning (MCIT) for Multimodal Large Language Models (MLLMs), where tasks with similar semantics but different response formats can lead to ineffective learning and interference among model experts. To solve this, the authors present ProtoAda, a framework that uses prototype-guided adaptive tuning to better match task assignments with both semantic meaning and output structures, while optimizing parameter updates geometrically. The results show that ProtoAda significantly improves performance, especially for tasks where sequential tuning can disrupt answer formats.

### 3. AdaCodec: A Predictive Visual Code for Video MLLMs
**Authors:** Haowen Hou, Zhen Huang, Zheming Liang, Qingyi Si, Chenglin Li, Shuai Dong, Kele Shao, Ruilin Li, Dianyi Wang, Nan Duan, Jiaqi Wang
**Link:** https://arxiv.org/abs/2606.02569v1
**Summary:** AdaCodec addresses the inefficiency of existing video multimodal large language models (MLLMs) that treat each frame as an independent RGB image, leading to redundant data transmission. Instead, it introduces a "predictive visual code" that sends a full reference frame only when necessary and compactly encodes inter-frame changes when possible. As a result, AdaCodec outperforms the baseline model, enhancing performance on long-video benchmarks while significantly reducing the time taken to generate visual tokens.

### 4. ClinEnv: An Interactive Multi-Stage Long Horizon EHR Environment for Agents
**Authors:** Yuxing Lu, Yushuhong Lin, Wenqi Shi, J. Ben Tamo, Xukai Zhao, Jinzhuo Wang, May Dongmei Wang
**Link:** https://arxiv.org/abs/2606.02568v1
**Summary:** The paper introduces ClinEnv, an interactive benchmark designed to evaluate large language models (LLMs) in clinical decision-making, addressing the limitations of static assessments by simulating long-term patient management. ClinEnv requires models to sequentially gather information from specialized agents before making irreversible medical decisions, revealing a significant gap between the quality of outcomes and the quality of the decision-making process. Key findings indicate that even the best-performing model struggled with complex management decisions, achieving only a 0.31 decision F1 score, highlighting the importance of process quality in medical AI evaluations.

### 5. IntraShuffler: A Privacy Preserving Framework for Heterogeneous DP Federated Learning
**Authors:** Farhin Farhad Riya, Olivera Kotevska, Jinyuan Stella Sun
**Link:** https://arxiv.org/abs/2606.02563v1
**Summary:** The paper addresses the vulnerability of heterogeneous differential privacy (HDP) in federated learning (FL) systems, where an honest-but-curious server can infer clients' data attributes by exploiting the structured patterns in gradient updates. To mitigate this, the authors propose IntraShuffler, a framework that introduces a privacy-aware shuffling mechanism to disrupt these patterns while still allowing for effective $\varepsilon$-aware server aggregation. Their experiments demonstrate that IntraShuffler significantly reduces the risk of privacy inference while maintaining good model performance.

### 6. Permissive Safety Through Trusted Inference: Verifiable Belief-Space Neural Safety Filters for Assured Interactive Robotics
**Authors:** Haimin Hu
**Link:** https://arxiv.org/abs/2606.02562v1
**Summary:** The paper addresses the challenge of ensuring safety for autonomous robots that interact with humans while minimizing performance impacts. It introduces a method to certify the safety of Belief-space safety filters, which adaptively reduce uncertainty during operation, using conformal prediction to assess reliability in real-time inference. The key contribution is that this approach allows for a less conservative safety filter compared to traditional methods, demonstrated through improved performance in a simulated human-vehicle interaction scenario.

### 7. From Layers to Submodules: Rethinking Granularity in Replacement-Based LLM Compression
**Authors:** Elia Cunegatti, Marcus Vukojevic, Erik Nielsen, Giovanni Iacca
**Link:** https://arxiv.org/abs/2606.02559v1
**Summary:** The paper addresses the limitations of existing methods for compressing Large Language Models (LLMs) by focusing on their architectural components, specifically advocating for a submodule-level approach rather than full-layer granularity. The authors introduce SubFit, a new technique that selectively replaces and fits non-contiguous submodules within the model, improving compression efficiency. SubFit demonstrates superior performance, achieving better trade-offs in perplexity and accuracy compared to other methods, particularly at higher compression levels.

### 8. HERO'S JOURNEY: Testing Complex Rule Induction with Text Games
**Authors:** Anshun Asher Zheng, Kanishka Misra, David I. Beaver, Junyi Jessy Li
**Link:** https://arxiv.org/abs/2606.02556v1
**Summary:** The paper presents HERO'S JOURNEY, a benchmark designed to test how well agents can infer and execute complex rules in goal-directed tasks based on demonstrations. The authors evaluated state-of-the-art language models on this benchmark and found that while they can perform some rule induction, their abilities are inconsistent, especially with procedural tasks. The study highlights that execution challenges hinder performance, and while certain methods can enhance outcomes for attribute tasks, procedural rule induction still requires significant improvement.

### 9. Modeling Depth Ambiguity: A Mixture-Density Representation for Flying-Point-Free Depth Estimation
**Authors:** Siyuan Bian, Congrong Xu, Jun Gao
**Link:** https://arxiv.org/abs/2606.02552v1
**Summary:** The paper addresses the issue of spurious depth estimations, known as flying points, which occur near object boundaries where traditional depth models assign a single, often incorrect depth to pixels. The authors propose a mixture-density approach (MDA) that allows each pixel to simultaneously predict multiple depth hypotheses along with their probabilities, enabling more accurate depth reconstruction at boundaries. This method significantly improves boundary reconstruction quality and effectively eliminates flying-point artifacts, even with blurry inputs, while maintaining low computational overhead.

### 10. SN-WER: Script-Normalized WER for Multi-Script Indic ASR Evaluation
**Authors:** Priyaranjan Pattnayak
**Link:** https://arxiv.org/abs/2606.02548v1
**Summary:** The paper addresses the issue of inflated Word Error Rate (WER) metrics in automatic speech recognition (ASR) for multilingual settings, particularly when references and outputs use different scripts. To tackle this, the authors propose a method called Script-Normalized WER (SN-WER), which standardizes both reference and hypothesis texts to a canonical script before calculating WER. They demonstrate that SN-WER can significantly reduce error rate discrepancies in certain datasets, suggesting its valuable role in more accurately evaluating ASR performance in multi-script environments.
