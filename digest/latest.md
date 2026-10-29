---
## 2026-10-29

### 1. MuonGS: Pretraining LLMs with Relaxed Weight-Norm Control
**Authors:** Athanasios Glentis, Dawei Li, Mingyi Hong
**Link:** https://arxiv.org/abs/2610.37647v1
**Summary:** The paper addresses the challenge of optimizing language model pretraining by improving weight norm control during updates, which can enhance training efficiency. The authors propose MuonGS, a method that utilizes Gram-Schmidt projection to manage weight updates while avoiding fixed weight norms. The key finding is that MuonGS achieves faster learning rates and better model performance, resulting in up to a 15% speedup in token processing compared to previous methods.

### 2. Multi-State Linear Attention with Generalized Second-Order Routing
**Authors:** Hee Seung Hwang, Sanghyuk Chun, Xindi Wu, Olga Russakovsky, Zhiwei Deng
**Link:** https://arxiv.org/abs/2610.37645v1
**Summary:** The paper addresses the inefficiency of self-attention mechanisms in processing long sequences due to their quadratic time complexity. The authors introduce MERLIN, a method that enhances Multi-State Linear Attention by considering both the mean and variance of segment alignments, resulting in a more nuanced aggregation of information. Key results show that MERLIN significantly improves performance on long-context tasks, consistently outpacing existing aggregation methods even when using less memory.

### 3. Metacognitive Decoding: Efficient Inference for Diffusion Language Agents
**Authors:** Mingyu Zhao, Shuhang Lin, Ligong Han, Xiaojing Yu, Zhenting Wang, Yifei Pang, Yang Zhou, Dimitris N. Metaxas
**Link:** https://arxiv.org/abs/2610.37642v1
**Summary:** The paper addresses the challenge of inefficient computation in diffusion language models during token generation for agent interactions. It proposes a metacognitive controller that optimizes the generation process by dynamically deciding when to finalize tokens and how much text to generate, significantly reducing computational costs. The approach achieved an average reduction of 20.6% in inference FLOPs while still maintaining competitive accuracy across various benchmarks.

### 4. What Improves During Pretraining? Tracking Knowledge Acquisition with Point-in-Time Models
**Authors:** Chang Su, Bin Wu, Emine Yilmaz, Yao Lu
**Link:** https://arxiv.org/abs/2610.37631v1
**Summary:** This paper investigates how language models acquire different types of knowledge during their pretraining phase by analyzing models trained on web data from various years. The authors introduce a temporal variability score (TVS) to track the consistency of knowledge representation over time, finding that while both low- and high-TVS items are learned similarly early on, high-TVS items improve more rapidly later in training. The key result reveals that high-TVS items significantly outperform low-TVS items in knowledge-intensive tasks, highlighting distinct patterns in knowledge acquisition throughout pretraining.

### 5. Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions
**Authors:** Anouar Imel, Imad Charradi, Abderrahman Sghir, Khalil El Khammar
**Link:** https://arxiv.org/abs/2610.37624v1
**Summary:** The paper addresses how to effectively compress discussions from groups of large language models (LLMs) into a memory for making final decisions, focusing on which claims to retain. It introduces the CrossProfile benchmark and finds that common heuristics—selecting the rarest claims or those most relevant—often fail, with performance improving when attribution tags are removed from facts. Key results show that balancing the evidence retained in memory is more important than the selection policy, and that complete transcripts can hinder decision-making accuracy rather than help.

### 6. VideoLVR: Latent Visual Reasoning over Grounded Video Evidence
**Authors:** Shilong Li, Xingyuan Bu, Hao Shi, Yun Xing, Weixin Feng, Qiangpeng Yang, Shilei Wen
**Link:** https://arxiv.org/abs/2610.37613v1
**Summary:** The paper presents VideoLVR, a new method to enhance video understanding in multimodal large language models by effectively integrating visual evidence during reasoning. Unlike existing methods that struggle with visual detail maintenance or rely on non-visual cues, VideoLVR generates latent visual evidence from relevant video moments and aligns this with text-based reasoning. The approach significantly improves performance on tasks requiring detailed visual understanding without increasing the model's context complexity.

### 7. EnvSched: Environment-Aware Scheduling for Rollout-Efficient Agent Reinforcement Learning
**Authors:** Sihan Yang, Weichen Bai, Ruichuan An, Yiming Cheng, Zhiyuan Feng, Tianyi Jiang, Renye Yan, Ning Ding, Yifan Zhang, Renrui Zhang, Yehui Tang, Wentao Zhang
**Link:** https://arxiv.org/abs/2610.37609v1
**Summary:** The paper addresses the challenge of improving the efficiency of reinforcement learning (RL) agents when faced with expensive environment rollouts. It introduces EnvSched, an online scheduling system that optimizes task selection by balancing between informative rewards and diverse environments, using a dual-relation graph to manage knowledge from historical rollouts. The results show that EnvSched significantly enhances performance, achieving a higher average score in various benchmarks with fewer training steps compared to random task selection.

### 8. Beyond Answer Changes: Matched Same-Class Controls for Local Audio Evidence
**Authors:** Yunuo Wang, Maoyuan Chen, Yuanjin Huang, Xing Liu
**Link:** https://arxiv.org/abs/2610.37605v1
**Summary:** This paper addresses the issue of understanding how audio-language models respond to local changes in sound events, specifically whether answer changes are due to sensitivity to the class of the event or to alterations in the audio waveform itself. The authors conducted experiments comparing same-class (which preserve the original answer) and different-class event replacements in synthetic soundscapes. They found that different-class replacements led to significantly more answer changes, while same-class replacements maintained high accuracy, suggesting that the class of the sound event plays a critical role in model responses.

### 9. MoI-Bench: A Benchmark for Image Generation and Editing on Mobile Devices
**Authors:** Kailai Feng, Haoxiang Rao, Yuxiang Wei, Bo Chen, Junsong Li, Yang Pan, Chengkun Cai, Jagmohan Chauhan
**Link:** https://arxiv.org/abs/2610.37599v1
**Summary:** The paper introduces MoI-Bench, a new benchmark specifically designed to evaluate image generation and editing models on mobile devices, addressing the gap between on-device and server-side capabilities. It comprises 64 subtasks and employs a two-dimensional Quality-Deployability capability map to provide nuanced insights into model performance. Key findings suggest that while on-device models perform well in generation and editing, there's a critical need to enhance task coverage and editing quality, especially in areas like identity preservation and text rendering.

### 10. GAS-PFN: Graph-Aware Spatiotemporal Prior-Data Fitted Networks for Zero-Shot Traffic Forecasting
**Authors:** Joseph Natter, Long Vu, Yifan Zhang, Bobin Deng, Kun Suo, Rui Wu
**Link:** https://arxiv.org/abs/2610.37598v1
**Summary:** The paper addresses the challenge of traffic forecasting, which involves understanding complex temporal and spatial dependencies in road networks, particularly for new or evolving systems. The authors propose the Graph-Aware Spatiotemporal Prior-Data Fitted Network (GAS-PFN), which enhances zero-shot forecasting by integrating road topology into its learning process through a random-walk diffusion method. The key result shows that GAS-PFN significantly improves forecasting accuracy, achieving a 34% reduction in mean squared error compared to its closest predecessor, demonstrating that aligning model design with graph structure enhances prediction performance.
