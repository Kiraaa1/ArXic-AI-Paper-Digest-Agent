---
## 2026-06-18

### 1. Native Active Perception as Reasoning for Omni-Modal Understanding
**Authors:** Zhenghao Xing, Ruiyang Xu, Yuxuan Wang, Jinzheng He, Ziyang Ma, Qize Yang, Yunfei Chu, Jin Xu, Junyang Lin, Chi-Wing Fu, Pheng-Ann Heng
**Link:** https://arxiv.org/abs/2606.19341v1
**Summary:** The paper addresses the inefficiencies of traditional video understanding models that process all frames uniformly, leading to increased computational costs for longer videos. The authors introduce OmniAgent, an innovative framework that optimizes video understanding through a dynamic, iterative cycle of observing, reasoning, and acting, effectively extracting key audio-visual cues into a manageable memory. The results show that OmniAgent achieves superior performance compared to larger models, notably outperforming a 72 billion parameter model with only 7 billion parameters on specific benchmarks.

### 2. Learning User Simulators with Turing Rewards
**Authors:** Yingshan Susan Wang, Cedegao E. Zhang, Linlu Qiu, Zexue He, Pengyuan Li, Alex Pentland, Roger P. Levy, Yoon Kim
**Link:** https://arxiv.org/abs/2606.19336v1
**Summary:** The paper addresses the challenge of creating effective user simulators to enhance training for agent assistants and system evaluations. The authors introduce a novel reinforcement learning method called Turing-RL, which uses a Turing-Test-based reward system to train a language model to generate responses that are indistinguishable from real users' inputs. Their results show that this approach significantly improves performance compared to traditional methods, both in automated metrics and human evaluations.

### 3. Freeing the Law with LOCUS: A Local Ordinance Corpus for the United States
**Authors:** Denis Peskoff, Joe Barrow, Christopher Vu, Diag Davenport
**Link:** https://arxiv.org/abs/2606.19334v1
**Summary:** The paper addresses the lack of accessible, machine-readable local ordinance codes in the U.S., which are essential for understanding various regulations that affect daily life. The authors introduce LOCUS, a comprehensive corpus and harmonized access layer for municipal and county ordinance codes, leveraging OCR technology to create a usable dataset from diverse document formats. This resource, covering over 9,200 cities and counties, enables researchers to analyze local laws at a scale and depth previously unattainable, with tools like ModernBERT classifiers to explore characteristics of the ordinances.

### 4. The Chandra-Gaia Catalog of Counterparts: Resolving ambiguous Gaia matches to X-ray sources in the Chandra Source Catalog using Machine Learning
**Authors:** V. Samuel Pérez-Díaz, Vinay L. Kashyap, Joshua D. Ingram, David Fouhey, Juan Rafael Martínez-Galarza, Pavlos Protopapas, Jeremy J. Drake, Dong-Woo Kim, Cecilia Garraffo
**Link:** https://arxiv.org/abs/2606.19329v1
**Summary:** The paper addresses the challenge of accurately identifying optical counterparts to X-ray sources in the Chandra Source Catalog, particularly in cases of ambiguous matches with Gaia data. The authors utilize a machine learning approach, specifically training a gradient-boosted classifier on various source properties, to improve the cross-matching process. They successfully identify counterparts for approximately 113,000 X-ray sources, revealing the ability to resolve ambiguities and providing a comprehensive catalog to aid future astronomical studies.

### 5. UBP2: Uncertainty-Balanced Preference Planning for Efficient Preference-based Reinforcement Learning
**Authors:** Mohamed Nabail, Leo Cheng, Jingmin Wang, Nicholas Rhinehart
**Link:** https://arxiv.org/abs/2606.19328v1
**Summary:** The paper addresses the inefficiency of sample collection in preference-based reinforcement learning, where learning from behavior comparisons typically requires a lot of data. The authors present a new method called Uncertainty-Balanced Preference Planning (UBP2), which actively explores potential actions by considering uncertainties in rewards and dynamics. Their results demonstrate that UBP2 significantly improves sample efficiency compared to existing methods, achieving better performance on the Meta-World benchmark.

### 6. Rethinking Reward Supervision: Rubric-Conditioned Self-Distillation
**Authors:** Siyi Gu, Jialin Chen, Sophia Zhou, Arman Cohan, Rex Ying
**Link:** https://arxiv.org/abs/2606.19327v1
**Summary:** The paper addresses the challenges in training reasoning language models, particularly the limitations of traditional distillation techniques that rely on costly annotations and scalar rewards. The authors propose a new approach called Rubric-Conditioned Self-Distillation, which uses detailed rubric feedback to provide more granular guidance during training, leading to improved model performance. Their method outperforms existing techniques, achieving higher scores on various scientific reasoning benchmarks.

### 7. Reference-Driven Multi-Speaker Audio Scene Generation from In-the-Wild Priors
**Authors:** Michael Finkelson, Daniel Segal, Eitan Richardson, Shahar Armon, Nani Goldring, Poriya Panet, Nir Zabari, Benjamin Brazowski, Or Patashnik, Yoav HaCohen
**Link:** https://arxiv.org/abs/2606.19325v1
**Summary:** The paper addresses the challenge of generating realistic multi-speaker audio scenes without the need for structured supervision typically used in dialogue systems. The authors introduce ScenA, a model that leverages a text-to-audio foundation model, allowing it to create rich, natural audio environments by conditioning on multiple reference voices and a descriptive text prompt. The key contribution is the model's ability to outperform existing systems in generating complex conversational audio, including overlapping speech and ambient sounds, while maintaining speaker identity without structured dialogue scripts.

### 8. Data Intelligence Agents: Interpreting, Modeling, and Querying Enterprise Data via Autonomous Coding Agents
**Authors:** Anoushka Vyas, Aarushi Dhanuka, Sina Khoshfetrat Pakazad, Henrik Ohlsson
**Link:** https://arxiv.org/abs/2606.19319v1
**Summary:** The paper addresses inefficiencies in data integration caused by repetitive handoffs between data teams, which can lead to loss of information. It introduces Data Intelligence Agents (DIA), a system of autonomous coding agents that independently interpret data, create schemas, and generate queries, while utilizing shared memory for improved efficiency. The key finding is that the Query Generator within DIA outperforms existing methods on a variety of SQL tasks, showcasing its effectiveness in automating and optimizing the data querying process.

### 9. Explaining Attention with Program Synthesis
**Authors:** Amiri Hayes, Belinda Li, Jacob Andreas
**Link:** https://arxiv.org/abs/2606.19317v1
**Summary:** This paper addresses the challenge of making the inner workings of deep learning models, specifically attention heads in transformer language models, more interpretable by generating human-readable programs that mimic their behavior. The authors compute attention patterns from various models and use a pre-trained language model to create Python programs that can replicate these patterns based on input text. They achieve high accuracy in reproducing attention patterns and demonstrate that these programs can replace parts of the neural model with minimal impact on performance, thus offering a novel method for enhancing transparency in AI systems.

### 10. Diffusion-Proof: Recipe for Formal Theorem Proving Beyond Auto-Regressive Generation
**Authors:** Ruida Wang, Rui Pan, Pengcheng Wang, Shizhe Diao, Tong Zhang
**Link:** https://arxiv.org/abs/2606.19315v1
**Summary:** The paper addresses the limitations of traditional auto-regressive language models in formal theorem proving, particularly their struggles with long-range coherence and error compounding. It introduces **Diffusion-Proof**, a framework that employs diffusion language models for formal reasoning, featuring two models for proof generation and correction. The results show that **Diffusion-Proof** outperforms existing models, achieving notable improvements on key benchmarks and successfully solving complex problems that previous models could not.
