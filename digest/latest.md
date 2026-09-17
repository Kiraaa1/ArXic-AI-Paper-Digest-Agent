---
## 2026-09-17

### 1. Objective vs. Search: Decomposing What Makes a Good Tokeniser
**Authors:** Ahmetcan Yavuz, Clara Meister, Tiago Pimentel
**Link:** https://arxiv.org/abs/2609.19145v1
**Summary:** This paper investigates the effectiveness of different tokenisation algorithms used in language models, specifically focusing on how the optimisation objective (compression versus likelihood) and search method (bottom-up versus top-down) affect performance. The authors introduce two novel tokenisers to isolate these factors and find that the search procedure is the primary influence on efficiency, with bottom-up tokenisers performing better in terms of bits-per-byte. However, when assessing overall language model performance, there is no clear relationship between the design choices of the tokenisers and task performance, providing insights for more effective tokeniser development.

### 2. A Zeroth-Order Paradigm for LLM Preference Alignment
**Authors:** Peter Chen, Xi Chen, Wotao Yin, Tianyi Lin
**Link:** https://arxiv.org/abs/2609.19144v1
**Summary:** The paper addresses the challenge of aligning large language models (LLMs) with human preferences while minimizing computational demands. It introduces a novel approach called Comparison-based Preference Optimization (ComPO), which uses comparison oracles to gather preference information without relying on traditional differentiable loss functions. The key contribution is the demonstration that this zeroth-order method yields better performance than existing direct alignment techniques across several LLMs, effectively reducing issues related to likelihood displacement.

### 3. PANORAMA: Panoptic Grounded Captioning via Mask Proposal Selection
**Authors:** Sara Pieri, Evangelos Kazakos, Shizhe Chen, Josef Sivic, Cordelia Schmid
**Link:** https://arxiv.org/abs/2609.19143v1
**Summary:** The paper addresses the challenge of accurately generating image captions that are both descriptive and precisely tied to specific image regions, a task referred to as panoptic grounded captioning. The authors introduce PANORAMA, a vision-language model that utilizes a selection process from multiple mask proposals, leveraging contextualized phrase representations for improved pixel-level grounding. The results demonstrate that PANORAMA outperforms existing methods, achieving high-quality segmentations and consistent captions, and it provides a new benchmark dataset and evaluation metrics for this task.

### 4. Dreaming the Sound of Contact: Leveraging Video and Audio Generation for Zero-Shot Force-Aware Manipulation and Data Generation
**Authors:** Guanhua Ji, Tianyu Li, Dayoon Suh, Yuqian Zhang, Boyan Zhang, Nadia Figueroa
**Link:** https://arxiv.org/abs/2609.19137v1
**Summary:** This paper addresses the challenge of robots learning to manipulate objects in contact-rich tasks, which require precise force application. The authors enhance conventional video-based trajectory generation by incorporating audio cues from contact sounds to define a desired force profile. Their results show that this approach enables robots to successfully complete tasks that a traditional method, relying solely on kinematic data, would fail to accomplish.

### 5. Exponential Hardness of Off-Policy Evaluation under History-Dependent Logging
**Authors:** Pranaya Jajoo
**Link:** https://arxiv.org/abs/2609.19135v1
**Summary:** This paper addresses the challenge of off-policy evaluation in partially observable Markov decision processes (POMDPs) with history-dependent logging. The authors demonstrate that even when a logged dataset frequently visits all hidden states, it can be exponentially uninformative about a target policy's value due to the logger's reliance on historical data. They construct specific POMDP instances to show that accurately evaluating a policy requires a prohibitively large number of logged episodes, emphasizing the intractability of this problem under certain conditions.

### 6. ScienceIDE: Turning World's Scientific Codebase into Agent Learnable Environments
**Authors:** Hejia Geng, Zesen Huang, Haoyang Li, Wenbin Li, Koutian Wu, Zihan Zhou, Yuanbo Pang, Weihao Liu, Zigong Xu, Zhiping Li, Zongzheng Zhang, Chuanfei Dong, Jiankai Sun, Tianzhe Zheng, Fengyu Xie, Yue Ma, Yueheng Shi, Tong Xie, Zonglin Di, Xianrong Liu, Qucheng Gao, Yimin Liu, Jiaming Pan, Sheng Huang, Xiao-Han Ma, Lanqing Yuan, Zhenlin Zhu, Ziang Liu, Ziyang Xu, Junkai Wang, Kangkai Liang, Jiayi Xian, Zehong Zhao, Liuwei Xu, Jingxu Xie, Peijin Zhang, Qiang Gao, Chengyi Xing, Zhe Zhao, Xi Wang, Yaopeng Xing, Xing Meng, Zhenfei Yin, Yingcheng Wu, Ling Yang
**Link:** https://arxiv.org/abs/2609.19134v1
**Summary:** The paper addresses the challenge of utilizing fragmented scientific codebases for training intelligent agents, an issue referred to as the scientific experience bottleneck. The authors introduce ScienceIDE, a framework that converts complex scientific repositories into programmable environments for agents, enabling them to learn and verify scientific tasks effectively. Their results demonstrate that models trained within these environments show improved performance in code repair and general reasoning tasks, highlighting the beneficial transfer of knowledge from scientific applications to broader AI capabilities.

### 7. Cognitive Extensions for Dual-Process Language Agents: Memory and Self-Reflection in Interactive Environments
**Authors:** João Meneses dos Santos, Arlindo L. Oliveira
**Link:** https://arxiv.org/abs/2609.19128v1
**Summary:** The paper addresses the limitations of language agents in interactive environments, where they struggle with tracking states and recovering from errors. The authors enhance an existing dual-process agent, SwiftSage, by adding two cognitive extensions: an Adaptive Memory Module and a Self-Reflection Module, which help with memory storage and corrective actions. The experiments show that the complete system outperforms all other configurations, highlighting the importance of execution-time control in improving agent performance.

### 8. Affora: A Design System for Agent-Friendly Interfaces
**Authors:** Jin Gao
**Link:** https://arxiv.org/abs/2609.19125v1
**Summary:** The paper introduces Affora, a design system aimed at improving user interfaces for both humans and software agents by making actions and task states clearer for machines. Through controlled studies, the authors demonstrate how to maintain visual appeal and familiar workflows while enhancing agent interpretability. The key finding is that Affora can significantly improve agent performance and reduce interaction costs by bridging the gap between user and agent experiences with a shared interface.

### 9. Flag Game: A Toy Model for Mechanistic Swarm Interpretability
**Authors:** Elizabeth Pavlova, Hidenori Tanaka
**Link:** https://arxiv.org/abs/2609.19124v1
**Summary:** The paper addresses the challenge of understanding how AI agents form and share beliefs, which is crucial for ensuring their safe and aligned behavior. The authors introduce the Flag Game, a simple model where agents observe private information and communicate with each other to shape collective beliefs about a hidden flag. They discover that as the population size increases, beliefs can either collapse or polarize, influencing performance outcomes, and they propose methods for analyzing these dynamics, contributing to the field of swarm interpretability.

### 10. Playing log(N)-Questions over Wikipedia Abstracts: Communication Efficiency Between Paired Frontier Models
**Authors:** Peter Potash
**Link:** https://arxiv.org/abs/2609.19113v1
**Summary:** The paper investigates the efficiency of communication between paired language models in a game where one model asks questions to identify a target document from a set of Wikipedia lead paragraphs, using a logarithmic number of questions. The study evaluates six models and finds that while the leading models perform closely, their win rates decrease with increasing document set size, with significant errors occurring mostly in answering with “No.” A notable finding is that models that incorporate strategies like partitioning on document titles achieve better performance, suggesting specific question strategies impact communication effectiveness.
