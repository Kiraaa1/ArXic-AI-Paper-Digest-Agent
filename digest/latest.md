---
## 2026-06-12

### 1. EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments
**Authors:** Jundong Xu, Qingchuan Li, Jiaying Wu, Yihuai Lan, Shuyue Stella Li, Huichi Zhou, Bowen Jiang, Lei Wang, Jun Wang, Anh Tuan Luu, Caiming Xiong, Hae Won Park, Bryan Hooi, Zhiyuan Hu
**Link:** https://arxiv.org/abs/2606.13681v1
**Summary:** The paper addresses the challenge of adapting large language model (LLM) agents to dynamic environments, where conditions and tasks change over time. The authors introduce EvoArena, a benchmark that simulates these changes, and propose EvoMem, a memory system that tracks how an agent's knowledge evolves. Key findings show that EvoMem significantly boosts performance on this benchmark and standard tests, indicating that effective memory management is crucial for agents to succeed in dynamic settings.

### 2. Learning to Reason by Analogy via Retrieval-Augmented Reinforcement Fine-Tuning
**Authors:** Zilin Xiao, Qi Ma, Chun-cheng Jason Chen, Xintao Chen, Avinash Atreya, Hanjie Chen, Vicente Ordonez
**Link:** https://arxiv.org/abs/2606.13680v1
**Summary:** The paper addresses the challenge of enabling language models to effectively reason by analogy, which is often hindered by traditional retrieval methods that rely on semantic similarity. The authors introduce a new framework called Retrieval-Augmented Reinforcement Fine-Tuning (RA-RFT) that teaches models to retrieve contexts based on their reasoning potential, enhancing their ability to solve complex problems. The key finding is that RA-RFT significantly improves performance on mathematical reasoning tasks compared to previous methods, demonstrating a new avenue for model enhancement through reasoning-aware retrieval.

### 3. Mana: Dexterous Manipulation of Articulated Tools
**Authors:** Zhao-Heng Yin, Guanya Shi, Pieter Abbeel, C. Karen Liu
**Link:** https://arxiv.org/abs/2606.13677v1
**Summary:** The paper addresses the challenge of manipulating articulated tools in robotics, which is complex due to their internal joint movements and interactions with objects. The authors introduce Mana, a framework that treats this manipulation as an animation problem, using a pipeline that combines keyframe generation, motion planning, and reinforcement learning to create manipulation trajectories. Mana successfully demonstrates the ability to transfer learned manipulation skills from simulation to the real world for various articulated tools without any prior adaptation, showcasing its scalability and effectiveness.

### 4. SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning
**Authors:** Seokju Cho, Ryo Hachiuma, Abhishek Badki, Hang Su, Byung-Kwan Lee, Chan Hee Song, Sifei Liu, Subhashree Radhakrishnan, Seungryong Kim, Yu-Chiang Frank Wang, Min-Hung Chen
**Link:** https://arxiv.org/abs/2606.13673v1
**Summary:** The paper presents SpatialClaw, a novel framework for improving spatial reasoning in vision-language models (VLMs) by using a flexible code-based action interface. This approach allows agents to dynamically compose and execute spatial analyses based on real-time observations rather than pre-planned strategies. SpatialClaw achieves a significant improvement in performance, with an average accuracy of 59.9% across various benchmarks, surpassing previous methods by over 11 percentage points.

### 5. Understanding Truncated Positional Encodings for Graph Neural Networks
**Authors:** James Flora, Mitchell Black, Weng-Keen Wong, Amir Nayyeri
**Link:** https://arxiv.org/abs/2606.13671v1
**Summary:** The paper investigates the effects of using truncated positional encodings in Graph Neural Networks, which are commonly employed to enhance their performance. The authors demonstrate that these truncated variants differ in expressive power, showing that truncated spectral positional encodings do not surpass the capabilities of the 1-WL test. Their experiments reveal that using a combination of truncated positional encodings outperforms any single type on real-world datasets.

### 6. Automated reproducibility assessments in the social and behavioral sciences using large language models
**Authors:** Tobias Holtdirk, Pietro Marcolongo, Anna Steinberg Schulten, Felix Henninger, Stefan Rose, Sarah Ball, Bolei Ma, Frauke Kreuter, Markus Weinmann, Stefan Feuerriegel
**Link:** https://arxiv.org/abs/2606.13670v1
**Summary:** This paper addresses the challenge of evaluating reproducibility in social and behavioral science research, which is often resource-intensive. The authors demonstrate that large language models (LLMs) can automate the process by reanalyzing published studies, and they found that LLMs successfully recovered original effect sizes in 41% of cases and aligned with original conclusions in 96% of instances. This approach offers a scalable solution for reproducibility assessments, enhancing the reliability of empirical research in these fields.

### 7. Agents-K1: Towards Agent-native Knowledge Orchestration
**Authors:** Zongsheng Cao, Bihao Zhan, Jinxin Shi, Jiong Wang, Fangchen Yu, Zhijie Zhong, Zijie Guo, Tianshuo Peng, Zhuo Liu, Yi Xie, Xiang Zhuang, Yue Fan, Runmin Ma, Shiyang Feng, Xiangchao Yan, Anran Liu, Peng Ye, Wenlong Zhang, Shufei Zhang, Chunfeng Song, Fenghua Ling, Jie Zhou, Liang He, Bo Zhang, Lei Bai
**Link:** https://arxiv.org/abs/2606.13669v1
**Summary:** The paper presents Agents-K1, a novel pipeline designed to improve the orchestration of scientific knowledge by transforming raw academic documents into structured knowledge graphs. This approach integrates a multimodal parser for comprehensive document analysis, an advanced information-extraction model, and a versatile agent interface for enhanced data retrieval. The key contribution is the creation of Scholar-KG, a large-scale knowledge graph derived from processing 2.46 million scientific papers, which demonstrates significant advancements in extracting scientific information and supporting complex reasoning across multiple documents.

### 8. Influcoder: Distilling Decoders' Gradient Influence Rankings into an Encoder for Data Attribution
**Authors:** Dimitri Kachler, Damien Sileo, Pascal Denis
**Link:** https://arxiv.org/abs/2606.13668v1
**Summary:** The paper proposes Influcoder, a novel method designed to enhance the efficiency of Data Attribution for large language models by quickly identifying which training samples influence model outputs, such as toxic behavior. This approach distills gradient influence rankings from decoders into a compact encoder, enabling faster and more storage-efficient analysis suitable for large datasets. The key contribution is a more practical implementation of influence functions that addresses the speed and storage limitations of existing methods.

### 9. HyperTool: Beyond Step-Wise Tool Calls for Tool-Augmented Agents
**Authors:** Yaxin Du, Yifan Zhou, Yujie Ge, Jiajun Wang, Xianghe Pang, Shuo Tang, Tuney Zheng, Bryan Dai, Jian Yang, Siheng Chen
**Link:** https://arxiv.org/abs/2606.13663v1
**Summary:** The paper presents HyperTool, a new tool interface that addresses the inefficiencies of current tool-augmented language model agents, which rely on step-wise calls that complicate the reasoning process. By allowing models to invoke a single code block that consolidates multiple tool actions and data manipulations, HyperTool simplifies execution and enhances performance. The results show significant improvements in task accuracy on benchmark tests, with average accuracy for Qwen3-32B rising from 15.69% to 35.29% and for Qwen3-8B from 9.93% to 33.33%.

### 10. EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery
**Authors:** Amy Xin, Jiening Siow, Junjie Wang, Zijun Yao, Fanjin Zhang, Jian Song, Lei Hou, Juanzi Li
**Link:** https://arxiv.org/abs/2606.13662v1
**Summary:** This paper addresses the challenge of enhancing autonomous scientific discovery by focusing on the design of agent environments rather than just workflows. The authors introduce EurekAgent, an agent system that optimizes environments to encourage productive behaviors while minimizing negative ones, leading to significant improvements in various scientific tasks. Notably, EurekAgent achieved state-of-the-art results in circle packing with minimal costs, highlighting the importance of environment engineering in developing effective research agents.
