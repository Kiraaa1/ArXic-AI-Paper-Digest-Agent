---
## 2026-10-30

### 1. Elucidating the Design Space of LM Data Attribution
**Authors:** Steven Yu, Sheng-Yu Wang, Kimia Hamidieh, Antonio Torralba, David Bau
**Link:** https://arxiv.org/abs/2610.40655v1
**Summary:** The paper addresses the challenges in evaluating data attribution methods for Language Models (LMs) by introducing a Controlled Attribution Benchmark (CATT) that uses fictitious knowledge to provide clear ground truth. By systematically altering dataset properties and examining the effects of loss functions and aggregation methods on attribution scores, the authors demonstrate that utilizing negative log-odds gradients improves the identification of critical tokens, leading to a significantly higher recall in attribution accuracy. This method also enhances counterfactual retraining performance across various techniques.

### 2. Propose-Filter-Release: Scaling Noise to Typical Sensitivity via Private Filtering
**Authors:** Moshe Shenfeld, Eliad Tsfadia, Katrina Ligett
**Link:** https://arxiv.org/abs/2610.40654v1
**Summary:** The paper addresses the issue of differential privacy being overly influenced by outlier records that can dictate the amount of noise added to data, leading to unnecessary sensitivity. The authors propose a method called "propose-filter-release" (PFR), which privately filters out these outlier records before applying a privacy mechanism. The key contribution is demonstrating that PFR can ensure differential privacy under various scenarios, making it a flexible and general approach applicable to different types of statistical analyses and estimations.

### 3. Rethinking Neural Thickets Without Weight Perturbations
**Authors:** Nicolas Dufour, Elouan Gardès, Amil Dravid, Patrick Pérez, Loic Landrieu
**Link:** https://arxiv.org/abs/2610.40649v1
**Summary:** The paper challenges the Neural Thickets hypothesis, which suggests that the performance gains in pretrained language models come from exploring dense neighborhoods in weight space through random perturbations. Instead, the authors propose an approach called Perturb-Select-Vote (PSV), which relies on generating output diversity and selecting high-performing predictions from a frozen model without modifying its weights. The key findings indicate that significant improvements can be achieved through this method, often surpassing the benefits of full weight perturbations, thereby offering a simpler, training-free alternative for enhancing model performance across language and vision tasks.

### 4. Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers
**Authors:** Jiongfan Yang, Weichen Fan, Haiwen Diao, Zhongang Cai, Ziwei Liu
**Link:** https://arxiv.org/abs/2610.40647v1
**Summary:** The paper addresses the inefficiency of pixel-space generative Transformers that use one token per image patch, which makes global attention costly when capturing fine details. To tackle this, the authors introduce SpecSlot, a novel approach that decouples the output detail from global attention length by assigning multiple local slots to each spatial anchor and restricting global attention to just the lowest-frequency slot. The key contribution is that SpecSlot achieves comparable or superior image quality while reducing computational costs, outperforming existing models on benchmark datasets.

### 5. Adaptive Scenario Generation for KL-DRO Around a Learned Density Model
**Authors:** Aron Brenner, Saurabh Amin
**Link:** https://arxiv.org/abs/2610.40644v1
**Summary:** This paper addresses the challenge of distributionally robust optimization (DRO) in scenarios where the available data is limited, particularly in how to hedge against potential distributional shifts. The authors propose an innovative approach using a Kullback-Leibler (KL) ball centered around a learned density model, which allows for adapting the scenario set by iteratively sampling and steering towards worse-case scenarios. The key result shows that this method can significantly reduce costs in situations where data is scarce and the model can extrapolate effectively, especially compared to traditional approaches that rely solely on the empirical distribution.

### 6. Luggage re-identification: A study of strategies towards a real-world application
**Authors:** Quentin Dhôte, Romaric Audigier
**Link:** https://arxiv.org/abs/2610.40643v1
**Summary:** The paper addresses the challenge of luggage re-identification in crowded and cluttered environments, which is crucial for security and lost luggage recovery. The authors propose an end-to-end system that utilizes multiple video streams to detect and re-identify luggage by effectively merging different views and shots. Their experiments on a benchmark dataset demonstrate improved performance in real-world scenarios compared to existing methods focused solely on single, clear images.

### 7. From extreme weather to agricultural consequences with agentic AI
**Authors:** Minghan Yu, Mengyu Dai, Yixin Wen, Haizhao Yang
**Link:** https://arxiv.org/abs/2610.40641v1
**Summary:** The paper addresses the challenge of predicting the agricultural impact of extreme weather events, which is often difficult despite accurate weather forecasts. The authors introduce WxCrop, an AI-based agent that uses causal analysis of weather indices to reliably predict crop losses for specific scenarios, such as hurricanes and droughts, by integrating weather data with agricultural records. The key result shows that WxCrop can accurately assess crop loss and validate predictions through extensive checks, significantly aiding governments and farmers in responding to agricultural crises.

### 8. world2vec: Mechanistic world models through latent dynamics learning
**Authors:** Tobias Schmidt, Rodrigo Gonzalez Laiz, Krisztián Szuppinger, Steffen Schneider
**Link:** https://arxiv.org/abs/2610.40637v1
**Summary:** The paper addresses the issue of conventional world models lacking mechanistic interpretability and efficient dynamics representation in controlling environments. The authors introduce "world2vec," a method that learns latent dynamics directly from observations and actions without relying on reward signals, achieving impressive control performance with significantly fewer parameters than existing models. Key results show that world2vec not only excels in controlling continuous environments from pixel data but also enhances system identification across a diverse set of 71 attractors.

### 9. Probing Spatial State Representations in Visual Foundation Models
**Authors:** Baiqiao Yin, Zhongang Cai, Ruisi Wang, Qiwei Liang, Lei Yang, Ziwei Liu
**Link:** https://arxiv.org/abs/2610.40636v1
**Summary:** This paper investigates whether visual foundation models can maintain and update spatial awareness beyond current visual observations, which is crucial for action guidance. The authors explore four dimensions of spatial capability using frozen-feature probes on various model representations while streaming images from static indoor environments. They find that while models can effectively read visible scenes, their ability to maintain object persistence and use that information for future actions often falls short, suggesting that evaluations of spatial representations should also consider their long-term usability and predictive capacities.

### 10. ShallowDefend: Harnessing Shallow Safety Alignment for Multi-Turn Defender
**Authors:** Qiyao Ma, Xiaodong Liu, Weiwei Yang, Mingqian Feng, Chengquan Guo, Jialin Song, Carolyn Buractaon, Zhe Zhao, Junshan Zhang, Sandeep Atluri, Christopher White, Jianfeng Gao
**Link:** https://arxiv.org/abs/2610.40627v1
**Summary:** The paper addresses the issue of large language models inadequately refusing harmful requests during multi-turn conversations due to shallow safety alignment, where safety responses are concentrated in the initial tokens. The authors propose a framework called Assess → Decide → Respond, which allows the model to evaluate user intent, make a clear safety decision, and then generate a response based on that decision. Their approach significantly enhances multi-turn safety performance while maintaining utility, demonstrating that intervening early in the response process can effectively control and improve safety outcomes.
