---
## 2026-08-13

### 1. AVA-Encoder: Towards Agent-Native Video Representation Learning
**Authors:** Chuyue Li, Jinpeng Yu, Haozhe Wang, Tian Xueyun, Zhijing Zhang, Bingnan Li, Shuqi Gu, Kan Ren, Jiaming Liu, Ruihua Hua
**Link:** https://arxiv.org/abs/2608.12313v1
**Summary:** The paper introduces the AVA-Encoder, a new framework designed to help creative agents learn from high-quality human films by providing a structured video representation that supports agentic reasoning. This approach transforms videos into knowledge graphs that can be reconstructed back into video, allowing for easier querying and editing by agents. The key result shows that AVA-Encoder significantly improves video representation learning, outperforming existing methods and requiring fewer system resources, while also providing a valuable dataset for further research.

### 2. DreamFly: Causal Memory and Receding-Horizon Diffusion Planning for Aerial Vision-Language Navigation
**Authors:** Yan Deng, Fei Xu
**Link:** https://arxiv.org/abs/2608.12308v1
**Summary:** DreamFly addresses the challenges of aerial vision-language navigation by enhancing an agent's ability to integrate historical visual context and make effective planning decisions in a partially observable environment. The framework employs a diffusion-based approach with a causally aligned memory and a receding-horizon planning strategy that focuses on executing one action at a time while considering future actions. Experimental results show that DreamFly significantly outperforms existing methods in navigation success rates and reduces navigation errors in various testing environments.

### 3. AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses
**Authors:** Cheng Qian, Wenting Zhao, Liangwei Yang, Heng Wang, Jielin Qiu, Heng Ji, Silvio Savarese, Huan Wang, Shelby Heinecke
**Link:** https://arxiv.org/abs/2608.12307v1
**Summary:** This paper explores whether stronger AI models can assist weaker models during testing without changing their parameters, by creating tailored inference-time harnesses that improve task performance. By refining these harnesses based on feedback from a limited validation set, the researchers demonstrated that this approach nearly doubled the target models' performance on certain benchmarks. The findings highlight the importance of designing effective inference-time aids as a complementary strategy to traditional training methods.

### 4. Redistribution-based Cost Inference Improves Sparse Safe Offline RL
**Authors:** Ebenezer Gelo, Geraud Nangue Tasse, Steven James, Benjamin Rosman
**Link:** https://arxiv.org/abs/2608.12306v1
**Summary:** The paper addresses the challenge of safe offline reinforcement learning (RL) where feedback is limited to binary signals indicating unsafe transitions rather than detailed per-step costs. The authors propose a Redistribution-based Cost Inference (RCI) framework that translates this sparse feedback into meaningful per-step cost annotations, enabling the training of a constrained offline policy. Their results show that this approach leads to significantly lower violation rates in safety-critical tasks like highway driving and robotic manipulation compared to traditional methods, while also being more robust to variations in the data.

### 5. Constructing Dynamic Master Logic Models as Knowledge Graphs for Complex System Diagnostics Using Retrieval-Augmented Large Language Models
**Authors:** Saman Marandi, Yu-Shu Hu, Mohammad Modarres
**Link:** https://arxiv.org/abs/2608.12304v1
**Summary:** The paper addresses the challenge of efficiently constructing Dynamic Master Logic (DML) models for complex systems, which typically require expert knowledge and manual interpretation of documentation. By leveraging Retrieval-Augmented Generation and Large Language Models, the authors propose an automated framework that transforms system descriptions into Knowledge Graphs (KG-DML). This approach not only enhances scalability but also demonstrates effective reconstruction of functional models for diagnostic and reliability analysis in a practical example from a reactor system.

### 6. A Framework for Designing Reward Functions: From Objectives to Features to Human-Aligned Reward Functions
**Authors:** Di Yang Shi, W. Bradley Knox
**Link:** https://arxiv.org/abs/2608.12302v1
**Summary:** The paper addresses the challenge of designing human-aligned reward functions that reflect user preferences for AI systems, particularly for those without technical expertise. The proposed method involves a three-step process: identifying fundamental objectives from natural language task descriptions, selecting relevant measurable outcomes, and determining the weights for these outcomes based on user preferences. A key contribution is the efficient approach to selecting reward terms using a polynomial-time algorithm and framing the weight fitting as a convex feasibility problem that allows for a precise and conflict-free reward function region.

### 7. Class Activation Mapping in Explainable Computer Vision: A Method-Centered Review of CNN, Transformer, and Foundation-Model-Era Visual Explanations
**Authors:** AmirHossein Eshghi, Hamid Saadatfar, Seyyed Ali Hoseini, AmirMohsen Eshghi, Siavash Arjomand Bigdel
**Link:** https://arxiv.org/abs/2608.12299v1
**Summary:** This paper reviews the evolution of Class Activation Mapping (CAM) methods in explainable AI, which generate heatmaps to highlight relevant features in images for model predictions. It categorizes 57 techniques based on how they attribute explanations and their dependence on model architecture, revealing a shift towards more complex, multi-layer, and probabilistic approaches. The study highlights the fragmentation in evaluating these methods, pointing out the need for standardized metrics to assess their effectiveness and trustworthiness.

### 8. Beyond Trial-and-Error: Agentic Optimization for Image-to-Video Adherence
**Authors:** Aman Tyagi, Hemanth Boinpally, Jonathan Chen, Douglas Gebert, Steven Hickson
**Link:** https://arxiv.org/abs/2608.12290v1
**Summary:** The paper addresses the challenge of inconsistent and unpredictable outputs in black-box Image-to-Video models, which often require tedious trial-and-error for fine-tuning. It introduces the "Agentic Self-Improvement" framework, which optimizes video generation through a two-stage process involving prompt refinement via a multimodal language model and Bayesian optimization of parameters. The approach significantly enhances the quality and reliability of generated videos, showing a strong preference for its outputs over traditional methods in preference studies.

### 9. Large Language Model-Driven Small-Capitalization Trading: Integrating Financial News Sentiment, Macroeconomic Indicators, and Technical Signals
**Authors:** Alireza Kargarzadeh, Nariman Khaledian, Navid Parvini, Arman Khaledian
**Link:** https://arxiv.org/abs/2608.12283v1
**Summary:** This paper investigates how large language models can enhance small-cap stock trading by integrating sentiment from financial news, macroeconomic indicators, and technical signals. The authors developed a portfolio construction method that considers predicted risks and separates influences from company-specific and macroeconomic factors. Key findings show that focusing on distinct signals often yields better performance, with a notable performance peak found in a strategy utilizing pure macro signals over a 40-day horizon, achieving a high Sharpe ratio.

### 10. VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use Policies
**Authors:** Ankita Rajaram Naik, Anupama Murthi, Benjamin Elder, Siyu Huo, Raavi Gupta, Abhinav Jain, Praveen Venkateswaran, Abdulhamid Adebayo, Danish Contractor
**Link:** https://arxiv.org/abs/2608.12282v1
**Summary:** The paper presents VAKRA, a benchmark designed to evaluate the reasoning abilities of agents in enterprise settings when interacting with APIs and document collections. It includes over 8,000 executable APIs and assesses agents across varying levels of complexity, revealing that even advanced models struggle significantly, achieving only about 70% accuracy on simple tasks and dropping to as low as 2.4% on unanswerable queries with complex reasoning under policy constraints. The findings highlight specific weaknesses in language-mediated reasoning and cross-source grounding, suggesting areas for future improvement in AI tool-use capabilities.
