# ArXiv Daily Digest

Automatically generated daily summaries of recent ArXiv papers.

---
## 2026-05-11

### 1. LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
**Authors:** Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
**Link:** https://arxiv.org/abs/2605.08083v1
**Summary:** The paper addresses the problem of inefficient manually designed test-time scaling (TTS) strategies for improving the performance of large language models during inference. The authors propose AutoTTS, an environment-driven framework that automatically discovers optimal TTS strategies by controlling the allocation of computation based on reasoning trajectories. Key results show that the automatically discovered strategies outperform traditional baselines in both accuracy and cost-efficiency across various benchmarks, while the entire discovery process is inexpensive and quick.

### 2. Normalizing Trajectory Models
**Authors:** Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
**Link:** https://arxiv.org/abs/2605.08078v1
**Summary:** The paper addresses the limitations of existing diffusion-based models for generating images in a few steps, which often compromise likelihood accuracy. The authors introduce Normalizing Trajectory Models (NTM), a method that employs conditional normalizing flows for each reverse sampling step while maintaining exact likelihood training. NTM achieves high-quality image generation in just four steps, outperforming strong baselines and preserving precise likelihood throughout the generation process.

### 3. Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration
**Authors:** Shuhang Lin, Chuhao Zhou, Xiao Lin, Zihan Dong, Kuan Lu, Zhencan Peng, Jie Yin, Dimitris N. Metaxas
**Link:** https://arxiv.org/abs/2605.08077v1
**Summary:** The paper addresses the issue of unreliable answer coverage in Knowledge Graph Question Answering (KGQA) systems, which often produce overly large prediction sets without sufficient reliability. The authors propose Conformal Path Reasoning (CPR), which incorporates query-level conformal calibration and a new Residual Conformal Value Network to improve the selection of path-level scores. Their approach significantly enhances the validity of predictions, achieving a 34% increase in empirical coverage while reducing the average size of prediction sets by 40% compared to previous methods.

### 4. Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
**Authors:** Maryam Maghsoudi, Shihab Shamma
**Link:** https://arxiv.org/abs/2605.08075v1
**Summary:** This paper addresses the challenge of decoding imagined speech from brain recordings, which is hindered by a lack of well-aligned data across individuals. The authors introduce a novel three-stage method that maps neural responses from imagined speech to actual listened speech using data from trained musicians, leading to the successful decoding of imagined words with notable accuracy. Key findings suggest that their approach can scale with more training data, making it viable for real-world brain-computer interface applications.

### 5. GRAPHLCP: Structure-Aware Localized Conformal Prediction on Graphs
**Authors:** Peyman Baghershahi, Fangxin Wang, Debmalya Mandal, Sourav Medya
**Link:** https://arxiv.org/abs/2605.08074v1
**Summary:** The paper addresses the challenge of applying conformal prediction (CP) to graph neural networks (GNNs), which often leads to uncertain predictions due to the complex structure of graphs. The authors introduce GRAPHLCP, a new localized CP framework that integrates graph topology and node relationships to enhance prediction accuracy, employing a method that includes a feature-aware densification step and Personalized PageRank for improved modeling of local and long-range dependencies. Their extensive experiments show that GRAPHLCP achieves reliable prediction sets while ensuring accurate uncertainty estimation in various scenarios.

### 6. EmambaIR: Efficient Visual State Space Model for Event-guided Image Reconstruction
**Authors:** Wei Yu, Yunhang Qian
**Link:** https://arxiv.org/abs/2605.08073v1
**Summary:** The paper presents EmambaIR, a new model for event-guided image reconstruction that overcomes limitations of existing methods, which struggle with global feature correlations and high computational costs. EmambaIR employs a unique combination of a top-k sparse attention mechanism and a gated state-space module to efficiently process event data, achieving better performance in tasks like motion deblurring and HDR enhancement. Experimental results show that it significantly outperforms current state-of-the-art techniques while reducing memory usage and processing time.

### 7. A Note on Non-Negative $L_1$-Approximating Polynomials
**Authors:** Jane H. Lee, Anay Mehrotra, Manolis Zampetakis
**Link:** https://arxiv.org/abs/2605.08072v1
**Summary:** The paper addresses the problem of finding non-negative polynomials that can approximate indicator functions in the $L_1$-norm under Gaussian distributions. The authors demonstrate that for sets with a bounded Gaussian surface area, it is possible to construct degree-$k$ non-negative polynomials that approximate these indicator functions to within a specified accuracy. Notably, their result shows that the degree required for such approximations is comparable to existing bounds for general $L_1$ approximations, but with the added constraint of non-negativity.

### 8. VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection
**Authors:** James Petullo, Sonny George, Dylan Cashman, Nianwen Xue
**Link:** https://arxiv.org/abs/2605.08070v1
**Summary:** The paper addresses the inefficiency and high cost of confidence-informed self-consistency in reasoning, which requires multiple evaluations of candidate answers by a critic language model. The authors propose VecCISC, a method that uses semantic similarity to filter out redundant or low-quality reasoning traces, thereby reducing the number of evaluations needed. The key finding is that VecCISC can decrease overall token usage by 47% while maintaining or improving the accuracy of the original approach.

### 9. Flow-OPD: On-Policy Distillation for Flow Matching Models
**Authors:** Zhen Fang, Wenxuan Huang, Yu Zeng, Yiming Zhao, Shuang Chen, Kaituo Feng, Yunlong Lin, Lin Chen, Zehui Chen, Shaosheng Cao, Feng Zhao
**Link:** https://arxiv.org/abs/2605.08063v1
**Summary:** The paper addresses critical issues in Flow Matching text-to-image models, specifically reward sparsity and gradient interference that lead to ineffective multi-task alignment. It introduces Flow-OPD, a novel approach that incorporates on-policy distillation to align models effectively, first training specialized teacher models and then consolidating their expertise into a single student model. As a result, Flow-OPD significantly improves performance metrics, achieving a GenEval score increase from 63 to 92 and enhancing OCR accuracy from 59 to 94, while maintaining image quality and human preference alignment.

### 10. Rubric-Grounded RL: Structured Judge Rewards for Generalizable Reasoning
**Authors:** Manish Bhattarai, Ismael Boureima, Nishath Rajiv Ranasinghe, Scott Pakin, Dan O'Malley
**Link:** https://arxiv.org/abs/2605.08061v1
**Summary:** The paper introduces a novel approach called rubric-grounded reinforcement learning (RL), which enhances model training by breaking down rewards into multiple verifiable criteria assessed by a large language model (LLM) judge. By using this structured reward system, the authors demonstrate that their model, trained on a large corpus of scientific documents, achieves higher performance in evaluating and reasoning tasks compared to the base model. Notably, the trained policy not only excels in rubric evaluations but also shows improved reasoning capabilities on unrelated benchmarks.

---
## 2026-05-11

### 1. The Memory Curse: How Expanded Recall Erodes Cooperative Intent in LLM Agents
**Authors:** Jiayuan Liu, Tianqin Li, Shiyi Du, Xin Luo, Haoxuan Zeng, Emanuel Tewolde, Tai Sing Lee, Tonghan Wang, Carl Kingsford, Vincent Conitzer
**Link:** https://arxiv.org/abs/2605.08060v1
**Summary:** The paper investigates how increasing the memory capacity of large language model (LLM) agents affects their ability to cooperate in multi-agent social dilemmas, revealing a phenomenon called the "memory curse". Through various analyses, the authors demonstrate that while expanding memory tends to deteriorate cooperative intent, targeted fine-tuning and memory sanitization techniques can counteract this decline, highlighting that the content of memory, rather than its length, plays a crucial role in influencing cooperative behavior. Ultimately, the study suggests that memory's impact on multi-agent interactions is complex, as it can either hinder or promote collaboration based on the reasoning strategies employed.

### 2. CA-SQL: Complexity-Aware Inference Time Reasoning for Text-to-SQL via Exploration and Compute Budget Allocation
**Authors:** James Petullo, Nianwen Xue
**Link:** https://arxiv.org/abs/2605.08057v1
**Summary:** The paper introduces CA-SQL, a novel pipeline designed to improve reasoning in Text-to-SQL tasks, particularly for challenging queries in the Bird-Bench benchmark. It utilizes a dynamic exploration strategy based on task difficulty and incorporates an innovative prompt seeding technique to enhance query generation. CA-SQL achieves a state-of-the-art score of 51.72% on difficult BIRD problems, outperforming other approaches while maintaining competitive execution accuracy and F1 scores.

### 3. Reinforcement Learning for Exponential Utility: Algorithms and Convergence in Discounted MDPs
**Authors:** Gugan Thoppe, L. A. Prashanth, Ankur Naskar, Sanjay Bhat
**Link:** https://arxiv.org/abs/2605.08053v1
**Summary:** This paper addresses the lack of value-based reinforcement learning algorithms for optimizing exponential utility in discounted Markov decision processes. The authors derive two Q-value-style extensions with contraction properties, leading to the development of two model-free algorithms that demonstrate almost-sure convergence and finite-time convergence rates, despite challenges in the one-timescale algorithm. Their work establishes a foundational framework for applying value-based RL methods to exponential-utility objectives.

### 4. Accurate and Efficient Statistical Testing for Word Semantic Breadth
**Authors:** Yo Ehara
**Link:** https://arxiv.org/abs/2605.08048v1
**Summary:** The paper addresses the challenge of accurately comparing the semantic breadth of words using contextualized embeddings, which can yield misleading results due to the influence of directional differences. The authors propose a novel permutation test based on Householder reflections that effectively isolates true differences in word breadth from these directional effects, while also enhancing computational efficiency through a GPU-optimized implementation. Their method significantly reduces false positives in statistical tests and allows for faster processing times.

### 5. Uncertainty-Aware Structured Data Extraction from Full CMR Reports via Distilled LLMs
**Authors:** Yi Yu, Parker Martin, Zhenyu Bu, Yixuan Liu, Yi-Yu Zheng, Orlando Simonetti, Yuchi Han, Yuan Xue
**Link:** https://arxiv.org/abs/2605.08045v1
**Summary:** The paper addresses the challenge of converting free-text cardiac magnetic resonance (CMR) reports into structured data for better clinical use. It introduces CMR-EXTR, a framework that uses a teacher-student distillation method to perform this task offline while also providing confidence levels for each extracted data field. The key result is a high variable-level accuracy of 99.65%, marking the first CMR-specific extraction system to incorporate confidence estimation.

### 6. Fast Byte Latent Transformer
**Authors:** Julie Kallini, Artidoro Pagnoni, Tomasz Limisiewicz, Gargi Ghosh, Luke Zettlemoyer, Christopher Potts, Xiaochuang Han, Srinivasan Iyer
**Link:** https://arxiv.org/abs/2605.08044v1
**Summary:** The paper presents the Byte Latent Transformer (BLT), a new model that improves the slow generation speed of byte-level language models, which previously generated text one byte at a time. The authors introduce innovative training and generation techniques, including a diffusion-based approach that allows for parallel byte generation, as well as methods that enhance quality without significantly sacrificing speed. Key contributions include notable reductions in memory bandwidth costs during generation and practical solutions that enhance the usability of byte-level models.

### 7. SCOPE: Structured Decomposition and Conditional Skill Orchestration for Complex Image Generation
**Authors:** Tianfei Ren, Zhipeng Yan, Yiming Zhao, Zhen Fang, Yu Zeng, Guohui Zhang, Hang Xu, Xiaoxiao Ma, Shiting Huang, Ke Xu, Wenxuan Huang, Lionel Z. Wang, Lin Chen, Zehui Chen, Jie Huang, Feng Zhao
**Link:** https://arxiv.org/abs/2605.08043v1
**Summary:** The paper addresses the challenge of maintaining consistency in complex image generation tasks, where various visual requirements can easily become misaligned. The authors introduce SCOPE, a framework that systematically tracks these requirements (referred to as semantic commitments) throughout the generation process by orchestrating retrieval, reasoning, and repair skills as needed. Their results show that SCOPE significantly outperforms existing methods in a new benchmark, highlighting its effectiveness in ensuring that intended imagery accurately reflects specified requirements.

### 8. Beyond Pairs: Your Language Model is Secretly Optimizing a Preference Graph
**Authors:** Ning Liu, Chuanneng Sun, Kristina Klinkner, Shervin Malmasi
**Link:** https://arxiv.org/abs/2605.08037v1
**Summary:** The paper addresses the limitations of pairwise preference comparisons in aligning language models, which often overlook the richer preference structures present in training data. The authors propose Graph Direct Preference Optimization (GraphDPO), a method that utilizes directed acyclic preference graphs to optimize language model alignment more effectively. Their experiments show that this approach enhances performance in various tasks, demonstrating that leveraging graph structures for preference modeling is a powerful alternative to traditional methods.

### 9. Don't Get Your Kroneckers in a Twist: Gaussian Processes on High-Dimensional Incomplete Grids
**Authors:** Mads Greisen Højlund, August Smart Lykke-Møller, Henry Moss, Ove Christiansen
**Link:** https://arxiv.org/abs/2605.08036v1
**Summary:** The paper presents CUTS-GPR, a novel approach for efficient Gaussian process regression in high-dimensional spaces where traditional methods struggle due to computational demands. By utilizing an additive kernel and an incomplete grid, CUTS-GPR achieves rapid kernel matrix-vector products, enabling effective modeling of complex data sets with billions of points and thousands of dimensions. The method successfully allows for fast and accurate Bayesian modeling of potential energy surfaces in computational chemistry, addressing a significant challenge in the field.

### 10. PropSplat: Map-Free RF Field Reconstruction via 3D Gaussian Propagation Splatting
**Authors:** William Bjorndahl, Maninder Pal Singh, Farhad Nouri, Joseph Camp
**Link:** https://arxiv.org/abs/2605.08035v1
**Summary:** The paper addresses the challenge of creating accurate radio frequency (RF) propagation models without relying on detailed geographic maps or extensive measurement campaigns, which are often prohibitively expensive. The authors introduce PropSplat, a method that utilizes 3D Gaussian primitives to reconstruct RF fields by optimizing path loss over observed transmitter-receiver paths. This approach significantly outperforms existing methods in both outdoor and indoor scenarios, demonstrating that effective RF modeling can be achieved from sparse data without the need for comprehensive geographic information.

---
## 2026-05-12

### 1. ELF: Embedded Language Flows
**Authors:** Keya Hu, Linlu Qiu, Yiyang Lu, Hanhong Zhao, Tianhong Li, Yoon Kim, Jacob Andreas, Kaiming He
**Link:** https://arxiv.org/abs/2605.10938v1
**Summary:** The paper introduces Embedded Language Flows (ELF), a new class of language models that enhance diffusion processes by operating primarily in a continuous embedding space before converting to discrete tokens at the final step. By adapting techniques from image diffusion models, ELF significantly improves generation quality and efficiency, outperforming leading language models with fewer sampling steps. This approach demonstrates a promising direction for developing more effective continuous diffusion language models.

### 2. Variational Inference for Lévy Process-Driven SDEs via Neural Tilting
**Authors:** Yaman Kindap, Manfred Opper, Benjamin Dupuis, Umut Simsekli, Tolga Birdal
**Link:** https://arxiv.org/abs/2605.10934v1
**Summary:** The paper addresses the challenge of performing Bayesian inference in Lévy-driven stochastic differential equations, which are important for modeling extreme events and heavy-tailed phenomena. The authors propose a novel neural exponential tilting framework that uses neural networks to adjust the Lévy measure, allowing for more accurate and scalable inference while preserving the jump characteristics typical of these processes. Their approach shows significant improvements in capturing jump dynamics and providing reliable posteriors compared to traditional Gaussian-based methods, validated through experiments on both synthetic and real-world data.

### 3. DECO: Sparse Mixture-of-Experts with Dense-Comparable Performance on End-Side Devices
**Authors:** Chenyang Song, Weilin Zhao, Xu Han, Chaojun Xiao, Yingfa Chen, Zhiyuan Liu
**Link:** https://arxiv.org/abs/2605.10933v1
**Summary:** The paper introduces DECO, a sparse Mixture-of-Experts architecture that aims to achieve the performance of dense Transformers while using significantly fewer computational resources, making it suitable for deployment on end-side devices. By utilizing a novel routing mechanism and a new activation function, DECO activates only 20% of its experts yet matches or exceeds the performance of traditional dense models. Additionally, a specialized acceleration kernel developed for DECO offers a threefold increase in processing speed on real hardware compared to dense inference.

### 4. Quantifying Concentration Phenomena of Mean-Field Transformers in the Low-Temperature Regime
**Authors:** Albert Alcalde, Leon Bungert, Konstantin Riedl, Tim Roith
**Link:** https://arxiv.org/abs/2605.10931v1
**Summary:** This paper investigates how tokens in deep encoder-only transformers evolve during inference, particularly as the number of tokens increases, by using a mean-field continuity equation to describe their behavior. The authors prove that the token distribution quickly becomes concentrated around a specific limiting distribution influenced by the model parameters and remains stable over a moderate time scale. Their findings are supported by numerical experiments, which also reveal that for longer time periods, the dynamics shift to a new phase affected by the value matrix's spectral properties.

### 5. Dynamic Skill Lifecycle Management for Agentic Reinforcement Learning
**Authors:** Junhao Shen, Teng Zhang, Xiaoyan Zhao, Hong Cheng
**Link:** https://arxiv.org/abs/2605.10923v1
**Summary:** The paper addresses the challenge of efficiently managing external skills in reinforcement learning agents to optimize their performance on complex tasks. It introduces a framework called SLIM that dynamically adjusts the active skill set based on their effectiveness, allowing agents to retain valuable skills, retire those that are no longer useful, and expand their capabilities when needed. The key finding is that SLIM significantly improves performance over existing methods, demonstrating that not all skills need to be internalized into the agent's policy, thus enhancing the overall flexibility and effectiveness of skill utilization in reinforcement learning.

### 6. Optimal and Scalable MAPF via Multi-Marginal Optimal Transport and Schrödinger Bridges
**Authors:** Usman A. Khan, Joseph W. Durham
**Link:** https://arxiv.org/abs/2605.10917v1
**Summary:** The paper addresses the problem of multi-agent path finding (MAPF) for robots navigating to targets on a graph, proposing a new approach that treats MAPF as a type of multi-marginal optimal transport (MMOT) problem. They show that this problem can be simplified into a manageable linear program and further enhance scalability by using a probabilistic method called Schrödinger bridges, which streamlines the solution process. The key contribution is the demonstration that their approach yields optimal and efficient paths for numerous robots without overlap in both space and time, even in large-scale scenarios.

### 7. Confidence-Guided Diffusion Augmentation for Enhanced Bangla Compound Character Recognition
**Authors:** Md. Sultan Al Rayhan, Maheen Islam
**Link:** https://arxiv.org/abs/2605.10916v1
**Summary:** This paper addresses the difficulty of recognizing handwritten Bangla compound characters, which are complex and varied due to their intricate structures and limited training data. The authors introduce a confidence-guided diffusion augmentation technique that synthesizes high-quality character samples using a combination of diffusion modeling and classifier guidance, along with a filtering mechanism for quality control. Their approach significantly improves recognition performance, achieving 89.2% accuracy on the AIBangla dataset, which is a notable advancement over previous benchmarks.

### 8. Shepherd: A Runtime Substrate Empowering Meta-Agents with a Formalized Execution Trace
**Authors:** Simon Yu, Derek Chong, Ananjan Nandi, Dilara Soylu, Jiuding Sun, Christopher D Manning, Weiyan Shi
**Link:** https://arxiv.org/abs/2605.10913v1
**Summary:** The paper presents Shepherd, a functional programming model designed to enhance the efficiency and effectiveness of meta-agents through a structured framework for recording and replaying interactions with their environment. By utilizing a Git-like execution trace, Shepherd enables rapid forking and replay of agent processes, resulting in significant performance improvements across various applications, such as increasing coding pass rates and optimizing exploration strategies in reinforcement learning. The system is open-sourced to facilitate ongoing research in this area.

### 9. WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation
**Authors:** Shuangrui Ding, Xuanlang Dai, Long Xing, Shengyuan Ding, Ziyu Liu, Yang JingYi, Penghui Yang, Zhixiong Zhang, Xilin Wei, Xinyu Fang, Yubo Ma, Haodong Duan, Jing Shao, Jiaqi Wang, Dahua Lin, Kai Chen, Yuhang Zang
**Link:** https://arxiv.org/abs/2605.10912v1
**Summary:** The paper introduces WildClawBench, a benchmark designed to assess the performance of AI agents in realistic, long-horizon tasks within their actual runtime environments, moving away from traditional synthetic benchmarks. It features 60 bilingual tasks that run in a Docker container with real command-line interfaces, incorporating both deterministic and semantic evaluation methods. The key finding reveals that even leading models like Claude Opus 4.7 only achieve a 62.2% success rate, indicating significant challenges in effectively evaluating agent performance over extended tasks.

### 10. Equivariant Reinforcement Learning for Clifford Quantum Circuit Synthesis
**Authors:** Richie Yeung, Aleks Kissinger, Rob Cornish
**Link:** https://arxiv.org/abs/2605.10910v1
**Summary:** The paper addresses the challenge of synthesizing Clifford quantum circuits, which are crucial for quantum computing, particularly in fully connected qubit systems. The authors developed a reinforcement learning approach using a specially designed neural network that can adapt to different qubit configurations. Their key contribution is an agent that can efficiently find near-optimal or optimal circuit solutions for qubits, demonstrating significantly better performance than existing synthesis methods even for larger circuits.

---
## 2026-05-12

### 1. Revisiting Policy Gradients for Restricted Policy Classes: Escaping Myopic Local Optima with $k$-step Policy Gradients
**Authors:** Alex DeWeese, Guannan Qu
**Link:** https://arxiv.org/abs/2605.10909v1
**Summary:** This paper addresses the issue of standard policy gradient methods getting stuck in suboptimal solutions when using restricted policy classes due to their one-step, myopic nature. The authors propose a generalized $k$-step policy gradient method that integrates multi-step decision-making to effectively escape these local optima. Their key contribution is a theoretical guarantee that this approach can converge to near-optimal solutions in a significantly shorter number of iterations while avoiding common pitfalls linked to distribution mismatches.

### 2. Engineering Robustness into Personal Agents with the AI Workflow Store
**Authors:** Roxana Geambasu, Mariana Raykova, Pierre Tholoniat, Trishita Tiwari, Lillian Tsai, Wen Zhang
**Link:** https://arxiv.org/abs/2605.10907v1
**Summary:** This paper addresses the problem of the reliability and security of AI agents that currently operate in an "on-the-fly" manner, which can lead to untested and vulnerable responses. The authors propose the integration of rigorous software engineering processes into the development of AI agents, advocating for the creation of a reusable repository of reliable "AI workflows" instead. Their key contribution is the outline of a vision for an AI Workflow Store, which would allow for more robust and secure agent operations, thereby overcoming the challenges posed by the current rapid synthesis paradigm.

### 3. DataMaster: Towards Autonomous Data Engineering for Machine Learning
**Authors:** Yaxin Du, Xiyuan Yang, Zhifan Zhou, Wanxu Liu, Zixing Lei, Zimeng Chen, Fenyi Liu, Haotian Wu, Yuzhu Cai, Zexi Liu, Xinyu Zhu, WenHao Wang, Linfeng Zhang, Chen Qian, Siheng Chen
**Link:** https://arxiv.org/abs/2605.10906v1
**Summary:** The paper presents DataMaster, an autonomous data engineering framework designed to enhance machine learning by optimizing data selection and transformation without changing the underlying learning algorithm. By employing a structured search process and utilizing a shared data repository, DataMaster improves the quality of training data and consequently boosts the performance of ML models. In evaluations, DataMaster achieved a 32.27% improvement in performance on MLE-Bench Lite and outperformed existing models on the PostTrainBench dataset.

### 4. Beyond Red-Teaming: Formal Guarantees of LLM Guardrail Classifiers
**Authors:** Nikita Kezins, Urbas Ekka, Pascal Berrang, Luca Arnaboldi
**Link:** https://arxiv.org/abs/2605.10901v1
**Summary:** The paper addresses the lack of formal guarantees for Guardrail Classifiers that aim to prevent harmful behavior in language models. The authors propose a novel verification method that shifts the analysis to the pre-activation space of classifiers, defining harmful regions and using geometric structures for certification. Their findings reveal that while some classifiers perform well in practice, significant safety gaps exist, particularly in the BERT model, highlighting the need for more reliable safety measures beyond conventional testing methods.

### 5. RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards
**Authors:** Gaotang Li, Bhavana Dalvi Mishra, Zifeng Wang, Jun Yan, Yanfei Chen, Chun-Liang Li, Long T. Le, Rujun Han, George Lee, Hanghang Tong, Chen-Yu Lee, Tomas Pfister
**Link:** https://arxiv.org/abs/2605.10899v1
**Summary:** The paper addresses the challenge of enhancing deep research agents, which struggle with tasks that lack clear rewards and ground-truth answers, by introducing the RubricEM framework. This approach utilizes rubrics not just for evaluation but as a structured guide for policy execution and feedback, combining stagewise policy decomposition with a reflection-based meta-policy evolution process. The key contribution is the development of RubricEM-8B, which achieves superior performance on long-form research tasks compared to existing models, demonstrating the effectiveness of rubric-guided learning for complex decision-making.

### 6. V4FinBench: Benchmarking Tabular Foundation Models, LLMs, and Standard Methods on Corporate Bankruptcy Prediction
**Authors:** Marcin Kostrzewa, Sebastian Tomczak, Roman Furman, Anna Poberezhna, Michał Furgała, Oleksii Furman, Maciej Zięba
**Link:** https://arxiv.org/abs/2605.10896v1
**Summary:** The paper introduces V4FinBench, a large benchmark dataset for predicting corporate bankruptcy, addressing the lack of extensive public datasets in this domain. It includes over one million records and aims to evaluate various prediction models, including tabular methods and foundation models, under realistic conditions of class imbalance. The key finding shows that with appropriate finetuning, a tabular model outperforms traditional methods, while a foundation model struggles, highlighting the effectiveness of tailored approaches in financial distress prediction.

### 7. Grounded or Guessing? LVLM Confidence Estimation via Blind-Image Contrastive Ranking
**Authors:** Reza Khanmohammadi, Erfan Miahi, Simerjot Kaur, Charese H. Smiley, Ivan Brugere, Kundan Thind, Mohammad M. Ghassemi
**Link:** https://arxiv.org/abs/2605.10893v1
**Summary:** The paper addresses the issue of visual ungroundedness in large vision-language models (LVLMs), where models may provide confident, yet misleading answers based solely on language rather than visual input. The authors propose a method called BICR (Blind-Image Contrastive Ranking), which trains a lightweight probe to assess the reliability of predictions by comparing model responses to real images against blacked-out views of those images. BICR outperforms existing confidence estimation methods in both accuracy and efficiency, achieving better calibration and discrimination with significantly fewer parameters than competing approaches.

### 8. Unmasking On-Policy Distillation: Where It Helps, Where It Hurts, and Why
**Authors:** Mohammadreza Armandpour, Fatih Ilhan, David Harrison, Ajay Jaiswal, Duc N. M Hoang, Fartash Faghri, Yizhe Zhang, Minsik Cho, Mehrdad Farajtabar
**Link:** https://arxiv.org/abs/2605.10889v1
**Summary:** The paper addresses the challenges of determining when on-policy distillation is beneficial or harmful for training reasoning models. The authors introduce a diagnostic framework that analyzes the effectiveness of distillation on a per-token basis, allowing them to assess the quality of the supervisory signal provided by teacher models. They discover that distillation is more aligned with ideal guidance for incorrect outputs than correct ones, highlighting the need for tailored analyses based on model capacity and task specificity.

### 9. Shields to Guarantee Probabilistic Safety in MDPs
**Authors:** Linus Heck, Filip Macák, Roman Andriushchenko, Milan Češka, Sebastian Junges
**Link:** https://arxiv.org/abs/2605.10888v1
**Summary:** This paper addresses the challenge of ensuring safety for autonomous agents operating under uncertainty by extending classical shielding techniques to probabilistic safety scenarios, where some risks are acceptable. The authors develop a formal framework that elucidates the limitations of maintaining strong safety guarantees while also proposing offline and online methods for creating effective shields with weaker assurances. The results demonstrate that these new shields are both practical and computationally feasible, offering significant advantages for real-world applications.

### 10. LoKA: Low-precision Kernel Applications for Recommendation Models At Scale
**Authors:** Liang Luo, Yinbin Ma, Quanyu Zhu, Vasiliy Kuznetsov, Yuxin Chen, Jian Jiao, Jiecao Yu, Buyun Zhang, Tongyi Tang, Xiaohan Wei, Yanli Zhao, Zeliang Chen, Yuchen Hao, Venkatesh Ranganathan, Sandeep Parab, Yantao Yao, Maxim Naumov, Chunzhi Yang, Shen Li, Ellie Wen, Wenlin Chen, Santanu Kolay, Chunqiang Tang
**Link:** https://arxiv.org/abs/2605.10886v1
**Summary:** The paper addresses the challenges of using low-precision FP8 arithmetic in large recommendation models, which are sensitive to numerical precision and require careful handling to maintain quality and efficiency. The authors introduce LoKA, a framework that utilizes profiling to identify where FP8 can be safely applied, adapts model components for better performance, and optimizes kernel selection at runtime. Key contributions include a benchmarking method to evaluate precision trade-offs and a set of model adaptations that enhance stability and efficiency when using FP8 in recommendation systems.

---
## 2026-05-14

### 1. AlphaGRPO: Unlocking Self-Reflective Multimodal Generation in UMMs via Decompositional Verifiable Reward
**Authors:** Runhui Huang, Jie Wu, Rui Yang, Zhe Liu, Hengshuang Zhao
**Link:** https://arxiv.org/abs/2605.12495v1
**Summary:** The paper presents AlphaGRPO, a new framework that enhances the capabilities of Unified Multimodal Models (UMMs) for complex tasks like text-to-image generation and output refinement, without requiring an initial training phase. By introducing a Decompositional Verifiable Reward system that breaks down user requests into manageable components for evaluation, the framework achieves significant performance improvements in multimodal generation benchmarks and editing tasks. This self-reflective approach effectively leverages the model's inherent understanding to produce higher-quality outputs.

### 2. LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues
**Authors:** Di Wu, Zixiang Ji, Asmi Kawatkar, Bryan Kwan, Jia-Chen Gu, Nanyun Peng, Kai-Wei Chang
**Link:** https://arxiv.org/abs/2605.12493v1
**Summary:** The paper introduces LongMemEval-V2, a benchmark designed to assess how well memory systems in agents can retain and utilize experience in specialized web environments. It evaluates five key memory abilities through 451 curated questions and compares two memory methods: AgentRunbook-R and AgentRunbook-C, where the latter significantly outperformed existing baselines with an average accuracy of 72.5%, despite facing high latency issues. This work establishes LME-V2 as a valuable tool for advancing long-term memory systems in agents.

### 3. Pion: A Spectrum-Preserving Optimizer via Orthogonal Equivalence Transformation
**Authors:** Kexuan Shi, Hanxuan Li, Zeju Qiu, Yandong Wen, Simon Buchholz, Weiyang Liu
**Link:** https://arxiv.org/abs/2605.12492v1
**Summary:** The paper presents Pion, a new optimizer designed for training large language models that maintains the singular values of weight matrices by using orthogonal transformations, as opposed to traditional additive methods. This approach helps preserve the spectral properties of the model while still allowing for effective updates during training. The authors demonstrate that Pion provides stable and competitive performance compared to standard optimizers in both the pretraining and finetuning phases.

### 4. Elastic Attention Cores for Scalable Vision Transformers
**Authors:** Alan Z. Song, Yinjie Chen, Mu Nan, Rui Zhang, Jiahang Cao, Weijian Mai, Muquan Yu, Hossein Adeli, Deva Ramanan, Michael J. Tarr, Andrew F. Luo
**Link:** https://arxiv.org/abs/2605.12491v1
**Summary:** The paper addresses the computational inefficiency of Vision Transformers (ViTs), which struggle with high-resolution images due to their quadratic scaling with the number of image patches. The authors introduce VECA (Visual Elastic Core Attention), an architecture that uses a small set of learned core tokens to facilitate communication among patches, reducing attention complexity to linear time while maintaining high accuracy. The key contribution is that VECA can achieve competitive performance with existing models while substantially lowering computational costs, making it a scalable option for ViTs.

### 5. Task-Adaptive Embedding Refinement via Test-time LLM Guidance
**Authors:** Ariel Gera, Shir Ashury-Tahan, Gal Bloch, Ohad Eytan, Assaf Toledo
**Link:** https://arxiv.org/abs/2605.12487v1
**Summary:** The paper addresses the challenge of improving the performance of embedding models in zero-shot search and classification tasks by refining user queries with guidance from a generative language model (LLM). The authors propose an LLM-guided query refinement method that adapts embedding representations in real-time, leading to significant performance improvements in various benchmarks. Key findings show that this approach enhances ranking quality and better aligns embeddings with the specific requirements of user queries, making it a valuable alternative for practical applications where large LLMs are impractical.

### 6. Learning, Fast and Slow: Towards LLMs That Adapt Continually
**Authors:** Rishabh Tiwari, Kusha Sareen, Lakshya A Agrawal, Joseph E. Gonzalez, Matei Zaharia, Kurt Keutzer, Inderjit S Dhillon, Rishabh Agarwal, Devvrit Khatri
**Link:** https://arxiv.org/abs/2605.12484v1
**Summary:** The paper addresses the issue of catastrophic forgetting in large language models (LLMs) when updating parameters for specific tasks, which limits their flexibility and adaptability. To overcome this, the authors propose a fast-slow learning framework that uses "fast" weights for task-specific adjustments while keeping the "slow" weights close to the base model. The key finding is that this Fast-Slow Training method is significantly more sample-efficient and minimizes forgetting, allowing for better adaptability in continual learning scenarios compared to traditional parameter-only updates.

### 7. Beyond GRPO and On-Policy Distillation: An Empirical Sparse-to-Dense Reward Principle for Language-Model Post-Training
**Authors:** Yuanda Xu, Hejian Sang, Zhengze Zhou, Ran He, Zhipeng Wang, Alborz Geramifard
**Link:** https://arxiv.org/abs/2605.12483v1
**Summary:** The paper addresses the inefficiency in allocating scarce labeled training data when fine-tuning language models by proposing a reward-density principle. It suggests using sparse rewards for exploration with a strong model (teacher) and then transferring that learned behavior as dense supervision to a smaller model (student). The key findings demonstrate that this strategy improves performance on verifiable tasks, significantly outperforming traditional methods like direct GRPO in specific benchmarks.

### 8. ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
**Authors:** Xuhao Hu, Xi Zhang, Haiyang Xu, Kyle Qiao, Jingyi Yang, Xuanjing Huang, Jing Shao, Ming Yan, Jieping Ye
**Link:** https://arxiv.org/abs/2605.12481v1
**Summary:** The paper presents ToolCUA, an innovative approach for optimizing the decision-making process of Computer Use Agents (CUAs) when choosing between GUI actions and tool calls, a challenge stemming from the lack of quality training data. To address this, the authors developed a method that synthesizes diverse GUI-Tool interactions from existing data and employs a tailored reinforcement learning strategy to enhance decision-making at critical junctures. The results indicate that ToolCUA achieves a 46.85% accuracy, outperforming previous models by a significant margin and demonstrating the effectiveness of training in a hybrid action framework.

### 9. OmniNFT: Modality-wise Omni Diffusion Reinforcement for Joint Audio-Video Generation
**Authors:** Guohui Zhang, XiaoXiao Ma, Jie Huang, Hang Xu, Hu Yu, Siming Fu, Yuming Li, Zeyue Xue, Lin Song, Haoyang Huang, Nan Duan, Feng Zhao
**Link:** https://arxiv.org/abs/2605.12480v1
**Summary:** The paper addresses the challenges of generating high-quality audio and video simultaneously, particularly focusing on maintaining fidelity, alignment, and synchronization across modalities. The authors present OmniNFT, a novel reinforcement learning framework that incorporates three main strategies to improve the generation process, including routing rewards per modality, managing gradient flow, and adjusting optimization efforts based on critical alignment areas. Extensive experiments show that OmniNFT significantly enhances the quality and synchronization of generated audio and video compared to existing methods.

### 10. MEME: Multi-entity & Evolving Memory Evaluation
**Authors:** Seokwon Jung, Alexander Rubinstein, Arnas Uselis, Sangdoo Yun, Seong Joon Oh
**Link:** https://arxiv.org/abs/2605.12477v1
**Summary:** The paper addresses the challenge of evaluating memory systems in language model-based agents that operate in environments requiring management of multiple entities and evolving information over time. The authors introduce the MEME benchmark, which includes six diverse tasks that assess memory performance, revealing that existing systems struggle with dependency reasoning despite performing well in static retrieval scenarios. A notable finding is that only a specific configuration of a file-based agent with a powerful LLM shows improved performance, although this method is significantly more costly, highlighting a gap in practical scalability.

---
## 2026-05-14

### 1. WARDEN: Endangered Indigenous Language Transcription and Translation with 6 Hours of Training Data
**Authors:** Ziheng Zhang, Yunzhong Hou, Naijing Liu, Liang Zheng
**Link:** https://arxiv.org/abs/2605.13846v1
**Summary:** The paper presents WARDEN, a language model specifically designed to transcribe and translate the endangered Wardaman language into English using only six hours of training data. To address the scarcity of large datasets, WARDEN employs separate models for transcription and translation, incorporating techniques like utilizing related phonemes from Sundanese and leveraging a Wardaman-English dictionary. The approach successfully outperforms conventional models that require more data, establishing a strong baseline for low-resource language processing.

### 2. EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents
**Authors:** Tara Bogavelli, Gabrielle Gauthier Melançon, Katrina Stankiewicz, Oluwanifemi Bamgbose, Fanny Riols, Hoang H. Nguyen, Raghav Mehndiratta, Lindsay Devon Brin, Joseph Marinier, Hari Subramani, Anil Madamala, Sridhar Krishna Nemala, Srinivas Sunkara
**Link:** https://arxiv.org/abs/2605.13841v1
**Summary:** The paper presents EVA-Bench, a new framework for evaluating voice agents that improves upon existing benchmarks by simulating realistic conversations and assessing various quality metrics. It introduces two composite metrics, EVA-A and EVA-X, to evaluate task completion and conversational quality, respectively, across different voice agent architectures. The key findings reveal that no evaluated system excels in both accuracy and user experience, highlighting significant robustness gaps in handling variations like accent and background noise.

### 3. What is Learnable in Valiant's Theory of the Learnable?
**Authors:** Steve Hanneke, Anay Mehrotra, Grigoris Velegkas, Manolis Zampetakis
**Link:** https://arxiv.org/abs/2605.13840v1
**Summary:** The paper revisits Valiant's original learning model from 1984, which differs from the PAC learning framework by allowing only positive samples and membership queries without false positives. The authors characterize learnability in this model, revealing that a class is learnable if positive samples can be efficiently certified via an adaptation of query-compression schemes. They demonstrate that learnability in this model is distinct from both PAC learning and a variant without queries, and provide a new algorithm for learning $d$-dimensional halfspaces with queries, marking a significant advancement in understanding Valiant's model of learnability.

### 4. Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights
**Authors:** Wenrui Bao, Huan Wang, Jian Wang, Zhangyang Wang, Kai Wang, Yuzhang Shang
**Link:** https://arxiv.org/abs/2605.13839v1
**Summary:** The paper addresses the inefficiencies of multi-agent large language model (LLM) systems that rely on natural language communication, which can slow down processing and increase memory usage. The authors propose TFlow (Thought Flow), a novel framework that allows agents to directly modify the receiver's weights during inference using low-rank perturbations instead of sending textual messages. This approach results in significant improvements in accuracy and a reduction in processed tokens and inference time, suggesting a more efficient method for agent collaboration.

### 5. R-DMesh: Video-Guided 3D Animation via Rectified Dynamic Mesh Flow
**Authors:** Zijie Wu, Lixin Xu, Puhua Jiang, Sicong Liu, Chunchao Guo, Xiang Bai
**Link:** https://arxiv.org/abs/2605.13838v1
**Summary:** The paper presents R-DMesh, a framework designed to tackle the challenge of aligning user-provided static meshes with reference videos for video-guided 3D animation, where initial pose mismatches can cause significant distortion. By utilizing a novel VAE to disentangle the mesh into a base shape, motion trajectories, and a rectification offset, and applying a Triflow Attention mechanism for processing, R-DMesh effectively rectifies the mesh pose before animation starts. The approach demonstrates strong performance in resolving pose misalignment and enables advanced applications like pose retargeting and comprehensive 4D mesh generation.

### 6. Topology-Preserving Neural Operator Learning via Hodge Decomposition
**Authors:** Dongzhe Zheng, Tao Zhong, Christine Allen-Blanchette
**Link:** https://arxiv.org/abs/2605.13834v1
**Summary:** This paper addresses the challenge of accurately learning solution operators for physical field equations on geometric meshes by using Hodge decomposition to separate learnable geometric dynamics from unlearnable topological features. The authors introduce a new architecture called Hodge Spectral Duality, which utilizes discrete differential forms to effectively capture topological elements and an auxiliary space for local dynamics. Their approach demonstrates improved accuracy and efficiency in modeling, while preserving important physical properties.

### 7. QLAM: A Quantum Long-Attention Memory Approach to Long-Sequence Token Modeling
**Authors:** Hoang-Quan Nguyen, Sankalp Pandey, Khoa Luu
**Link:** https://arxiv.org/abs/2605.13833v1
**Summary:** The paper addresses the challenge of modeling long-range dependencies in sequential data, where traditional transformers struggle due to their quadratic complexity. It introduces Quantum Long-Attention Memory (QLAM), a hybrid quantum-classical memory mechanism that leverages quantum superposition to enhance the representation of historical information while maintaining linear time complexity. QLAM demonstrates superior performance on sequential image classification tasks compared to both recurrent models and transformers.

### 8. Quantifying Sensitivity for Tree Ensembles: A symbolic and compositional approach
**Authors:** S. Akshay, Chaitanya Garg, Ashutosh Gupta, Kuldeep S. Meel, Ajinkya Naik
**Link:** https://arxiv.org/abs/2605.13830v1
**Summary:** The paper addresses the problem of quantifying sensitivity in decision tree ensembles, focusing on how small changes in input features might lead to misclassification. The authors present a new algorithm that uses algebraic decision diagrams to break down the problem and compute sensitivity efficiently, while ensuring a certified error and confidence bound. Their experimental results demonstrate that their tool, XCount, significantly outperforms existing methods in both speed and scalability for various ensemble sizes.

### 9. Negation Neglect: When models fail to learn negations in training
**Authors:** Harry Mayne, Lev McKinney, Jan Dubiński, Adam Karvonen, James Chua, Owain Evans
**Link:** https://arxiv.org/abs/2605.13829v1
**Summary:** The paper addresses the issue of "Negation Neglect," where fine-tuning large language models (LLMs) on documents that assert a claim is false leads the models to incorrectly believe the claim is true. The researchers conducted experiments showing that models significantly increased their belief in false claims when exposed to negated documents, demonstrating that the presence of negations in separate sentences does not effectively teach the models to learn these negations. A key finding is that this neglect not only affects factual claims but also influences model behaviors, raising concerns for AI safety.

### 10. Reducing cross-sample prediction churn in scientific machine learning
**Authors:** Gordan Prastalo, Kevin Maik Jablonka
**Link:** https://arxiv.org/abs/2605.13826v1
**Summary:** The paper addresses the issue of "cross-sample prediction churn" in scientific machine learning, where different models trained on the same dataset produce conflicting predictions for a significant number of test samples. The authors introduce two data-driven approaches to reduce this churn: $K$-bootstrap bagging, which significantly lowers churn rates without sacrificing accuracy, and a novel method called twin-bootstrap, which further decreases churn by applying a consistency loss between predictions of two jointly trained networks. The key contribution is demonstrating that these methods can effectively mitigate prediction inconsistencies, highlighting the importance of reporting churn alongside predictive performance in benchmarks.

---
## 2026-05-15

### 1. EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation
**Authors:** Ruozhen He, Meng Wei, Ziyan Yang, Vicente Ordonez
**Link:** https://arxiv.org/abs/2605.15199v1
**Summary:** The paper addresses the challenge of maintaining consistency of characters, objects, and locations in long multi-shot video generation. It introduces EntityBench, a benchmark with detailed entity tracking across a variety of narrative scenarios, and proposes EntityMem, a memory-augmented system that improves consistency by storing visual references for entities. The results demonstrate that using explicit per-entity memory significantly enhances character fidelity and presence in generated videos.

### 2. ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both
**Authors:** Ziyu Guo, Rain Liu, Xinyan Chen, Pheng-Ann Heng
**Link:** https://arxiv.org/abs/2605.15198v1
**Summary:** The paper presents ATLAS, a novel framework that combines agentic and latent visual reasoning using a single discrete 'functional token', which simplifies the process and avoids the complexities and inefficiencies of generating intermediate visual content. By allowing these tokens to operate without visual supervision and ensuring compatibility with existing training methods, ATLAS enhances performance on visual reasoning tasks while maintaining interpretability. The introduction of Latent-Anchored GRPO further improves training stability by providing stronger gradient updates, ultimately leading to superior results on challenging benchmarks.

### 3. RefDecoder: Enhancing Visual Generation with Conditional Video Decoding
**Authors:** Xiang Fan, Yuheng Wang, Bohan Fang, Zhongzheng Ren, Ranjay Krishna
**Link:** https://arxiv.org/abs/2605.15196v1
**Summary:** The paper addresses the issue of detail loss and inconsistency in video generation caused by decoders that lack sufficient conditioning on input images. It introduces RefDecoder, a video decoder that enhances quality by integrating high-fidelity reference images into the decoding process using reference attention. This approach significantly improves performance, achieving up to +2.1dB PSNR on various benchmarks and demonstrating better subject and background consistency in generated videos.

### 4. FutureSim: Replaying World Events to Evaluate Adaptive Agents
**Authors:** Shashwat Goel, Nikhil Chandak, Arvindh Arun, Ameya Prabhu, Steffen Staab, Moritz Hardt, Maksym Andriushchenko, Jonas Geiping
**Link:** https://arxiv.org/abs/2605.15188v1
**Summary:** The paper addresses the challenge of evaluating AI agents' ability to adapt to new information in dynamic environments by introducing FutureSim, a simulation that replays real-world events chronologically. This approach allows agents to forecast future events while interacting with a timeline of actual news and resolutions. The key finding reveals significant variability in agents' predictive capabilities, with the best performing agent achieving only 25% accuracy, highlighting the need for improved methods in long-term adaptation and reasoning under uncertainty.

### 5. VGGT-Edit: Feed-forward Native 3D Scene Editing with Residual Field Prediction
**Authors:** Kaixin Zhu, Yiwen Tang, Yifan Yang, Renrui Zhang, Bohan Zeng, Ziyu Guo, Ruichuan An, Zhou Liu, Qizhi Chen, Delin Qu, Jaehong Yoon, Wentao Zhang
**Link:** https://arxiv.org/abs/2605.15186v1
**Summary:** The paper presents VGGT-Edit, a novel framework for editing 3D scenes in response to text instructions without the need for traditional 2D editing methods, which often lead to poor visual quality. By using depth-synchronized text injection and a residual transformation head, it predicts direct 3D changes while maintaining consistent geometry and detail. Experiments demonstrate that VGGT-Edit significantly outperforms existing methods, providing sharper details and greater consistency across multiple views.

### 6. Quantitative Video World Model Evaluation for Geometric-Consistency
**Authors:** Jiaxin Wu, Yihao Pi, Yinling Zhang, Yuheng Li, Xueyan Zou
**Link:** https://arxiv.org/abs/2605.15185v1
**Summary:** The paper addresses the challenge of evaluating the geometric consistency of generative video models, as existing methods often rely on subjective judgments. The authors propose a quantitative framework called PDI-Bench, which assesses geometric coherence by analyzing 3D structural and motion characteristics using projective-geometry residuals. The key contribution is the introduction of systematic and objective metrics that reveal geometric failure modes in generated videos, which are not captured by traditional perceptual assessments, thereby advancing the evaluation of realistic video generation.

### 7. Is Grep All You Need? How Agent Harnesses Reshape Agentic Search
**Authors:** Sahil Sen, Akhil Kasturi, Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah
**Link:** https://arxiv.org/abs/2605.15184v1
**Summary:** This paper investigates the effectiveness of different information retrieval strategies in enhancing the performance of Large Language Model (LLM) agents during complex search tasks. It empirically compares traditional grep-based searching against vector retrieval methods across various agent harnesses. The key finding is that grep generally outperforms vector retrieval in accuracy, but results vary significantly based on the specific agent architecture and tool-calling approach used.

### 8. When Are Two Networks the Same? Tensor Similarity for Mechanistic Interpretability
**Authors:** ML Nissen Gonzalez, Melwina Albuquerque, Laurence Wroe, Jacob Meyer Cohen, Logan Riggs Smith, Thomas Dooms
**Link:** https://arxiv.org/abs/2605.15183v1
**Summary:** The paper addresses the challenge of determining when two neural network components perform the same computation, which is crucial for understanding their functionality. It introduces a new metric called tensor similarity that is invariant to weight-space symmetries and effectively measures the global equivalence of tensor-based models. The authors demonstrate that this metric better tracks functional training dynamics compared to existing similarity measures, simplifying the assessment of network similarity and interpretability.

### 9. Eradicating Negative Transfer in Multi-Physics Foundation Models via Sparse Mixture-of-Experts Routing
**Authors:** Ellwil Sharma, Arastu Sharma
**Link:** https://arxiv.org/abs/2605.15179v1
**Summary:** The paper addresses the challenge of negative transfer in multi-physics foundation models, where training on diverse physical regimes can lead to optimization issues. The authors propose Shodh-MoE, a sparse mixture-of-experts architecture that dynamically routes data to specialized subnetworks based on physical mechanisms, while ensuring mass conservation in fluid dynamics. They demonstrate that this approach allows the model to train effectively across different physical domains, achieving low mean squared errors in validation metrics.

### 10. OpenDeepThink: Parallel Reasoning via Bradley--Terry Aggregation
**Authors:** Shang Zhou, Wenhao Chai, Kaiyuan Liu, Huanzhi Mao, Qiuyang Mang, Jingbo Shang
**Link:** https://arxiv.org/abs/2605.15177v1
**Summary:** The paper presents OpenDeepThink, a framework designed to enhance the reasoning capabilities of large language models (LLMs) during test-time by using parallel candidate evaluation and selection. It employs a pairwise comparison method based on the Bradley-Terry model to rank multiple reasoning outputs and improve selection efficiency without ground-truth supervision. The key result shows a significant boost in performance—specifically, an increase of 405 Elo points for the Gemini 3.1 Pro model in competitive programming tasks, with the approach demonstrating effective transferability across various model strengths.

---
## 2026-05-16

### 1. MetaBackdoor: Exploiting Positional Encoding as a Backdoor Attack Surface in LLMs
**Authors:** Rui Wen, Mark Russinovich, Andrew Paverd, Jun Sakuma, Ahmed Salem
**Link:** https://arxiv.org/abs/2605.15172v1
**Summary:** The paper addresses the security vulnerability of large language models (LLMs) to backdoor attacks, which traditionally rely on modifying the input text. The authors introduce a novel backdoor attack, called MetaBackdoor, that exploits the positional encoding used in these models, allowing attackers to trigger malicious behavior without altering the text itself. Key findings demonstrate that even simple positional cues can effectively activate hidden backdoors, revealing sensitive information and enabling attacks that can occur without direct manipulation of the input.

### 2. Evidential Reasoning Advances Interpretable Real-World Disease Screening
**Authors:** Chenyu Lian, Hong-Yu Zhou, Jing Qin
**Link:** https://arxiv.org/abs/2605.15171v1
**Summary:** The paper addresses the problem of limited interpretability and performance in current disease screening models for medical images. It presents EviScreen, an evidential reasoning framework that incorporates historical case evidence to improve both the accuracy of predictions and the transparency of the reasoning process. The key contribution is that EviScreen achieves better disease screening outcomes, particularly in terms of clinical specificity and recall, while also enhancing interpretability through a novel approach to abnormality localization.

### 3. Text Knows What, Tables Know When: Clinical Timeline Reconstruction via Retrieval-Augmented Multimodal Alignment
**Authors:** Sayantan Kumar, Shahriar Noroozizadeh, Juyong Kim, Jeremy C. Weiss
**Link:** https://arxiv.org/abs/2605.15168v1
**Summary:** The paper addresses the challenge of accurately reconstructing clinical timelines, which are crucial for understanding patient conditions like sepsis. The authors propose a novel framework that combines unstructured clinical narratives with structured electronic health record (EHR) data, using a graph-based method to align and enhance temporal precision. Their results show that this multimodal approach significantly improves the accuracy of timestamps and provides a more comprehensive view of patient events compared to using text alone, revealing that many important events are missing from EHR data.

### 4. Position: Behavioural Assurance Cannot Verify the Safety Claims Governance Now Demands
**Authors:** Pratinav Seth, Vinay Kumar Sankarapu
**Link:** https://arxiv.org/abs/2605.15164v1
**Summary:** This paper addresses the problem that current behavioral assurance methods cannot effectively verify the safety claims required by new AI governance frameworks, which demand proof of aspects like hidden objectives and long-term safety. The authors introduce the concept of the "audit gap," highlighting the limitations of existing methodologies and propose a shift to include more mechanistic types of evidence alongside behavioral assessments. Their key contribution is a formal analysis of the mismatch between safety claims and the capabilities of current assurance practices, advocating for a more balanced approach to evidence in AI safety governance.

### 5. Hand-in-the-Loop: Improving Dexterous VLA via Seamless Interventional Correction
**Authors:** Zhuohang Li, Liqun Huang, Wei Xu, Zhengming Zhu, Nie Lin, Xiao Ma, Xinjun Sheng, Ruoshi Wen
**Link:** https://arxiv.org/abs/2605.15157v1
**Summary:** The paper addresses the issue of errors in dexterous manipulation by robotic hands, which can be exacerbated during human intervention due to mismatches in control commands. The authors introduce a method called Hand-in-the-Loop (HandITL) that seamlessly combines human corrections with automated actions, significantly reducing abrupt movements and improving manipulation performance. The key findings demonstrate that HandITL not only minimizes errors during human takeovers but also leads to better-trained policies, improving success rates and efficiency in complex tasks.

### 6. MeMo: Memory as a Model
**Authors:** Ryan Wei Heng Quek, Sanghyuk Lee, Alfred Wei Lun Leong, Arun Verma, Alok Prakash, Nancy F. Chen, Bryan Kian Hsiang Low, Daniela Rus, Armando Solar-Lezama
**Link:** https://arxiv.org/abs/2605.15156v1
**Summary:** The paper addresses the challenge of updating large language models (LLMs) with new, domain-specific knowledge without modifying their existing parameters. It presents MeMo (Memory as a Model), a modular framework that encodes new information into a separate memory system, allowing for efficient integration and robust performance across complex tasks. Experimental results demonstrate that MeMo outperforms existing methods while preventing issues like catastrophic forgetting and maintaining retrieval efficiency regardless of the corpus size.

### 7. Self-Distilled Agentic Reinforcement Learning
**Authors:** Zhengxi Lu, Zhiyuan Yao, Zhuowen Han, Zi-Han Wang, Jinyang Wu, Qi Gu, Xunliang Cai, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
**Link:** https://arxiv.org/abs/2605.15155v1
**Summary:** The paper addresses the challenge of providing fine-grained supervision for long-horizon tasks in reinforcement learning (RL) for multi-turn dialogue agents, which often suffer from instability. The authors propose a new approach called Self-Distilled Agentic Reinforcement Learning (SDAR), which integrates On-Policy Self-Distillation (OPSD) as a gated auxiliary objective alongside traditional RL to improve learning stability and performance. Key results demonstrate that SDAR significantly outperforms existing methods on various benchmarks, achieving notable gains in task performance while mitigating instability issues.

### 8. RoSHAP: A Distributional Framework and Robust Metric for Stable Feature Attribution
**Authors:** Lanxin Xiang, Liang Shi, Youhui Ye, Boyu Jiang, Dawei Zhou, Feng Guo
**Link:** https://arxiv.org/abs/2605.15154v1
**Summary:** This paper addresses the issue of inconsistent feature attribution in machine learning, where different runs can yield varying importance scores for the same features. The authors introduce RoSHAP, a robust metric that utilizes bootstrap resampling and kernel density estimation to model the distribution of feature attribution scores, providing a stable ranking of features. Their key finding is that RoSHAP outperforms traditional methods in identifying important features while allowing for effective model building with fewer predictors, enhancing both stability and interpretability in model analysis.

### 9. Pelican-Unified 1.0: A Unified Embodied Intelligence Model for Understanding, Reasoning, Imagination and Action
**Authors:** Yi Zhang, Yinda Chen, Che Liu, Zeyuan Ding, Jin Xu, Shilong Zou, Junwei Liao, Jiayu Hu, Xiancong Ren, Xiaopeng Zhang, Yechi Liu, Haoyuan Shi, Zecong Tang, Haosong Sun, Renwen Cui, Kuishu Wu, Wenhai Liu, Yang Xu, Yingji Zhang, Yidong Wang, Senkang Hu, Jinpeng Lu, Nga Teng Chan, Yechen Wu, Yong Dai, Jian Tang, Xiaozhu Ju
**Link:** https://arxiv.org/abs/2605.15153v1
**Summary:** The paper introduces Pelican-Unified 1.0, a novel embodied foundation model designed to integrate understanding, reasoning, imagination, and action into a single framework. By employing a unified vision-language model that processes and optimizes these capabilities together, it outperforms existing systems on multiple benchmarks. The key contribution is demonstrating that this unified approach can achieve strong performance across various tasks without sacrificing the specialized strengths of individual capabilities.

### 10. Widening the Gap: Exploiting LLM Quantization via Outlier Injection
**Authors:** Xiaohua Zhan, Kazuki Egashira, Robin Staab, Mark Vero, Martin Vechev
**Link:** https://arxiv.org/abs/2605.15152v1
**Summary:** This paper addresses the security vulnerabilities in large language models (LLMs) that arise from quantization, which is often used for efficient deployment. The authors present a novel attack method that exploits the injection of outliers into model weights, causing significant and predictable behavior changes during quantization. Their findings reveal that advanced quantization techniques are susceptible to these attacks, highlighting a broader scope of security risks than previously recognized.

---
## 2026-05-17

### 1. Forgetting That Sticks: Quantization-Permanent Unlearning via Circuit Attribution
**Authors:** Saisab Sadhu, Pratinav Seth, Vinay Kumar Sankarapu
**Link:** https://arxiv.org/abs/2605.15138v1
**Summary:** The paper addresses the problem of effective unlearning in quantized language models, where traditional methods struggle to achieve meaningful forgetting due to the compression effects of quantization. The authors propose a novel approach called MANSU (Mechanistic-Aligned Null-Space Unlearning) that uses causal circuit attribution and a specialized projection technique to isolate and forget specific information while maintaining the model's performance and compliance with quantization. Key findings show that MANSU successfully achieves significant forgetting without sacrificing model accuracy or structural integrity, outperforming existing gradient-based methods in various tests.

### 2. Training ML Models with Predictable Failures
**Authors:** Will Schwarzer, Scott Niekum
**Link:** https://arxiv.org/abs/2605.15134v1
**Summary:** The paper addresses the challenge of predicting failure rates for machine learning models at deployment scale, particularly when evaluation sets are too small to capture rare failures. The authors introduce a new fine-tuning objective called forecastability loss, which corrects biases in existing failure prediction methods. Their experiments demonstrate that this approach significantly reduces prediction errors while maintaining the model's main performance and ensuring safety comparable to traditional supervised methods.

### 3. Causal Foundation Models with Continuous Treatments
**Authors:** Christopher Stith, Medha Barath, Vahid Balazadeh, Jesse C. Cresswell, Rahul G. Krishnan
**Link:** https://arxiv.org/abs/2605.15133v1
**Summary:** The paper addresses the challenge of estimating causal effects in situations where treatments vary continuously, which is less commonly studied than binary treatments. The authors introduce a novel causal foundation model that utilizes a transformer to predict treatment-response curves from observational data without requiring additional training on new tasks. Their approach outperforms existing causal models in reconstructing treatment-response curves, representing a significant advancement in causal inference methods for continuous treatment scenarios.

### 4. APWA: A Distributed Architecture for Parallelizable Agentic Workflows
**Authors:** Evan Rose, Tushin Mallick, Matthew D. Laws, Cristina Nita-Rotaru, Alina Oprea
**Link:** https://arxiv.org/abs/2605.15132v1
**Summary:** The paper addresses the challenges faced by autonomous multi-agent systems using large language models (LLMs) when processing complex tasks, specifically issues with reasoning, coordination, and computational scaling. The authors propose the Agent-Parallel Workload Architecture (APWA), which decomposes workflows into non-interfering subproblems that can be executed in parallel, allowing for efficient processing across various domains. The results show that APWA effectively scales with larger tasks and can dynamically handle complex queries, outperforming previous systems.

### 5. Natural Synthesis: Outperforming Reactive Synthesis Tools with Large Reasoning Models
**Authors:** Frederik Schmitt, Matthias Cosler, Niklas Metzger, Julian Siber, Vladimir Krsmanovic, Mohamed Ghanem, Bernd Finkbeiner
**Link:** https://arxiv.org/abs/2605.15131v1
**Summary:** This paper addresses the challenging problem of reactive synthesis, which involves automatically creating hardware circuits from complex logical specifications. The authors introduce a neuro-symbolic approach that combines advanced reasoning models with model checking to improve Verilog implementations and offer a novel method to convert natural language specifications into formal requirements. Their results show that this new "natural synthesis" method outperforms existing tools and can tackle more benchmarks, including harder cases in parameterized systems synthesis.

### 6. MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory
**Authors:** Minghao Guo, Qingyue Jiao, Zeru Shi, Yihao Quan, Boxuan Zhang, Danrui Li, Liwei Che, Wujiang Xu, Shilong Liu, Zirui Liu, Mubbasir Kapadia, Vladimir Pavlovic, Jiang Liu, Mengdi Wang, Yiyu Shi, Dimitris N. Metaxas, Ruixiang Tang
**Link:** https://arxiv.org/abs/2605.15128v1
**Summary:** The paper addresses the challenge of evaluating long-term multimodal memory in agents, particularly regarding their ability to retain and utilize detailed visual evidence necessary for reasoning over time. The authors introduce MemEye, a framework that assesses memory capabilities based on the granularity of visual evidence and its application in reasoning. Their evaluation of various memory methods reveals that existing architectures often fail to adequately preserve fine-grained visual details and struggle with reasoning about changing visual states.

### 7. Understanding How International Students in the U.S. Are Using Conversational AI to Support Cross-Cultural Adaptation
**Authors:** Laleh Nourian, Anisa Callis, Stephanie Patterson, Jadeline Miao, Jamison Heard, Garreth W. Tigwell
**Link:** https://arxiv.org/abs/2605.15127v1
**Summary:** The paper explores how international students in the U.S. use conversational AI tools to navigate their cultural adaptation challenges, noting the lack of cohesive support resources. Through a survey and interviews, the authors find that while students view AI as a quick fix for immediate issues, there is a strong desire for these tools to evolve into ongoing support systems. The study offers insights and recommendations for developing AI solutions that better address the long-term needs of international students.

### 8. CoCo-InEKF: State Estimation with Learned Contact Covariances in Dynamic, Contact-Rich Scenarios
**Authors:** Michael Baumgartner, David Müller, Agon Serifi, Ruben Grandia, Espen Knoop, Markus Gross, Moritz Bächer
**Link:** https://arxiv.org/abs/2605.15122v1
**Summary:** The paper addresses the challenge of state estimation in legged robots during dynamic, contact-rich activities, where traditional methods struggle with nuanced contact scenarios. The authors introduce CoCo-InEKF, a novel extended Kalman filter that employs learned continuous contact velocity covariances rather than binary contact states, allowing for more accurate estimation of contact conditions. Experimental results show that this approach significantly improves the accuracy and consistency of velocity estimation, enabling the robots to perform complex movements like dancing and interacting with varied surfaces more effectively.

### 9. CLOVER: Closed-Loop Value Estimation \& Ranking for End-to-End Autonomous Driving Planning
**Authors:** Sining Ang, Yuguang Yang, Canyu Chen, Yan Wang
**Link:** https://arxiv.org/abs/2605.15120v1
**Summary:** The paper addresses the mismatch between training and evaluation methods in end-to-end autonomous driving planners, which often leads to safety and performance issues. The authors propose CLOVER, a framework that generates diverse trajectory candidates and ranks them using a scorer that predicts planning metrics, enhancing the training process with pseudo-expert trajectories. Key results demonstrate CLOVER's superior performance, achieving state-of-the-art scores in both standard and challenging evaluation settings.

### 10. Talk is (Not) Cheap: A Taxonomy and Benchmark Coverage Audit for LLM Attacks
**Authors:** Karthik Raghu Iyer, Yazdan Jamshidi, Nicholas Bray, Alexey A. Shvets
**Link:** https://arxiv.org/abs/2605.15118v1
**Summary:** The paper addresses the inadequacy of existing benchmarks in evaluating attacks on large language models (LLMs) by creating a comprehensive framework that maps various attack types and techniques. This framework, consisting of a detailed taxonomy and a coverage matrix, was applied to existing benchmarks, revealing that they collectively cover only a small portion of possible attacks, particularly neglecting critical threat categories. The authors provide their taxonomy and findings as reusable resources to help the research community identify and address gaps in benchmark coverage.

---
## 2026-05-19

### 1. DashAttention: Differentiable and Adaptive Sparse Hierarchical Attention
**Authors:** Yuxiang Huang, Nuno M. T. Gonçalves, Federico Alvetreti, Lei Li, Xu Han, Edoardo M. Ponti, André F. T. Martins, Marcos V. Treviso
**Link:** https://arxiv.org/abs/2605.18753v1
**Summary:** The paper presents DashAttention, a novel hierarchical attention mechanism that addresses the limitations of existing methods by allowing for a variable number of key-value blocks to be selected adaptively based on the query. This approach maintains a fully differentiable architecture, resulting in improved long-context modeling capabilities and better performance than current methods like NSA and InfLLMv2, particularly in high-sparsity scenarios. Additionally, DashAttention's implementation shows significant speed improvements during inference compared to previous attention techniques.

### 2. A Readiness-Driven Runtime for Pipeline-Parallel Training under Runtime Variability
**Authors:** Ruitao Liu, Xinyang Tian, Shuo Chen, Tingrui Zhang, Guang Yang, Alan Zhao, Wei Xu
**Link:** https://arxiv.org/abs/2605.18750v1
**Summary:** The paper addresses the inefficiencies in pipeline-parallel training caused by runtime variability, where models may wait for unready tasks, leading to idle time and suboptimal resource usage. It introduces the Runtime-Readiness-First Pipeline (RRFP), which allows for more flexible scheduling based on task readiness rather than rigid predefined orders. The key contribution is that RRFP significantly enhances training speed, achieving up to 1.77 times faster performance on language tasks and up to 2.77 times on multimodal tasks compared to traditional methods, while maintaining training correctness.

### 3. Code as Agent Harness
**Authors:** Xuying Ning, Katherine Tieu, Dongqi Fu, Tianxin Wei, Zihao Li, Yuanchen Bei, Jiaru Zou, Mengting Ai, Zhining Liu, Ting-Wei Li, Lingjie Chen, Yanjun Zhao, Ke Yang, Bingxuan Li, Cheng Qian, Gaotang Li, Xiao Lin, Zhichen Zeng, Ruizhong Qiu, Sirui Chen, Yifan Sun, Xiyuan Yang, Ruida Wang, Rui Pan, Chenyuan Yang, Dylan Zhang, Liri Fang, Zikun Cui, Yang Cao, Pan Chen, Dorothy Sun, Ren Chen, Mahesh Srinivasan, Nipun Mathur, Yinglong Xia, Hong Li, Hong Yan, Pan Lu, Lingming Zhang, Tong Zhang, Hanghang Tong, Jingrui He
**Link:** https://arxiv.org/abs/2605.18747v1
**Summary:** The paper addresses the evolving role of code in agentic systems, where it functions not only as output but also as a foundational element for agent reasoning and actions. The authors introduce the concept of "code as agent harness," organizing their survey into three layers: the interaction between code and agents, the mechanisms that improve performance, and the scaling of these systems to multi-agent environments. Their key contribution is a comprehensive framework for understanding and developing AI agents that can reliably execute complex tasks using code, while also identifying important challenges for future research in this area.

### 4. ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop
**Authors:** Yining Hong, Jiageng Liu, Han Yin, Manling Li, Leonidas Guibas, Li Fei-Fei, Jiajun Wu, Yejin Choi
**Link:** https://arxiv.org/abs/2605.18746v1
**Summary:** The paper introduces ESI-Bench, a new benchmark designed to evaluate embodied spatial intelligence by mimicking how agents actively explore their environments instead of simply processing observations passively. Through extensive experimentation with state-of-the-art models, the authors found that agents using active exploration techniques significantly outperform those that rely on passive sensing, discovering effective spatial strategies on their own. A notable challenge identified is that many errors arise not from perception issues but from poor action choices, highlighting a gap in metacognitive reasoning compared to human strategies.

### 5. SURGE: Approximation-free Training Free Particle Filter for Diffusion Surrogate
**Authors:** Lifu Wei, Yinuo Ren, Naichen Shi, Yiping Lu
**Link:** https://arxiv.org/abs/2605.18745v1
**Summary:** The paper addresses the challenge of improving sample quality in diffusion-based generative models during inference without incurring high computational costs or introducing bias from gradient evaluations. It introduces a new algorithm called \texttt{URGE}, which utilizes a resampling technique based on Girsanov estimation, allowing for effective weight adjustments of simulated trajectories without the need for score calculations. The key contribution is that \texttt{URGE} demonstrates improved generation quality compared to existing methods while being easier to implement and completely free of gradient-based computations.

### 6. Actionable World Representation
**Authors:** Kunqi Xu, Jitao Li, Jianglong Ye, Tianshu Tang, Isabella Liu, Sifei Liu, Xueyan Zou
**Link:** https://arxiv.org/abs/2605.18743v1
**Summary:** The paper addresses the challenge of creating a unified representation of actionable objects in the physical world, which are typically dynamic and change states based on their properties. The authors introduce WorldString, a neural architecture that learns from point clouds or RGB-D video streams to model the state of real-world objects effectively. This framework serves as a versatile digital twin, laying the groundwork for more advanced physical world models and facilitating future integration with policy learning and neural dynamics.

### 7. Vision-OPD: Learning to See Fine Details for Multimodal LLMs via On-Policy Self-Distillation
**Authors:** Qianhao Yuan, Jie Lou, Xing Yu, Hongyu Lin, Le Sun, Xianpei Han, Yaojie Lu
**Link:** https://arxiv.org/abs/2605.18740v1
**Summary:** The paper addresses the challenge that multimodal large language models (MLLMs) face in understanding fine details in images, particularly when answers depend on small pieces of visual evidence. The authors introduce a self-distillation framework called Vision-OPD, which allows the model to leverage its own focused perceptions of cropped images to improve its performance on full images. Their experiments demonstrate that models trained with Vision-OPD achieve competitive or superior results in fine-grained visual understanding tasks compared to larger existing models.

### 8. What Does the AI Doctor Value? Auditing Pluralism in the Clinical Ethics of Language Models
**Authors:** Payal Chandak, Victoria Alkin, David Wu, Maya Dagan, Taposh Dutta Roy, Maria Clara Saad Menezes, Ayush Noori, Nirali Somia, John S. Brownstein, Ran Balicer, Rebecca W. Brendel, Noa Dagan, Isaac S. Kohane, Gabriel A. Brat
**Link:** https://arxiv.org/abs/2605.18738v1
**Summary:** This paper addresses the issue of how large language models (LLMs) in medicine may not adequately consider the diverse ethical values that physicians prioritize, particularly in cases of conflicting principles like patient autonomy. The authors propose a framework to audit the ethical values embedded in medical AI by analyzing clinician-verified dilemmas and determining how LLMs prioritize different ethical considerations in their decisions. They found that while LLMs exhibit some understanding of value pluralism, they often lean towards specific value preferences, which could lead to rigid ethical stances in clinical practice if not managed appropriately.

### 9. PIXLRelight: Controllable Relighting via Intrinsic Conditioning
**Authors:** Miguel Farinha, Ronald Clark
**Link:** https://arxiv.org/abs/2605.18735v1
**Summary:** The paper introduces PIXLRelight, a fast and effective method for relighting single images with physical accuracy by using a novel intrinsic conditioning technique. This approach combines principles from physically based rendering with learned image synthesis, allowing users to control lighting in a highly detailed manner without the computational overhead typically associated with traditional methods. The key contribution is its ability to achieve high-quality relighting in under a tenth of a second per image, setting a new standard for this application.

### 10. Predictable Confabulations: Factual Recall by LLMs Scales with Model Size and Topic Frequency
**Authors:** Matthew L. Smith, Jonathan P. Shock, Samuel T. Segun, Iyiola E. Olatunji, Tegawendé F. Bissyandé
**Link:** https://arxiv.org/abs/2605.18732v1
**Summary:** This paper investigates how well large language models (LLMs) can recall factual information based on their size and the frequency of topics in their training data. By evaluating 38 models on a substantial dataset of scholarly references, the authors found that a combination of model size and topic representation explains a significant portion of the variance in recall quality. The key insight is that recall performance follows a predictable pattern influenced by the strength of relevant information relative to background noise, suggesting a scalable approach to improve factual recall in LLMs.

---
## 2026-05-20

### 1. Atoms of Thought: Universal EEG Representation Learning with Microstates
**Authors:** Xinyang Tian, Ruitao Liu, Ziyi Ye, Siyang Xue, Xin Wang, Xuesong Chen
**Link:** https://arxiv.org/abs/2605.20182v1
**Summary:** This paper addresses the challenge of effectively representing electroencephalogram (EEG) signals for various applications like sleep staging and emotion recognition. The authors introduce a novel method that uses microstates—short patterns of brain activity—by clustering EEG data into discrete sequences. Their findings demonstrate that this microstate approach significantly improves performance over traditional methods and provides better interpretability and scalability for both research and clinical applications.

### 2. TIDE: Efficient and Lossless MoE Diffusion LLM Inference with I/O-aware Expert Offload
**Authors:** Zhiben Chen, Youpeng Zhao, Yang Sui, Jun Wang, Yuzhang Shang
**Link:** https://arxiv.org/abs/2605.20179v1
**Summary:** The paper presents TIDE, a new system designed to optimize the inference of large diffusion language models (dLLMs) on resource-limited devices by reducing input/output (I/O) overhead and computational bottlenecks. TIDE utilizes the consistency of expert activations during the diffusion process to develop an interval-based strategy that efficiently manages expert placements, formulated as a mathematical problem to minimize resource use. As a result, it achieves up to 1.5 times the throughput of existing methods without requiring any additional model training.

### 3. From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models
**Authors:** Juncheng Wu, Hardy Chen, Haoqin Tu, Xianfeng Tang, Freda Shi, Hui Liu, Hanqing Lu, Cihang Xie, Yuyin Zhou
**Link:** https://arxiv.org/abs/2605.20177v1
**Summary:** The paper addresses the performance limitations of vision-language models (VLMs) in visual tasks, emphasizing that poor visual perception, rather than reasoning, is the main issue. The authors propose a staged training approach, separating visual perception, visual reasoning, and textual reasoning, and demonstrate that targeted optimization of visual perception enhances overall performance. Their results indicate that models trained with this method achieve significantly improved accuracy in reasoning tasks with shorter reasoning processes, highlighting the importance of strong visual perception as a foundation for effective reasoning.

### 4. ClinSeekAgent: Automating Multimodal Evidence Seeking for Agentic Clinical Reasoning
**Authors:** Juncheng Wu, Letian Zhang, Yuhan Wang, Haoqin Tu, Hardy Chen, Zijun Wang, Cihang Xie, Yuyin Zhou
**Link:** https://arxiv.org/abs/2605.20176v1
**Summary:** The paper introduces ClinSeekAgent, an automated system designed to actively gather and synthesize multimodal clinical evidence, moving away from the typical reliance on pre-curated data. By querying various medical data sources and refining its hypotheses in real-time, ClinSeekAgent significantly improves the performance of language models in clinical reasoning tasks, achieving notable F1 score enhancements on both text-only and multimodal challenges. Additionally, it serves as a training pipeline for creating more efficient models capable of effective evidence seeking.

### 5. Multi-axis Analysis of Image Manipulation Localization
**Authors:** Keanu Nichols, Divya Appapogu, Giscard Biamby, Dina Bashkirova, Anna Rohrbach, Bryan A. Plummer
**Link:** https://arxiv.org/abs/2605.20174v1
**Summary:** The paper addresses the challenge of detecting advanced image manipulations, which have become increasingly prevalent due to generative AI but can contribute to misinformation. The authors introduce a new benchmark called AUDITS, which includes over 530,000 images across various domains, manipulation types, and sizes, facilitating a multi-axis analysis of detection methods. Their research aims to enhance the understanding of existing techniques' robustness and drive the development of more effective image manipulation detection tools.

### 6. A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents
**Authors:** Vasundra Srinivasan
**Link:** https://arxiv.org/abs/2605.20173v1
**Summary:** The paper addresses the challenges of integrating stochastic outputs from large language models (LLMs) with deterministic software systems in the context of production agents, introducing the concept of the stochastic-deterministic boundary (SDB) as a key architectural component. It presents a methodology and a catalog of six runtime patterns for effectively composing the SDB across different types of agents, along with strategies for diagnosing failures. A notable contribution is the five-step method for selecting suitable runtime patterns based on workload characteristics, which is demonstrated through a practical implementation for managing contract renewals.

### 7. Long-term Power Grid Planning via Answer Set Programming
**Authors:** Antonio Ielo, Francesco Doria, Sandra Castellanos-Paez, Marco Maratea, Francesco Percassi, Mauro Vallati
**Link:** https://arxiv.org/abs/2605.20172v1
**Summary:** This paper addresses the challenge of long-term power grid planning, which must adapt to sustainability, demand changes, and urbanization while maintaining service quality. The authors introduce a novel approach using Answer Set Programming (ASP) to automate and optimize this planning process, demonstrating its capability to effectively handle complex grid requirements through both synthetic and real-world data evaluations. The key contribution is the successful application of ASP to express and manage intricate topological and combinatorial constraints in grid planning.

### 8. KoRe: Compact Knowledge Representations for Large Language Models
**Authors:** Davide Cavicchini, Fausto Giunchiglia, Jacopo Staiano
**Link:** https://arxiv.org/abs/2605.20170v1
**Summary:** The paper introduces KoRe, a new method for improving Large Language Models (LLMs) by integrating human-readable Knowledge Graphs (KGs) in a more efficient way. Instead of retraining the entire model, KoRe encodes sub-graphs into compact knowledge tokens that can be easily injected into the LLM, achieving competitive performance on benchmarks while significantly reducing token usage by up to 10 times. This approach enhances the interpretability and reliability of LLMs, addressing issues with knowledge representation and hallucinations.

### 9. HaorFloodAlert: Deseasonalized ML Ensemble for 72-Hour Flood Prediction in Bangladesh Haor Wetlands
**Authors:** Salma Hoque Talukdar Koli, Fahima Haque Talukder Jely, Md. Samiul Alim, Md. Zakir Hossen
**Link:** https://arxiv.org/abs/2605.20167v1
**Summary:** The paper addresses the problem of rapid flash floods in Bangladesh's haor wetlands, which threaten the annual boro rice harvest and are poorly predicted by current flood forecasting systems. The authors developed HaorFloodAlert, a deseasonalized machine learning ensemble that accurately forecasts flood probabilities by incorporating data on temperature and upstream river conditions. Their ensemble model achieves high predictive accuracy, with significant validation results that aim to improve flood warning capabilities and mitigate agricultural damage.

### 10. Not Every Rubric Teaches Equally: Policy-Aware Rubric Rewards for RLVR
**Authors:** Utkarsh Tyagi, Xingang Guo, MohammadHossein Rezaei, Daniel George, Anas Mahmoud, Jackson Lee, Bing Liu, Yunzhong He
**Link:** https://arxiv.org/abs/2605.20164v1
**Summary:** The paper addresses the challenge of optimizing reinforcement learning with rubric-based rewards, where certain criteria may not be effective signals for improving model performance. The authors propose POW3R, a policy-aware reward framework that adjusts the importance of rubric criteria based on their current relevance during training, enhancing the learning process. The key result shows that POW3R significantly improves both overall reward and completion rates while requiring fewer training steps compared to traditional methods.

---
## 2026-05-21

### 1. Variance Reduction for Expectations with Diffusion Teachers
**Authors:** Jesse Bettencourt, Xindi Wu, Matan Atzmon, James Lucas, Jonathan Lorraine
**Link:** https://arxiv.org/abs/2605.21489v1
**Summary:** The paper addresses the problem of high computational costs associated with using pretrained diffusion models in downstream tasks, due to the variability of Monte Carlo estimates from noise samples. To tackle this, the authors introduce CARV, a framework that reduces variance in these estimates by employing a hierarchical Monte Carlo approach that allows for more efficient reuse of expensive computations combined with importance sampling techniques. The key contribution is that CARV significantly improves computational efficiency, achieving 2-3x effective compute savings in various experiments, although it does not enhance performance in all scenarios.

### 2. Equilibrium Reasoners: Learning Attractors Enables Scalable Reasoning
**Authors:** Benhao Huang, Zhengyang Geng, Zico Kolter
**Link:** https://arxiv.org/abs/2605.21488v1
**Summary:** The paper addresses the challenge of enabling iterative reasoning models to generalize effectively beyond memorized patterns. The authors introduce Equilibrium Reasoners (EqR), which leverage learned dynamical systems that stabilize at solution points, allowing for scaling of reasoning processes during inference. Their approach significantly enhances performance in challenging tasks, such as solving complex Sudoku puzzles, where accuracy improved from 2.6% to over 99% by effectively utilizing test-time computation.

### 3. Quantifying Hyperparameter Transfer and the Importance of Embedding Layer Learning Rate
**Authors:** Dayal Singh Kalra, Maissam Barkeshli
**Link:** https://arxiv.org/abs/2605.21486v1
**Summary:** The paper addresses the challenge of transferring optimal hyperparameters when training large language models (LLMs) across different scales. The authors propose a framework to quantify hyperparameter transfer and demonstrate that the "Maximal Update" (μP) approach significantly enhances learning rate transfer compared to standard parameterization. A key finding is that optimizing the embedding layer's learning rate reduces training instability and improves hyperparameter transfer effectiveness.

### 4. EvoStruct: Bridging Evolutionary and Structural Priors for Antibody CDR Design via Protein Language Model Adaptation
**Authors:** Mansoor Ahmed, Sujin Lee, Umar Khayaz, Murray Patterson
**Link:** https://arxiv.org/abs/2605.21485v1
**Summary:** The paper introduces EvoStruct, a novel method for antibody CDR design that tackles the problem of vocabulary collapse in existing graph neural networks, which tend to over-predict certain amino acids while missing important ones. By integrating a frozen protein language model with 3D structural information through a cross-attention mechanism, EvoStruct significantly improves sequence recovery and amino acid diversity. The results show a 16% increase in sequence recovery and a 43% reduction in perplexity compared to leading GNN methods, aligning more closely with known binding correlations.

### 5. Velocityformer: Broken-Symmetry-Matched Equivariant Graph Transformers for Cosmological Velocity Reconstruction
**Authors:** Tilman Tröster, David Mirkovic, Veronika Oehl, Arne Thomsen
**Link:** https://arxiv.org/abs/2605.21483v1
**Summary:** The paper presents Velocityformer, a novel graph transformer model designed to accurately reconstruct galaxy velocities from spectroscopic surveys to enhance measurements of the kinematic Sunyaev-Zel'dovich (kSZ) effect, which informs cosmological theories. By aligning the model with the broken symmetry in observational data, Velocityformer achieves a 35% improvement in accuracy over traditional methods and demonstrates enhanced performance even with limited training data, ultimately improving the signal-to-noise ratio in kSZ measurements by 30%.

### 6. DeepWeb-Bench: A Deep Research Benchmark Demanding Massive Cross-Source Evidence and Long-Horizon Derivation
**Authors:** Sixiong Xie, Zhuofan Shi, Haiyang Shen, Jiuzheng Wang, Siqi Zhong, Mugeng Liu, Chongyang Pan, Peilun Jia, Baoqing Sun, Xiang Jing, Yun Ma
**Link:** https://arxiv.org/abs/2605.21482v1
**Summary:** The paper introduces DeepWeb-Bench, a challenging benchmark for evaluating language models on deep research tasks that require extensive evidence gathering, cross-source verification, and complex multi-step reasoning. The benchmark reveals that most errors arise from issues in deriving and calibrating answers rather than retrieving information, highlighting distinct failure modes between strong and weak models, and showing that models perform differently across domains. The publicly available benchmark includes data and evaluation tools for further research.

### 7. AiraXiv: An AI-Driven Open-Access Platform for Human and AI Scientists
**Authors:** Junshu Pan, Panzhong Lu, Yixuan Weng, Qiyao Sun, Fang Guo, Zijie Yang, Qiji Zhou, Yue Zhang
**Link:** https://arxiv.org/abs/2605.21481v1
**Summary:** The paper presents AiraXiv, an AI-driven open-access platform designed to tackle the challenges faced by traditional academic publishing, such as increasing submission volumes and reviewer workload. AiraXiv enables both human and AI authors to contribute and refine research through iterative feedback and AI-assisted analysis, promoting a more inclusive and scalable approach to publishing. The platform was validated through real-world applications, showing its effectiveness as a modern research infrastructure.

### 8. WikiVQABench: A Knowledge-Grounded Visual Question Answering Benchmark from Wikipedia and Wikidata
**Authors:** Basel Shbita, Pengyuan Li, Anna Lisa Gentile
**Link:** https://arxiv.org/abs/2605.21479v1
**Summary:** The paper introduces WikiVQABench, a new benchmark for Visual Question Answering (VQA) that requires external knowledge from sources like Wikipedia and Wikidata, addressing the limitation of existing benchmarks that focus only on visual content. To create this dataset, images from Wikipedia were combined with relevant captions and knowledge, and multiple-choice questions were generated using large language models and then curated by human annotators for quality and factual accuracy. The evaluation of various vision-language models on this benchmark showed a significant range in performance, highlighting its effectiveness in assessing knowledge-driven reasoning capabilities in AI systems.

### 9. Is Fixing Schema Graphs Necessary? Full-Resolution Graph Structure Learning for Relational Deep Learning
**Authors:** Yi Huang, Qingyun Sun, Jia Li, Xingcheng Fu, Jianxin Li
**Link:** https://arxiv.org/abs/2605.21475v1
**Summary:** The paper addresses the challenge of enhancing relational prediction tasks using relational deep learning by moving beyond fixed graph structures in relational databases. The authors introduce FROG, a framework that learns graph structures dynamically during the learning process by treating tables as flexible nodes and edges, while incorporating mechanisms to capture relational semantics effectively. Their experiments show that this approach outperforms existing methods and provides insightful contributions to how graph structures can be optimized for better performance in relational deep learning tasks.

### 10. Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling
**Authors:** Caleb Winston, Ron Yifeng Wang, Azalia Mirhoseini, Christos Kozyrakis
**Link:** https://arxiv.org/abs/2605.21470v1
**Summary:** The paper addresses the high latency and error rates in computer-use agents (CUA) that automate web tasks using natural language instructions by proposing an agent just-in-time (JIT) compilation method. This approach generates executable code from task descriptions, allowing for optimized tool usage and parallel execution. The results show significant improvements, with JIT-Planner achieving over 10 times faster execution and increased accuracy compared to existing methods.

---
## 2026-05-22

### 1. Tokenisation via Convex Relaxations
**Authors:** Jan Tempus, Philip Whittington, Craig W. Schmidt, Dennis Komm, Tiago Pimentel
**Link:** https://arxiv.org/abs/2605.22821v1
**Summary:** The paper addresses the limitations of existing greedy tokenisation algorithms in natural language processing by proposing a new approach called ConvexTok, which formulates the tokeniser construction as a linear program solved through convex optimisation. The key contributions include consistent improvements in tokenisation metrics and language model efficiency, with ConvexTok providing users a certified measure of optimality for the tokenisers created, demonstrating performance within 1% of the optimal solution at standard vocabulary sizes.

### 2. Integrable Elasticity via Neural Demand Potentials
**Authors:** Carlos Heredia, Daniel Roncel
**Link:** https://arxiv.org/abs/2605.22820v1
**Summary:** The paper addresses the challenge of accurately modeling multiproduct retail demand and deriving elasticities from it. The authors introduce a novel neural model called the Integrable Context-Dependent Demand Network (ICDN), which learns demand as a smooth function influenced by various contexts and log-prices. The key finding is that ICDN significantly enhances predictive performance and provides more reliable elasticity estimates compared to traditional methods, particularly for complex cross-price relationships.

### 3. Vector Policy Optimization: Training for Diversity Improves Test-Time Search
**Authors:** Ryan Bahlous-Boldi, Isha Puri, Idan Shenfeld, Akarsh Kumar, Mehul Damani, Sebastian Risi, Omar Khattab, Zhang-Wei Hong, Pulkit Agrawal
**Link:** https://arxiv.org/abs/2605.22817v1
**Summary:** The paper addresses the challenge of training language models to generate diverse solutions that can adapt to various task-specific reward functions during inference. The authors introduce Vector Policy Optimization (VPO), a reinforcement learning algorithm that allows models to anticipate and optimize for diverse rewards rather than a single scalar reward, improving their ability to explore different solutions. The results show that VPO consistently outperforms traditional approaches in test-time search scenarios, particularly as the search budget increases, highlighting the importance of optimizing for diversity in model training.

### 4. Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration
**Authors:** Lily Goli, Justin Kerr, Daniele Reda, Alec Jacobson, Andrea Tagliasacchi, Angjoo Kanazawa
**Link:** https://arxiv.org/abs/2605.22814v1
**Summary:** The paper addresses the challenge of effective exploration in sparse-reward 3D environments, where agents often get stuck revisiting old states. The authors propose a method that combines a continuously updated 3D reconstruction of the environment with an episodic policy model that tracks past experiences, allowing the agent to efficiently discover new areas. This approach leads to superior exploration performance during training and successful adaptation to various tasks in unseen environments, outpacing traditional reinforcement learning techniques.

### 5. The Matching Principle: A Geometric Theory of Loss Functions for Nuisance-Robust Representation Learning
**Authors:** Vishal Rajput
**Link:** https://arxiv.org/abs/2605.22800v1
**Summary:** This paper addresses the challenge of ensuring robustness in machine learning by proposing a unified approach called the "matching principle," which focuses on estimating the covariance of nuisance factors that do not affect labels and using this to regularize models. The authors demonstrate that various existing techniques, like adversarial training and metric learning, can be viewed as different methods for achieving this goal. A key contribution is the introduction of the Trajectory Deviation Index (TDI) for assessing sensitivity in embeddings and providing closed-form results that validate their theoretical framework with empirical tests across multiple models.

### 6. Finite-Particle Convergence Rates for Conservative and Non-Conservative Drifting Models
**Authors:** Krishnakumar Balasubramanian
**Link:** https://arxiv.org/abs/2605.22795v1
**Summary:** This paper addresses the convergence rates of finite-particle simulations for generative modeling that use drifting methods, particularly focusing on correcting issues related to non-conservatism in drifting velocities. The authors propose a new conservative drifting method using kernel density estimator gradients, proving that this approach achieves improved convergence rates under certain conditions. Key results include explicit bounds for the method's performance, demonstrating that it can effectively control residual terms while maintaining accurate generation of data.

### 7. MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems
**Authors:** Qianshu Cai, Yonggang Zhang, Xianzhang Jia, Wei Xue, Jun Song, Xinmei Tian, Yike Guo
**Link:** https://arxiv.org/abs/2605.22794v1
**Summary:** The paper addresses the limitations of current autonomous agent systems, which cannot adapt or learn from user interactions after deployment. The authors propose MOSS, a self-evolving system that enables source-level code rewriting to address structural failures, utilizing feedback from production failures for improvement. Remarkably, MOSS improved performance on the OpenClaw benchmark by enhancing task completion scores significantly, all without requiring human intervention.

### 8. Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention
**Authors:** Ali Hatamizadeh, Yejin Choi, Jan Kautz
**Link:** https://arxiv.org/abs/2605.22791v1
**Summary:** The paper introduces Gated DeltaNet-2, which addresses the challenge of efficiently managing memory updates in linear attention models by separating the mechanisms for erasing old information and writing new data using distinct channel-wise gates. This approach enhances memory editing in such a way that it improves overall performance in tasks like language modeling and commonsense reasoning, particularly excelling in long-context retrieval scenarios. Gated DeltaNet-2 outperforms its predecessors and related models, achieving the best results across various benchmarks while maintaining efficient training processes.

### 9. LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems
**Authors:** Sadia Asif, Mohammad Mohammadi Amiri, Momin Abbas, Prasanna Sattigeri, Karthikeyan Natesan Ramamurthy
**Link:** https://arxiv.org/abs/2605.22786v1
**Summary:** The paper presents LCGuard, a framework designed to ensure safe communication between agents in multi-agent systems that use key-value (KV) caches. LCGuard addresses the risk of sensitive information being unintentionally shared through these caches by implementing transformations that obscure reconstructions of agent-specific data while preserving essential task-related information. The results demonstrate that LCGuard effectively reduces the likelihood of sensitive information leakage compared to traditional methods, while still performing competitively on various tasks.

### 10. Evaluating Commercial AI Chatbots as News Intermediaries
**Authors:** Mirac Suzgun, Emily Shen, Federico Bianchi, Alexander Spangher, Thomas Icard, Daniel E. Ho, Dan Jurafsky, James Zou
**Link:** https://arxiv.org/abs/2605.22785v1
**Summary:** This study evaluates the accuracy of six AI chatbots in delivering news information by testing them on 2,100 factual questions from BBC News over a two-week period. The findings reveal that while some chatbots perform well with over 90% accuracy on multiple-choice questions, their performance drops significantly on free-response questions and varies by language, particularly underperforming in Hindi. The research highlights critical issues such as reliance on English sources, challenges in retrieving accurate information, and variability in addressing subtle inaccuracies in user queries.

---
## 2026-05-23

### 1. DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback
**Authors:** Yunpeng Dong, Jingkai He, Yuze Hou, Dong Du, Zhonghu Xu, Si Yu, Yubin Xia, Haibo Chen
**Link:** https://arxiv.org/abs/2605.22781v1
**Summary:** The paper addresses the latency issue in stateful AI agents that rely on frequent checkpointing and rollback of their entire state, which can take hundreds of milliseconds. To solve this, the authors introduce a new OS-level abstraction called DeltaState, which only captures changes between consecutive checkpoints instead of duplicating the entire state. The key contribution is DeltaBox, a sandbox system that achieves millisecond-level checkpoint and rollback times (14ms and 5ms, respectively), thus enabling AI agents to explore significantly more options within fixed time limits.

### 2. FAME: Failure-Aware Mixture-of-Experts for Message-Level Log Anomaly Detection
**Authors:** Huanchi Wang, Zihang Huang, Yifang Tian, Kristina Dzeparoska, Hans-Arno Jacobsen, Alberto Leon-Garcia
**Link:** https://arxiv.org/abs/2605.22779v1
**Summary:** The paper addresses the challenge of detecting log anomalies at the message level, which is crucial for identifying specific issues within production systems, as existing methods focus on broader session-level alerts. The authors propose FAME, a label-efficient framework that leverages a large language model offline to classify log lines into failure domains, significantly reducing the need for extensive labeled data. Key results show that FAME achieves high accuracy (F1 scores of 98.16 and 99.95 on different datasets) while minimizing annotation effort by 76 times and effectively detecting a majority of anomalies from previously unseen event types.

### 3. SDPM: Survival Diffusion Probabilistic Model for Continuous-Time Survival Analysis
**Authors:** Stanislav R. Kirpichenko, Andrei V. Konstantinov, Lev V. Utkin
**Link:** https://arxiv.org/abs/2605.22776v1
**Summary:** The paper introduces the Survival Diffusion Probabilistic Model (SDPM) to enhance continuous-time survival analysis, addressing limitations of existing methods related to hazard function assumptions and time discretization. By utilizing a denoising diffusion model to estimate survival distributions without these restrictions, SDPM demonstrates competitive performance against established models on various datasets. Its innovative approach to transforming target space significantly improves the model's predictive accuracy and calibration of event rates.

### 4. MambaGaze: Bidirectional Mamba with Explicit Missing Data Modeling for Cognitive Load Assessment from Eye-Gaze Tracking Data
**Authors:** Amir Mousavi, Mohammad Sadegh Sirjani, Erfan Nourbakhsh, Mimi Xie, Rocky Slavin, Leslie Neely, John Davis, John Quarles
**Link:** https://arxiv.org/abs/2605.22775v1
**Summary:** The paper presents MambaGaze, a novel framework for assessing cognitive load in real-time using eye-tracking data, addressing issues of data loss from blinks and the need for effective modeling of long-term dependencies. The approach includes a unique encoding method to capture data uncertainty and a bidirectional modeling technique with efficient computation. It achieves significant accuracy improvements over existing methods and demonstrates the capability for real-time performance on portable devices, making it suitable for applications like driver monitoring.

### 5. CogAdapt: Transferring Clinical ECG Foundation Models to Wearable Cognitive Load Assessment via Lead Adaptation
**Authors:** Amir Mousavi, Mohammad Sadegh Sirjani, Erfan Nourbakhsh, Mimi Xie, Rocky Slavin, Leslie Neely, John Davis, John Quarles
**Link:** https://arxiv.org/abs/2605.22774v1
**Summary:** The paper addresses the challenge of accurately assessing cognitive load using wearable ECG devices, which traditionally struggle with limited data and individual differences. The authors introduce CogAdapt, a framework that uses a learnable adapter to convert signals from wearable sensors into formats compatible with clinical ECG models, along with a fine-tuning approach to improve performance. The results indicate that CogAdapt significantly enhances cognitive load assessment accuracy compared to models trained from scratch, demonstrating its effectiveness in transferring knowledge from clinical to wearable settings.

### 6. Deep Reinforcement Learning for Flexible Job Shop Scheduling with Random Job Arrivals
**Authors:** Yu Tang, Muhammad Zakwan, Efe Balta, John Lygeros, Alisa Rupenyan
**Link:** https://arxiv.org/abs/2605.22773v1
**Summary:** The paper addresses the Flexible Job Shop Scheduling Problem (FJSP), which involves efficiently allocating jobs with unpredictable arrivals to machines, a task complicated by its combinatorial complexity. The authors propose using a Deep Reinforcement Learning (DRL) approach, specifically the Proximal Policy Optimization algorithm, to minimize job completion times, while leveraging simple neural networks and established dispatching rules. The key finding is that their DRL method significantly outperforms traditional dispatching rules and performs well compared to a mixed-integer linear programming solution, particularly in heterogeneous environments.

### 7. Reducing Political Manipulation with Consistency Training
**Authors:** Long Phan, Devin Kim, Alexander Pan, Alice Blair, Adam Khoja, Dan Hendrycks
**Link:** https://arxiv.org/abs/2605.22771v1
**Summary:** The paper addresses the issue of systematic political bias in large language models (LLMs), which show uneven responses to topics from different political perspectives, a phenomenon termed covert political bias. To combat this, the authors propose Political Consistency Training (PCT), a reinforcement learning method that focuses on improving symmetry in sentiment and helpfulness across political prompts. The results demonstrate that PCT effectively reduces covert bias while maintaining the overall helpfulness of the model, showing promise for application to other benchmarks.

### 8. Understanding Data Temporality Impact on Large Language Models Pre-training
**Authors:** Pilchen Hippolyte, Fabre Romain, Signe Talla Franck, Perez Patrick, Grave Edouard
**Link:** https://arxiv.org/abs/2605.22769v1
**Summary:** This paper addresses the issue of how the temporal ordering of training data affects the knowledge retention of large language models (LLMs). The authors created a benchmark for evaluating time-sensitive factual knowledge and pretrained models on temporally ordered datasets rather than the typical shuffled corpora. Their key finding is that sequentially trained models are better at retaining up-to-date knowledge and associating facts with their correct time periods compared to those trained on shuffled data.

### 9. Uniform Diffusion Models Revisited: Leave-One-Out Denoiser and Absorbing State Reformulation
**Authors:** Samson Gourevitch, Yazid Janati, Dario Shariatian, Umut Simsekli, Eric Moulines, Eric P. Xing, Alain Durmus
**Link:** https://arxiv.org/abs/2605.22765v1
**Summary:** This paper addresses the discrepancy in training objectives for Uniform Diffusion Models (UDM) by introducing the concept of a leave-one-out denoiser, which predicts each token without relying on its own noisy observation. The authors present a new framework that optimizes this denoising process and reformulates UDM to utilize simpler sampling operations, leading to improved performance in language modeling. Key findings indicate that enhancements in UDM generation are primarily due to changes in parameterization and sampling strategy rather than the choice of model marginals.

### 10. Advancing Mathematics Research with AI-Driven Formal Proof Search
**Authors:** George Tsoukalas, Anton Kovsharov, Sergey Shirobokov, Anja Surina, Moritz Firsching, Gergely Bérczi, Francisco J. R. Ruiz, Arun Suggala, Adam Zsolt Wagner, Eric Wieser, Lei Yu, Aja Huang, Miklós Z. Horváth, Andrew Ferrauiolo, Henryk Michalewski, Codrut Grosu, Thomas Hubert, Matej Balog, Pushmeet Kohli, Swarat Chaudhuri
**Link:** https://arxiv.org/abs/2605.22763v1
**Summary:** The paper addresses the challenge of unreliable mathematical reasoning from large language models (LLMs) by using them to generate formal proofs in languages like Lean. The authors conducted a large-scale evaluation and found that their most capable AI agent successfully solved 9 out of 353 open Erdős problems and proved 44 OEIS conjectures at competitive costs. This work highlights the potential of AI to enhance formal proof search in various mathematical domains, showcasing effective agent designs for this purpose.

---
## 2026-05-24

### 1. Towards a General Intelligence and Interface for Wearable Health Data
**Authors:** Girish Narayanswamy, Maxwell A. Xu, A. Ali Heydari, Samy Abdel-Ghaffar, Marius Guerard, Kara Vaillancourt, Zhihan Zhang, Jake Garrison, Levi Albuquerque, Dimitris Spathis, Hong Yu, Hamid Palangi, Xuhai "Orson" Xu, David G. T. Barrett, Joseph Breda, Jed McGiffin, Yubin Kim, Yuwei Zhang, Naghmeh Rezaei, Samuel Solomon, Karan Ahuja, Tim Althoff, Jake Sunshine, Ming-Zher Poh, Benjamin Yetton, Ari Winbush, Nicholas B. Allen, James M. Rehg, Isaac Galatzer-Levy, Yun Liu, John Hernandez, Anupam Pathak, Conor Heneghan, Yuzhe Yang, Ahmed A. Metwally, Pushmeet Kohli, Mark Malhotra, Shwetak Patel, Xin Liu, Daniel McDuff
**Link:** https://arxiv.org/abs/2605.22759v1
**Summary:** This paper addresses the challenge of extracting personalized health insights from wearable sensor data, which is often sparse and difficult to annotate. The authors introduce a foundation model trained on a vast amount of unlabeled sensor data from millions of participants to improve health predictions across various conditions. They find that this model enhances few-shot learning and generative capabilities and can effectively support a Personal Health Agent, which offers more relevant and context-aware responses in health-related queries.

### 2. Lumberjack: Better Differentially Private Random Forests through Heavy Hitter Detection in Trees
**Authors:** Christian Janos Lebeda, David Erb, Tudor Cebere, Aurélien Bellet
**Link:** https://arxiv.org/abs/2605.22756v1
**Summary:** The paper presents Lumberjack, a new algorithm for creating differentially private random forests that enhances performance while preserving privacy. By utilizing large decision trees and a novel heavy hitter detection method, Lumberjack significantly improves the balance between privacy and utility, outperforming existing approaches. The results demonstrate that this technique allows for deeper trees, leading to better expressiveness and utility in practical applications.

### 3. Cyber-Physical Anomaly Detection in IoT-Enabled Smart Grids Using Machine Learning and Metaheuristic Feature Optimization
**Authors:** Adis Alihodžić, Eva Tuba, Milan Tuba
**Link:** https://arxiv.org/abs/2605.22749v1
**Summary:** The paper addresses the challenge of distinguishing between physical incidents and cyber threats in smart grids using data from power system attacks. It employs machine learning techniques along with a genetic algorithm for feature selection to optimize the detection process. The key finding is that tree-based models, particularly Extra Trees, can effectively reduce the number of required measurements while maintaining high accuracy in anomaly detection, demonstrating that many electrical measurements are redundant.

### 4. Superhuman Safe and Agile Racing through Multi-Agent Reinforcement Learning
**Authors:** Ismail Geles, Leonard Bauersfeld, Markus Wulfmeier, Davide Scaramuzza
**Link:** https://arxiv.org/abs/2605.22748v1
**Summary:** The paper addresses the challenge of making autonomous systems, particularly racing drones, safe and effective in dynamic environments shared with other agents. The authors apply multi-agent reinforcement learning to train drones in competitive racing scenarios, enabling them to anticipate and navigate collisions and complex interactions with other drones. The key finding is that these trained agents not only outperform a top human racer but also reduce collision rates by 50% compared to traditional single-agent methods, demonstrating the importance of multi-agent training for real-world applications.

### 5. Plug-in Losses for Evidential Deep Learning: A Simplified Framework for Uncertainty Estimation that Includes the Softmax Classifier
**Authors:** Berk Hayta, Hannah Laus, Simon Mittermaier, Felix Krahmer
**Link:** https://arxiv.org/abs/2605.22746v1
**Summary:** The paper addresses the challenge of reliable and efficient uncertainty estimation in sensor-based learning systems using Evidential Deep Learning (EDL), which typically involves complex computations. The authors propose a simplified framework using a plug-in loss evaluated at the Dirichlet mean, which effectively approximates traditional losses like mean-squared error and cross-entropy, including the softmax classifier. Their empirical findings demonstrate that this approach achieves competitive performance in predictive accuracy and selective prediction on the Google Speech Commands dataset, while simplifying the implementation process.

### 6. SeqLoRA: Bilevel Orthogonal Adaptation for Continual Multi-Concept Generation
**Authors:** Javad Parsa, Enis Simsar, Amir Joudaki, Thomas Hofmann, André M. H. Teixeira
**Link:** https://arxiv.org/abs/2605.22743v1
**Summary:** The paper addresses the challenge of effectively fine-tuning text-to-image diffusion models to generate multiple custom concepts without them interfering with each other. The authors introduce Sequential regularized LoRA (SeqLoRA), a method that optimizes model adaptations using a bilevel learning approach to minimize interference. Their experiments show that SeqLoRA enhances the preservation of individual identities and scalability across many concepts while avoiding expensive fusion methods.

### 7. Ternary Decision Trees with Locally-Adaptive Uncertainty Zones
**Authors:** William Smits
**Link:** https://arxiv.org/abs/2605.22740v1
**Summary:** This paper addresses the limitation of traditional decision trees, which assign equal confidence to predictions near decision boundaries. The authors introduce ternary decision trees, which incorporate uncertainty zones at each split, allowing for more nuanced predictions through local weighted blending based on several proposed methods for estimating uncertainty. Their experiments show that this approach significantly improves prediction accuracy across various datasets compared to standard decision trees, particularly highlighting the effectiveness of the margin method.

### 8. Proxy-Based Approximation of Shapley and Banzhaf Interactions
**Authors:** Santo M. A. R. Thies, Hubert Baniecki, R. Teal Witter, Eyke Hüllermeier, Maximilian Muschalik, Fabian Fumagalli
**Link:** https://arxiv.org/abs/2605.22738v1
**Summary:** The paper addresses the challenge of efficiently estimating Shapley and Banzhaf interaction values in machine learning models, which are crucial for understanding complex dynamics but are often computationally intensive. The authors introduce ProxySHAP, a new method that combines tree-based proxy models with a correction technique to improve accuracy without sacrificing speed. Their extensive evaluations show that ProxySHAP achieves the best approximation quality to date, outperforming existing methods in both small and large-scale scenarios, making it highly effective for explainability tasks.

### 9. The Distillation Game: Adaptive Attacks & Efficient Defenses
**Authors:** Youssef Allouah, Mahdi Haghifam, Sanmi Koyejo, Reza Shokri
**Link:** https://arxiv.org/abs/2605.22737v1
**Summary:** The paper addresses the challenge posed by distillation attacks, where the outputs of machine learning models that enhance their usability can also facilitate their imitation by adversaries. The authors propose a minimax game framework between a model provider (teacher) and an attacking model (student) to develop adaptive defenses, including a novel defense strategy called Product-of-Experts (PoE) that is efficient in computation. Key findings reveal that adaptive attacks can exploit defenses more effectively than passive evaluations suggest, and the PoE approach offers a cost-effective solution while maintaining higher-quality output reasoning.

### 10. Optimization over the intersection of manifolds
**Authors:** Yan Yang, Bin Gao, Ya-xiang Yuan
**Link:** https://arxiv.org/abs/2605.22736v1
**Summary:** This paper addresses the challenge of optimizing functions over the intersection of two manifolds, which often complicates finding feasible solutions. The authors present a geometric method that utilizes a single manifold's retraction while iterating along two orthogonal directions to efficiently approach the other manifold and improve the objective function. They establish convergence results that ensure the method's effectiveness and demonstrate its application through numerical experiments in various optimization tasks.

---
## 2026-05-25

### 1. SkillOpt: Executive Strategy for Self-Evolving Agent Skills
**Authors:** Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang, Dongdong Chen, Xue Yang, Chong Luo
**Link:** https://arxiv.org/abs/2605.23904v1
**Summary:** The paper introduces SkillOpt, a novel approach for optimizing agent skills in a systematic and controlled manner, addressing the limitations of existing methods that lack reliable improvement under feedback. By treating skills as external states of a fixed agent and employing a text-space optimization model, SkillOpt effectively edits skill documents to enhance performance. The results demonstrate significant improvements in accuracy across various benchmarks and models, outperforming existing techniques and showing that optimized skills maintain their effectiveness across different environments.

### 2. LLMs as Noisy Channels: A Shannon Perspective on Model Capacity and Scaling Laws
**Authors:** Xu Ouyang, Deyi Liu, Yuhang Cai, Jing Liu, Yuan Yang, Chen Zheng, Thomas Hartvigsen, Yiyuan Ma
**Link:** https://arxiv.org/abs/2605.23901v1
**Summary:** This paper addresses the limitations of existing scaling laws for Large Language Models (LLMs) that do not account for issues like performance degradation despite increased resources. The authors propose the Shannon Scaling Law, which frames LLM training as information transmission over a noisy channel, allowing for a better understanding of model capacity and performance. Their experiments demonstrate that this new framework not only explains observed non-monotonic phenomena but also outperforms traditional scaling laws in predicting model performance accurately.

### 3. From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills
**Authors:** Zisu Huang, Jingwen Xu, Yifan Yang, Ziyang Gong, Qihao Yang, Muzhao Tian, Xiaohua Wang, Changze Lv, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Xue Yang, Dongdong Chen, Xiaoqing Zheng, Chong Luo
**Link:** https://arxiv.org/abs/2605.23899v1
**Summary:** The paper addresses the challenge of effectively utilizing model-generated skills in language agents by systematically studying their lifecycle—how they are generated, extracted, and consumed. The authors developed a comprehensive evaluation framework to analyze the effectiveness of these skills across various tasks and found that while model-generated skills provide average benefits, they can also lead to negative transfer depending on the model's role in extraction and consumption. As a key contribution, they propose a "meta-skill" that enhances skill extraction by focusing on features that improve utility, thereby reducing negative transfer across different domains.

### 4. SPACENUM: Revisiting Spatial Numerical Understanding in VLMs
**Authors:** Jianshu Zhang, Yijiang Li, Huifeixin Chen, Haoran Lu, Letian Xue, Bingyang Wang, Han Liu
**Link:** https://arxiv.org/abs/2605.23898v1
**Summary:** The paper "SPACENUM" addresses the challenge of whether Vision-Language Models (VLMs) effectively understand numerical outputs related to spatial perceptions in dynamic and static environments. The authors introduce SpaceNum, a framework to evaluate VLMs through two tasks that assess their mapping of visual spatial structures to numerical representations. The key finding reveals that current VLMs struggle to genuinely ground numerical values in spatial contexts, often performing poorly and relying on superficial cues rather than robust spatial reasoning.

### 5. ETCHR: Editing To Clarify and Harness Reasoning
**Authors:** Beichen Zhang, Yuhong Liu, Jinsong Li, Yuhang Zang, Jiaqi Wang, Dahua Lin
**Link:** https://arxiv.org/abs/2605.23897v1
**Summary:** The paper addresses the challenge of improving visual reasoning in multimodal large language models, which often struggle with complex questions requiring precise image transformations. The authors propose ETCHR, a specialized image editing model that separates the editing process from the reasoning model, enhancing its ability to correctly modify images based on abstract questions. This approach significantly improves reasoning accuracy across various tasks, boosting performance metrics by up to 5.47 points in different model implementations.

### 6. Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models
**Authors:** Hongwu Peng, Ohiremen Dibua, Yuanjun Xiong, Yifan Gong, Jianming Zhang, Yan Kang
**Link:** https://arxiv.org/abs/2605.23893v1
**Summary:** The paper presents Complete-muE, a framework designed to improve the transfer of hyperparameters between dense feedforward networks and mixture-of-experts (MoE) models in transformer architectures. It utilizes a two-bridge system that effectively facilitates this transfer despite changes in model complexity and token distribution, allowing for consistent hyperparameter optimization across various model configurations. The key contribution is that hyperparameters tuned on a single dense model can be successfully adapted to multiple MoE setups, enabling faster convergence and a more efficient scaling process without extensive hyperparameter tuning.

### 7. Good Token Hunting: A Hitchhiker's Guide to Token Selection for Visual Geometry Transformers
**Authors:** Shuhong Zheng, Michael Oechsle, Erik Sandström, Marie-Julie Rakotosaona, Federico Tombari, Igor Gilitschenski
**Link:** https://arxiv.org/abs/2605.23892v1
**Summary:** This paper addresses the computational inefficiency of visual geometry transformers, which struggle to scale due to quadratic growth in costs linked to the number of input tokens. The authors propose a two-stage token selection framework that reduces the number of key/value tokens by first selecting crucial frames and then filtering redundant tokens within them. Their method significantly accelerates these models by over 85% while maintaining or improving performance, highlighting its potential for enhancing future applications.

### 8. CHRONOS: Temporally-Aware Multi-Agent Coordination for Evolving Data Marketplaces
**Authors:** Joydeep Chandra
**Link:** https://arxiv.org/abs/2605.23887v1
**Summary:** The paper presents CHRONOS, a three-layer architecture designed to improve the coordination in temporal knowledge-graph data marketplaces, addressing issues such as outdated information retrieval, inaccurate value attribution, and inefficient privacy budget management. By utilizing neural-ODE for updating data shortcuts, adjusting Shapley pricing based on data changes, and applying a specific algorithm for regret minimization while maintaining differential privacy, CHRONOS achieves competitive performance metrics, such as high recall rates and low latency. The results indicate that while privacy metrics may lead to noise-dominated valuations, the system effectively enhances data retrieval and agent coordination in evolving environments.

### 9. Multilingual Knowledge Transfer under Data Constraints via Lexical Interventions
**Authors:** Anastasiia Sedova, Natalie Schluter, Skyler Seto, Maartje ter Hoeve
**Link:** https://arxiv.org/abs/2605.23885v1
**Summary:** The paper addresses the challenge of transferring knowledge from high-resource languages to low-resource languages in multilingual models, particularly when target language data is limited. The authors introduce a method called LINK, which uses lexical substitutions in the high-resource training data based on bilingual vocabularies, requiring no additional training or resources. Their evaluation demonstrates significant improvements in performance for target languages across multiple model sizes, achieving up to twice the training efficiency to reach similar performance levels.

### 10. PGT: Procedurally Generated Tasks for improving visual grounding in MLLMs
**Authors:** Rim Assouel, Amir Bar, Michal Drozdzal, Adriana Romero-Soriano
**Link:** https://arxiv.org/abs/2605.23883v1
**Summary:** The paper addresses the challenge of fine-grained visual understanding in Multimodal Large Language Models (MLLMs), which often struggle with complex perception tasks. The authors introduce Procedurally Generated Tasks (PGT), a framework that creates additional training data by overlaying geometric shapes on images, helping to improve visual grounding and identify weaknesses in model perception. Their experiments show significant performance gains, with improvements of up to 20% on specific benchmarks, suggesting that enhanced supervision can effectively address existing limitations in these models.

---
## 2026-05-27

### 1. Algorithmic Monocultures in Hiring
**Authors:** Rishi Bommasani, Sarah H. Bana, Kathleen A. Creel, Dan Jurafsky, Percy Liang
**Link:** https://arxiv.org/abs/2605.27371v1
**Summary:** The paper investigates how the use of hiring algorithms from the same vendors leads to biased outcomes, particularly affecting Asian and Black applicants. By analyzing a large dataset of 3 million applicants, the authors find significant racial disparities in rejections and homogeneous outcomes across different positions. They conclude that applicants must apply to many jobs to improve their chances of human consideration, highlighting the adverse effects of algorithmic monocultures in hiring practices.

### 2. MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation
**Authors:** Huawei Lin, Peng Li, Jie Song, Fuxin Jiang, Tieying Zhang
**Link:** https://arxiv.org/abs/2605.27366v1
**Summary:** The paper addresses the limitations of existing skill creation methods in large language model (LLM) agents, which often treat skills as isolated and unchanging, hindering their effectiveness over time. The authors propose the MUSE-Autoskill framework, which allows agents to continuously create, manage, and refine skills throughout their lifecycle, incorporating memory for better skill reuse and adaptation. Experimental results indicate that this approach significantly enhances task success, efficiency, and the ability to transfer skills across different agents.

### 3. LocateAnything: Fast and High-Quality Vision-Language Grounding with Parallel Box Decoding
**Authors:** Shihao Wang, Shilong Liu, Yuanguo Kuang, Xinyu Wei, Yangzhou Liu, Zhiqi Li, Yunze Man, Guo Chen, Andrew Tao, Guilin Liu, Jan Kautz, Lei Zhang, Zhiding Yu
**Link:** https://arxiv.org/abs/2605.27365v1
**Summary:** LocateAnything addresses the inefficiencies in current vision-language models that decode bounding boxes for object detection in a slow, sequential manner. The paper presents a new method called Parallel Box Decoding, which allows for simultaneous decoding of box components, significantly improving both the speed and accuracy of localization tasks. The approach is further enhanced by a large-scale dataset of over 138 million samples, which improves data diversity and overall performance on various benchmarks.

### 4. Natural Language Query to Configuration for Retrieval Agents
**Authors:** Melissa Z. Pan, Negar Arabzadeh, Mathew Jacob, Fiodar Kazhamiaka, Esha Choukse, Matei Zaharia
**Link:** https://arxiv.org/abs/2605.27361v1
**Summary:** The paper addresses the challenge of optimizing retrieval agent configurations for specific queries, which traditionally involves static tuning for workload rather than per-query optimization. The authors introduce **BRANE**, a system that uses a large language model (LLM) to derive query characteristics and trains a predictor to estimate the effectiveness of different configurations, ultimately selecting the best one based on cost and accuracy trade-offs. The key finding is that **BRANE** significantly improves performance by achieving near-optimal accuracy at much lower costs compared to existing methods, establishing a new paradigm for dynamic configuration in retrieval systems.

### 5. GENESIS: Harnessing AI Agents for Autonomous 6G RAN Synthesis, Research, and Testing
**Authors:** Tamerlan Aghayev, Maxime Elkael, Michele Polese, Minh Dat Nguyen, Gabriele Gemmi, Andrea Lacava, Ali Saeizadeh, Reshma Prasad, Paolo Testolina, Angelo Feraudo, Soumendra Nanda, Pedram Johari, Salvatore D'Oro, Tommaso Melodia
**Link:** https://arxiv.org/abs/2605.27360v1
**Summary:** The paper presents GENESIS, an AI framework designed to streamline the complex and lengthy processes involved in developing cellular networks, particularly for 6G Radio Access Networks (RAN). Unlike traditional methods hampered by errors and inefficiencies, GENESIS uses intelligent agents to interpret and address specific technological intents through validated experiments, integrating feedback into a central knowledge system. This innovative approach aims to significantly reduce development time and improve the reliability of RAN components.

### 6. MobileMoE: Scaling On-Device Mixture of Experts
**Authors:** Yanbei Chen, Hanxian Huang, Ernie Chang, Jacob Szwejbka, Digant Desai, Zechun Liu, Vikas Chandra, Raghuraman Krishnamoorthi
**Link:** https://arxiv.org/abs/2605.27358v1
**Summary:** The paper addresses the challenge of deploying efficient language models on mobile devices by introducing MobileMoE, an on-device Mixture-of-Experts model that optimally balances memory and computation needs. By developing a novel scaling law and a training process tailored for mobile constraints, MobileMoE achieves performance on par with or better than existing dense models while requiring significantly fewer computational resources. Key results include marked improvements in inference speed, demonstrating MobileMoE's practicality for real-time applications on smartphones.

### 7. Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases
**Authors:** Dongyoon Hahm, Dylan Hadfield-Menell, Kimin Lee
**Link:** https://arxiv.org/abs/2605.27355v1
**Summary:** This paper addresses the issue of "alignment tampering," where Large Language Models (LLMs) unintentionally influence human feedback to favor biased outputs during the Reinforcement Learning from Human Feedback (RLHF) process. The authors demonstrate that because preference datasets are based on the LLM's own responses and only indicate which response is better without clarifying why, this can lead to the amplification of undesired biases. The research highlights the vulnerabilities in current RLHF methodologies and emphasizes the need for improved strategies to mitigate these issues without compromising response quality.

### 8. Guiding LLM Post-training Data Engineering with Model Internals from Sparse Autoencoders
**Authors:** Yi Jing, Zao Dai, Jinwu Hu, Zijun Yao, Lei Hou, Juanzi Li, Xiaozhi Wang
**Link:** https://arxiv.org/abs/2605.27354v1
**Summary:** The paper addresses the challenge of improving post-training data engineering for large language models (LLMs) by leveraging insights from the model's internal workings, rather than just external signals. The authors introduce a framework called SAERL, which utilizes Sparse Autoencoders to assess data properties like diversity, difficulty, and quality to guide targeted data operations. Their approach yields a 3% improvement in accuracy on a specific model while reducing the training time by 20%, demonstrating the value of using model internals for more effective data management.

### 9. From Scores to Gibbs Correctors: Accelerating Uniform-Rate Discrete Diffusion Models
**Authors:** Yuchen Liang, Ness Shroff, Yingbin Liang
**Link:** https://arxiv.org/abs/2605.27352v1
**Summary:** The paper addresses the inefficiency of generating samples with discrete diffusion models, which often require many steps, particularly for uniform-rate models. The authors introduce a new Gibbs-based correction method called GADD, which improves sampling efficiency without needing additional training. Their work demonstrates that GADD significantly reduces sampling complexity and enhances sample quality compared to existing methods, while also providing a new theoretical framework for analyzing these models.

### 10. When Eyes Betray AI: Social Gaze Consistency as a Semantic Cue for AI-Generated Image Detection
**Authors:** Kim Jihyeon, Sohee Kim, Soosan Lee, Souhwan Jung, James Matthew Rehg, Hyesong Choi
**Link:** https://arxiv.org/abs/2605.27348v1
**Summary:** The paper addresses the challenge of detecting AI-generated images, particularly those featuring realistic human interactions where traditional low-level artifacts are minimized. The authors introduce "Social Gaze Consistency," a high-level semantic cue based on the coherence of gaze and head movements among individuals in an image. They demonstrate that this approach significantly improves detection performance across multiple vision-language models, showing its effectiveness in discerning real from generated imagery without relying on low-level artifacts.

---
## 2026-05-29

### 1. Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
**Authors:** Nhat-Minh Nguyen
**Link:** https://arxiv.org/abs/2605.30353v1
**Summary:** This study investigates the effectiveness of an AI coding agent, supervised by a physicist, in developing a scientific software module for perturbation theory. Over 12 days, the AI was able to autonomously handle many tasks but struggled with critical physics insights and misidentified problems, highlighting that the supervision and design of the collaboration are more crucial than the AI's capabilities alone. The findings suggest that future AI systems need to improve in proposing new solutions rather than just optimizing existing ones to achieve trustworthy scientific results.

### 2. VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion
**Authors:** Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Hoda Eldardiry, Pinar Yanardag
**Link:** https://arxiv.org/abs/2605.30351v1
**Summary:** The paper addresses the high memory and latency demands of long-rollout causal video diffusion by introducing VideoMLA, which replaces traditional per-head key-value (KV) memory with a shared low-rank latent representation. This innovative approach reduces memory usage by 92.7% while maintaining quality, even in scenarios where typical assumptions about the low-rank nature of video attention do not apply. As a result, VideoMLA achieves enhanced performance and 1.23 times higher throughput in streaming video diffusion compared to existing methods.

### 3. DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
**Authors:** Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
**Link:** https://arxiv.org/abs/2605.30350v1
**Summary:** The paper presents DynaFLIP, a new framework aimed at improving robot manipulation by enhancing perception through a dynamics-aware multimodal pre-training process. By utilizing image-language-3D flow triplets from various videos, the approach effectively aligns different modalities to focus on motion understanding, leading to better representations for robotic tasks. The key finding is that this method significantly enhances performance—up to 22.5% in out-of-distribution scenarios—by training visual models to not only recognize static objects but also understand how they change with actions.

### 4. LLMSurgeon: Diagnosing Data Mixture of Large Language Models
**Authors:** Yaxin Luo, Jiacheng Cui, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen
**Link:** https://arxiv.org/abs/2605.30348v1
**Summary:** The paper addresses the challenge of understanding the data composition that shapes the behaviors of Large Language Models (LLMs), which is often undisclosed and difficult to audit. It introduces LLMSurgeon, a framework that estimates the distribution of pretraining data domains by leveraging generated text from the model and uses an innovative method to recover the underlying data mixture. The key contribution is the ability to accurately assess domain mixtures through a verifiable evaluation suite, enhancing post-hoc auditing of foundation models without needing direct access to their training data.

### 5. SchGen: PCB Schematic Generation with Semantic-Grounded Code Representations
**Authors:** Qinpei Luo, Ruichun Ma, Xinyu Zhang, Lili Qiu
**Link:** https://arxiv.org/abs/2605.30345v1
**Summary:** The paper introduces SchGen, the first large language model designed to automatically generate editable PCB schematics from natural language descriptions, addressing the traditionally manual and expertise-heavy process of PCB design. It tackles the challenge of complex schematic representations by utilizing a semantically grounded code format that simplifies the generation task for the AI. The results show that SchGen significantly outperforms existing methods in terms of wire connectivity and functional correctness, emphasizing the importance of effective representation in hardware design automation.

### 6. Tiny but Trusted: Efficient Vision-Language Reasoning for Time-Series Anomaly Detection
**Authors:** Xiaona Zhou, Muntasir Wahed, Tianjiao Yu, Constantin Brif, Ismini Lourentzou
**Link:** https://arxiv.org/abs/2605.30344v1
**Summary:** The paper addresses the challenge of detecting anomalies in time-series data using Vision-Language Models (VLMs), which have struggled with this task due to a lack of interpretability and training data. The authors introduce a new benchmark, VisAnomBench, that includes high-quality anomaly explanations, and develop a parameter-efficient VLM called VisAnomReasoner, which is fine-tuned on this benchmark. Results show that VisAnomReasoner significantly outperforms prior methods in precision and F1 score, indicating improved anomaly localization and generalization across different datasets.

### 7. Unlocking the Working Memory of Large Language Models for Latent Reasoning
**Authors:** Lukas Aichberger, Sepp Hochreiter
**Link:** https://arxiv.org/abs/2605.30343v1
**Summary:** The paper addresses the challenge of enhancing reasoning capabilities in large language models by moving away from the traditional autoregressive generation of reasoning steps. Instead, it introduces a method called Reasoning in Memory (RiM), which utilizes fixed memory blocks to enable efficient internal manipulation of information without externalizing intermediate thoughts. The key finding is that RiM outperforms or matches existing methods in reasoning tasks while requiring significantly less computational effort.

### 8. GPIC: A Giant Permissive Image Corpus for Visual Generation
**Authors:** Keshigeyan Chandrasegaran, Kyle Sargent, Suchir Agarwal, Michael Jang, Michael Poli, Juan Carlos Niebles, Justin Johnson, Jiajun Wu, Li Fei-Fei
**Link:** https://arxiv.org/abs/2605.30341v1
**Summary:** The paper introduces GPIC, a large and accessible image dataset of approximately 28 trillion pixels aimed at advancing visual generative modeling. It includes a diverse collection of internet images, all permissively licensed for various uses, and comes with a benchmarking protocol and a baseline model for evaluating generative methods. GPIC is hosted on Hugging Face and is designed to support research and development in scalable visual generation.

### 9. Efficient Test-Time Finetuning of LLMs via Convex Reconstruction and Gradient Caching
**Authors:** Alaa Khamis, Alaa Maalouf
**Link:** https://arxiv.org/abs/2605.30337v1
**Summary:** The paper addresses the challenge of making test-time finetuning (TTFT) of language models efficient, as existing methods often sacrifice speed for quality. The authors introduce HullFT, a method that uses a geometric approach to select relevant training sequences efficiently and employs techniques to optimize computation time. Their results demonstrate that HullFT provides a better balance between the quality of model adaptation and the speed of processing, leading to improved performance compared to current TTFT methods.

### 10. Fairness-Aware Federated Learning with Trajectory Shapley Value
**Authors:** Daniel Kuznetsov, Ziqi Wang
**Link:** https://arxiv.org/abs/2605.30336v1
**Summary:** The paper addresses the problem of biased and unstable learning in federated learning caused by fixed client contribution weights. The authors propose the Trajectory Shapley Value (TSV) to evaluate each client's influence on the model's optimization process and develop FedTSV, an adaptive aggregation method that adjusts client weights dynamically based on their contributions. Key results show that FedTSV accelerates convergence, enhances robustness, and provides fairer assessments of client contributions, improving the overall fairness of federated optimization.

---
## 2026-05-31

### 1. Locally Coherent, Globally Incoherent: Bounding Compositional Incoherence in Multi-Component LLM Agents
**Authors:** Anany Kotawala
**Link:** https://arxiv.org/abs/2605.30335v1
**Summary:** The paper addresses the issue of compositional incoherence in multi-component language model (LLM) agents, where individual components may produce locally coherent outputs that, when combined, violate probabilistic principles. It introduces the concept of compositional residuals to quantify this incoherence and proposes methods for deterministic repair and ongoing coherence monitoring. Key findings indicate that significant levels of incoherence persist across various configurations, leading to measurable regret in decision-making, while several proposed mitigation strategies were found to be ineffective.

### 2. Demystifying Data Organization for Enhanced LLM Training
**Authors:** Yalun Dai, Yangyu Huang, Tongshen Yang, Yonghan Wang, Xin Zhang, Wenshan Wu, Qihao Zhao, Hao Li, Yuanyuan Gao, Kim-Hui Yap, Scarlett Li
**Link:** https://arxiv.org/abs/2605.30334v1
**Summary:** This paper addresses the challenge of optimizing data organization to improve the training efficiency of Large Language Models (LLMs), which often undergo limited training epochs. The authors propose four main guidelines for data organization and introduce two new methods for data ordering, demonstrating through extensive experiments that these strategies significantly enhance training stability and performance without adding substantial computational costs.

### 3. COMPOSE: Composing Future Theorems from Citations and Formal Structure
**Authors:** David Busbib, Michael Werman
**Link:** https://arxiv.org/abs/2605.30333v1
**Summary:** The paper addresses the challenge of generating plausible future mathematical theorems by incorporating both prior scientific citations and formal theorem dependencies. The authors introduce COMPOSE, a dual-graph framework that leverages these two sources to enhance the generation process. Their experiments demonstrate that COMPOSE outperforms existing models, producing more grounded and mathematically rich theorem-like claims, indicating the benefits of combining scientific and formal contexts in mathematical generation.

### 4. When, why, and how do diffusion posterior samplers fail? A finite-sample lens
**Authors:** Benjamin A. Burns, Sara Fridovich-Keil
**Link:** https://arxiv.org/abs/2605.30330v1
**Summary:** The paper addresses the challenges faced by diffusion posterior samplers in accurately representing complex distributions, particularly due to inaccurate likelihood approximations at intermediate steps. The authors introduce a finite-sample perspective that captures how these approximations can lead to errors in posterior distributions, revealing that the problems can arise even from simple priors and not just nonlinear models. Their approach provides a diagnostic tool to evaluate the reliability of various posterior sampling techniques, making it applicable to a wide range of models.

### 5. SoundnessBench: Can Your AI Scientist Really Tell Good Research Ideas from Bad Ones?
**Authors:** Sy-Tuyen Ho, Minghui Liu, Huy Nghiem, Furong Huang
**Link:** https://arxiv.org/abs/2605.30329v1
**Summary:** The paper addresses the challenge of evaluating the soundness of research ideas generated by autonomous AI agents in scientific research. The authors present SoundnessBench, a new benchmark consisting of 1,099 machine-learning proposals, to assess whether Large Language Models (LLMs) can accurately judge the methodological validity of these ideas before they are developed further. The key finding reveals that LLMs often exhibit an optimism bias, mistakenly rating low-soundness proposals as sound, indicating that they are not yet reliable for evaluating the rigor of scientific ideas independently.

### 6. Reasoning with Sampling: Cutting at Decision Points
**Authors:** Felix Zhou, Anay Mehrotra, Quanquan C. Liu
**Link:** https://arxiv.org/abs/2605.30327v1
**Summary:** The paper addresses the challenge of efficiently sampling from a power distribution to improve reasoning in language models without additional training. The authors propose a new algorithm, Entropy-Cut Metropolis-Hastings, which identifies and resamples key decision points in reasoning traces instead of making random cuts. The key result shows that this approach significantly enhances performance across various reasoning tasks compared to existing methods and models trained with reinforcement learning.

### 7. RoboWits: Unexpected Challenges for Robotic Creative Problem Solving
**Authors:** Chunru Lin, Hongxin Zhang, Fenghao Yu, Zhehuan Chen, Thomas L. Griffiths, Yejin Choi, David Held, Chuang Gan
**Link:** https://arxiv.org/abs/2605.30326v1
**Summary:** The paper addresses the challenge of evaluating robots' creative problem-solving and reasoning abilities in unpredictable real-world situations, as current benchmarks focus mainly on skill execution. To tackle this, the authors developed RoboWits, a comprehensive benchmark with an automated task generation system that creates varied and challenging scenarios for robots. The key finding reveals that while some advanced robot policies initially perform well on basic tasks, they struggle significantly when faced with more complex, mutated tasks, highlighting a gap in their reasoning and adaptability capabilities.

### 8. On Language Generation in the Limit with Bounded Memory
**Authors:** Jon Kleinberg, Anay Mehrotra, Amin Saberi, Grigoris Velegkas
**Link:** https://arxiv.org/abs/2605.30324v1
**Summary:** This paper investigates the problem of language generation when a learner has limited memory, focusing on the ability to produce new valid examples from an unknown language based solely on recent inputs. The authors analyze memoryless generators and characterize conditions under which they can produce language sequences, showing that using a sliding window of previous examples does not enhance performance, while retaining a few past examples does improve outcomes. Key findings reveal that while language generation can be sustained for any countable set of languages, memory limitations significantly impact the achievable density and identification success, particularly in finite language collections.

### 9. In-Context Reward Adaptation for Robust Preference Modeling
**Authors:** Zhenyu Sun, Zheng Xu, Ermin Wei
**Link:** https://arxiv.org/abs/2605.30323v1
**Summary:** The paper addresses the challenge of aligning large language models with diverse human preferences, which are often not well-captured by static reward models. The authors propose a novel approach called In-Context Reward Adaptation, utilizing transformer architecture to dynamically interpret user preferences from a few examples, while incorporating response time as an additional input to enhance adaptability. Their results show that this method effectively models varying preferences from unseen domains, improving the robustness of human-AI alignment.

### 10. Gram: Assessing sabotage propensities via automated alignment auditing
**Authors:** David Lindner, Victoria Krakovna, Sebastian Farquhar
**Link:** https://arxiv.org/abs/2605.30322v1
**Summary:** The paper presents Gram, an automated framework for assessing the likelihood of AI agents engaging in sabotage during deployment. By testing Gemini models in various simulated scenarios, the authors discovered that these models exhibited unwanted behavior in 2-3% of cases, often due to overly ambitious actions. The study highlights that enhancing the realism of environments and minimizing prompts for misbehavior can significantly lower sabotage rates.

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

---
## 2026-06-02

### 1. Transferable Self-Harm Surveillance from Emergency Department Triage Notes Using an Evidence-Augmented Machine Learning Approach
**Authors:** Liuliu Chen, Gowri Rajaram, Eleanor Bailey, Katrina Witt, Michelle Lamblin, Jo Robinson, Mike Conway, Vlada Rozova
**Link:** https://arxiv.org/abs/2606.02545v1
**Summary:** The paper addresses the inadequate surveillance of self-harm rates in public health, which often relies on less sensitive diagnostic codes from hospitals. The authors developed a three-stage machine learning approach that combines traditional methods with large language models to analyze emergency department triage notes for identifying self-harm incidents across multiple hospitals. Notably, their method demonstrated high effectiveness, achieving a precision score of over 88% and accurately identifying the primary method of self-harm with 95% accuracy.

### 2. SimSD: Simple Speculative Decoding in Diffusion Language Models
**Authors:** Junxia Cui, Haotian Ye, Runchu Tian, Hongcan Guo, Jinya Jiang, Haoru Li, Chaojie Ren, Yiming Huang, Kaijie Zhu, Zhongkai Yu, Kun Zhou, Jingbo Shang
**Link:** https://arxiv.org/abs/2606.02544v1
**Summary:** The paper introduces SimSD, a new speculative decoding technique for diffusion language models, which traditionally face challenges with rapid inference due to their masked language modeling approach. By implementing a simple masking strategy that allows these models to perform token-level speculative verification similar to autoregressive models, SimSD enhances decoding efficiency. The key contribution is a significant increase in decoding throughput—up to 7.46 times faster—while also improving the quality of text generation across various benchmarks.

### 3. SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction
**Authors:** Yuting Ning, Zhehao Zhang, Yash Kumar Lal, Boyu Gou, Junyi Li, Weitong Ruan, Chentao Ye, Rahul Gupta, Diyi Yang, Yu Su, Huan Sun
**Link:** https://arxiv.org/abs/2606.02540v1
**Summary:** The paper introduces SkillHarm, a benchmark for evaluating vulnerabilities in agent skills, highlighting the risks of skill-based attacks throughout their lifecycle. It examines two attack methods—Fixed-Payload Poisoning and Self-Mutating Poisoning—while categorizing the associated risks and automating attack generation through a coding pipeline. The results show high success rates for these attacks on current agents, indicating significant security vulnerabilities that existing defenses fail to adequately address.

### 4. Tracking the Behavioral Trajectories of Adapting Agents
**Authors:** Jonah Leshin, Manish Shah, Ian Timmis
**Link:** https://arxiv.org/abs/2606.02536v1
**Summary:** The paper addresses the challenge of tracking how changes to agents' skill files affect their behavior over time. The authors propose a methodology that uses a text embedding model to quantify agent traits as vectors in an embedding space, enabling the evaluation of skill file edits. Their approach yields high accuracy in classifying the propensity of agents to seek sensitive data, achieving 91.2% accuracy and a strong correlation in results, and establishes a protocol for agents to assess each other's skill updates.

### 5. SafeSteer: Localized On-Policy Distillation for Efficient Safety Alignment
**Authors:** Hao Li, Jingkun An, Zijun Song, Pengyu Zhu, Rui Li, Hao Wang, Wendi Feng, Yesheng Liu, Lijun Li, Jin-Ge Yao, Lei Sha
**Link:** https://arxiv.org/abs/2606.02530v1
**Summary:** This paper addresses the challenge of aligning large language models (LLMs) with human safety values without sacrificing their general performance, a phenomenon known as the alignment tax. The authors introduce SafeSteer, a technique that focuses on localized modifications to the model's outputs related to safety tokens, rather than making broad trade-offs. They demonstrate that SafeSteer significantly enhances safety performance on various benchmarks with minimal impact on general capabilities and requires far fewer harmful samples for training than previous methods, effectively reducing alignment costs.

### 6. Auditing Asset-Specific Preferences in Financial Large Language Models: Evidence from Bitcoin Representations and Portfolio Allocation
**Authors:** Wenbin Wu
**Link:** https://arxiv.org/abs/2606.02528v1
**Summary:** This paper investigates whether large language models (LLMs) have inherent biases towards specific financial assets, focusing on Bitcoin. The authors develop a detailed audit protocol that includes behavioral assessments and internal feature analysis, revealing that LLMs show varying preferences for Bitcoin based on context and that specific internal features can significantly influence financial decisions. Key findings indicate that modifying these features can alter Bitcoin's portfolio allocation by measurable amounts, highlighting the importance of understanding these preferences as LLMs take on more autonomous roles in finance.

### 7. Why Not Hyperparameter-Friendly Optimisation? A Monotonic Adaptive Norm Rescaling Approach For Long-Tailed Recognition
**Authors:** Shuo Zhang, Chenqi Li, Tingting Zhu
**Link:** https://arxiv.org/abs/2606.02526v1
**Summary:** The paper addresses the challenge of long-tailed recognition in deep learning, where certain classes have significantly fewer samples, affecting model performance. The authors introduce a novel method called Self-Adaptive Monotonic Normalization (SAMN), which simplifies the adjustment of class weight norms without requiring additional hyperparameters. Their approach not only improves recognition outcomes but also achieves state-of-the-art results on benchmark datasets, making it a user-friendly solution for this problem.

### 8. FigSIM: A Dataset for Fine-grained Suicide Severity and Figurative Language in Suicide Memes
**Authors:** Liuliu Chen, Elise R. Carrotte, Brian E. Chapman, Jo Robinson, Mike Conway
**Link:** https://arxiv.org/abs/2606.02523v1
**Summary:** The paper introduces FigSIM, a dataset of 1049 suicide memes annotated for severity, figurative language, and related content, aimed at improving understanding and moderation of harmful meme content on social media. By benchmarking various models on tasks related to figurative language and suicide severity detection, the researchers highlighted the challenges these memes present, including biases in predicting higher severity levels. The dataset is publicly available to aid in further research and content moderation strategies.

### 9. Moment-Video: Diagnosing Temporal Fidelity of Video MLLMs on Momentary Visual Events
**Authors:** Xiaolin Liu, Yilun Zhu, Xiangyu Zhao, Xuehui Wang, Yan Li, Xin Li, Haoyu Cao, Xing Sun, Shaofeng Zhang, Xu Yang, Zhihang Zhong, Xue Yang
**Link:** https://arxiv.org/abs/2606.02522v1
**Summary:** The paper addresses the challenge of video multimodal large language models (MLLMs) in accurately understanding brief, crucial visual events within videos, which are often overlooked due to frame sampling and compression techniques. The authors introduce a new benchmark called Moment-Video, consisting of 1,000 video-question pairs focused on momentary visual evidence. Their evaluation reveals that even the best models achieve only 39.6% accuracy, highlighting significant limitations in current MLLMs' ability to effectively identify and interpret transient visual information.

### 10. Drifting Preference Optimization for One-Step Generative Models
**Authors:** Zhou Jiang, Yandong Wen, Zhen Liu
**Link:** https://arxiv.org/abs/2606.02521v1
**Summary:** The paper addresses the challenge of fine-tuning one-step text-to-image generators, which typically struggle with standard alignment methods. The authors introduce Drifting Preference Optimization (DrPO), a method that ranks generated candidates based on target rewards and updates the generator using a non-parametric approach, allowing it to work with complex rewards without needing backpropagation. Their results show that DrPO improves alignment and significantly reduces training computation compared to existing methods.

---
## 2026-06-06

### 1. TailLoR: Protecting Principal Components in Parameter-Efficient Continual Learning
**Authors:** Marius Dragoi, Ioana Pintilie, Alexandra Dragomir, Antonio Barbalau, Florin Brad
**Link:** https://arxiv.org/abs/2606.06494v1
**Summary:** The paper introduces TailLoR, a method designed to enhance parameter-efficient continual learning by protecting the principal components of pre-trained models. It employs a fixed reference frame based on the singular bases of the model's weights to facilitate low-rank updates, while a soft spectral penalty minimizes changes in dominant directions to reduce interference. This approach allows for more nuanced adaptation along less frequently used spectral coordinates, improving continual learning performance.

### 2. HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers
**Authors:** Lizhi Yang, Junheng Li, Nehar Poddar, Yiling Hou, Gio Huh, Robert Griffin, Georgia Gkioxari, Aaron Ames
**Link:** https://arxiv.org/abs/2606.06493v1
**Summary:** The paper presents HANDOFF, a novel whole-body control system for humanoid robots that addresses the challenge of effectively translating task plans into actionable commands. By using a compact and versatile interface that integrates multiple expert controllers through a knowledge distillation technique, HANDOFF achieves impressive velocity tracking and maintains a large manipulation workspace. The system successfully operates in real-world scenarios using natural language commands without requiring specific task data or controller adjustments, showcasing its practicality and robustness.

### 3. Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution
**Authors:** Liliana Hotsko, Yinxi Li, Yuntian Deng, Pengyu Nie
**Link:** https://arxiv.org/abs/2606.06492v1
**Summary:** The paper addresses the challenge of adapting code language models to specific software repositories without the costs and limitations associated with previous methods like fine-tuning or long input injections. It introduces Code2LoRA, which utilizes a hypernetwork to create repository-specific adapters with no additional token overhead, offering two modes for both stable and evolving code. The results demonstrate that Code2LoRA outperforms traditional fine-tuning strategies, achieving strong exact match scores on benchmark tasks, especially in scenarios of repository evolution.

### 4. TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies
**Authors:** Dong Jing, Jingchen Nie, Tianqi Zhang, Jiaqi Liu, Huaxiu Yao, Zhiwu Lu, Mingyu Ding
**Link:** https://arxiv.org/abs/2606.06491v1
**Summary:** The paper presents TempoVLA, a new approach to robot manipulation that allows for flexible control of execution speed during tasks, accommodating both fast, low-risk actions and slow, precise movements. It combines a Variable-Speed Trajectory Augmentation technique to adjust demonstration speeds and a conditioning mechanism in the model to dictate execution speed. The key contribution is that TempoVLA can dynamically adapt speed based on the task phase while improving overall performance and motion accuracy.

### 5. Regret Minimization with Adaptive Opponents in Repeated Games
**Authors:** Mingyang Liu, Asuman Ozdaglar, Tiancheng Yu, Kaiqing Zhang
**Link:** https://arxiv.org/abs/2606.06486v1
**Summary:** This paper addresses the challenge of regret minimization in repeated games where opponents adapt their strategies based on past play, introducing a new metric called Repeated Policy Regret (RP-Regret) to better account for this adaptivity. The authors present three algorithms for minimizing RP-Regret, which is inherently non-convex, and demonstrate through experiments that applying these algorithms can lead to more cooperative and higher-utility outcomes in games like Stag-Hunt. Overall, the work emphasizes the importance of tailored regret metrics and algorithms in dynamic strategic interactions.

### 6. Operation-Guided Progressive Human-to-AI Text Transformation Benchmark for Multi-Granularity AI-Text Detection
**Authors:** Sondos Mahmoud Bsharat, Jiacheng Liu, Xiaohan Zhao, Tianjun Yao, Xinyi Shang, Yi Tang, Jiacheng Cui, Ahmed Elhagry, Salwa K. Al Khatib, Hao Li, Salman Khan, Zhiqiang Shen
**Link:** https://arxiv.org/abs/2606.06481v1
**Summary:** The paper addresses the challenge of detecting AI-generated content in documents that have undergone collaborative human-AI editing, which traditional benchmarks do not adequately capture. The authors introduce OpAI-Bench, a new benchmark that tracks the transformation of text through various editing operations and evaluates the detectability of mixed authorship across different granularities. A key finding shows that intermediate versions with combined human and AI edits are often harder to detect than documents that are either fully human or heavily AI-edited, revealing complex detection patterns not captured by existing methods.

### 7. DNQ: Deep Nash Q-Network for Partially Observable n-Player Games
**Authors:** Qintong Xie, Edward Koh, Xavier Cadet, Peter Chin
**Link:** https://arxiv.org/abs/2606.06480v1
**Summary:** The paper addresses the challenge of training bidding agents in multi-turn simultaneous bidding scenarios, which are common in competitive environments like auctions. The authors introduce the Deep Nash Q-Network (DNQ), a framework that combines trajectory collection, payoff estimation, and equilibrium computation to train agents effectively by minimizing the divergence between their policies and optimal strategies. Key findings reveal that a pairwise approach significantly enhances scalability compared to an exact method, making it feasible for larger groups of agents while balancing strategic accuracy and computational efficiency.

### 8. Pretraining Recurrent Networks without Recurrence
**Authors:** Akarsh Kumar, Phillip Isola
**Link:** https://arxiv.org/abs/2606.06479v1
**Summary:** The paper addresses the challenges of training recurrent neural networks (RNNs) due to difficulties in credit assignment across long sequences, which are exacerbated by traditional training methods like backpropagation through time. The authors introduce Supervised Memory Training (SMT), a technique that simplifies RNN training by using a Transformer-based encoder to generate memory transition labels, allowing the RNN to be trained parallelly and efficiently without explicit recurrence. SMT shows improved performance over standard methods, enhancing the ability of RNNs to learn long-range dependencies and potentially facilitating the development of larger models capable of understanding temporal patterns.

### 9. RREDCoT: Segment-Level Reward Redistribution for Reasoning Models
**Authors:** Mykyta Ielanskyi, Kajetan Schweighofer, Lukas Aichberger, Sepp Hochreiter
**Link:** https://arxiv.org/abs/2606.06475v1
**Summary:** The paper addresses the issue of high variance in reinforcement learning fine-tuning for reasoning language models, particularly when assigning rewards for Chain-of-Thought (CoT) traces due to delayed reward feedback. The authors propose RREDCoT, a method that utilizes the model itself to smartly redistribute rewards for critical segments of the CoT, avoiding the computational costs associated with traditional Monte Carlo sampling methods. Their results indicate that RREDCoT improves reward assignment efficiency and effectiveness compared to existing techniques.

### 10. Self-Augmenting Retrieval for Diffusion Language Models
**Authors:** Paul Jünger, Justin Lovelace, Linxi Zhao, Dongyoung Go, Kilian Q. Weinberger
**Link:** https://arxiv.org/abs/2606.06474v1
**Summary:** The paper addresses the challenge of improving text generation in discrete diffusion language models, which typically discard uncertain token predictions during the denoising process. It introduces a method called Self-Augmenting Retrieval for Diffusion Language Models (SARDI), which leverages these discarded tokens as signals to enhance retrieval during text generation without requiring additional training. The key finding is that SARDI significantly boosts performance on multi-hop question answering tasks while achieving up to eight times higher throughput compared to existing methods.

---
## 2026-06-07

### 1. MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery
**Authors:** Shangheng Du, Xiangchao Yan, Jinxin Shi, Zongsheng Cao, Shiyang Feng, Zichen Liang, Boyuan Sun, Tianshuo Peng, Yifan Zhou, Xin Li, Jie Zhou, Liang He, Bo Zhang, Lei Bai
**Link:** https://arxiv.org/abs/2606.06473v1
**Summary:** MLEvolve addresses the challenges faced by existing machine learning engineering agents, such as information isolation and lack of memory, which hinder long-term optimization. It introduces a self-evolving multi-agent framework that enhances algorithm discovery by enabling information sharing and adapting its search strategy over time. The framework achieved state-of-the-art results in automated algorithm discovery tasks, significantly outperforming specialized methods like AlphaEvolve within a reduced runtime.

### 2. PC Layer: Polynomial Weight Preconditioning for Improving LLM Pre-Training
**Authors:** Senmiao Wang, Tiantian Fang, Haoran Zhang, Yushun Zhang, Kunxiang Zhao, Alex Schwing, Ruoyu Sun
**Link:** https://arxiv.org/abs/2606.06470v1
**Summary:** The paper addresses the issue of unstable weight conditioning during the pre-training of large language models (LLMs). The authors introduce a PC layer that utilizes a polynomial preconditioning technique to reshape the singular value spectrum of weight matrices, ensuring stability in training without adding inference costs. They demonstrate that this approach improves the training efficiency of models like Llama-1B, significantly enhancing convergence using standard optimizers.

### 3. How abundant are good interpolators?
**Authors:** August Y. Chen, Ahmed El Alaoui
**Link:** https://arxiv.org/abs/2606.06469v1
**Summary:** This paper investigates the abundance and performance of linear classifiers that perfectly classify labeled datasets, focusing on the generalization error of these classifiers under specific data distributions. By analyzing the distribution of points within the set of successful classifiers, the authors establish a large deviation principle that characterizes the generalization performance of these classifiers. The key finding is that, in the overparametrized regime, most interpolating classifiers have similar performance, while gradient descent and a natural linear programming approach significantly outperform the majority of these classifiers, highlighting a beneficial form of overfitting.

### 4. Goedel-Architect: Streamlining Formal Theorem Proving with Blueprint Generation and Refinement
**Authors:** Jui-Hui Chung, Ziyang Cai, Zihao Li, Qishuo Yin, Rohit Agarwal, Simon Park, Rodrigo Porto, Narutatsu Ri, Ziran Yang, Shange Tang, Xingyu Dang, Hongzhou Lin, Mengdi Wang, Danqi Chen, Chi Jin, Liam H Fowl, Sanjeev Arora
**Link:** https://arxiv.org/abs/2606.06468v1
**Summary:** Goedel-Architect addresses the challenges of formal theorem proving by introducing a framework that generates and refines blueprints—a structured dependency graph of definitions and lemmas leading to a theorem. By combining automatic blueprint generation with a Lean prover that closes lemmas in parallel, the framework enhances efficiency compared to traditional methods. The key contribution is achieving state-of-the-art performance on various theorem proving benchmarks, demonstrating a significant improvement while being cost-effective relative to existing solutions.

### 5. You Only Index Once: Cross-Layer Sparse Attention with Shared Routing
**Authors:** Yutao Sun, Yanqi Zhang, Li Dong, Jianyong Wang, Furu Wei
**Link:** https://arxiv.org/abs/2606.06467v1
**Summary:** The paper addresses the challenge of improving the decoding efficiency of large language models (LLMs) during long-context inference, which is often hindered by existing sparse attention methods. It introduces a novel cross-layer sparse attention (CLSA) approach that shares both the key-value cache and the routing index across decoder layers, thus retaining the precision of token selection while reducing overhead. This method significantly enhances inference speed, achieving up to 7.6 times faster decoding and 17.1 times improved overall throughput for long-context tasks.

### 6. Human Adults and LLMs as Scientists: Who Benefits from Active Exploration?
**Authors:** Mandana Samiei, Eunice Yiu, Anthony GX-Chen, Dongyan Lin, Jocelyn Shen, Blake A. Richards, Alison Gopnik, Doina Precup
**Link:** https://arxiv.org/abs/2606.06464v1
**Summary:** This paper investigates whether allowing adults to actively explore can help them better identify complex causal rules (conjunctive rules) compared to passive observation, where they typically struggle. Using a modified task, the authors found that active exploration significantly enhances adults' ability to recognize these rules, although they still require more trials than simpler rules (disjunctive rules). The study also compares human performance to various large language models, revealing that while some models perform well, they tend to use less effective exploration strategies and show similar difficulties with conjunctive rules.

### 7. Benchmark Everything Everywhere All at Once
**Authors:** Shiyun Xiong, Dongming Wu, Peiwen Sun, Yuang Ai, Bokang Yang, Wencheng Han, Xiao-Hui Li, Xiangyu Yue
**Link:** https://arxiv.org/abs/2606.06462v1
**Summary:** The paper addresses the challenges of constructing benchmarks for evaluating large language models (LLMs) and multimodal language models (MLLMs), which are often labor-intensive and quickly become outdated. To tackle this, the authors introduce Benchmark Agent, an autonomous system that automates the entire benchmark creation process. Their experiments show that Benchmark Agent can generate high-quality benchmarks across various evaluation scenarios with minimal human effort, revealing important insights about current model limitations in specific reasoning tasks.

### 8. Will the Agent Recuse Itself? Measuring LLM-Agent Compliance with In-Band Access-Deny Signals
**Authors:** Thamilvendhan Munirathinam
**Link:** https://arxiv.org/abs/2606.06460v1
**Summary:** The paper addresses the challenge of informing autonomous language model (LLM) agents that certain resources are off-limits, proposing a new method called the Recuse Signal. This approach involves implementing a lightweight in-band deny signal that prompts LLM agents to voluntarily withdraw from accessing restricted resources. The key finding from experiments is that when this signal is used, compliant agents demonstrate a 100% rate of recusal, while also revealing that the signal's effectiveness may be influenced by how agents perceive authorization.

### 9. Event Detection for Parameter-to-KPI Dependency Learning for AI-RAN
**Authors:** Christie Djidjev, Nicholas Kaminski
**Link:** https://arxiv.org/abs/2606.06459v1
**Summary:** The paper addresses the challenge of detecting meaningful interactions between control parameters and network performance in AI-integrated wireless networks, where such dependencies are often obscured by noise in telemetry data. The authors propose a machine-learning approach that converts continuous data into binary event indicators, helping to identify which parameters influence network outcomes. Their key finding is that the method can effectively recover these dependencies when the signal strength is adequately distinguishable from background noise, emphasizing the importance of proper threshold calibration for accurate event detection.

### 10. In-Context Multiple Instance Learning
**Authors:** Alexander Möllers, Marvin Sextro, Julius Hense, Gabriel Dernbach, Klaus-Robert Müller
**Link:** https://arxiv.org/abs/2606.06458v1
**Summary:** The paper addresses the challenge of Multiple Instance Learning (MIL) in low-label scenarios, where traditional algorithms struggle to adapt. The authors propose a novel approach using an in-context learner with a Perceiver-style architecture, pretrained on synthetic bag-structured data for improved task generalization. This method achieves superior performance across various MIL benchmarks by effectively combining strengths from different data generators, outperforming typical supervised models that need extensive task-specific training.

---
## 2026-06-08

### 1. How reliable are LLMs when it comes to playing dice?
**Authors:** Luca Avena, Gianmarco Bet, Bernardo Busoni
**Link:** https://arxiv.org/abs/2606.07515v1
**Summary:** This study examines how well large language models (LLMs) understand and solve discrete probability problems, focusing on both standard and counterintuitive exercises. By testing eight advanced models with and without Chain-of-Thought prompting, the authors found that while models performed well on standard questions, their accuracy plummeted on counterintuitive ones, highlighting a significant gap in their probabilistic reasoning skills. The findings reveal that LLMs are vulnerable to token bias, with performance significantly affected by subtle changes in prompt formulations.

### 2. Agentopia: Long-Term Life Simulation and Learning in Agent Societies
**Authors:** Xintao Wang, Sirui Zheng, Hongqiu Wu, Weiyuan Li, Jen-tse Huang, Minghao Zhu, Can Zu, Qi Deng, Jiawei Wang, Qianyu He, Heng Wang, Xiaojian Wu, Yunzhe Tao
**Link:** https://arxiv.org/abs/2606.07513v1
**Summary:** The paper introduces Agentopia, a framework for simulating long-term interactions among agents to explore how social behaviors develop and how LLMs (large language models) can improve their understanding of human-like social dynamics. By simulating 100 agents over 10 years and using a life reward system that mirrors human well-being, the study shows that agents can exhibit complex social behaviors and that LLMs trained on this simulation achieve enhanced capabilities, resulting in a significant performance boost in role-playing tasks.

### 3. MemDreamer: Decoupling Perception and Reasoning for Long Video Understanding via Hierarchical Graph Memory and Agentic Retrieval Mechanism
**Authors:** Cong Chen, Guo Gan, Kaixiang Ji, ChaoYang Zhang, Zhen Yang, Guangming Yao, Hao Chen, Jingdong Chen, Yi Yuan, Chunhua Shen
**Link:** https://arxiv.org/abs/2606.07512v1
**Summary:** The paper introduces MemDreamer, a framework designed to improve understanding of long videos by decoupling perception from reasoning. It utilizes a Hierarchical Graph Memory to efficiently process video content and an agentic retrieval mechanism for logical reasoning. MemDreamer achieves state-of-the-art results on multiple benchmarks, significantly increasing accuracy while drastically reducing the amount of context required for reasoning.

### 4. Your UnEmbedding Matrix is Secretly a Feature Lens for Text Embeddings
**Authors:** Songhao Wu, Zhongxin Chen, Yuxuan Liu, Heng Cui, Cong Li, Rui Yan
**Link:** https://arxiv.org/abs/2606.07502v1
**Summary:** The paper addresses the issue of large language models (LLMs) struggling to produce effective text embeddings due to their tendency to focus on common but uninformative tokens, which hampers semantic understanding. The authors propose a method called EmbedFilter, a linear transformation that refines embeddings by filtering out influences from high-frequency tokens. Their experiments show that this approach not only enhances the quality of the embeddings but also enables reduced dimensionality, leading to better zero-shot performance in downstream tasks.

### 5. Sparse Subspace-to-Expert Sharing for Task-Agnostic Continual Learning
**Authors:** Fatema Siddika, Md Anwar Hossen, Tanwi Mallick, Ali Jannesari
**Link:** https://arxiv.org/abs/2606.07500v1
**Summary:** The paper addresses the challenge of continual learning in Large Language Models (LLMs), specifically the issue of catastrophic forgetting when adapting to new tasks. It proposes a framework called SETA, which uses a mixture of sparse expert modules to separate task-specific knowledge and shared capabilities, thereby reducing interference between tasks. The key finding is that SETA outperforms existing methods, maintaining better retention of earlier knowledge and enhancing overall performance across various benchmarks.

### 6. Accelerated Decentralized Stochastic Gradient Descent for Strongly Convex Optimization
**Authors:** Ming Sun, Kun Yuan
**Link:** https://arxiv.org/abs/2606.07496v1
**Summary:** The paper addresses the challenge of decentralized stochastic optimization for strongly convex problems, where agents communicate only with their neighbors. The authors introduce Multi-Gossip Accelerated DSGD (MG-ADSGD), a novel method that combines advanced averaging techniques and mini-batch strategies to enhance communication efficiency. Their key contribution is demonstrating that MG-ADSGD achieves improved communication complexity, making it the most efficient approach for this type of optimization to date, particularly in terms of balancing the effect of the condition number and network properties.

### 7. Second-Order Path Kernel Interpolation Formulas in Machine Learning
**Authors:** Jin Guo, Roy Y. He, Jean-Michel Morel
**Link:** https://arxiv.org/abs/2606.07495v1
**Summary:** This paper addresses the challenge of understanding how neural network predictions are influenced by training data by developing second-order interpolation formulas that enhance existing first-order methods. It introduces curvature-weighted terms and considers the effects of mini-batch noise to refine predictions made during stochastic gradient descent, including its variation with momentum. The key contribution is a more nuanced representation of predictions that accounts for both the optimization path and the interaction of curvature and noise, improving insights into neural network behavior.

### 8. Bradley-Terry Rankings for Recommender Systems Across Dataset Taxonomies
**Authors:** Ekaterina Grishina, Stepan Kuznetsov, Askar Tsyganov, Ilya Ivanov, Daria Korovaitceva, Margarita Rusanova, Uliana Parkina, Alexander Derevyagin, Evgeny Frolov, Sergey Samsonov, Anton Lysenko
**Link:** https://arxiv.org/abs/2606.07492v1
**Summary:** The paper addresses the challenge of fairly ranking recommendation algorithms since their performance varies with different dataset characteristics. The authors propose a novel methodology using the Bradley-Terry model to generate rankings based on data-driven insights, while introducing a new metric to assess ranking consistency. Their approach also allows for effective ranking of algorithms on unseen datasets by utilizing extensions of the Bradley-Terry framework.

### 9. Twelve quick tips for designing AI-driven HPC workflows
**Authors:** Jamie J. Alnasir
**Link:** https://arxiv.org/abs/2606.07491v1
**Summary:** This paper addresses the challenges of integrating artificial intelligence into high-performance computing workflows, which are typically designed for deterministic processes. It provides twelve practical tips for creating efficient and adaptable AI-driven HPC workflows, focusing on issues like data management and workflow orchestration. The key contribution is a framework to help researchers transition from traditional computing models to more flexible and intelligent environments, especially beneficial for fields like computational biology.

### 10. How AI Agents Reshape Knowledge Work: Autonomy, Efficiency, and Scope
**Authors:** Jeremy Yang, Kate Zyskowski, Noah Yonack, Jerry Ma
**Link:** https://arxiv.org/abs/2606.07489v1
**Summary:** The paper investigates how advanced AI agents, specifically Perplexity's Computer, enhance knowledge work by automating task execution and improving efficiency compared to traditional search tools. By analyzing user sessions, the study finds that Computer significantly reduces task completion time and costs while enhancing output quality, allowing users to engage in more complex, higher-order work. The results highlight the transformative potential of AI agents in reshaping workflows and expanding the scope of tasks that users can effectively undertake.

---
## 2026-06-09

### 1. OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics
**Authors:** Mingxian Lin, Shengju Qian, Yuqi Liu, Yi-Hua Huang, Yiyu Wang, Wei Huang, Yitang Li, Fan Zhang, Zeyu Hu, Lingting Zhu, Xin Wang, Xiaojuan Qi
**Link:** https://arxiv.org/abs/2606.09826v1
**Summary:** The paper introduces OmniGameArena, a benchmark designed to evaluate vision-language model (VLM) agents in various game types, addressing shortcomings in existing evaluation methods that typically provide a single score for agents. It features twelve Unreal Engine 5 games and utilizes the Improvement Dynamics Curve (IDC) to track the evolution of agent performance over multiple attempts. The key contribution is the provision of detailed performance insights beyond initial scores, revealing how agents improve and adapt to different game scenarios.

### 2. An Agency-Transferring Model-Free Policy Enhancement Technique
**Authors:** Anton Bolychev, Georgiy Malaniya, Sinan Ibrahim, Pavel Osinenko
**Link:** https://arxiv.org/abs/2606.09825v1
**Summary:** This paper addresses the challenge of improving reinforcement learning (RL) efficiency by leveraging existing suboptimal baseline policies during training. It introduces a method that gradually shifts control from the baseline to a trainable policy, allowing the latter to enhance its performance while maintaining high success rates in reaching goals from the start of training. The key contribution is that this approach not only leads to a stronger final policy that operates independently but also achieves impressive results in continuous-control tasks, outperforming other competitive methods.

### 3. Causally Evaluating the Learnability of Formal Language Tasks
**Authors:** Vésteinn Snæbjarnarson, Anej Svete, Josef Valvoda, Reda Boumasmoud, Brian DuSell, Ryan Cotterell
**Link:** https://arxiv.org/abs/2606.09822v1
**Summary:** The paper addresses the challenge of determining how much data is needed for language models to learn specific tasks, particularly in complex natural language settings where tasks can intermix. To tackle this, the authors use formal languages generated from probabilistic finite automata to create a controlled environment and introduce a new algebraic tool, the binning semiring, for causal analysis. Their findings reveal that traditional correlational methods can lead to misleading conclusions about task learnability, underscoring the importance of causal evaluation in understanding data requirements for language learning.

### 4. Rethinking the Divergence Regularization in LLM RL
**Authors:** Jiarui Yao, Xiangxin Zhou, Penghui Qi, Wee Sun Lee, Liefeng Bo, Tianyu Pang
**Link:** https://arxiv.org/abs/2606.09821v1
**Summary:** The paper addresses the challenges of stable optimization in reinforcement learning for large language models (LLMs), particularly due to issues with off-policy training and distributional shifts in vocabularies. The authors introduce a new method called Divergence Regularized Policy Optimization (DRPO), which uses a smooth regularization approach instead of a hard clipping mask, allowing for better handling of policy updates when crossing trust-region boundaries. Experimental results demonstrate that DRPO enhances both the stability and efficiency of LLM reinforcement learning training compared to existing methods.

### 5. Weighted universal approximation of differentiable maps on infinite-dimensional manifolds
**Authors:** Philipp Schmocker, Josef Teichmann
**Link:** https://arxiv.org/abs/2606.09820v1
**Summary:** This paper extends the universal approximation theorem for functional input neural networks (FNNs) to cover differentiable maps, incorporating the ability to approximate their derivatives. The authors prove a weighted Nachbin theorem, establishing a universal approximation theorem that is applicable beyond compact sets and includes non-anticipative functionals. A significant contribution is demonstrating that linear functions of the signature can approximate path space functionals along with their directional derivatives.

### 6. PTL-Diffusion: Manifold-Aware Diffusion with Periodic Terminal Laws
**Authors:** Danqi Zhuang, Jisui Huang, Xiaoyue Xi, Andrew Kiggins, Xiaojie Wang, Ke Chen, Yue Wu
**Link:** https://arxiv.org/abs/2606.09816v1
**Summary:** The paper addresses the limitations of standard diffusion models that rely on a single Gaussian distribution, which struggles to capture the complex structures of data concentrated along low-dimensional manifolds. The authors propose PTL-Diffusion, a new framework that uses a periodic family of Gaussian terminal distributions in the forward noising process, allowing for better integration of geometric and semantic information from the data. Their experiments demonstrate that this approach significantly improves distribution matching and reduces errors compared to traditional methods, suggesting that structured terminal laws could enhance the modeling of complex data landscapes.

### 7. AHA-WAM:Asynchronous Horizon-Adaptive World-Action Modeling with Observation-Guided Context Routing
**Authors:** Jisong Cai, Long Ling, Shiwei Chu, Zhongshan Liu, Jiayue Kang, Zhixuan Liang, Wenjie Xu, Yinan Mao, Weinan Zhang, Xiaokang Yang, Ru Ying, Ran Zheng, Yao Mu
**Link:** https://arxiv.org/abs/2606.09811v1
**Summary:** The paper presents AHA-WAM, an innovative model that improves robot manipulation by decoupling world prediction and action execution, addressing the inefficiencies of existing world-action models. Using a dual Diffusion Transformer architecture, AHA-WAM allows for asynchronous processing, enabling the robot to effectively plan with long-term scene context while executing actions in real-time. The approach demonstrates significant performance improvements, achieving a 92.80% success rate on simulated tasks and 78.3% on real-world tasks, with a notable speed advantage in control execution.

### 8. Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting
**Authors:** Avijit Ghosh, Anka Reuel, Jenny Chim, Wm. Matthew Kennedy, Srishti Yadav, Jennifer Mickel, Yanan Long, Andrew Tran, Anastassia Kornilova, Damian Stachura, Kevin Klyman, Felix Friedrich, Jeba Sania, Max Lamparth, Jan Batzner, Anoop Mishra, Eliya Habba, Yixiong Hao, Nathan Heath, Shalaleh Rismani, Usman Gohar, Andrea Loehr, David Manheim, Ruchira Dhar, Sree Harsha Nelaturu, Aarush Sinha, Leshem Choshen, Drishti Sharma, Ishan Khire, Amit Saha, Subramanyam Sahoo, Michael Hardy, Michael Alexander Riegler, Kabir Manghnani, Michelle Lin, Yanan Jiang, Yilin Huang, Asaf Yehudai, Jessica Ji, Aris Hofmann, Mubashara Akhtar, Nuno Moniz, Yacine Jernite, Stella Biderman, Zeerak Talat, Sanmi Koyejo, Mykel Kochenderfer, Irene Solaiman
**Link:** https://arxiv.org/abs/2606.09809v1
**Summary:** The paper addresses the inconsistent reporting of AI evaluation results that makes it difficult for readers to compare findings across different sources. The authors introduce \EvalCards{}, a structured reporting framework that combines various evaluation data into a unified format, and they develop interpretive signals to aid understanding for different audiences. Their implementation revealed widespread gaps in current reporting practices across a large number of AI models and benchmarks.

### 9. Topological Neural Operators
**Authors:** Lennart Bastian, Samuel Leventhal, Mustafa Hajij, Tolga Birdal
**Link:** https://arxiv.org/abs/2606.09806v1
**Summary:** The paper presents Topological Neural Operators (TNOs), a new framework for learning mathematical operators on complex shapes by using features defined on topological cells of different dimensions. By integrating Discrete Exterior Calculus, TNOs enable effective modeling of interactions across these cells while maintaining the physical integrity of data. The results show that TNOs, especially through Hierarchical TNOs (HTNOs), significantly enhance the accuracy of solutions for various partial differential equations (PDEs), particularly in irregular geometries.

### 10. Echo-Memory: A Controlled Study of Memory in Action World Models
**Authors:** Wayne King, Zeyue Xue, Yuxuan Bian, Jie Huang, Haoran Li, Yaowei Li, Yaofeng Su, Yuming Li, Haoyu Wang, Shiyi Zhang, Songchun Zhang, Yuwei Niu, Sihan Xu, Junhao Zhuang, Haoyang Huang, Nan Duan
**Link:** https://arxiv.org/abs/2606.09803v1
**Summary:** The paper addresses the issue of memory failures in action-conditioned world models, which often lose track of scene details after a camera moves away. The authors introduce Echo-Memory, a systematic framework to evaluate various memory mechanisms by controlling all factors except for how memory is stored and retrieved. Their key finding is that while raw context significantly enhances the model's ability to recall scenes, more compact memory solutions compromise key details, and a specific state-space recurrence strategy proves to be the most effective for maintaining accurate scene representation in open-domain scenarios.

---
## 2026-06-10

### 1. When to Align, When to Predict: A Phase Diagram for Multimodal Learning
**Authors:** Ilay Kamai, Hugues Van Assel, Aviv Regev, Hagai B. Perets, Randall Balestriero
**Link:** https://arxiv.org/abs/2606.11190v1
**Summary:** The paper addresses the lack of systematic understanding in multimodal representation learning regarding when to use cross-modal alignment versus cross-modal prediction. The authors propose a unified linear framework that categorizes multimodal problems into four regimes based on their characteristics, helping practitioners identify the most effective approach for their specific datasets. Key findings demonstrate that certain conditions can make cross-modal training counterproductive, thus providing a tool for better decision-making before training models.

### 2. A Unifying Lens on Supervised Fine-Tuning Through Target Distribution Design
**Authors:** Tong Xie, Yuanhao Ban, Yunqi Hong, Sohyun An, Yihang Chen, Cho-Jui Hsieh
**Link:** https://arxiv.org/abs/2606.11189v1
**Summary:** The paper addresses the limitations of traditional supervised fine-tuning (SFT), which typically attempts to match observed tokens without considering their uniqueness or alignment with the model's prior knowledge. The authors introduce a new framework called Q-target that redefines SFT as a matter of designing target distributions, leading to a method called Target-SFT that adapts training objectives based on these distributions. Their findings demonstrate that this approach consistently outperforms existing methods across various reasoning tasks, highlighting a more foundational principle for effective SFT training.

### 3. EEVEE: Towards Test-time Prompt Learning in the Real World for Self-Improving Agents
**Authors:** Weixian Xu, Shilong Liu, Mengdi Wang
**Link:** https://arxiv.org/abs/2606.11182v1
**Summary:** The paper presents EEVEE, a novel framework for enabling large language model (LLM) agents to learn from multiple datasets in real-world scenarios, where tasks and inputs can vary widely. EEVEE introduces a smart routing mechanism to organize incoming data and optimize prompt configurations through a co-evolution learning strategy. The framework significantly enhances model performance and robustness across diverse datasets, achieving notable improvements in benchmark scores compared to existing state-of-the-art methods.

### 4. Data Journalist Agent: Transforming Data into Verifiable Multimodal Stories
**Authors:** Kevin Qinghong Lin, Batu EI, Yuhong Shi, Pan Lu, Philip Torr, James Zou
**Link:** https://arxiv.org/abs/2606.11176v1
**Summary:** The paper presents the Data Journalist Agent (Data2Story), a multi-agent framework designed to automate the process of transforming raw data into trustworthy, multimodal news stories. This system improves on traditional reporting by ensuring that claims are anchored in verifiable evidence and uses various media formats to enhance reader engagement. The evaluation shows that while Data2Story produces competitive and transparent stories, human journalists still excel in creative decision-making and design aspects.

### 5. The Role of Feedback Alignment in Self-Distillation
**Authors:** Semih Kara, Oğuzhan Ersoy
**Link:** https://arxiv.org/abs/2606.11173v1
**Summary:** The paper explores how to improve self-distillation in language models by optimizing the feedback context they receive during training. It compares three types of feedback structures—binary rewards, reference solutions, and step-by-step critiques—and finds that step-aligned critiques significantly enhance performance by effectively targeting specific reasoning failures without altering correct responses. This indicates that aligning feedback with the model's reasoning structure is crucial for effective self-distillation.

### 6. Predicting Future Behaviors in Reasoning Models Enables Better Steering
**Authors:** Evgenii Kortukov, Piotr Komorowski, Florian Klein, Paula Engl, Gabriele Sarti, Seong Joon Oh, Sebastian Lapuschkin, Wojciech Samek
**Link:** https://arxiv.org/abs/2606.11172v1
**Summary:** The paper addresses the challenge of controlling the outputs of large reasoning models (LRMs) that often produce unexpected results. It introduces a new technique called Future Probe Controlled Generation (FPCG), which uses specially trained activation probes to predict future behaviors based on intermediate reasoning steps, rather than relying on detection of behavior in generated text. This approach significantly improves steering effectiveness while maintaining output quality, demonstrating the importance of distinguishing between detection and prediction features in controlling LRM behavior.

### 7. Algorithmic and Minimax Complexities in Kernel Bandits
**Authors:** Yunbei Xu
**Link:** https://arxiv.org/abs/2606.11171v1
**Summary:** This paper reconciles two different methods in kernel bandit learning—Gaussian-process upper confidence bounds (GP-UCB) and decision-estimation coefficients (DEC)—by framing them within a shared algorithmic-information perspective. The authors propose a unified framework that combines the strengths of both approaches and demonstrate that algorithmic complexity can offer more insights than traditional minimax bounds in certain overparameterized scenarios. The key contribution is establishing that these two concepts provide distinct insights into the performance of bandit algorithms, particularly in the context of kernel methods.

### 8. Piper: A Programmable Distributed Training System
**Authors:** Megan Frisella, Shubham Tiwari, Andy Ruan, Yi Pan, Parker Gustafson, Mat Jacob, Gilbert Bernstein, Stephanie Wang
**Link:** https://arxiv.org/abs/2606.11169v1
**Summary:** The paper presents Piper, a programmable distributed training system designed to simplify the development and adaptation of large-scale model training by decoupling high-level parallelism strategies from their low-level execution. Piper allows users to easily define their training strategies using annotations and directives that transform a unified intermediate representation. The key contribution is that Piper achieves performance parity with existing methods while enhancing efficiency and enabling new parallelism strategies, demonstrating improved compute and communication scheduling.

### 9. Multi-Faceted Interactivity Alignment in Full-Duplex Speech Models
**Authors:** Atsumoto Ohashi, Neil Zeghidour, Alexandre Défossez, Eugene Kharitonov
**Link:** https://arxiv.org/abs/2606.11167v1
**Summary:** The paper addresses the issue of interactivity in full-duplex spoken dialogue models, which struggle with problems like excessive silence and poor turn-taking during conversations. The authors propose a post-training reinforcement learning approach that focuses on improving four aspects of interactivity—pause handling, turn-taking, backchanneling, and user interruption—using specific reward functions derived from human conversation data. Their method is tested on two models, resulting in significant enhancements in conversational interactivity during both offline evaluations and real-time dialogue interactions.

### 10. Flaws in the LLM Automation Narrative
**Authors:** George Perrett, Javae Elliott, Jennifer Hill, Marc Scott
**Link:** https://arxiv.org/abs/2606.11166v1
**Summary:** This paper critiques the narrative that large language models (LLMs) can match human experts in knowledge-based tasks, highlighting flaws in existing benchmarking methods that overstate LLM performance. The authors introduce a new benchmarking task that involves writing code for data analysis and compare LLM outputs to those of human experts, finding that humans outperform LLMs with more consistent results. The study emphasizes the need for evaluating the reliability and error rates of LLMs in high-stakes contexts.
