---
## 2026-07-18

### 1. teLLMe Why (Ain't Nothing but a Jam): Exploratory Causal Analysis of Urban Driving Data
**Authors:** Qiwei Li, Jorge Ortiz
**Link:** https://arxiv.org/abs/2607.15254v1
**Summary:** The paper presents teLLMe, a system aimed at helping traffic agencies explore causal relationships within large urban driving datasets derived from video, enabling them to answer questions about factors like weather's impact on traffic density. It utilizes a combination of causal structure learning techniques and natural language processing to translate user queries into structured causal analyses. The key contribution is the creation of a "Causal Card" that summarizes the effects and assumptions of these analyses, providing insights while clearly communicating uncertainty and supporting expert reasoning rather than definitive conclusions.

### 2. Bridge Evidence: Static Retrieval Utility Does Not Predict Causal Utility in Multi-Step Agentic Search
**Authors:** Debayan Mukhopadhyay, Utshab Kumar Ghosh, Shubham Chatterjee
**Link:** https://arxiv.org/abs/2607.15253v1
**Summary:** This paper addresses the disconnect between traditional measures of document usefulness in retrieval systems and their actual utility in dynamic, multi-step search scenarios where language models operate as agents. The authors introduce the Counterfactual Trajectory Utility (CTU) score to evaluate the impact of each document on the agent's performance across multiple queries, revealing that approximately one-third of the documents, termed "bridge documents," are crucial for facilitating better future queries despite appearing irrelevant in static assessments. Their findings demonstrate that static relevance and causal usefulness are fundamentally different, suggesting a need to rethink evaluation methodologies for retrieval systems operating in agentic contexts.

### 3. AutoSynthesis: An agentic system for automated meta-analysis
**Authors:** Moein Taherinezhad, Sebastian Maier, Gerardo Vitagliano, Francesco Pierri, Stefan Feuerriegel
**Link:** https://arxiv.org/abs/2607.15247v1
**Summary:** AutoSynthesis addresses the challenge of scaling quantitative evidence synthesis, which is typically a manual and labor-intensive process necessary for fields like science and medicine. It is an automated system that uses multiple agents to conduct meta-analyses by retrieving literature, screening studies, and computing effect sizes, producing results comparable to those from expert analyses. The key contribution of this work is that AutoSynthesis enhances the efficiency and scalability of evidence synthesis, supporting better evidence-based decision-making across various disciplines.

### 4. Mutable Low-Rank Sketches for Retrain-Free Recommendation
**Authors:** Hector J. Garcia, Nick Clayton
**Link:** https://arxiv.org/abs/2607.15242v1
**Summary:** The paper addresses the issue of embedding staleness in recommendation systems, where user preferences are not updated until the next model retraining occurs. It introduces mutable sketches that utilize a KP-tree structure to dynamically update user embeddings in real-time as new ratings are received. The key contribution is that this approach achieves superior recommendation accuracy (lower RMSE) and significantly faster updates compared to traditional methods, enabling near-instant personalized suggestions for new users without the need for retraining the model.

### 5. Beyond the Leaderboard: Design Lessons for Trustworthy Multimodal VQA
**Authors:** Sushant Gautam, Vajira Thambawita, Michael A. Riegler, Pål Halvorsen, Steven A. Hicks
**Link:** https://arxiv.org/abs/2607.15241v1
**Summary:** The paper addresses the challenge of creating trustworthy multimodal AI systems for healthcare, specifically for visual question answering (VQA) in gastrointestinal endoscopy. By analyzing various design approaches from existing systems, the researchers found that while pretrained models perform well, methods that emphasize structured reasoning and clear evidence linkage lead to more reliable results. This study highlights the need for improved evaluation metrics and frameworks that prioritize both explainability and robustness in healthcare AI.

### 6. TikStance: A Multimodal and Hierarchical Dataset for Multi-target Stance Analysis in TikTok Political Conversations
**Authors:** Yazhi Zhang, Fuqiang Niu, Bowen Zhang
**Link:** https://arxiv.org/abs/2607.15240v1
**Summary:** The paper introduces TikStance, a new dataset designed to enable the analysis of political stances in TikTok videos, addressing the challenge of limited data that captures both video content and hierarchically structured comments. It comprises 161 videos and nearly 14,000 comments related to key political figures in the upcoming U.S. election, with well-documented human annotations for stance detection. A significant finding is that nested replies make up over 23% of comments, revealing complexities in political discourse that the dataset aims to facilitate further research into.

### 7. Language Identification via Compositional Data Analysis: A Linear-Time Classifier Based on Log-Ratio Geometry
**Authors:** Paul-Andrei Pogăcean, Sanda-Maria Avram
**Link:** https://arxiv.org/abs/2607.15238v1
**Summary:** This paper addresses the problem of language identification, traditionally dominated by resource-intensive neural networks or less effective statistical methods. The authors propose a new approach that represents character and bigram frequencies as compositional vectors transformed with log-ratio geometry, allowing for efficient and robust classification. Their method demonstrates strong accuracy, especially with longer text sequences, providing a fast and interpretable solution for language identification tasks.

### 8. In-Place Tokenizer Expansion for Pre-trained LLMs
**Authors:** Jimmy T. H. Smith, Tarek Dakhran, Alberto Cabrera, Simon S. Lee, Paul Pak, Aditya Tadimeti, Tim Seyde, Maxime Labonne, Alexander Amini, Mathias Lechner
**Link:** https://arxiv.org/abs/2607.15232v1
**Summary:** The paper addresses the inefficiencies of fixed tokenizers in pre-trained language models, particularly when accommodating newly prioritized languages that lead to increased token fragmentation. It proposes an in-place tokenizer expansion method that builds upon the existing tokenizer's merges, allowing for a more efficient and compact vocabulary without losing prior information. The key outcome is a substantial reduction in token count and an estimated 2.2 to 3.7 times speedup in decoding for Hindi and Vietnamese, which enhances performance while releasing updated model weights and tokenizer.

### 9. Data Driven Block Replacement Scheduling
**Authors:** Aniruddhan Ganesaraman, VIdyadhar Kulkarni
**Link:** https://arxiv.org/abs/2607.15229v1
**Summary:** The paper addresses the challenge of optimizing the interval for replacing machines under a block replacement policy, where machines are replaced upon failure and periodically as a group. The authors develop data-driven algorithms based on multi-armed bandit techniques to dynamically learn the cost-minimizing replacement interval while handling incomplete lifetime data. Key contributions include establishing a regret bound that matches theoretical limits and demonstrating that their approach can estimate lifetime distributions effectively, leading to optimized replacement strategies that outperform traditional methods.

### 10. When Words Are Safe But Actions Kill: Probing Physical Danger Beyond Text Safety in Hidden-State Risk Space
**Authors:** Weimeng Wang, Ziqiang Wang, Zihang Zhan, Chuanpu Fu, Qi Li, Ke Xu
**Link:** https://arxiv.org/abs/2607.15218v1
**Summary:** The paper addresses the issue of distinguishing between the safety of language used in instructions and the physical dangers that may arise when these instructions are acted upon in the real world. The authors propose a method called PRISM that uses logistic regression to analyze hidden states in large language models, achieving high accuracy in detecting physical risks without relying on explicit harmful keywords. Key findings indicate that PRISM significantly outperforms standard language model evaluations in recognizing physical dangers, demonstrating its effectiveness in enhancing safety in embodied AI applications.
