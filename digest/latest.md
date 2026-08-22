---
## 2026-08-22

### 1. MidTool: Mid-training Data Synthesis for Agentic Tool Use
**Authors:** Fengqing Jiang, Yite Wang, Boyi Liu, Zhaoyang Wang, Canwen Xu, Zhewei Yao, Radha Poovendran, Yuxiong He
**Link:** https://arxiv.org/abs/2608.20314v1
**Summary:** The paper addresses the challenge of improving large language models' ability to effectively use tools by introducing MidTool, a data synthesis pipeline that enhances mid-training with diverse data sources and supervision from real-world tool APIs. By mid-training the Qwen3 models using the MidTool framework, the authors demonstrate notable improvements in the models' performance on various benchmarks, indicating that targeted mid-training can be crucial for developing general tool-use capabilities in language models.

### 2. Physical-Support Confidence Sets for Highly Coherent Dictionaries
**Authors:** Guan-Ju Peng
**Link:** https://arxiv.org/abs/2608.20295v1
**Summary:** The paper addresses the challenge of accurately identifying physical support in highly coherent dictionary learning, where different dictionaries might interpret the same data differently. The authors propose a novel method called resolution-aware physical-support inference, which considers uncertainties in both the learned dictionary and the deployment signal to project explanations onto a physical support space. Their key contribution is the introduction of active endpoint bracketing (AEB), a computational technique that selectively evaluates candidate solutions, leading to improved physical localization with fewer evaluations compared to traditional methods.

### 3. Phantom Gains: Auditing Self-Improvement Against a Measured Null
**Authors:** Cheng Xu, Nan Yan, Liming Chen, M-Tahar Kechadi
**Link:** https://arxiv.org/abs/2608.20290v1
**Summary:** The paper addresses the challenge of accurately auditing improvements in language models by examining the transition in solving individual problems, rather than just overall accuracy. Through a series of controlled experiments comparing self-training methods against a frozen model, the authors identify measurement failures that can misrepresent model performance. They propose a new auditing approach that relies on a per-problem null hypothesis derived from existing data, revealing that external distillation enhances problem-solving abilities, while self-training does not consistently yield positive results.

### 4. Dynamic Structural Causal Modeling for Sleep
**Authors:** Ranveer Singh, Saurabh Mathur, Pranuthi Tenali, Arun Badi, Sriraam Natarajan
**Link:** https://arxiv.org/abs/2608.20285v1
**Summary:** The study addresses the complex causal dynamics of sleep-disordered breathing, which vary among different patient groups, making it difficult to create targeted treatments. By analyzing Home Sleep Apnea Test recordings using the PCMCI+ algorithm and incorporating domain knowledge, the researchers constructed dynamic causal graphs that reveal systematic differences in causal relationships based on sex and age. Key findings indicate that while certain relationships remain consistent across all patient cohorts, others show significant variation, highlighting the need for tailored interventions.

### 5. Inject, Align, Recover: Staged Post-Training for Retrieval-Free Document Knowledge Internalization
**Authors:** Qian Kou, Xiaofeng Shi, Xiaosong Qiu, Hua Zhou
**Link:** https://arxiv.org/abs/2608.20281v1
**Summary:** The paper addresses the issue of large language models struggling to answer questions when the relevant documents are not retrieved during inference, a challenge known as document knowledge internalization. The proposed solution, IAR (Inject, Align, and Recover), is a three-stage post-training framework that effectively transforms a fixed corpus into usable knowledge for question answering without retrieval. Key results demonstrate that IAR significantly enhances both domain-specific and general performance across various model families and benchmarks, achieving better accuracies in retrieval-free document internalization compared to conventional methods.

### 6. Which Eviction Policy Should an LLM Cache Use? A Systematic Study Across Workloads, Capacities, and Encoders
**Authors:** Yash Kulkarni, Shubham Harkare, Arvind Suresh Yogesh Babu
**Link:** https://arxiv.org/abs/2608.20280v1
**Summary:** The paper investigates which eviction policy is most effective for caching responses from large language models (LLMs) under different workloads and settings. The authors systematically evaluate several eviction strategies, including LFU, FIFO, and others, using a tool called CLEVER, but find that LFU consistently outperforms other policies by a small margin across various conditions. A significant finding is that many cached responses are not answer-substitutable, suggesting that cache effectiveness is hindered by the quality of hits rather than simply the eviction mechanism used.

### 7. Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents
**Authors:** Yiyang Feng, Biddut Sarker Bijoy, Niranjan Balasubramanian, Jiawei Zhou
**Link:** https://arxiv.org/abs/2608.20274v1
**Summary:** The paper investigates how skills learned by Large Language Model (LLM) agents can be effectively transferred across different tasks. It compares two approaches to skill induction: using larger tasks versus breaking them down into subtasks, as well as using text versus code formats. The key finding is that skills induced from subtasks generally perform better and that a new "skill utility score," which combines two properties of skills, can predict their success during transfer, thus providing a useful diagnostic tool.

### 8. Catching the Rug: Early Prediction of Fraudulent Memecoins on Solana via Machine Learning
**Authors:** Jianghai Li, Pavel Kuznetsov, Yury Yanovich, Konstantin Nott-Whaley, Igor Vodolazov
**Link:** https://arxiv.org/abs/2608.20271v1
**Summary:** This paper addresses the growing risk of fraudulent memecoins, specifically rug pulls, on the Solana blockchain by developing a machine learning framework for early detection. Through analyzing a dataset of 6.4 million tokens, the researchers found that traditional models, like Gradient Boosting (XGBoost), can accurately identify potential rug pulls using just the first 5 minutes of trading data. The study contributes to better understanding and mitigating DeFi fraud on Solana, aiming to protect investors from risky assets.

### 9. DICS: Data-Informed Centroid Splitting for Decision Tree Classifiers
**Authors:** MD Saifur Rahman Mazumder, Feng Yu
**Link:** https://arxiv.org/abs/2608.20258v1
**Summary:** The paper addresses the challenge of high computational costs in training decision tree classifiers, particularly for large and complex datasets. It introduces a clustering-based method called Data-Informed Centroid Splitting (DICS), which efficiently narrows down the candidate splits by using data-driven insights. The key contribution is that DICS maintains classification accuracy while significantly reducing training time, demonstrating its effectiveness in enhancing the performance of decision tree models.

### 10. Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation
**Authors:** Gijs Kassenaar, Zhao Yang, Vincent François-Lavet
**Link:** https://arxiv.org/abs/2608.20256v1
**Summary:** The paper addresses the inefficiency of reasoning language models that use a fixed token budget, which can lead to unnecessary computation on easier problems and insufficient computation on harder ones. The authors propose an adaptive approach where the model learns to decide its reasoning depth using three modes: NoThink, Short, or Long, leading to optimal token allocation based on problem difficulty. Key results show that this adaptive reasoning not only reduces the average response length significantly by 41% without major loss in accuracy on the MATH benchmark but also performs better on other tasks like GSM8K, achieving both higher accuracy and greater token savings.
