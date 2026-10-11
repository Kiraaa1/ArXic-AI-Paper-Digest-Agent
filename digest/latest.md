---
## 2026-10-11

### 1. Predicting Alignment Generalization with Value Representations
**Authors:** Andy Liu, Mehar Bhatia, Karolina Stanczak, Mona Diab, Vered Shwartz, Daniel Fried
**Link:** https://arxiv.org/abs/2610.12410v1
**Summary:** This paper addresses the challenge of predicting how fine-tuning large language models (LLMs) to adhere to specific values affects their behavior in unfamiliar contexts. The authors analyze the impact of various value representations, finding that using model activations during value application is far more effective for this prediction than relying on descriptions of the values. A key contribution is the identification of correlations between value similarity and model robustness, which aids in developing a taxonomy of LLM values based on empirical data.

### 2. Searching for "Harmful Refusal": A Psychometric Audit of an AI Safety Benchmark
**Authors:** Christopher M. Stewart, Preston Botter, Natalie Sarabosing, Muye Zhang, Rachel Phinnemore, Shalini Ghosh, Hong Shen, Hoda Heidari
**Link:** https://arxiv.org/abs/2610.12409v1
**Summary:** The paper investigates the effectiveness of the HELM Safety benchmark in assessing the attribute of "harmful refusal" in AI models, focusing on whether it truly measures a distinct safety-related behavior. Employing psychometric analyses, the authors find that the relevant dataset (HarmBench) does not capture a single attribute and that existing evaluation scores may obscure individual model behaviors through aggregation. The key contribution highlights the need for benchmarks to clearly establish their composite scores reflect singular safety attributes before comparing AI models.

### 3. LeWAM: A JEPA World Action Model with Diffusion-Steering-Based MPC
**Authors:** Shashank Hegde, Alexander Popov, Elie Aljalbout, Nikolai Smolyanskiy
**Link:** https://arxiv.org/abs/2610.12407v1
**Summary:** The paper presents LeWAM, a new type of World Action Model that leverages a bidirectional transformer for more accurate action and observation predictions in robotic systems. By training on both forward and backward dynamics in a structured manner, LeWAM effectively filters out noisy information and improves understanding of the robot's and object's states. The key results show that LeWAM not only aligns better with actual state representations compared to its predecessors but also enhances closed-loop action performance and planning capabilities.

### 4. ViSkill: Reinforcing VLM Agents with Evolving Visual-Native Skills
**Authors:** Hongxing Li, Dingming Li, Yixin Li, Yong Du, Wenqi Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
**Link:** https://arxiv.org/abs/2610.12403v1
**Summary:** The paper introduces ViSkill, a framework designed to enhance visual language model (VLM) agents by allowing them to learn and reinforce skills through direct visual interactions rather than relying solely on text-based representations. By combining visual skill retrieval with reward shaping and policy optimization in a feedback loop, ViSkill improves sample efficiency and performance. The results demonstrate a high success rate of 0.89, and 0.91 with an accelerated learning mechanism, outperforming existing methods in various environments.

### 5. SpaceCast-Bench: Evaluating Predictive Spatial Reasoning in Vision-Language Models
**Authors:** Hongxing Li, Jinyue Su, Dingming Li, Wenqi Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
**Link:** https://arxiv.org/abs/2610.12402v1
**Summary:** The paper introduces SpaceCast-Bench, a new benchmark designed to assess predictive spatial reasoning in vision-language models, which is essential for understanding and anticipating spatial changes in scenes rather than just perceiving existing relationships. Through its evaluate-transform-infer framework with a diverse set of questions, the authors reveal a significant performance gap between models and human capabilities, highlighting that even the best-performing model only achieves 58% accuracy compared to 87% for humans. Key findings suggest that incorporating bridge views and explicit 3D evidence improves model performance, and fine-tuning can lead to substantial gains in predictive accuracy.

### 6. Learning Kilometer-Scale Weather Prediction with Global-Regional Alignment
**Authors:** Guowen Li, Yang Liu, Yujie Wang, Qiuyan Sun, Haoyuan Liang, Juepeng Zheng, Hong Cheng, Haohuan Fu
**Link:** https://arxiv.org/abs/2610.12401v1
**Summary:** The paper addresses the challenge of enhancing kilometer-scale regional weather forecasting by effectively integrating large-scale predictions from global weather models. The authors introduce ScaleCast, a framework that aligns global and regional weather information and combines them with local interactions, leading to improved forecasting accuracy. Key results show that ScaleCast significantly enhances predictions for various weather variables and adapts well across different regional domains and resolutions, outperforming existing methods in cyclone tracking and local climate metrics.

### 7. SpaceFlow: Locally Controllable 3D Generation
**Authors:** Neil De La Fuente, Joan Lafuente, Mukhammadali Sayfiddinov, Felicia Scharitzer, Marc Pollefeys, Ata Celen, Sayan Deb Sarkar, Elisabetta Fedele
**Link:** https://arxiv.org/abs/2610.12399v1
**Summary:** The paper presents SpaceFlow, a new method for generating 3D objects that allows users to have precise local control over both shape and appearance, addressing the limitations of existing 3D generation techniques that rely on global parameters. By assigning local control levels to geometric primitives, the approach enforces specific spatial constraints during generation and achieves high fidelity in desired areas while allowing creative variation elsewhere. The results show that SpaceFlow balances geometric accuracy and generative flexibility effectively, outperforming previous methods in appearance fidelity and local control capabilities.

### 8. Prospective Prediction of OOD Degradation from Source-Side Training Dynamics
**Authors:** Sasha, Monin
**Link:** https://arxiv.org/abs/2610.12397v1
**Summary:** This paper addresses the challenge of predicting out-of-distribution (OOD) performance degradation in machine learning models before it occurs. The authors demonstrate that by analyzing training dynamics from the source data, particularly through temporal summaries of model confidence and entropy, it is possible to develop an effective predictor for OOD failure. Importantly, the study shows that this predictive capability can be generalized between different model architectures without requiring additional training.

### 9. HRIL: Learning Multimodal Synergy via Higher-Order Tensor Modeling
**Authors:** Qun Dai, Liangjian Wen, Jiang Duan, Yong Dai, Dongkai Wang, Maolin Wang, Mingjie Wang, Jianzhuang Liu, He Yan, Zhao Kang
**Link:** https://arxiv.org/abs/2610.12393v1
**Summary:** The paper addresses the challenge of learning multimodal representations that effectively capture synergistic information, which is the unique signal that arises from the interaction of multiple modalities. The authors introduce a method called Higher-order Representation and Information Learning (HRIL), which uses higher-order tensor modeling to explicitly represent these joint interactions and incorporates a regularizer to enhance synergy capture. Their experiments show that HRIL outperforms existing multimodal methods, especially in scenarios where synergistic interactions are crucial.

### 10. GeoReform: Reflective Formalization Evolution for Multimodal Geometry Problem Solving
**Authors:** Jialu Wang, Ruichen Zhang, Xiaoou Liu, Hua Wei, Tianlong Chen
**Link:** https://arxiv.org/abs/2610.12391v1
**Summary:** The paper addresses the challenge that multimodal large language models (MLLMs) face in understanding geometric relationships in diagrams, often due to ineffective formalization of geometric elements. The proposed solution, GeoReform, is a framework that optimizes the formal representation of these elements by learning from errors in the reasoning process and adjusting how geometric information is organized and presented. This approach significantly improves the accuracy of a specific MLLM, Qwen3VL-2B, from 42.0% to 56.0% on the Geometry3K benchmark, highlighting the importance of effective formalization for geometry reasoning tasks.
