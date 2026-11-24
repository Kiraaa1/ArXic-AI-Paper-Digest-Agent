---
## 2026-11-24

### 1. Pruning Autonomous Driving VLAs: What to Preserve for Reasoning and Action
**Authors:** Seongchan Kim, Soowon Son, Sangoh Kim, Hyunah Ko, Eunbeen Hong, Hyunkoo Lee, Sanghyun Lee, WonJun Moon, Kihong Kim, Dongyeon Son, Woongchan Nam, Seungryong Kim
**Link:** https://arxiv.org/abs/2611.31240v1
**Summary:** The paper addresses the high memory and computational costs of reasoning vision-language-action (VLA) models used in autonomous driving by exploring structured pruning techniques. It introduces MoOP, a pruning method that effectively identifies and preserves essential components of the model based on their importance for scene understanding and trajectory prediction. The key contribution is that MoOP enables significant parameter reduction while maintaining competitive performance and improving inference speed and memory efficiency, outperforming existing methods without the need for post-pruning fine-tuning.

### 2. Let Vision-Language Models Generate Images through Their Representations
**Authors:** JB Kim, Byungwoo Jeon, Kyungmin Lee, Hyeonmo Kang, Cheonbok Park, Shinyoung Joo, Jinwoo Shin, Jeonghoon Kim
**Link:** https://arxiv.org/abs/2611.31237v1
**Summary:** The paper addresses the challenge of integrating visual understanding and generation in unified multimodal models. The authors introduce Integral, a framework that creates a shared visual representation space by combining hierarchical representations and a lightweight generative stream, enhancing the model's ability to generate images while preserving its understanding capabilities. Key results show that sharing visual representations significantly improves generative learning compared to using separate representations, indicating that pretrained vision-language models can effectively support visual generation tasks.

### 3. TowerBridge: Bridging the Dual-Encoder Modality Gap via Weight-Space Programming
**Authors:** Hani Alomari, Md Atabuzzaman, Chris Thomas
**Link:** https://arxiv.org/abs/2611.31233v1
**Summary:** The paper addresses the problem of ineffective retrieval in CLIP-style dual encoders, where images and text are mapped poorly due to a modality gap separating their shared embedding space. The authors propose a method called TowerBridge, which uses weight-space programming to make targeted weight adjustments in the encoders without traditional backpropagation, enhancing retrieval accuracy. Their approach improves retrieval performance significantly across multiple datasets, boosting COCO and Flickr30k retrieval scores while minimally impacting other metrics like ImageNet accuracy.

### 4. Language Models Steer on Injected Uncertainty Tokens, but Fail to Self-Monitor In Situ
**Authors:** Daniel Theron
**Link:** https://arxiv.org/abs/2611.31228v1
**Summary:** This study investigates the ability of language models to detect and correct their own reasoning errors while performing numerical tasks. The researchers tested four models by prompting them to express their confidence in real-time during problem-solving and found that, although models can be guided to correct mistakes when uncertainty is introduced, they consistently fail to recognize their own errors. The key result highlights a critical disconnect: while models struggle with self-monitoring, they can effectively adjust their responses when prompted with external indicators of uncertainty.

### 5. How Far Can Linear Go? BiPert, a Unified Framework for Single-Cell Perturbation Modelling
**Authors:** Abhishek Sharma, Aleksej Zelezniak
**Link:** https://arxiv.org/abs/2611.31227v1
**Summary:** The paper addresses the challenge of predicting how genetic changes affect cell behavior and identifying which genes are involved, particularly in new cell types. The authors developed a linear framework called BiPert that effectively predicts gene expression changes and identifies perturbed genes by breaking down transcriptional responses into shared and specific components. Key findings show that BiPert outperforms existing methods without requiring extensive biological knowledge and highlights the relationship between consistent perturbation effects and successful gene identification.

### 6. Self-Supervised Dataset Distillation via Mutual Information Maximization
**Authors:** Mohammad Hossein Moslemi, Mahdi Beitollahi, Zhimin Mei, Jiale Cai, Bissan Ghaddar, Boyu Wang
**Link:** https://arxiv.org/abs/2611.31225v1
**Summary:** The paper addresses the challenge of dataset distillation in self-supervised learning, where the goal is to create a smaller synthetic dataset that effectively captures the essential information from a larger dataset. The authors propose a new method called Mutual Information Prototype Alignment (MIPA), which optimizes synthetic images to maintain information that is invariant to different data augmentations. Their results demonstrate that MIPA generates higher-quality representations compared to existing methods, while also being more efficient in terms of time and storage.

### 7. Agentic AI for Intent Management and Control in Autonomous Communication Networks
**Authors:** Burak Demirel, Yu Wang, Pablo Soldati
**Link:** https://arxiv.org/abs/2611.31223v1
**Summary:** The paper addresses the challenge of translating high-level intents for mobile networks into actionable optimization and control strategies. It proposes a triadic framework with three agents—a language model for intent interpretation, an optimizer for policy adaptation, and a controller for decision-making—and integrates these components to effectively manage and fulfill network intents. The results from a case study in radio resource management demonstrate the framework's ability to align high-level goals with real-time network operations, showing adaptability to service needs and changing conditions.

### 8. CTLink: A Text-Prompted Segmentation Model for Linking Radiology Report Findings to 3D Chest CT Scans
**Authors:** Mohammed Baharoon, Sung Eun Kim, Mahmoud Hussain Alabbad, Lucas Bijnens, Ali Piracha, Reem Alwasiah, Talal Yahyan, Abdulrahman Alamoudi, Mashael Alshehri, Rayan Alsager, Hannah Hancock, Anna M. Hunkemöller, Peter Youssef, Mona A. Alhammad, Afnan Aljumayan, Brecht Van Berkel, Eric Bijnens, Saud Alhussain, Maarten Steyvers, Rolf Symons, Bryan Eelen, Ayed Alaklubi, Maha Buraykan Alshammari, Amirah Fahad Alshammeri, Tomas Gilvydis, Ibrahim AlTurki, Monerah Almohideb, Ali Alburkani, Shahad Alhomaiani, Fatima Jabali, Abdulrhman Aljouie, Daesung Kim, Junha Im, Michael Moritz, Hassan R. Alomaish, Pranav Rajpurkar
**Link:** https://arxiv.org/abs/2611.31222v1
**Summary:** CTLink addresses the challenge of linking text descriptions of findings in radiology reports to corresponding areas in 3D chest CT scans, which traditionally lack visual markers for these findings. The model was trained using a newly annotated dataset and significantly outperformed an existing model in terms of accuracy, achieving high hit rates and instance F1 scores in evaluations. Its development enhances the interpretability of radiology reports, although it still faces challenges with certain diffuse findings.

### 9. LeJEPA Features Are Not Isotropic, and Should Not Be
**Authors:** Richeek Das, Pratik Chaudhari
**Link:** https://arxiv.org/abs/2611.31216v1
**Summary:** The paper addresses the limitations of the LeJEPA regularizer, which aims to create isotropic Gaussian feature distributions but falls short in practice. The authors propose a new regularization term, PolarReg, which effectively optimizes the marginal distributions of feature magnitudes and directions without enforcing strict independence. This approach significantly improves training efficiency and accuracy, achieving comparable results to LeJEPA in much fewer epochs.

### 10. Seeking in Space: Benchmarking Purposeful Active Exploration of Vision-Language Models for Spatial Reasoning
**Authors:** Xiwei Liu, Yulong Li, Xuhui Li, Xinlin Zhuang, Zhixiang Lu, Haolin Yang, Jianxu Chen, Yifan Lu, Zhiran Zhang, Yutong Xie
**Link:** https://arxiv.org/abs/2611.31215v1
**Summary:** The paper addresses the challenge of enabling vision-language models (VLMs) to purposefully explore and gather evidence in real indoor spaces to answer spatial reasoning questions. The authors introduce ActSpace-Bench, a benchmark with 994 questions requiring exploration across various real environments, and evaluate how well different VLMs perform in this active exploration. The key finding is that while the best models can purposefully seek evidence, their performance is hampered by limited memory, highlighting the need for improvements in memory management and evidence-based reasoning for better spatial intelligence.
