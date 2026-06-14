---
## 2026-06-14

### 1. Generative Modeling of Bach-Style Symbolic Music: A Comparative Study of Autoregressive, Latent-Variable, and Adversarial Approaches
**Authors:** Kyuil Lee, Dezhi Yu, Yongkang Huang
**Link:** https://arxiv.org/abs/2606.13626v1
**Summary:** This paper investigates the generative modeling of Bach-style piano music by comparing three different approaches: autoregressive models, latent-variable models, and generative adversarial networks. The key finding is that autoregressive LSTMs with attention generate the most coherent music, while vector-quantized VAEs improve output structure and mitigate issues found in traditional VAEs. In contrast, the adversarial models struggle with training and generalization to Bach's style.

### 2. Beyond Uniform Tokens: Adaptive Compression for Time Series Language Models
**Authors:** Jialin Gan, Xin Qiu, Guangzhe Chen, Xue Wang
**Link:** https://arxiv.org/abs/2606.13624v1
**Summary:** The paper addresses the inefficiency of processing time series data and prompts with the same uniform token approach in large language models. The authors propose a new method that adapts token usage based on the varying importance of information within time series data, allowing for a more efficient representation by compressing less critical tokens and focusing on significant ones. This adaptive compression leads to significant speed improvements and enhanced performance in various time series tasks, achieving up to 7.68 times faster inference and better results in 78% of cases tested.

### 3. Beyond Runtime Enforcement: Shield Synthesis as Defensibility Analysis for Adversarial Networks
**Authors:** Achraf Hsain, Sultan Almuhammadi
**Link:** https://arxiv.org/abs/2606.13621v1
**Summary:** This paper rethinks shielded reinforcement learning, proposing that instead of just acting as a runtime safety mechanism, the automata-theoretic methods used can serve as a design-time analysis tool for assessing the defensibility of networks against adversarial attacks. By framing network safety as a constrained two-player game, the authors derive a defensibility verdict that evaluates if a given network configuration can effectively withstand attacks, along with broader metrics on its operational safety and adaptability. The key contribution is that this approach provides deeper architectural insights into the defensibility of network systems, demonstrating that formal safety and actual operational effectiveness can differ significantly based on system design.

### 4. Majority-of-Three is Optimal
**Authors:** Divit Rawal, Nikita Zhivotovskiy
**Link:** https://arxiv.org/abs/2606.13614v1
**Summary:** The paper addresses the problem of determining the optimal voting scheme for combining classifiers in the PAC learning framework. The authors provide a concise proof that using a majority vote among three independent consistent classifiers is the most effective approach. This result simplifies previous analyses and algorithms related to voting mechanisms in machine learning.

### 5. One Polluted Page Is Enough: Evaluating Web Content Pollution in Generative Recommenders
**Authors:** Minghao Luo, Liang Chen
**Link:** https://arxiv.org/abs/2606.13610v1
**Summary:** This paper addresses the issue of generative recommenders unintentionally promoting fake products due to polluted web content, such as misleading reviews and promotional pages. The authors introduce a benchmark called FORGE, which simulates web-content pollution by replacing real products in search results with fake ones, revealing that all evaluated language models can easily be misled, with promotion rates reaching as high as 73.8%. The study also investigates potential defenses, revealing that some approaches can inadvertently increase vulnerability rather than mitigate it.

### 6. AgentBeats: Agentifying Agent Assessment for Openness, Standardization, and Reproducibility
**Authors:** Xiaoyuan Liu, Jianhong Tu, Yuqi Chen, Siyuan Xie, Sihan Ren, Tianneng Shi, Gal Gantar, Evan Sandoval, Donghyun Lee, Daniel Miao, Peter J. Gilbert, Nick Hynes, Mauro Staver, Warren He, David Marn, Andrew Low, Xi Zhang, Elron Bandel, Michal Shmueli-Scheuer, Siva Reddy, Alexandre Drouin, Alexandre Lacoste, Ramayya Krishnan, Elham Tabassi, Yu Su, Victor Barres, Chenguang Wang, Wenbo Guo, Dawn Song
**Link:** https://arxiv.org/abs/2606.13608v1
**Summary:** The paper addresses the fragmented evaluation of agent systems by proposing a unified framework for standardized assessment called Agentified Agent Assessment (AAA), which allows for fair comparisons across diverse agent designs through standardized protocols. To implement this, the authors introduce AgentBeats, which was tested in an open competition and a case study, demonstrating its effectiveness in facilitating reproducible and interoperable evaluations while preserving accuracy and yielding valuable insights into agent design. Overall, AAA and AgentBeats provide a solution for improving openness, standardization, and reproducibility in agent assessment.

### 7. Reasoning as Pattern Matching: Shared Mechanisms in Human and LLM Everyday Reasoning
**Authors:** Zach Studdiford, Gary Lupyan
**Link:** https://arxiv.org/abs/2606.13607v1
**Summary:** This paper examines the similarities between human reasoning and the reasoning of large language models (LLMs), particularly in everyday situations where both can make similar errors. The researchers evaluated human participants alongside 25 LLMs and found that both demonstrate patterns of reasoning errors linked to pattern-matching rather than relying on abstract world models. The study highlights that certain attention mechanisms in LLMs contribute to these errors, suggesting a common pattern-matching strategy in both humans and models when making causal inferences.

### 8. Distribution-Agnostic Robust Trajectory Optimization via Chance-Constrained Reinforcement Learning
**Authors:** Yashdeep Chaudhary, Roberto Armellin, Harry Holt, Marco Sagliano
**Link:** https://arxiv.org/abs/2606.13605v1
**Summary:** The paper addresses the challenge of robust trajectory optimization in uncertain environments, specifically for spacecraft missions. It introduces a framework that combines deterministic trajectory planning with chance-constrained reinforcement learning to improve robustness against various uncertainties. The results demonstrate that this approach effectively maintains fuel efficiency and probabilistic feasibility across different trajectory design scenarios, showcasing its versatility for diverse spacecraft applications without needing significant redesign.

### 9. Multi-Agent Reinforcement Learning from Delayed Marketplace Feedback for Objective-Weight Adaptation in Three-Sided Dispatch
**Authors:** Haochen Wu, Yi Hou, Shiguang Xie
**Link:** https://arxiv.org/abs/2606.13604v1
**Summary:** The paper addresses the challenge of optimizing dispatch strategies in a three-sided food delivery marketplace by adapting the weight of different objectives based on delayed feedback from operational outcomes. It presents a reinforcement learning system that learns a policy to adjust these objectives without replacing the existing optimization framework, using data from real marketplace operations. The key result shows that this approach effectively increases batching efficiency and decreases costs for couriers while maintaining delivery quality for customers.

### 10. Beyond the Commitment Boundary: Probing Epiphenomenal Chain-of-Thought in Large Reasoning Models
**Authors:** Daniel Scalena, Sara Candussio, Luca Bortolussi, Elisabetta Fersini, Malvina Nissim, Gabriele Sarti
**Link:** https://arxiv.org/abs/2606.13603v1
**Summary:** The paper investigates how individual steps in chain-of-thought reasoning influence the final answers produced by large language models. By analyzing the causal importance of reasoning steps and identifying a "commitment boundary," the authors demonstrate that answers often stabilize early, allowing for the possibility of shortening reasoning processes without compromising performance. Their approach enables early exits in reasoning blocks, resulting in up to a 55% reduction in reasoning length while maintaining accuracy.
