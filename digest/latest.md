---
## 2026-09-20

### 1. OPTED: On-Policy Fine-Tuning for End-to-End Driving using a Render-Free Teacher
**Authors:** Damiano Da Col, Maximilian Igl, Peter Karkus, Kashyap Chitta, Boris Ivanovic, Marco Pavone, Konrad Schindler, Christos Sakaridis
**Link:** https://arxiv.org/abs/2609.20756v1
**Summary:** The paper addresses the challenge of improving end-to-end autonomous driving policies, which can struggle with safety when deployed in real-world conditions due to errors compounding outside their training data. The authors introduce OPTED, a method that fine-tunes pre-trained driving models using a reinforcement learning teacher that operates on simplified input data, reducing the need for expensive simulation runs. The key result is a significant performance improvement in two camera-based driving models, achieving higher driving scores with far fewer simulator interactions than traditional reinforcement learning approaches.

### 2. RAFT: A Stateful Retrieval-Augmented Framework for Troubleshooting Agents
**Authors:** Mingxuan Zhang, Xiaowen Wang, Anupma Sharan, Zhengyi Chen, Chenyu Diana Zhang, Shanshan Yang, Chittibabu Pacharu
**Link:** https://arxiv.org/abs/2609.20754v1
**Summary:** The paper presents RAFT, a novel framework designed to improve troubleshooting agents in enterprise customer support by effectively retrieving relevant guidance from complex historical cases. Unlike traditional methods that treat cases as static documents, RAFT uses a stateful retrieval system that abstracts cases into timelines, allowing for better matches based on the specific stage of the troubleshooting process. The results show that RAFT significantly outperforms existing retrieval methods in retrieving relevant case histories, demonstrating its potential to enhance troubleshooting efficiency.

### 3. Large Language Models as Falsifiers for Cyber-Physical Systems
**Authors:** Ali ArjomandBigdeli, Jiawei Zhou, Stanley Bak
**Link:** https://arxiv.org/abs/2609.20752v1
**Summary:** The paper addresses the challenge of falsifying specifications in cyber-physical systems (CPS) by using large language models (LLMs) to efficiently find counterexamples that violate these specifications. The proposed method, LLM-Falsifier, enhances traditional robustness optimization techniques by leveraging the LLM's ability to process natural language and semantic information related to the system, leading to more effective and sample-efficient searches. The results show that LLM-Falsifier significantly outperforms existing falsification tools on standard benchmarks, requiring fewer simulations to identify counterexamples.

### 4. dQwen3.5: Hybrid-Attention Diffusion Language Models
**Authors:** Anton Xue, Litu Rout, Aditya Akella, Adam Klivans, Sujay Sanghavi, Sanjay Shakkottai
**Link:** https://arxiv.org/abs/2609.20751v1
**Summary:** The paper addresses the challenge of adapting pretrained autoregressive models into diffusion language models, specifically with hybrid architectures that combine attention and RNN layers. The authors adapted the Qwen3.5 model across multiple scales and discovered that these hybrid models can effectively serve as efficient bases for adaptation, achieving training losses faster than traditional full-attention models. A key finding is that the dQwen3.5 models exhibit similar performance to full-attention models while benefiting from faster parallel decoding.

### 5. MILER: Semantic Mid-Level Representation for Sim-to-Real Reinforcement Learning in Unstructured Autonomous Driving
**Authors:** Thomas Steinecker, Denis Trescher, Alexander Bienemann, Thorsten Luettel, Mirko Maehlisch
**Link:** https://arxiv.org/abs/2609.20747v1
**Summary:** The paper addresses the challenge of transferring reinforcement learning policies for autonomous driving from simulation to real-world unstructured environments, where such applications have been limited. It introduces MILER, a novel framework that uses a semantic mid-level representation to train driving policies offline and employs a trajectory-alignment strategy for zero-shot transfer during real-world deployment. The framework was successfully tested over 17.3 km, navigating a complex 3.0 km track with various obstacles, demonstrating effective control without human intervention.

### 6. Video DeltaNet: A Video-Native Hybrid Attention for Livestream Video Generation
**Authors:** Haocheng Xi, Yiming Xie, Hexu Zhao, Yiwen Zhang, Michael Liu, Thomas Creavin, Kurt Keutzer, Xiuyu Li, Zhaoyang Lv, Chenfeng Xu, Haiwen Feng
**Link:** https://arxiv.org/abs/2609.20744v1
**Summary:** The paper addresses the computational inefficiencies of video diffusion models, particularly the bottleneck caused by traditional attention mechanisms during long video generation tasks. To resolve this, the authors introduce Video DeltaNet (VDN), which combines local Softmax attention with a novel linear attention method (Video Delta Attention) that updates memory efficiently while maintaining fine-grained interactions. The key result demonstrates a significant speedup in processing time—14.5 times faster—when generating 768p videos, making the approach highly effective for real-time applications.

### 7. On-Demand Attention: Language Models Know When to Recall
**Authors:** Haibo Feng, Ruiqi Liang, Hanyang Peng, Shiqi Yu
**Link:** https://arxiv.org/abs/2609.20734v1
**Summary:** The paper addresses the inefficiencies in long-context inference in language models, where full attention requires reading the entire historical context at every step, often unnecessarily. The authors propose a novel method called On-Demand Attention (ODA), which uses a lightweight recall mechanism to selectively access global context only when needed, helping to speed up the decoding process significantly. Experiments demonstrate that ODA maintains performance while substantially reducing the number of global reads, improving the efficiency of pretrained models in handling long contexts.

### 8. Q&A on Any Spreadsheet Requires Interpreting Its Grid Structure
**Authors:** Zofia Smoleń
**Link:** https://arxiv.org/abs/2609.20732v1
**Summary:** The paper addresses the challenge of improving how large language models (LLMs) interpret data from spreadsheets for question and answer tasks. It introduces a framework that annotates cells based on their roles to create interpretable chunks of spreadsheet data, enhancing context for answer generation. However, the authors note that existing classification models cannot fully capture the complexity of spreadsheet structures, suggesting a need for methods that transform 2D spreadsheets into simpler 1D text for better processing by LLMs.

### 9. Deep Noir: Autonomous Steering Discovery via Architectural Chronometry in Transformer Models
**Authors:** Frank E. Bobe, Gregory D. Vetaw, Darshan W. Bryner, Matthew G. Cook, Jose L. Salas-Vernis
**Link:** https://arxiv.org/abs/2609.20722v1
**Summary:** The paper presents Deep Noir, a framework that automates the process of tuning large language models (LLMs) for optimal performance during inference by discovering where and how to modify their behavior, a task that was previously done manually. By employing techniques like Logit Lens convergence and causal head-level attribution, Deep Noir significantly improves model performance on tasks such as spam detection and sentiment analysis, achieving impressive gains across various model sizes and architectures. A notable contribution is the framework's ability to identify intervention points that can be applied broadly, while also revealing vulnerabilities associated with steering that could affect the security of deployed systems.

### 10. Don't Mask the Environment: Observation Supervision Changes How Agents Explore Under RL
**Authors:** Juzheng Zhang, Disha Makhija, Manoj Ghuhan Arivazhagan, Vinayshekhar Bannihatti Kumar, Rashmi Gangadharaiah
**Link:** https://arxiv.org/abs/2609.20715v1
**Summary:** The paper addresses the issue of how standard supervised fine-tuning (SFT) could limit reinforcement learning (RL) by only focusing on action tokens, neglecting the predictive power of environmental observations. The authors introduce a method called ActObs, which supervises both action and observation tokens during training, enhancing the agent's ability to model the consequences of its actions. The key contribution is that ActObs leads to better exploration and higher task performance in RL, resulting in improved outcomes compared to traditional action-only training methods.
