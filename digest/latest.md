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
