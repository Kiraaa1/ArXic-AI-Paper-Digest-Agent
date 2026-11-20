---
## 2026-11-20

### 1. RL Post-Training in Diffusion Transformers Is Activation Steering
**Authors:** Tuna Han Salih Meral, Kaan Oktay, Alec Helbling, Atakan Kara, Duen Horng Chau, Pinar Yanardag
**Link:** https://arxiv.org/abs/2611.26627v1
**Summary:** The paper tackles the problem of enhancing the performance of diffusion transformers in tasks like text rendering and object composition using reinforcement learning (RL) post-training. The authors propose a simpler approach utilizing fixed steering vectors, which significantly reduce the number of parameters compared to conventional RL-tuned methods. Remarkably, these fixed vectors recover most of the performance improvements achieved through RL post-training, demonstrating that a constant shift can effectively guide the already-trained model towards better outputs without needing complex, input-dependent modifications.

### 2. PlayCraft: Designing Engaging Games from Agent Play Experience
**Authors:** Weihao Cheng
**Link:** https://arxiv.org/abs/2611.26624v1
**Summary:** The paper addresses the challenge of creating engaging games by focusing on player mastery, which requires extensive human feedback and tuning. It introduces PlayCraft, an automated framework that uses a vision-based AI agent to play and analyze games, revising them for better player experience based on its play experience. The results show that PlayCraft significantly enhances learning outcomes in games, leading to larger gains in player performance and a more effective progression of skills compared to initial game designs.

### 3. TideCache: Efficient Hybrid LLM Serving with Transparent Cache Management and Layer-Wise Streaming
**Authors:** Jinbin Luo, Xiaozhe Yao, Shang Yang, Zhijian Liu, Song Han, Qinghao Hu
**Link:** https://arxiv.org/abs/2611.26619v1
**Summary:** TideCache addresses the challenge of efficiently managing GPU memory for hybrid language model architectures, which have varying cache needs based on context. The system introduces a three-part solution that optimizes cache allocation and memory management, allowing for better performance by overlapping data transfer with computation. As a result, TideCache significantly increases the number of completed tasks and reduces latency compared to existing systems, showcasing its efficiency in handling language model serving on superchips.

### 4. One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning
**Authors:** Yuxin Jiang, Wenqiang Sun, Jiaqi Li, Yuchao Gu, Lvmin Zhang, Ivor Tsang, Mike Zheng Shou
**Link:** https://arxiv.org/abs/2611.26617v1
**Summary:** The paper addresses the challenge of learning actions in videos without explicit supervision by leveraging a pretrained video generation model. The authors propose a method called O²LaF, which uses a single video generator to support two dynamic learning tasks: understanding how actions influence changes in videos and generating future video frames based on those actions. The key contribution is that O²LaF achieves state-of-the-art performance in few-shot action learning and enables effective transfer of learned actions across different contexts, demonstrating the potential of repurposing pretrained models for this purpose.

### 5. AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control
**Authors:** Yiyang Du, Yuxuan Kuang, Qitao Zhao, Yixuan Wang, Zhanqiu Guo, Yi Xu, Xin Li, Wenbin He, Liu Ren, Chenyan Xiong
**Link:** https://arxiv.org/abs/2611.26613v1
**Summary:** The paper addresses the challenge of evaluating and understanding how advanced multimodal language agents like GPT-6 Astra perform in direct robot control tasks, particularly when existing benchmarks only provide high-level success rates. To tackle this, the authors developed AgentRoboCritic, which combines a policy agent that articulates its intentions with a critic that assesses the outcomes of actions against these intentions. The key contributions include a detailed analysis of agent performance in 12 manipulation benchmarks, identification of specific limitations, and the creation of a new dataset that enhances action-level evaluation accuracy significantly.

### 6. Bio-PM-Guided Synthetic IMU Generation
**Authors:** Deepali Singh, Deepesh Parpani, Aviral Gupta
**Link:** https://arxiv.org/abs/2611.26607v1
**Summary:** This paper addresses the challenge of collecting and labeling inertial measurement unit (IMU) data for human activity recognition, particularly the issue of models failing to generalize across different subjects. The authors propose generating synthetic IMU data using token embeddings from a pretrained biosignal encoder, Bio-PM, employing both an autoregressive transformer and a diffusion decoder. Their approach improves classification performance on real data, achieving a significant increase in accuracy for difficult activity classes, thus demonstrating that the synthetic data generated is both realistic and beneficial for training classifiers.

### 7. Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth
**Authors:** Peiyun Hu, Marko Mihajlovic, Lyndon Duong, Lahav Lipson, Wei Dong, Amaël Delaunoy, Stephan R. Richter, Vladlen Koltun
**Link:** https://arxiv.org/abs/2611.26603v1
**Summary:** The paper presents Depth Pro 2, a novel method for estimating dense metric depth from images and videos that achieves both sharpness and temporal consistency without sacrificing accuracy. By training a single scalable network that processes both static images and video frames at full resolution, Depth Pro 2 overcomes the traditional trade-offs seen in earlier monocular depth estimation methods. The approach outperforms prior techniques, establishing new benchmarks for depth map quality and efficiency, and the authors have made the models and code publicly available.

### 8. SoK: Assessing the Evolution of LLM Capability in Software Vulnerability Research
**Authors:** Amine Lbath, Manan Suri, Aurelien Delaitre, Vadim Okun, Massih-Reza Amini, Dinesh Manocha
**Link:** https://arxiv.org/abs/2611.26601v1
**Summary:** This paper addresses the growing role of large language models (LLMs) in identifying and fixing software vulnerabilities by establishing a framework to assess their capabilities based on autonomy levels. The authors systematically review existing evidence on LLM performance in vulnerability research and find that these models have been able to discover, validate, and patch vulnerabilities without human intervention, particularly noted in a significant increase in disclosed critical vulnerabilities over the past decade. Ultimately, while LLMs are enhancing vulnerability detection, the response times from report to fix have not significantly changed.

### 9. Active Feature Acquisition by Distilling an Oracle Teacher
**Authors:** Yang Meng, Zixin Ding, Robert L. Grossman, Yuxin Chen
**Link:** https://arxiv.org/abs/2611.26598v1
**Summary:** The paper addresses the problem of Active Feature Acquisition (AFA), which involves selecting which features to gather from data under budget constraints, as acquiring features can be expensive or time-consuming. The authors propose a method called OracleImitator, which explicitly constructs a teacher that ranks features based on their impact on prediction accuracy, and distills this ranking into a practical policy for feature acquisition. The key finding is that OracleImitator outperforms existing AFA approaches, achieving significant improvements in accuracy while reducing acquisition costs, demonstrating the effectiveness of using an explicit ranking strategy.

### 10. PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation
**Authors:** Kai Lu, Chenyang Ma, Ioannis Havoutis
**Link:** https://arxiv.org/abs/2611.26596v1
**Summary:** The paper addresses the challenge of enabling robotic systems to perform complex, long-horizon loco-manipulation tasks that require precise timing and skill execution. The authors introduce the Physically Grounded Execution (PGX) framework, which breaks down these tasks into manageable components using a predicate-based state machine, focused action execution, and spatial consistency techniques. Their experiments demonstrate that PGX improves the ability of a humanoid robot to progress through task stages and achieve higher success rates in both simulated and real-world scenarios.
