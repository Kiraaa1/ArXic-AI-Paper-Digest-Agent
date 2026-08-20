---
## 2026-08-20

### 1. SPADE: Self-Play in Adaptive Synthetic Executable Environments
**Authors:** Bo Liu, Simon Yu, Yiding Jiang, Ao Qu, Andrew Zhao, Zichen Liu, Junsu Kim, Zijian Zhou, Seungone Kim, Tongzheng Ren, Mickel Liu, Hanfei Yu, Zhaorun Chen, Weiyan Shi, Paul Pu Liang, Luke Zettlemoyer, Yejin Choi, Natasha Jaques
**Link:** https://arxiv.org/abs/2608.19197v1
**Summary:** The paper addresses the challenge of enabling language agents to continuously improve by generating diverse and adaptive training environments. SPADE introduces a self-play reinforcement learning framework where a single language model acts both as an Environment Designer, creating executable training environments, and as a Reasoning Agent, learning to navigate them. The key contribution is that SPADE outperforms traditional fixed-environment approaches by significantly enhancing performance on various reasoning tasks, demonstrating a path toward open-ended self-improvement for AI systems.

### 2. ADEPT: Accelerating Dexterity via Pre-Training and Post-Training using Reinforcement Learning
**Authors:** Jayjun Lee, Jessica Yin, Asif Rana, Nicholas Blauch, Sam Mady, Mohak Bhardwaj, Nima Fazeli, Nathan Ratliff, Karl Van Wyk, Ankur Handa
**Link:** https://arxiv.org/abs/2608.19182v1
**Summary:** The paper presents ADEPT, a reinforcement learning framework designed to improve the dexterity of high-degree-of-freedom robots in solving complex tasks directly from raw sensory input. The approach involves first pretraining a robot's policy on a basic task and then fine-tuning it for more complex tasks using a combination of techniques to maintain its learned skills. The key contribution is a successful application of this method on two robotic models, enabling them to perform intricate tasks with human-like speed while efficiently transferring knowledge between tasks.

### 3. Beyond Teacher Likelihood: Group-Calibrated On-Policy Distillation for Long-Context Reasoning
**Authors:** Zhu Zhang, Jixun Wang, Xiaoang Xu, Xiaorong Wang, Zihan Zhou, Zhiyuan Wang, Shuo Wang, Chaojun Xiao, Yuezhi Zhou
**Link:** https://arxiv.org/abs/2608.19181v1
**Summary:** The paper addresses the challenge of training language models for long-context reasoning, where traditional on-policy distillation can lead to misalignment between local teacher guidance and global task success. The authors propose a method called Group-Calibrated On-Policy Distillation (GC-OPD), which adjusts the teacher's feedback based on a disagreement with task-specific verifier rewards, enabling better credit assignment across tokens. The approach significantly improves performance on long-context tasks, as demonstrated by notable increases in benchmark scores compared to standard distillation methods.

### 4. Finetuning Strategies for Querying Sounds by Vocal Imitation
**Authors:** Aditya Bhattacharjee, Christos Plachouras, Sungkyun Chang, Emmanouil Benetos
**Link:** https://arxiv.org/abs/2608.19174v1
**Summary:** This paper presents a winning approach to the AES AIMLA 2025 Challenge, which focuses on querying sound effects using vocal imitation. The authors employed two fine-tuning strategies: one using a frozen pretrained CED encoder with contrastive learning, and another using joint contrastive-triplet learning with semi-hard negatives paired with a MobileNetV3 encoder. The key contribution lies in the effectiveness of these strategies for improving sound retrieval accuracy based on vocal input.

### 5. Lévy Attention: Single-Pass Predictive Uncertainty for Continuous-Time Attention
**Authors:** Sotirios P. Chatzis, Loukas Papadoulas
**Link:** https://arxiv.org/abs/2608.19171v1
**Summary:** The paper addresses the challenge of quantifying predictive uncertainty in deep models for irregularly-sampled time series, where traditional methods do not provide a measure of trust in the predictions. The authors introduce Lévy Attention, a novel attention mechanism that simultaneously generates predictions and uncertainty estimates using a stochastic integral approach based on Poisson processes. The key contribution is the efficient calculation of predictive uncertainty, which significantly enhances performance in sparse data scenarios, leading to better trust rankings and improved calibration compared to existing methods.

### 6. Learned, Then Lost: A Measured Single-Example Counterfactual in Pre-training
**Authors:** Zachary Speck, Asa Shepard
**Link:** https://arxiv.org/abs/2608.19168v1
**Summary:** The paper investigates the impact of a single training example on a language model's performance by conducting careful counterfactual experiments. Specifically, researchers replaced one row in a training batch with various text styles and measured the subsequent effect on model predictions. The key finding is that while the injected example improved predictions shortly after its introduction, this effect diminished over time, indicating that the contribution of a single training instance may be transient and context-dependent.

### 7. ChildSafeAds Shared Task 2026: Commercial Content in Child-Facing YouTube Videos
**Authors:** Thales Bertaglia, Catalina Goanta, Gerasimos Spanakis, Gunes Acar
**Link:** https://arxiv.org/abs/2608.19165v1
**Summary:** The ChildSafeAds shared task addresses the challenge of identifying commercial content in YouTube videos aimed at children and teenagers, using a dataset of 3,360 videos along with their transcripts and additional metadata. The approach involves determining the type of promotional content, categorizing products, and flagging legal risks, with the help of models like GPT-5.4 and GPT-5.6-luna for labeling. A key finding is that 45.5% of the videos did not comply with the required ad disclosure, highlighting a significant gap in compliance with advertising regulations.

### 8. Interpretable AI predicts a 2026 summer dry anomaly in central China
**Authors:** Anran Wang, Wen Shi, Yong Luo, Jianbin Huang, Lijuan Chen, Junhu Zhao, Weixin Jin, Huihui Yuan
**Link:** https://arxiv.org/abs/2608.19163v1
**Summary:** The paper addresses the challenge of predicting seasonal precipitation anomalies in central China, specifically forecasting a dry summer anomaly for 2026. The authors developed a deep learning model that translates atmospheric circulation predictions into precipitation estimates, successfully identifying that northerly winds play a key role in this predicted dry anomaly. This approach not only improves predictive accuracy but also provides interpretable insights into the mechanisms driving these climate projections, supporting evidence-based assessments ahead of time.

### 9. Beyond the Transcript: Detecting Covert Co ordination in Latent Multi-Agent Communication
**Authors:** Ramneet Kaur, Pradyumna Chari, Ramesh Raskar, Jugad Singh, Sumit Kumar Jha, Anirban Roy
**Link:** https://arxiv.org/abs/2608.19161v1
**Summary:** The paper addresses the challenge of covert communication between language-model agents that may lead to harmful coordination without being visible in public transcripts. The authors propose a framework called Verifiable Latent Alignments (VLA) to monitor and guide these private communications through a combination of anomaly detection and counterfactual analysis. Key results show that VLA effectively identifies collusion in multi-agent settings, achieving high monitoring accuracy and significantly reducing collusive behavior in auctions without needing prior training on specific attack examples.

### 10. Continuous-Time Reinforcement Learning for Controlled Hawkes Jump-Diffusions
**Authors:** Tomasz R. Bielecki, Thibaut Mastrolia, Haoze Yan
**Link:** https://arxiv.org/abs/2608.19151v1
**Summary:** The paper addresses the challenge of controlling multivariate Hawkes-driven stochastic differential equations in a non-Markovian setting, where traditional control methods are inadequate due to the memory effects of Hawkes processes. The authors propose a continuous-time reinforcement learning algorithm, Hawkes-CT DDPG, which approximates these processes through a Markovianization approach, allowing for effective policy gradient learning despite the unknown parameters of the Hawkes kernels. Key findings demonstrate the method's effectiveness in optimizing scenarios involving different types of kernels compared to discrete time reinforcement learning techniques.
