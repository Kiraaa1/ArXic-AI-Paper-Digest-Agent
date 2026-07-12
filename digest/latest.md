---
## 2026-07-12

### 1. Do You Need a Frontier Model as a Citation Verifier? Benchmarking Rubric LLMs for Deep-Research Source Attribution
**Authors:** Ethan Leung, Elias Lumer, Corey Feld, Austin Huber, Vamse Kumar Subbiah, Kevin Paul
**Link:** https://arxiv.org/abs/2607.08700v1
**Summary:** The paper addresses the challenge of assessing citation quality in deep-research systems, focusing on how well different large language models (LLMs) can evaluate citations based on relevance and factual support. The authors benchmark eight LLM judges from different families against human-reviewed gold standards, showing that less expensive models can perform competitively with more advanced ones in terms of source relevance, while all models exhibit similar performance in factual support. The key contribution highlights the importance of calibrating these models before they can reliably be used as reward signals in reinforcement learning setups, suggesting that one does not need the most costly models for effective citation verification.

### 2. ProjAgent: Procedural Similarity Retrieval for Repository-Level Code Generation
**Authors:** QiHong Chen, Aaron Imani, Iftekhar Ahmed
**Link:** https://arxiv.org/abs/2607.08691v1
**Summary:** ProjAgent addresses the challenge of generating code for functions in software repositories that often have complex interdependencies and project-specific rules. The system introduces the concept of procedural similarity, allowing it to retrieve functions that may differ in naming but share similar logic by breaking down target functions into intermediate steps. As a result, ProjAgent significantly improves code generation performance, achieving a Pass@1 rate of 41.14%, surpassing existing methods.

### 3. A Practical Investigation of Training-free Relaxed Speculative Decoding
**Authors:** Guoxuan Xia, Luka Ribar, Paul Balanca
**Link:** https://arxiv.org/abs/2607.08690v1
**Summary:** The paper investigates relaxed speculative decoding methods that aim to speed up token sampling in autoregressive language models by using a faster auxiliary model to propose tokens. By analyzing various training-free approaches, the authors find that while relaxed methods can provide efficiency gains, they often require substantial capability assessments and depend on having a good language model for drafting, which may not be suitable for lightweight applications.

### 4. SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized Energy Markets
**Authors:** Shilin Ou, Yifan Xu, Luyao Zhang
**Link:** https://arxiv.org/abs/2607.08681v1
**Summary:** The paper addresses the need for evaluating trustworthy autonomous agents in decentralized energy markets, where they can potentially exploit data and destabilize governance. It introduces SolarChain-Eval, a benchmark that uses a physics-constrained model to assess agent performance across various metrics like market utility and safety, complemented by a Planner/Auditor that monitors and revises high-risk actions. Key findings highlight a trade-off between market utility and safety, with reinforcement learning agents showing improved utility but still exhibiting unsafe behaviors, underscoring the importance of incorporating physical constraints and transparent auditing for reliable evaluations.

### 5. Resample or Reroute? Budget-Aware Test-Time Model Selection for Large Language Models
**Authors:** Teng-Ruei Chen
**Link:** https://arxiv.org/abs/2607.08665v1
**Summary:** This paper addresses the challenge of optimizing budget allocation during test-time model selection for large language models (LLMs), balancing the costs of rerouting to alternative models versus resampling from the committed model. The authors propose a novel online policy that dynamically allocates budget based on the estimated correctness of each approach. Their experiments demonstrate that this budget-aware resample-or-reroute strategy outperforms existing methods in terms of cost and quality, particularly in diverse benchmark scenarios.

### 6. WebSwarm: Recursive Multi-Agent Orchestration for Deep-and-Wide Web Search
**Authors:** Xiaoshuai Song, Liancheng Zhang, Kangzhi Zhao, Yutao Zhu, Zhongyuan Wang, Guanting Dong, Jinghan Yang, Han Li, Kun Gai, Ji-Rong Wen, Zhicheng Dou
**Link:** https://arxiv.org/abs/2607.08662v1
**Summary:** The paper addresses the limitations of existing multi-agent systems in handling complex web searches that require both depth and extensive coverage. It introduces WebSwarm, a framework that allows multiple search agents to recursively delegate tasks and collaborate dynamically during the search process. The key result is that WebSwarm consistently outperforms traditional single-agent and multi-agent approaches in various complex search scenarios, demonstrating improved effectiveness in deep-and-wide research tasks.

### 7. EdgeRefine: Privacy-Utility Balance for Graphs via Jaccard Sampling under Edge Differential Privacy
**Authors:** Wenxiu Ding, Muzhi Liu, Zheng Yan, Mingjun Wang, Yifan Zhao, Qiao Liu
**Link:** https://arxiv.org/abs/2607.08659v1
**Summary:** The paper addresses the challenge of maintaining privacy while using Graph Neural Networks (GNNs), as traditional methods often compromise performance due to excessive noise. The authors introduce EdgeRefine, a framework that optimizes the privacy-utility balance by adaptively refining edges based on Jaccard similarity to selectively apply noise. Key results indicate that EdgeRefine significantly enhances node classification accuracy compared to existing methods, with improvements of up to 19.7%, while still preserving robustness against potential privacy breaches.

### 8. Formal Mechanisms for Market Stability in Self-Interested Agent Societies: A Marketplace Simulation Study
**Authors:** Eugene Ng Yi Sheng, Bingquan Shen
**Link:** https://arxiv.org/abs/2607.08652v1
**Summary:** The paper addresses the issue of market instability caused by self-interested agents in trading environments, which often leads to cooperation breakdown. Through a multi-agent simulation involving 18 trading agents, the authors compare various mechanisms designed to enhance market stability and identify "Mediation" as the most effective approach, demonstrating that it maintains positive outcomes for honest agents even under targeted attacks. The study defines "adversarial robustness" for these mechanisms, highlighting that Mediation can withstand pressure without collapsing the market.

### 9. Secure Decentralized Federated Learning via Gossip and Virtual Voting
**Authors:** Amirhossein Taherpour, Xiaodong Wang
**Link:** https://arxiv.org/abs/2607.08651v1
**Summary:** This paper addresses the challenges of achieving reliable and secure decentralized federated learning (DFL) without a central server, particularly in the presence of faulty participants. The authors introduce gspDAG-FL, a novel framework where nodes exchange model updates through peer-to-peer gossip while ensuring consensus through a compact directed acyclic graph and virtual voting. The results demonstrate that gspDAG-FL maintains high learning quality with reduced coordination costs and enhanced resilience against adversarial behaviors compared to traditional ledger-assisted approaches.

### 10. Multi-Modal, Multi-Environment Machine Teaching for Robust Reward Learning
**Authors:** Ali Larian, Qian Lin, Chang Zong Wu, Daniel S. Brown
**Link:** https://arxiv.org/abs/2607.08647v1
**Summary:** The paper addresses the challenge of teaching autonomous agents to learn reward functions that remain effective across different environments, rather than being tailored to just one specific context. The authors propose a hierarchical machine teaching algorithm that intelligently selects diverse environments and gathers strategic feedback to improve the learning process. Their approach outperforms traditional methods by yielding better generalization and lower regret when applied to new environments, highlighting the significance of using multiple teaching modalities and contexts.
