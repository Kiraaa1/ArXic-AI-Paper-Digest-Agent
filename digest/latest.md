---
## 2026-07-14

### 1. Requential Coding: Pushing the Limits of Model Compression with Self-Generated Training Data
**Authors:** Shikai Qiu, Marc Finzi, Yujia Zheng, Kun Zhang, Andrew Gordon Wilson
**Link:** https://arxiv.org/abs/2607.11883v1
**Summary:** The paper addresses the challenge of efficiently compressing large neural networks by introducing requential coding, a new method that selects training samples from the student model's distribution to create shorter codes reflecting only where the student model disagrees with the teacher. This approach is shown to yield significantly smaller code lengths compared to traditional methods, especially as model size increases, and provides superior generalization guarantees for large language models. Additionally, the study highlights that lower-entropy data contains more learnable structure than higher-entropy data, suggesting a deeper understanding of model capacity and dataset complexity.

### 2. Metacognition in LLMs: Foundations, Progress, and Opportunities
**Authors:** Gabrielle Kaili-May Liu, Areeb Gani, Jacqueline Lu, Jordan Thomas, Mark Steyvers, Arman Cohan
**Link:** https://arxiv.org/abs/2607.11881v1
**Summary:** The paper addresses the challenge of understanding how large language models (LLMs) can develop metacognitive abilities critical for tasks like learning and decision-making. It provides a comprehensive overview of the current state of research, including methods for measuring and enhancing these abilities in LLMs. The authors aim to stimulate further research in this area by categorizing advancements and identifying open questions and future directions.

### 3. Invariant Learning Dynamics of Transformers in Inductive Reasoning Tasks
**Authors:** Tiberiu Musat, Tiago Pimentel, Nicholas Zucchet, Thomas Hofmann
**Link:** https://arxiv.org/abs/2607.11875v1
**Summary:** This paper addresses the challenge of understanding how Transformer language models develop inductive reasoning skills across various tasks. The authors propose a theoretical framework that describes the learning dynamics of these models as confined to a low-dimensional invariant manifold, allowing for a clearer analysis of their behavior. Key findings include insights into how data statistics influence learning and how initial conditions affect the solutions identified by the model, paving the way for a more predictive understanding of Transformer learning processes.

### 4. A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation
**Authors:** Yunhai Feng, Natalie Leung, Jiaxuan Wang, Lujie Yang, Haozhi Qi, Preston Culbertson
**Link:** https://arxiv.org/abs/2607.11874v1
**Summary:** The paper presents REGRIND, a new approach for teaching robots how to manipulate objects dexterously by using a single demonstration from a human. This method involves retargeting the human's hand movements to a robot's kinematic structure and training a reinforcement learning policy to follow these movements while maintaining important contact dynamics. The key contribution is the successful transfer of this policy to real robots, demonstrating fluent, human-like performance in complex tool-use tasks.

### 5. A Durability and Cross-Language Transfer Benchmark for a Validated Teaching-Feedback Classification Protocol
**Authors:** Esteban U. Vega Barajas
**Link:** https://arxiv.org/abs/2607.11873v1
**Summary:** The paper addresses the challenge of effectively classifying open-ended teaching evaluation comments, which are often underutilized by institutions. The authors tested a previously validated classification protocol with different modern representation methods on Spanish data and examined its transferability to English. They found that while the latest models performed well on thematic classification, there was no significant advantage in sentiment classification across different model types, suggesting that the choice of model may be less critical than the methodology itself.

### 6. Inside the Unfair Judge: A Mechanistic Interpretability Account of LLM-as-Judge Bias
**Authors:** Zixiang Xu, Sixian Li, Huaxing Liu, Xiang Wang, Shuai Li, Zirui Song, Xiuying Chen
**Link:** https://arxiv.org/abs/2607.11871v1
**Summary:** This paper addresses the bias present in large language models (LLMs) when used as judges in scoring tasks, moving beyond traditional input-output analysis. The authors introduce a representation-level perspective, showing that biased inputs lead to distinct changes in the model's hidden state geometry, allowing for predictive measures of bias. Key results indicate that manipulating these hidden states can control scoring outcomes, with their approach significantly outperforming existing methods at anticipating judge failures on unseen benchmarks.

### 7. Evidence-Backed Video Question Answering
**Authors:** Shijie Wang, Honglu Zhou, Ziyang Wang, Ran Xu, Caiming Xiong, Silvio Savarese, Chen Sun, Juan Carlos Niebles
**Link:** https://arxiv.org/abs/2607.11862v1
**Summary:** The paper addresses the issue of explainability in Video Large Language Models (Video LLMs) for question answering, which often lack visual grounding for their answers. The authors introduce Evidence-Backed Video Question Answering (E-VQA), a task that requires models to provide both answers and precise visual evidence from videos, along with a new benchmark dataset called ST-Evidence for training. Their approach shows significant performance improvements in answer accuracy and visual grounding, establishing a strong baseline for future explainable video understanding.

### 8. AdvancedMathBench: A Benchmark Suite for Advanced Mathematical Proof Generation and Verification
**Authors:** Lingkai Kong, Zijian Wu, Yuzhe Gu, Haiteng Zhao, Wenyong Huang, Shuang Sun, Zhicheng Xiong, Xiaotian Zhang, Shuya Zhao, Yan Wang, Disheng Xu, Wenwei Zhang, Kai Chen
**Link:** https://arxiv.org/abs/2607.11849v1
**Summary:** The paper presents AdvancedMathBench, a new benchmark suite designed to assess the advanced mathematical reasoning abilities of large language models (LLMs). It includes a proof-generation benchmark (ProverBench) with 296 challenging problems and a verification benchmark (VerifierBench) featuring 888 proof trajectories, both accompanied by expert evaluations. Key findings indicate that top models struggle with advanced proof generation and verification, highlighting significant limitations in their current capabilities in these areas.

### 9. Input-Aware Dynamic Backdoor Attack Against Quantum Neural Networks
**Authors:** Junrui Zhang, Zemin Chen, Lusi Li, Mohammad Ghasemigol, Daniel Takabi, Rui Ning
**Link:** https://arxiv.org/abs/2607.11843v1
**Summary:** The paper addresses the security vulnerability of Quantum Neural Networks (QNNs) to backdoor attacks, specifically by proposing a novel attack method called Q-DIBA that employs input-aware dynamic backdoors. This technique trains a classical trigger generator alongside a QNN to create effective and stealthy backdoor inputs, while overcoming challenges posed by quantum measurements. The results demonstrate that Q-DIBA maintains high accuracy in clean data, successfully activates attacks, and remains resilient against various defense mechanisms, highlighting the need for enhanced security measures in QNN deployments.

### 10. LoRA-Based Cascaded Multimodal Fusion for Action Recognition in Medical Training Environments
**Authors:** Divya Mereddy, Jeevan Beedareddy
**Link:** https://arxiv.org/abs/2607.11839v1
**Summary:** This paper addresses the challenge of action and activity recognition in medical training environments by introducing a cascaded multimodal fusion framework that utilizes Low-Rank Adaptation (LoRA). The approach efficiently integrates different modalities in stages without retraining earlier components, allowing for scalable adaptation across various datasets. Preliminary results demonstrate that this method outperforms individual modality models and achieves competitive performance compared to existing baselines, highlighting its effectiveness for multimodal integration in healthcare training.
