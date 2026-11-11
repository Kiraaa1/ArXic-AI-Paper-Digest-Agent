---
## 2026-11-11

### 1. Medical Image Segmentation: Foundation Model Adaptation versus Task-Specific Training
**Authors:** Emre Kutlusan, Yongmin Li
**Link:** https://arxiv.org/abs/2611.14519v1
**Summary:** This paper investigates whether foundation models pre-trained on large natural image datasets can effectively be adapted for medical image segmentation, compared to training models specifically for each task. Researchers adapted the DINOv2 foundation model using various fine-tuning strategies and tested its performance against task-specific models on multiple medical imaging datasets. The key finding is that the adapted foundation model outperformed task-specific models on external datasets, suggesting that it can generalize better across different clinical sites, while still maintaining some competitiveness in scenarios with abundant training data.

### 2. Toward Foundation Detection Models via Example-Based Grounding in EM-DETR
**Authors:** Sheethal Bhat, Bogdan Georgescu, Awais Mansoor, Florin C. Ghesu, Sasa Grbic, Andreas Maier
**Link:** https://arxiv.org/abs/2611.14518v1
**Summary:** The paper addresses the challenge of limited and inconsistent annotations in medical image datasets, which hampers the development of effective lesion detection models. The authors propose a novel student-teacher training strategy that combines diverse datasets with varying label types, utilizing an adapted example-based EM-DETR framework for improved detection accuracy across different imaging modalities. This approach achieves state-of-the-art results in chest X-rays and mammography, improving image-level AUC scores by 1% and mAP50 by 2-3% compared to existing single-dataset models, thus paving the way for more scalable and robust medical imaging models.

### 3. TorchCurves: Differentiable Parametric Curves
**Authors:** Alex Shtoff
**Link:** https://arxiv.org/abs/2611.14516v1
**Summary:** The paper introduces TorchCurves, a PyTorch library designed to make vector-valued parametric curves learnable, allowing for optimization and differentiation. By using B-spline or Legendre polynomial bases, the library supports various applications such as feature embeddings and functional regression, while offering an easy-to-use interface and good performance. The results show that while the library provides powerful generality for curve operations, its computational efficiency varies depending on the problem size.

### 4. AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models
**Authors:** Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, Shiyang Li, Sujay Bhatt, Sihan Zeng, Mingyi Hong
**Link:** https://arxiv.org/abs/2611.14515v1
**Summary:** The paper presents AutoScaffold, an AI-driven framework designed to enhance reinforcement learning in language models by dynamically creating training aids, or "scaffolds," based on the model’s experiences, without any human input. This approach effectively identifies and addresses learning bottlenecks, leading to significant performance improvements in various tasks, such as increased success rates in ALFWorld and enhanced accuracy in QA and mathematical reasoning. The results demonstrate that AutoScaffold-trained models outperform traditional reinforcement learning baselines across all tested domains.

### 5. Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations
**Authors:** Ziang Liu, James J. Kim, Yijia Dai, Jennifer J. Sun
**Link:** https://arxiv.org/abs/2611.14514v1
**Summary:** The paper addresses the limitation of large language model (LLM) agents in scientific discovery, which typically evaluate hypotheses against their negations but fail to identify which alternative explanations are supported by evidence. To overcome this, the authors introduce "Contrastive Discovery," a methodology that utilizes a set of competing explanations for a scientific question, enabling agents to more effectively redistribute belief based on experimental evidence. The key finding is that this approach allows agents to resolve significantly more questions—73% of candidates can be determined to specific alternatives—compared to traditional pointwise evaluation, demonstrating its potential to enhance data-driven scientific inquiry.

### 6. Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents
**Authors:** Megha Srivastava, Michael H. Lim, Allison M. Keys, Pranav Murugan, Nate Gruver
**Link:** https://arxiv.org/abs/2611.14511v1
**Summary:** The paper introduces Pyrite, a benchmark for evaluating how well automated systems can rank candidate poses of protein-ligand interactions, which is critical for drug discovery. The authors develop two large language model (LLM)-based agents that show promising results by either reasoning about poses or generating features for machine learning, outperforming expert chemists in accuracy. The study highlights the potential of LLM-guided feature discovery in improving automated pose ranking in computational chemistry.

### 7. When Does the Real Wiring Win? Testing connectome structure-function claims against unmeasured physiology
**Authors:** Yeyuan Liu
**Link:** https://arxiv.org/abs/2611.14508v1
**Summary:** This paper addresses the issue of determining whether the structure of neural connections (the connectome) directly influences function, as seen in models of brain circuits. The authors propose a method to disentangle the effects of connectome wiring from model tuning by testing various physiological parameters and comparing results across multiple scenarios. They find that while some claims about the advantages of real wiring hold true, others do not, particularly when physiological data is independently validated, suggesting the need for careful optimization and modeling in neuroscience research.

### 8. Continual-ARC: Measuring Skill Acquisition over a Working Lifetime
**Authors:** Daniel Lenton
**Link:** https://arxiv.org/abs/2611.14505v1
**Summary:** The paper addresses the limitations of current continual learning benchmarks by introducing Continual-ARC, a framework that evaluates skill acquisition over a lifetime without requiring domain knowledge. It allows agents to engage with tasks multiple times, scoring them based on feedback usage while comparing memory-based and weight-based learning systems. The key finding indicates that traditional harness methods generally underperform compared to caching strategies and that weight-based learning significantly benefits from exposure to new tasks, highlighting potential pathways for improved continual learning methodologies.

### 9. Emergent Biological Capabilities in a Foundation Model for Molecular Interactions
**Authors:** Adi Mashiach
**Link:** https://arxiv.org/abs/2611.14504v1
**Summary:** The paper introduces Bonbon, a foundation model designed to predict molecular interactions by analyzing vast amounts of paired protein-ligand sequences. Bonbon demonstrates three emergent capabilities related to understanding molecular function and binding site localization without needing specific task instructions or structural data. Notably, it achieves a high success rate in predicting effective compounds for various disease targets, significantly outpacing traditional methods in speed and efficiency.

### 10. Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents
**Authors:** Howard Zhang, Chuck Arvin, Logan Brown, Mihir Bhatia, Neelu Choudhary, Lily Miao
**Link:** https://arxiv.org/abs/2611.14493v1
**Summary:** This study addresses the challenge of effectively evaluating LLM-based analytics agents in enterprise settings to ensure reliability in complex workflows. By comparing three evaluation frameworks—trace-based LLM judging, text-only LLM judging with red-teaming, and deterministic heuristics—the researchers found that trace-based evaluation provided the best performance in detecting known risks, while highlighting complementary strengths in security red-teaming for uncovering previously unknown failures. The results suggest a dual approach combining trace-based and adversarial evaluations for optimal assessment of such agents.
