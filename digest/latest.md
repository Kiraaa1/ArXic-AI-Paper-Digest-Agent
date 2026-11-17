---
## 2026-11-17

### 1. Latent Lattice Language Models
**Authors:** Shivam Duggal, Zongze Wu, William T. Freeman, Antonio Torralba, Richard Zhang, Eli Shechtman
**Link:** https://arxiv.org/abs/2611.21608v1
**Summary:** The paper addresses the challenge of enhancing language model performance without solely relying on deeper or looped architectures by introducing a novel approach called the Lattice of Latents. This method maintains horizontal latent streams that work alongside traditional vertical connections to improve computation and information flow. The key contribution is the demonstration that this lattice structure significantly reduces perplexity in language models, achieving improved performance over existing architectures with comparable parameters.

### 2. ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative Policy Optimization
**Authors:** Huawei Lin, Jinting Liu, Tongyan Wang, Xuyang Chen, Ruihua Shi, Zhichao Xu, Jiaxin Qin, Guoshenghui Zhao, Baijian Yang, Yingjie Victor Chen, Tan Yu, Weijie Zhao
**Link:** https://arxiv.org/abs/2611.21605v1
**Summary:** The paper addresses the issue of visual agents providing answers based on common sense rather than actually analyzing high-resolution images. The authors introduce a new method called Cross-Input Relative Policy Optimization (CrossRPO), which trains agents using specially designed contrast sets to ensure they focus on relevant evidence in images. As a result, their trained agents, ViRA-9B and ViRA-27B, achieve superior accuracy in answering questions correctly, surpassing existing models and demonstrating effective learning from evidence rather than assumptions.

### 3. Quantifying the added value of human forecaster discussions for tropical cyclone intensity prediction
**Authors:** Ilia Azizi, Frederick Iat-Hin Tam, Marc-Olivier Boldi, Valérie Chavez-Demoulin, Tom Beucler
**Link:** https://arxiv.org/abs/2611.21602v1
**Summary:** This study investigates how the National Hurricane Center's Tropical Cyclone Discussions enhance forecasts of hurricane intensity by assessing their value beyond standard numerical predictors. By analyzing data from 637 tropical cyclones and employing a deep learning framework, the researchers found that incorporating the discussions improved the accuracy of short-term wind forecasts significantly. The findings underscore the importance of human judgment in forecasting while highlighting the limitations of the data's timeliness for operational use.

### 4. How VLMs Plan What's Next
**Authors:** Rohit Gandikota, Arnab Sen Sharma, Adam Belfki, David Bau
**Link:** https://arxiv.org/abs/2611.21600v1
**Summary:** The paper investigates how vision-language models (VLMs) determine the order in which they describe objects in an image, addressing the lack of clarity around this process. The authors propose a mechanism with four key components that guides the model's focus while generating responses, validated through experiments with Qwen3-VL models. Notably, this framework is applicable across various input formats and model sizes, enhancing understanding of how VLMs handle complex tasks sequentially.

### 5. Hyperlyve: Parallelized Enumeration and Exact Lyapunov Stability Certification for Deep ReLU Networks
**Authors:** Brian Yarbrough, Jesse Wayment, Jingbo Wang, Philip E. Paré, Shreyas Sundaram
**Link:** https://arxiv.org/abs/2611.21599v1
**Summary:** Hyperlyve is a framework designed to prove the stability of nonlinear dynamical systems controlled by neural networks, specifically those using ReLU activations. It employs a parallel algorithm to efficiently enumerate the hyperplanes formed by these activations and certifies the stability conditions across the resulting polyhedral regions. The key contribution is that Hyperlyve significantly outperforms existing tools, providing stability proofs for complex systems that were previously impossible to verify, while also clarifying the difficulty of the verification problem as co-NP-complete.

### 6. Mitigating Catastrophic Forgetting with Physics-Indexed Specialist Memory: the Evolutionary Neuroplastic Agent
**Authors:** Blas Eugenio Vicco Zarate, Miguel Hernán Vicco
**Link:** https://arxiv.org/abs/2611.21598v1
**Summary:** The paper addresses the challenge of catastrophic forgetting in continual reinforcement learning, where an agent must adapt to new environments while retaining knowledge from previous ones. The authors introduce the Evolutionary Neuroplastic Agent (ENA), which uses an evolutionary approach to create specialized neural networks that can store and retrieve policies based on detected environment changes. The key finding is that ENA showed promising retention of learned behaviors in various tests, outperforming certain variants in consistent performance, although it did not surpass all contemporary methods in overall efficiency or returns.

### 7. Optimal Autoregressive Chain-of-Thought Learning via Bagging
**Authors:** Awni Altabaa, John Lafferty, Omar Montasser
**Link:** https://arxiv.org/abs/2611.21597v1
**Summary:** This paper addresses the challenge of effectively learning an autoregressive next-token generator using chain-of-thought demonstrations. The authors propose a bagging algorithm that combines multiple generators trained on bootstrap samples to enhance CoT consistency. A key contribution is the establishment of optimal sample complexity bounds for this method, demonstrating robust performance irrespective of CoT length and enabling the reduction of the ensemble into a single generator efficiently.

### 8. SADL: On the Demand-Supply Geometry of Representation Collapse
**Authors:** Junhan Sun, Yigui Feng, Mingzhe Liu, Haoyan Xu, Lei Ye, Ziqi Han, Hanru Bai, Yanzhao Zhang, Hao Zhao, Guofeng Zhang
**Link:** https://arxiv.org/abs/2611.21596v1
**Summary:** The paper addresses the issue of representation collapse in Joint-Embedding Predictive Architectures (JEPAs), where initial encoder outputs are overly similar due to shared components in the input data. The authors introduce a method called Supply And Demand Loss (SADL) that constrains the encoder based on the differences required by the projector output, effectively preventing collapse without altering the core training structure. Key results show that SADL significantly reduces representation collapse and improves learning stability and accuracy across multiple tasks and datasets.

### 9. Surrogate-Assisted Compact-Model Extraction for SKY130 CMOS at 77 K
**Authors:** Aaron Wang, Olivia Gzamouranis, Vaibhav Lohia, Hershel Fei Xun Weiner, Olivia Seidel, Richard Cavanaugh, Giuseppe Di Guglielmo, Nhan Tran, Davide Braga
**Link:** https://arxiv.org/abs/2611.21594v1
**Summary:** This paper addresses the need for accurate compact models of SKY130 CMOS transistors for cryogenic applications by developing a surrogate-assisted method to extract these models from measured low-temperature data. The authors utilize a neural network as a surrogate to optimize the fitting of compact-model parameters, achieving improved accuracy over existing models. Their results show that using a specific set of 43 parameters reduces simulation errors significantly compared to traditional methods, particularly for higher bias conditions.

### 10. Beyond Job Titles: Interpreting Early-Career Job Advertisements with Sparse Autoencoders and Semantic Clustering
**Authors:** Yisong Cao, Leah Kim, Brian Wright, Ali Rivera
**Link:** https://arxiv.org/abs/2611.21586v1
**Summary:** The paper addresses the challenge of understanding the distinct nature of technical job roles in a rapidly evolving job market, given that job titles and descriptions are often insufficient. The authors developed a methodology combining deep learning techniques, including sparse autoencoders and transformer representations, to analyze over 36,000 job postings and segment them into meaningful clusters based on their content. Key findings indicate that different roles, such as Data Scientist and Data Analyst, emphasize varying aspects of their responsibilities, revealing nuanced insights into the job landscape that could enhance job description analysis.
