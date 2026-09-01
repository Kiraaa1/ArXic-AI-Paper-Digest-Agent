---
## 2026-09-01

### 1. Context-Aware Interleaved Batching for WhisperX
**Authors:** Carlos Bain, Max Bain
**Link:** https://arxiv.org/abs/2608.31170v1
**Summary:** The paper addresses the challenge of losing historical context in speech transcription when using batching techniques, which can negatively impact punctuation and proper noun accuracy. The authors introduce a new method called Context-Aware Interleaved Batching that utilizes segment boundaries from Voice Activity Detection (VAD) to enhance context preservation during transcription. Their approach demonstrates improved transcription quality, with lower Word Error Rate (WER) and better handling of proper nouns, all while maintaining fast inference speeds.

### 2. Constant Individual Regret in General Games
**Authors:** Mingyang Liu, Gabriele Farina, Asuman Ozdaglar
**Link:** https://arxiv.org/abs/2608.31166v1
**Summary:** The paper addresses the challenge of achieving low individual regret in multi-player games using decentralized strategies, specifically without the usual dependence on the time horizon. The authors propose a new algorithm called ECHO-OFTRL, which combines optimistic follow-the-regularized-leader dynamics with an exponential moving average approach to enhance optimism. The key contribution is that this algorithm allows each player to achieve constant individual regret, independent of the horizon, with a bound that depends polylogarithmically on the number of players and the maximum action set size.

### 3. SUN: Persistent Programs For Language-Grounded Control-to-Learning-to-Real Policies
**Authors:** Weiqi Wang, Zhi Li, Yudong Lei, David Martinez, Xiaofeng Gao, Yuxin Jiang, Chenfanfu Jiang, Yingnian Wu, Demetri Terzopoulos, Ran Gong
**Link:** https://arxiv.org/abs/2608.31167v1
**Summary:** The paper addresses the challenge of aligning model-based control with learned policies in long-horizon manipulation tasks, where existing methods often neglect task semantics and reward design. The authors introduce Semantically UNified (SUN) Programs, which unify control objectives and learning through a system called Kuafu that converts language and scene semantics into effective policies. Their approach significantly outperforms traditional methods, achieving an 82.03% success rate across multiple tasks while efficiently generating more successful trajectories compared to alternatives, demonstrating the benefits of integrating symbolic planning with data-driven execution.

### 4. Sharp Approximation Rates for Neural Networks with Affine Latent Parameterizations
**Authors:** Shijun Zhang
**Link:** https://arxiv.org/abs/2608.31157v1
**Summary:** This paper addresses the challenge of efficiently approximating functions using neural networks with a low-dimensional latent representation. The authors study a framework where neural network parameters are generated from a latent vector, focusing on affine parameter generators and ReLU architectures. They prove that the worst-case approximation error decreases with the increase in the network's parameter budget, even when using a fixed-dimensional latent space, achieving significant efficiency in function approximation.

### 5. Auditing Anonymous AI Models: A Four-Stage Protocol for Black-Box Identity Verification
**Authors:** Yisen Xi
**Link:** https://arxiv.org/abs/2608.31142v1
**Summary:** The paper addresses the challenge of verifying the identity of anonymous AI models launched under codenames, given the increasing prevalence of such models. The authors propose a four-stage forensic audit protocol that analyzes historical configurations, configures fingerprints, and tests tokenizers to ensure accurate identity verification. Their approach effectively validated model identities in multiple cases, confirming their methodology's reliability and offering a practical implementation for use.

### 6. Configurable Semantic Chunking for Biomedical Information Extraction in Retrieval-Augmented Generation
**Authors:** Riya Ahuja, Tim Kacprowski, Roya Shiasi Sardoabi
**Link:** https://arxiv.org/abs/2608.31139v1
**Summary:** The paper addresses the limitations of fixed-size chunking in biomedical information extraction, which can disrupt semantic evidence during data retrieval. The authors present a configurable semantic chunking framework that enhances the chunking process by using more flexible methods such as entity-preserving windows and tiered trigger prioritization. Their results show that this approach significantly improves performance on certain biomedical relation extraction tasks, achieving an F1 score of 82.6%, outperforming the previous fixed-size method by over eight points.

### 7. OntoAligner-Ensemble: Voting-Based Fusion across Heterogeneous Ontology Alignment Techniques
**Authors:** Hamed Babaei Giglou, Sören Auer, Peio Popov, Mahsa Sanaei, Jennifer D'Souza
**Link:** https://arxiv.org/abs/2608.31137v1
**Summary:** The paper addresses the challenge of improving ontology alignment (OA) by combining predictions from various alignment techniques, which can sometimes conflict with each other. The authors introduce OntoAligner-Ensemble, a flexible framework that utilizes a two-stage voting-based fusion approach to integrate these predictions. Their experiments show that this ensemble method consistently enhances the balance between precision and recall, often outperforming individual aligners across different domains.

### 8. Implementing neural network mixed-effects models in Template Model Builder (TMB)
**Authors:** Nan Zheng, Hoi Yiu Cheung, Vibhu Sharma, James T. Thorson, Noel G. Cadigan
**Link:** https://arxiv.org/abs/2608.31133v1
**Summary:** This paper addresses the challenges of implementing neural network mixed-effects models (NMMs), which combine the predictive power of neural networks with mixed-effects modeling's ability to handle complex data structures. The authors propose a framework using Template Model Builder (TMB) that simplifies the implementation process by utilizing automatic differentiation and Laplace approximation to efficiently estimate the models without the need for manual derivations. Their approach enhances the flexibility and accuracy of NMMs, demonstrating improved statistical performance through two numerical examples and providing reproducible code for wider use.

### 9. DIASENTINEL: An Auditable Multi-Agent System for Guideline-Grounded Diabetes Risk Screening
**Authors:** Yung Wei Shueh, Zhi-Jie Chen, Chia-Hsuan Hsu, Hsin-Ling Hsu, Donghua Zhang, Chenwei Wu, Jun-En Ding, Tongze Zhang, Shihao Yang, Pengfei Hu, Fang-Ming Hung, Feng Liu
**Link:** https://arxiv.org/abs/2608.31128v1
**Summary:** The paper introduces DIASENTINEL, a multi-agent system designed to accurately screen for one-year risk of type 2 diabetes by analyzing electronic health records while adhering to clinical guidelines from the American Diabetes Association. It combines risk prediction, extraction of relevant clinical signals, and a verification process that checks recommendations against established guidelines. The key contribution is a framework that ensures reliable, auditable, and privacy-preserving decision support in clinical settings, complete with an interactive dashboard for real-time screening and patient reporting.

### 10. On the Complexity of the Compatibility Problem for Succinctly Encoded Conditional Distributions
**Authors:** Guy Emerson
**Link:** https://arxiv.org/abs/2608.31120v1
**Summary:** This paper investigates the compatibility problem for conditional probability distributions encoded as succinct arithmetic circuits, which is relevant for high-dimensional probabilistic models in machine learning. The authors establish that determining the existence of a compatible joint distribution is computationally intractable, showing that the problem is co-NP-complete when all probabilities are non-zero, and PSPACE-complete when zero probabilities are allowed. They also highlight implications for the expressibility of compatible conditionals in probabilistic modeling.
