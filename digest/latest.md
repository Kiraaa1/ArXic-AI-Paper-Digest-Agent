---
## 2026-08-29

### 1. Learning a Continuous Sepsis Severity Score Without Hour-by-Hour Supervision: A Two-Site Retrospective Study
**Authors:** Kevin Zhu, Ryan Zhang, Baraa Abed, Tilendra Choudhary, Malvern Madondo, Mehak Arora, Yixuan Yang, Alasdair Gent, Aditya Nagori, Omer T. Inan, Krista L. Haines, Patrick Georgoff, Suresh M. Agarwal, Vijay Krishnamoorthy, Tetsu Ohnuma, Mihai V. Podgoreanu, Michael R. Pinsky, Gilles Clermont, Craig M. Coopersmith, Craig S. Jabaley, Rishikesan Kamaleswaran
**Link:** https://arxiv.org/abs/2608.27421v1
**Summary:** This study addresses the limitations of traditional sepsis severity scores, which are outdated and do not reflect current patient dynamics. The researchers developed a new sepsis index by analyzing real-time patient data over a 72-hour period, using mortality as a guiding factor for score allocation. The key finding is that this new index effectively predicts patient outcomes, correlating well with established indicators and showing potential as a useful decision support tool in critical care settings.

### 2. Boosting LLM Exploration via Weak-Model Guidance in RLVR
**Authors:** Xingyu Shen, Huishuai Zhang, Peng Li, Yinchun Wang, Dongyan Zhao
**Link:** https://arxiv.org/abs/2608.27420v1
**Summary:** The paper addresses the issue of reduced reasoning diversity in large language models (LLMs) during reinforcement learning with verifiable rewards (RLVR), which typically leads to a decline in performance. The authors propose a novel method that utilizes partial reasoning paths from smaller, weaker models to encourage exploration and prevent overconfidence in the target LLM. Their experiments demonstrate that this approach significantly enhances reasoning coverage, especially as the complexity of tasks increases, outperforming traditional RLVR methods and effectively mitigating entropy collapse without added complexity.

### 3. Scaling Graph Neural Networks for Friend Recommendation: Multi-Hash User Embeddings and Temporal Neighbor Sampling
**Authors:** Maksim Utushkin, Andrei Ovsiannikov, Alexander D'yakonov
**Link:** https://arxiv.org/abs/2608.27413v1
**Summary:** The paper addresses the challenge of efficiently recommending friends in large social networks by utilizing Graph Neural Networks (GNNs) and highlights two key innovations: multi-hash user embeddings to significantly reduce memory usage, and temporal neighbor sampling to enhance performance. The proposed system effectively scales to handle vast social graphs, leading to a notable 16% increase in friend additions and 11.5% more unique users adding friends during online tests compared to existing systems. The authors also share their framework for distributed training and inference on large temporal graphs.

### 4. Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms
**Authors:** Siye Wu, Kai Yang, Yuchen Cai, Xin Xu, Peng-Yuan Wang, Jiaxuan Wang, Jiashun Liu, Jiafei Lyu, Yangkun Chen, Saiyong Yang, Yanghua Xiao
**Link:** https://arxiv.org/abs/2608.27409v1
**Summary:** The paper addresses the challenge of consolidating multiple reinforcement learning capabilities in language models by comparing three fusion paradigms: Merge, Mix RL, and multi-teacher on-policy distillation (MOPD). The authors evaluate these approaches using shared experts and data across various model scales and benchmarks, discovering that while their overall performances are similar, they differ significantly in specific scenarios. The findings suggest practical guidelines for choosing the appropriate fusion method based on the existence of expert models, domain proportions, and the importance of preserving domain-specific strengths.

### 5. CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators
**Authors:** Kechen Liu, Ola Shorinwa
**Link:** https://arxiv.org/abs/2608.27406v1
**Summary:** The paper presents CLAP, a new framework designed to enable video models to simulate physical actions across different robot types by leveraging diverse video data from both humans and robots. By reconciling differing action representations and using a curriculum-based learning approach, CLAP can effectively learn universal physical laws that apply regardless of the actor. The key contribution is its ability to outperform existing models in complex environments while supporting various action representations and robot forms, making it a versatile tool for training video world models.

### 6. How Language Models Organize and Structure Moral Knowledge
**Authors:** Orion Reblitz-Richardson
**Link:** https://arxiv.org/abs/2608.27402v1
**Summary:** This paper investigates how large language models (LLMs) organize moral knowledge by examining their ability to detect and differentiate between various moral foundations. The authors employed linear probes to analyze representation spaces within LLMs, revealing that the models capture multiple independent moral dimensions while also having a shared component indicative of integration. Notably, the findings suggest that LLMs reflect the statistical properties of the training corpus rather than adhering to the expected distinctions in moral reasoning proposed by traditional Moral Foundations Theory.

### 7. Making Clinical Language Models Auditable: Concept-Guided Fine-Tuning for Robust Prediction
**Authors:** Jin Mu, Guanhua Chen
**Link:** https://arxiv.org/abs/2608.27397v1
**Summary:** The paper addresses the issue of clinical language models performing well in controlled environments but struggling in real-world scenarios due to reliance on non-informative features in medical text. To tackle this, the authors introduce CAST (Concept-guided Artifact Suppression Tuning), which uses Sparse Autoencoders to identify and suppress these misleading features while enhancing model interpretability. The key contribution is that CAST not only improves prediction accuracy on discharge-note mortality but also provides a transparent audit trail of clinical decisions, making the model's reasoning clearer and more reliable.

### 8. LeVJEPA: Efficient & Scalable Video Pretraining without the Heuristics
**Authors:** Lukas Kuhn, Lucas Maes, Giuseppe Serra, Quentin Le Lidec, Yann LeCun, Randall Balestriero, Florian Buettner
**Link:** https://arxiv.org/abs/2608.27395v1
**Summary:** The paper introduces LeVJEPA, a novel method for efficiently training video representations without the common complications of previous approaches. It employs a collapse-free learning objective using a single encoder to improve video representation while significantly reducing the computational resources required for pretraining. Notably, LeVJEPA matches or surpasses existing models in performance while using 5.6 to 20.8 times less compute, demonstrating that video can serve as a more effective foundation for visual pretraining.

### 9. RATIO: A Benchmark for Retrieval Across Typed Ideation Operations in Scientific Literature
**Authors:** Maayan Sharon, Tom Hope
**Link:** https://arxiv.org/abs/2608.27394v1
**Summary:** The paper presents RATIO, a benchmark designed to improve the retrieval of scientific literature based on different ideation operations, specifically addressing problems, broadening concepts, and specifying details. It utilizes a method that combines discourse-marker distant supervision with large-scale paper vetting to create a dataset from millions of scientific texts. The key finding is that fine-tuning retrieval models to these specific ideation operations significantly enhances their performance, while also highlighting the potential for further advancements in literature-based idea generation.

### 10. Property-Specific Recoverability from Contact PPG to Camera rPPG under Heterogeneous Observation Conditions
**Authors:** Timothy Oladunni, Farouk Ganiyu-Adewumi
**Link:** https://arxiv.org/abs/2608.27392v1
**Summary:** This study investigates how well physiological data from contact photoplethysmography (PPG) can be recovered using remote photoplethysmography (rPPG) techniques under varying observation conditions. By analyzing 655 recordings with specific algorithms, the researchers found that while some overall metrics, like heart rate, are preserved, the ability to recover different physiological properties varies significantly based on individual recordings and conditions. The key finding is that population-level similarities do not guarantee consistent recovery of individual recordings, highlighting the need for tailored approaches in rPPG applications.
