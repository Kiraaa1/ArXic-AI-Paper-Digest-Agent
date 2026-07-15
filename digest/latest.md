---
## 2026-07-15

### 1. Do AI Agents Know When a Task Is Simple? Toward Complexity-Aware Reasoning and Execution
**Authors:** Junjie Yin, Xinyu Feng
**Link:** https://arxiv.org/abs/2607.13034v1
**Summary:** The paper addresses the challenge of AI agents overestimating the complexity of tasks, leading to unnecessary additional work when executing multi-step workflows. The authors propose a new framework called E3, which enables agents to assess task difficulty and follow a more efficient execution path. The key finding is that E3 significantly reduces resource consumption while maintaining success rates, demonstrating a promising direction towards creating more efficient AI systems grounded in real engineering tasks.

### 2. The Seriality Gap in Video Diffusion Models
**Authors:** Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu, Yutong Bai
**Link:** https://arxiv.org/abs/2607.13031v1
**Summary:** The paper addresses the challenge of video diffusion models struggling to predict outcomes in sequences of events (like bounces between balls) as the number of events increases. The researchers conducted experiments to show that the performance of these models declines with longer causal chains, primarily due to the inherent limitations of their denoising processes. They introduce the concept of the "seriality gap," highlighting how these models fail to efficiently handle tasks requiring sequential reasoning, and suggest that improving the model's architecture and computation methods could enhance performance in such scenarios.

### 3. TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale
**Authors:** Zhouchonghao Wu, Akshay Rangesh, Weixin Li, Wei-Jer Chang, Zachary Lee, Tim Wang, Wei Zhan
**Link:** https://arxiv.org/abs/2607.13028v1
**Summary:** The paper introduces TerraZero, a high-performance procedural driving simulator designed for training autonomous driving agents without relying on human demonstration data. By enabling rapid self-play training with diverse, realistic scenarios generated from real-world map geometry, TerraZero achieves impressive results, including ranking among the best in safety and collision metrics in various driving benchmarks. Notably, it is the first fully learned policy to excel in the challenging InterPlan long-tail benchmark.

### 4. PalmClaw: A Native On-Device Agent Framework for Mobile Phones
**Authors:** Hongru Cai, Yongqi Li, Ran Wei, Wenjie Li
**Link:** https://arxiv.org/abs/2607.13027v1
**Summary:** PalmClaw is a new open-source framework designed to enable mobile phone agents to perform multi-step tasks more efficiently by directly accessing device capabilities rather than relying on user interface actions. By structuring how agents interact with mobile tools, it improves task success rates by 11.5% and significantly reduces completion times by nearly 95% compared to existing methods. This framework simplifies the execution process for mobile agents and enhances their effectiveness in leveraging smartphone functionalities.

### 5. A Shortcut to Statistically Steady-State Turbulence with Flow Matching
**Authors:** Gianluca Galletti, Gerald Gutenbrunner, William Hornsby, Lorenzo Zanisi, Naomi Carey, Stanislas Pamela, Johannes Brandstetter, Fabian Paischer
**Link:** https://arxiv.org/abs/2607.13022v1
**Summary:** This paper addresses the challenge of computationally expensive simulations required to reach the steady-state of turbulent systems, specifically in gyrokinetic turbulence. The authors introduce GyroFlow, a latent generative model that bypasses the transient phase by directly modeling the distribution of steady states, leading to significant computational speedups and improved accuracy compared to traditional methods. Their new approach not only performs well in generating accurate steady-state statistics but also enhances numerical code efficiency for producing relevant data.

### 6. Audio-Native Speech Recognition with a Frozen Discrete-Diffusion Language Model
**Authors:** Harsha Vardhan Khurdula, Abhinav Kumar Singh, Yoeven D Khemlani, Vineet Agarwal
**Link:** https://arxiv.org/abs/2607.13013v1
**Summary:** The paper introduces a new approach to automatic speech recognition using a discrete diffusion language model instead of traditional autoregressive decoders. By training a model that refines transcripts in parallel and utilizing a frozen Whisper encoder for acoustic features, the authors achieve a significant reduction in word error rate to 6.6% on the LibriSpeech test-clean dataset. This method allows for efficient transcription in about eight parallel steps and demonstrates effective multilingual performance with a single adapter.

### 7. Dynamic Resource Allocation for Ensemble Determinization MCTS
**Authors:** Jakub Kowalski, Adam Ciężkowski, Artur Krzyżyński, Mark H. M. Winands
**Link:** https://arxiv.org/abs/2607.13007v1
**Summary:** The paper addresses the challenge of improving the performance of Ensemble Determinization Monte Carlo Tree Search (MCTS) in high-uncertainty environments like board games with randomness and hidden information. The authors introduce two enhancements for dynamic resource allocation: adjusting the number of determinization trees based on search behavior and optimizing simulation budget allocation across these trees. Their experiments with tabletop games show that these enhancements significantly improve the algorithm's performance.

### 8. The Spectrum Is Not Enough: When Context Helps Time-Series Forecasting
**Authors:** Mert Onur Cakiroglu, Mehmet Dalkilic, Hasan Kurban
**Link:** https://arxiv.org/abs/2607.13006v1
**Summary:** This paper addresses the misconception that the predictability of time-series data can be solely assessed through spectral analysis. The authors demonstrate that the value of adding contextual information (like longer lookback periods or advanced retrieval models) depends on specific features of the series rather than its spectral properties. Key findings include a novel diagnostic called the "coverage deficit," which better captures the predictive value beyond traditional spectral indices across multiple benchmarks, showing that context can significantly change prediction outcomes.

### 9. Watermark Forensics for Generative Models: An Information-Theoretic Perspective
**Authors:** Xiaoyu Li, Zheng Gao, Xiaoyan Feng, Jiaojiao Jiang, Yulei Sui, Jiankun Hu
**Link:** https://arxiv.org/abs/2607.13003v1
**Summary:** The paper addresses the problem of watermarking generative model outputs to not only detect machine-generated text but also attribute it to specific users and extract hidden information. The authors employ an information-theoretic framework to analyze the costs associated with different watermarking capabilities, establishing a precise relationship between sample length and information retrieval outcomes. A key contribution is the provision of a tight entropy-rate law for multi-user attribution, alongside the identification of two significant gaps in watermarking effectiveness, demonstrated through experiments on various generative models.

### 10. Win by Silence: Deletion Non-Monotonicity, Autonomous Exploitation, and Typed-State Gating in LLM Plan Evaluation
**Authors:** Aleh Manchuliantsau
**Link:** https://arxiv.org/abs/2607.12986v1
**Summary:** The paper addresses the problem of plan evaluators rewarding less explicit strategies in LLM-generated venture routes, which can lead to improvements based on omissions rather than genuine enhancements. The authors analyze the effects of deletions within these plans using a mathematical model and an adaptive framework, finding that many routes can score better through strategic omissions. A key contribution is the introduction of a detection mechanism, PCSC, that neutralizes these omissions, highlighting GATE's role in shaping search outcomes rather than simply filtering plans based on their quality.
