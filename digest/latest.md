---
## 2026-07-28

### 1. ClinFusion: A Vision-Centric Multimodal LLM System for Holistic Medical Understanding
**Authors:** Hangjie Yuan, Yichen Qian, Zhiwei Tang, Xianzhe Xu, Lirong Wu, Sicheng Yang, Jinwang Wang, Pengju Wang, Zhitao Zeng, Yizeng Han, Yan Xing, Shengxuan Luo, Tao Feng, Qing Xie, Weigen Yao, Yi Yang, Zuozhu Liu, Jiasheng Tang, Shaocheng Wang, Jitao Wang, Jiahong Dong, Weihua Chen, Feng Xu, Fan Wang
**Link:** https://arxiv.org/abs/2607.24743v1
**Summary:** ClinFusion addresses the challenge of integrating and understanding various 2D and 3D medical images in clinical practice using a vision-centric multimodal large language model (MLLM). It employs a novel architecture to effectively fuse different medical image types and introduces a new evaluation framework that aligns with clinical standards. The model outperforms existing open-source and proprietary MLLMs across multiple benchmarks and receives strong validation from radiologists for producing high-quality reports.

### 2. Certified Parallel-in-Time Sinkhorn for Dynamic Entropic Optimal Transport
**Authors:** Xinyang Wen
**Link:** https://arxiv.org/abs/2607.24741v1
**Summary:** The paper addresses the inefficiencies of traditional sequential methods in solving dynamic entropic optimal transport problems, specifically in applications like Flow Matching. The authors introduce TemporalSinkhorn, a parallel-in-time approach that batches candidate solutions and effectively manages updates to maintain accuracy. Key results show significant performance improvements, with speedups of up to 3.632 times faster than traditional methods, while ensuring no tolerance violations in output accuracy.

### 3. Learning Distributions from Multiple Data Providers
**Authors:** Jon Kleinberg, Amin Saberi, Xizhi Tan, Grigoris Velegkas
**Link:** https://arxiv.org/abs/2607.24732v1
**Summary:** The paper addresses the challenge of learning an unknown distribution from diverse datasets provided by different sources, which offer samples conditioned on specific subsets. The authors analyze how the structure of these subsets affects the learning process and demonstrate that while complete interaction between sets leads to higher sample complexity, certain structural properties can significantly reduce it. A key contribution includes identifying conditions under which optimal sample complexity can be achieved, ranging from nearly linear to quadratic, and providing a method to attain a smooth range of complexities depending on the configuration of the data.

### 4. Rethinking Classifier-Free Guidance in On-Policy Diffusion Distillation
**Authors:** Bingnan Li, Haozhe Wang, Haozhong Xiong, Fangtai Wu, Jinpeng Yu, Yang Shi, Jiaming Liu, Ruihua Huang
**Link:** https://arxiv.org/abs/2607.24731v1
**Summary:** This paper addresses the challenges of applying classifier-free guidance (CFG) in on-policy distillation (OPD) of diffusion models, particularly when errors between predicted outcomes aren’t well identified. The authors identify a problem called Negative Branch Asymmetry (NBA), where guidance misalignment increases errors. They propose a new method called Positive-Direction Matching (PDM), which improves error handling by separately constraining the positive predictions, resulting in more effective and robust knowledge transfer in tasks like video control.

### 5. KANEx: Translating Kolmogorov-Arnold Networks' Interpretability to Medical Explainability
**Authors:** Krithi Shailya, Ananya Lakshmi Ravi, Venkatanathan K. V., Sowmya S. Sundaram, Gokul S. Krishnan, Aditi Anand, Balaraman Ravindran
**Link:** https://arxiv.org/abs/2607.24730v1
**Summary:** The paper addresses the issue of trust in medical AI systems, specifically chest X-ray classifiers, which often lack interpretability. To enhance explainability, the authors introduce KANEx, a framework that utilizes Kolmogorov-Arnold Networks to create transparent, interpretable models and generate more reliable natural-language explanations through Vision-Language Models. The results show that this approach improves the quality of visual attributions and reasoning in medical contexts, leading to a 10% enhancement in performance over traditional methods.

### 6. Global Convergence of DGM and PINN Algorithms for Solving Nonlinear PDEs
**Authors:** Justin Sirignano, Konstantinos Spiliopoulos, Samuel Cohen
**Link:** https://arxiv.org/abs/2607.24726v1
**Summary:** This paper addresses the challenge of ensuring that neural networks used to solve nonlinear partial differential equations (PDEs) through the Deep Galerkin Method (DGM) and Physics Informed Neural Networks (PINNs) can reliably converge to the actual PDE solutions, rather than just local minima. The authors prove that, for a specific class of semi-linear PDEs, training these neural networks with gradient descent to minimize the PDE residual will indeed lead to convergence to the true solution. This establishes a crucial mathematical foundation for the use of these methods in scientific machine learning.

### 7. The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training via Single- and Multi-Teacher On-Policy Agentic Distillation
**Authors:** Tianyi Men, Zhuoran Jin, Kang Liu, Jun Zhao
**Link:** https://arxiv.org/abs/2607.24720v1
**Summary:** The paper addresses the challenge of improving multi-turn long-horizon planning in foundation model agents by creating a controlled environment that systematically studies planning across three stages: acquisition, shaping, and integration. The authors find that training with a constructed world model and utilizing multi-teacher on-policy distillation can enhance planning abilities, highlighting the importance of data quality and the effective integration of learned patterns for generalization across different tasks. Their results indicate that better planning requires careful management of training trajectories and the interplay between various planning strategies.

### 8. DataOrchestra: Learning to Orchestrate Per-Example Curation of Pretraining Data
**Authors:** Zhen Huang, Yikun Wang, Shijie Xia, Pengfei Liu
**Link:** https://arxiv.org/abs/2607.24717v1
**Summary:** The paper presents DataOrchestra, a framework designed to enhance the pretraining of Large Language Models (LLMs) by customizing data processing for each individual example rather than applying a one-size-fits-all strategy. By intelligently deciding whether to drop, retain, or clean data chunks and tailoring the cleaning methods to specific needs, DataOrchestra improves model performance across multiple benchmarks while also reducing processing costs. The results show consistent gains over traditional data processing methods, demonstrating its effectiveness even in specialized tasks like math continued pretraining.

### 9. Efficient LLM-Generated Shuttling Compilers for Complex Trapped-Ion Architectures
**Authors:** Fabian Kreppel, Reza Salkhordeh, Ferdinand Schmidt-Kaler, André Brinkmann
**Link:** https://arxiv.org/abs/2607.24714v1
**Summary:** The paper addresses the challenge of creating efficient shuttling compilers for trapped-ion quantum computers, which manage the movement of ion-qubits based on given algorithms. The authors utilized the Claude Opus 4.7 large language model (LLM) to automatically generate and refine Python code for these compilers, resulting in significant reductions in shuttling timesteps—up to 76% for simpler architectures—without requiring extensive manual coding. The study demonstrates that LLMs can effectively streamline the development of quantum compilers, drastically shortening the time needed to adapt to new architectures.

### 10. ERUnderstand: Evaluating Vision-Language Models on Structured ER Diagrams
**Authors:** Ali Ansari, Yasmin Mohammadi, Farnoush Nili, Parsa Esmaeilkhani, Longin Jan Latecki, Eduard Dragut
**Link:** https://arxiv.org/abs/2607.24707v1
**Summary:** The paper introduces ERUnderstand, a benchmark designed to enhance AI's ability to understand Entity-Relationship Diagrams (ERDs), which are important for database design but often found in non-machine-readable formats. By compiling a dataset of 2,960 ER diagrams and evaluating state-of-the-art Vision-Language Models (VLMs), the authors discover that while these models can accurately identify common schema elements, their performance significantly declines on more complex features. The benchmark, along with the dataset and evaluation tools, is made publicly available to facilitate further research in this area.
