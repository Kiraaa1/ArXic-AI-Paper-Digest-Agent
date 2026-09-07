---
## 2026-09-07

### 1. UniMate: One Unified Model to Animate Diverse Skeletons
**Authors:** Linzhan Mou, Jiahui Lei, Zhiyang Dou, Chenyue Cai, Chaoyue Song, Adam Finkelstein, Szymon Rusinkiewicz
**Link:** https://arxiv.org/abs/2609.05415v1
**Summary:** The paper introduces UniMate, a unified model designed to generate realistic animations for various 3D skeletons without needing customization for each individual skeleton. Instead of relying on specific templates or pre-existing motion data, UniMate employs innovative techniques such as a topology-aware diffusion transformer that understands skeletal structure through advanced attention mechanisms. The key contribution is its ability to deliver high-quality, generalized motion synthesis across different skeleton types, significantly improving the efficiency and flexibility of automating 3D animations.

### 2. WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data
**Authors:** Ji Soo Lee, Xilun Chen, Pierce Chuang, Ashish Shenoy, Jason Wei, Dohwan Ko, Hyunwoo J. Kim, Benoit Corda
**Link:** https://arxiv.org/abs/2609.05405v1
**Summary:** WearableQA addresses the challenge of evaluating how well AI systems can reason about health using data from real-world wearable devices. The benchmark consists of thousands of multiple-choice questions derived from extensive longitudinal data of users, allowing for diverse reasoning evaluations. Key findings show that existing large language models vary significantly in their performance, highlighting that the task remains challenging, with most models scoring below 60% accuracy compared to a random chance baseline.

### 3. Diffusion TV: Experiencing Diffusion Models through Tangible, Embodied Interaction
**Authors:** Sihwa Park
**Link:** https://arxiv.org/abs/2609.05404v1
**Summary:** Diffusion TV addresses the challenge of making complex AI-generated diffusion processes more accessible and engaging to the public. It does this by creating an interactive art installation where participants physically manipulate a modified CRT TV to influence the clarity of AI-generated images and sounds, which represent different time periods of animal species. The key contribution is the promotion of an embodied, experiential understanding of AI generative technologies, allowing users to actively engage with the creative process rather than just the final outputs.

### 4. RegionFed: Federated Learning for Personalized Query Understanding in Heterogeneous Retail Environments
**Authors:** Quoc H. Nguyen, Ali Lafzi, Abhijeet Phatak, Siddharth Pratap Singh, Rohit Upadhyay, Yogananda Domlur Seetharama, Chittaranjan Tripathy
**Link:** https://arxiv.org/abs/2609.05403v1
**Summary:** The paper presents RegionFed, a federated learning framework designed to improve personalized query understanding in diverse retail environments, which struggle with data heterogeneity and privacy concerns. Unlike traditional methods that create global models, RegionFed operates at the gradient level, allowing for better personalization without collapsing on modern transformer models. The results show RegionFed achieves 92.27% accuracy, effectively closing the gap to centralized models while ensuring privacy and maintaining stability across various architectures.

### 5. Same Trajectory, Contradictory Rewards (ROBORMBENCH): Paraphrase Fragility in Vision Language Reward Models
**Authors:** Wonje Jeung, Sangyeon Yoon, Hyesoo Hong, Yoonjun Cho, Dongjae Jeon, Bumjun Kim, Jean Oh, Youngjae Yu, Albert No
**Link:** https://arxiv.org/abs/2609.05401v1
**Summary:** The paper addresses the issue of paraphrase invariance in vision-language models (VLMs) used as reward functions in robotic learning, where the same robot behavior should receive consistent rewards regardless of how the goal is described. The authors introduce ROBORMBENCH, a comprehensive benchmark that reveals significant instability in current VLMs due to paraphrased instructions, leading to inconsistent reward assessments. Their key finding is that dedicated reward models specifically trained with trajectory-grounded supervision are much more stable, highlighting the need for robustness against paraphrasing in VLM-based reward systems for robotics.

### 6. A Deep Generative Model for Synthesizing Labeled Wireless Signals
**Authors:** Yuxiao Li, Keke Hu, Santiago Mazuelas, Yuan Shen
**Link:** https://arxiv.org/abs/2609.05396v1
**Summary:** This paper addresses the challenge of acquiring realistic labeled wireless signal datasets needed for training models in wireless sensing, which can be costly and difficult to obtain. The authors propose a new deep learning approach called Inter-Instance Generative Adversarial Networks (IIns-GAN) to generate these labeled signals, making them adaptable to various environments. The experimental results reveal that the generated signals closely resemble real-world data and enhance the performance of models in tasks such as distance estimation and environment identification.

### 7. Multi-Step Tool-Calling over Korean Open Public APIs: A Benchmark and a Data-Synthesis Recipe
**Authors:** Dain Kim, Eungi Cho, Kyumin Kim, Shinyeong Noh, Kyuseong Lim
**Link:** https://arxiv.org/abs/2609.05395v1
**Summary:** The paper addresses the challenge of using open-source language models for multi-step tool-calling in executing tasks through Korean public APIs, where existing models perform poorly. The authors introduce KOPA-Bench, a benchmark with 145 tasks, and develop EDGE, a method for synthesizing executable paths by dynamically linking API outputs and inputs based on live execution success. Their approach enables a smaller 9B model to significantly improve its performance, coming close to a larger 27B model while exceeding results on additional benchmarks.

### 8. Necessary or Sufficient? Evaluating LLM Explanations With Behavioural Evidence
**Authors:** Urja Pawar, Rajitha Ramanayake, Nabeel Kemal, Ashwin Kandath, Owen O'Neill, Guillaume Bourgeon, Houssem Chatbri
**Link:** https://arxiv.org/abs/2609.05385v1
**Summary:** This paper investigates the reliability of explanations provided by large language models (LLMs) in decision-making tasks, specifically whether these explanations are necessary and sufficient for the outputs these models generate. The authors use controlled interventions to evaluate how often changes to identified factors impact decisions (necessity) and how often keeping them while removing other information preserves decisions (sufficiency). They find that while the explanations contain relevant information, they do not consistently reflect the factors with the strongest influence, highlighting a need for more reliable frameworks in understanding LLM behaviors during agent oversight.

### 9. Reflection-aware Generative Novel View Synthesis
**Authors:** GeonU Kim, Shin Dong-Yeon, Tae-Hyun Oh
**Link:** https://arxiv.org/abs/2609.05382v1
**Summary:** The paper introduces Ref-GeNVS, a novel method for generating new views of scenes that include mirrors without requiring additional training. The approach involves treating the reflections in mirrors as additional viewpoints and using a two-stage generation process to create consistent and coherent images that accurately represent reflected scene details. As a result, Ref-GeNVS significantly outperforms existing methods, delivering high-quality novel views with a clear representation of the scene structures seen through mirrors.

### 10. Molecular Déjà Vu: Digit-Level Retrieval of Published Values in Frontier Language Models
**Authors:** Matthias Busch, Marius Tacke, Sviatlana V. Lamaka, Mikhail L. Zheludkevich, Christian J. Cyron, Roland C. Aydin, Christian Feiler
**Link:** https://arxiv.org/abs/2609.05381v1
**Summary:** The paper addresses the issue of large language models (LLMs) potentially relying on memorized molecular property values rather than performing genuine predictions. The authors evaluated 22 advanced LLMs on 12 regression benchmarks to assess the prevalence of verbatim retrieval of published data, finding that such retrieval was common in certain datasets and influenced by the reasoning level applied. A key finding is that while retrieval is significant, it does not solely determine a model's predictive ability, suggesting that LLMs can still demonstrate general predictive capabilities despite high rates of memorization.
