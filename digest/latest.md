---
## 2026-07-20

### 1. PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization
**Authors:** Yuchen Yang, Yifan Zhao, Anisha Dasgupta, Sasa Misailovic
**Link:** https://arxiv.org/abs/2607.16184v1
**Summary:** The paper addresses the challenge of efficiently serving Mixture-of-Experts (MoE) large language models, which struggle with high GPU memory demands and cache issues during inference. The authors present PagedWeight, a method that dynamically quantizes model weights at runtime, balancing the trade-off between accuracy, memory usage, and processing speed. Key results show that PagedWeight can deliver performance equivalent to FP16 accuracy while achieving up to 72% GPU memory savings and nearly double the throughput, significantly outperforming existing quantization techniques.

### 2. A Blueprint for Equilibrium-Based Differentiable Continuous-Variable Thermodynamic Computing
**Authors:** Owen Lockwood, Jérémy Béjanin, Joost Bus, Christopher Chamberland, Patrick Huembeli, Frank Schäfer, Guillaume Verdon
**Link:** https://arxiv.org/abs/2607.16183v1
**Summary:** This paper proposes a new design for energy-efficient computing that utilizes thermodynamic principles to address the rising energy and speed requirements of machine learning tasks. The authors focus on a method that employs Langevin dynamics in hardware to create and sample energy-based models, enabling the construction of various machine learning models. Key findings include a framework for using this thermodynamic approach and initial results from experiments with superconducting circuits that highlight its potential for reducing energy consumption in probabilistic computing.

### 3. Cluster-Aware Matching via Laplacian Optimal Transport
**Authors:** Gabriel Samberg, YoonHaeng Hur, Yuehaw Khoo, Nir Sharon
**Link:** https://arxiv.org/abs/2607.16178v1
**Summary:** The paper addresses the challenge of matching point clouds that have intrinsic cluster structures, where standard point-to-point correspondences may not be effective. The authors propose a method called Laplacian Optimal Transport (LapOT), which incorporates cluster information by regularizing the optimal transport problem with Laplacian terms derived from similarity graphs. The key contribution is the development of this cluster-aware matching framework, along with a technique called Refined Simultaneous Clustering (RSC), which together yield more reliable and interpretable alignments between point clouds.

### 4. Physics-enhanced reinforcement learning for real-time optimal control of dynamical systems
**Authors:** Matteo Tomasetto, Nicolò Botteghi, Gabriele Bruni, Andrea Manzoni
**Link:** https://arxiv.org/abs/2607.16177v1
**Summary:** The paper addresses the challenge of sample inefficiency in reinforcement learning (RL) for controlling complex, high-dimensional dynamical systems. It introduces the Physics-Enhanced Reinforcement Learning (PEARL) approach, which combines RL with traditional optimal control by utilizing the differentiability of the system's dynamics. The key results demonstrate that PEARL significantly reduces the number of required interactions with the environment, improves performance compared to existing RL methods, and effectively generalizes across various parametric scenarios.

### 5. Evaluating Open-Weight LLMs for Generating Structured Threat Information for Autonomous Vehicle Vulnerabilities
**Authors:** Md Erfan, Ahmed Ryan, Md Kamal Hossain Chowdhury, Md Rayhanur Rahman
**Link:** https://arxiv.org/abs/2607.16175v1
**Summary:** This paper addresses the need for structured information on vulnerabilities in Connected and Autonomous Vehicles (CAVs) to aid security practitioners in mitigating risks. The authors evaluated various open-weight Large Language Models (LLMs) to generate Structured Threat Information Expression (STIX) from vulnerability descriptions, creating a dataset called CAV-STIXGen for this purpose. They found that certain LLMs performed well in mapping vulnerabilities to structured formats, achieving high accuracy while also identifying recurring threat patterns in the CAV domain that could enhance threat intelligence and defense prioritization.

### 6. When Does Muon Help Agentic Reinforcement Learning?
**Authors:** Kai Ruan, Jinghao Lin, Zihe Huang, Ziqi Zhou, Qianshan Wei, Xuan Wang, Hao Sun
**Link:** https://arxiv.org/abs/2607.16169v1
**Summary:** The paper investigates the effectiveness of the Muon optimizer for enhancing performance in sparse-reward reinforcement learning (RL) tasks, particularly comparing it to the AdamW optimizer. By applying Muon specifically to hidden weight matrices in the ALFWorld environment, the researchers found significant improvements in validation success rates, particularly at lower learning rates, indicating that Muon can effectively contribute to agentic RL strategies. The results highlight the need for further exploration of the interaction between policy optimization methods, advantage estimators, and learning rates in RL applications.

### 7. Behaviour-Conditioned Neural Processes for Adaptive Residential Short-Term Load Forecasting
**Authors:** Ramin Soleimani, Andrea Visentin, Dirk Pesch
**Link:** https://arxiv.org/abs/2607.16168v1
**Summary:** This paper addresses the challenge of short-term load forecasting in residential settings, where energy demand varies significantly among households due to differing behaviors. The authors introduce a novel framework called the behaviour-conditioned Attentive Neural Process, which incorporates inferred behavioral patterns directly into the forecasting model rather than treating them as separate features. The results demonstrate that this approach significantly improves forecasting accuracy, achieving notable reductions in both mean absolute error and continuous ranked probability score compared to existing methods, especially when context information is limited.

### 8. An Exam for Active Observers
**Authors:** Jiarui Zhang, Muzi Tao, Shangshang Wang, Ollie Liu, Xuezhe Ma, Willie Neiswanger
**Link:** https://arxiv.org/abs/2607.16165v1
**Summary:** The paper addresses the limitation of current multimodal large language models (MLLMs) in performing active observation—an essential aspect of human visual perception. The researchers introduced a benchmark called ActiveVision, comprising 17 tasks that require repeated visual engagement, revealing that top MLLMs like GPT-5.5 and Claude Fable 5 significantly underperformed, solving only 10.6% and 3.5% of tasks, respectively, compared to human participants averaging 96.1%. This indicates a need for improved model architectures and training methods to enhance active visual observation capabilities in MLLMs.

### 9. PRISA: Proactive Infrastructure LiDAR Framework for Intersection Safety Assessment
**Authors:** Tam Bang, Hussam Abubakr, Emiliano de la Garza Villarreal, Truc Phuong Nguyen, Austin Harris, Toru Hirano, Mina Sartipi, Yunfei Xu, Hoang H. Nguyen
**Link:** https://arxiv.org/abs/2607.16156v1
**Summary:** The paper introduces PRISA, a system designed to improve safety at urban intersections by using LiDAR sensors to monitor traffic and predict potential conflicts involving vehicles and vulnerable road users like pedestrians and cyclists. PRISA features a modular design that includes real-time risk assessment capabilities without the need for manual data annotation, allowing it to forecast movements and evaluate safety risks effectively. The system was tested in a live setting, achieving quick response times that demonstrate its feasibility for enhancing intersection safety.

### 10. Learning Standard Model structure from LHC data with Riemannian flow matching
**Authors:** Midori Kato, Kevin A. Urquía-Calderón, Inar Timiryasov, Oleg Ruchayskiy
**Link:** https://arxiv.org/abs/2607.16144v1
**Summary:** This paper presents a novel approach to learn the structure of the Standard Model using data from the Large Hadron Collider (LHC) by employing a transformer-based generative model called ShellFlow. The researchers trained this model on a vast dataset of collision events and demonstrated its ability to accurately reproduce fundamental particle characteristics and correlations without explicit prior knowledge, thereby capturing a significant portion of the Standard Model directly from the data. This work highlights the potential of machine learning techniques in physics, particularly in extracting complex structures from experimental data.
