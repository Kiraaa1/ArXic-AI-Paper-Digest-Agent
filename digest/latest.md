---
## 2026-09-08

### 1. What Matters, When? Diagnosing and Improving Conditional Visual Grounding in Visuomotor Imitation Policies
**Authors:** Vivek Chavan, Pengtao Xie, Yahuan Shi, Oliver Heimann, Kevin Haninger, Jörg Krüger
**Link:** https://arxiv.org/abs/2609.05376v1
**Summary:** This paper addresses the issue of visuomotor imitation policies that struggle with object selection when faced with visually similar distractors. The authors use a method called Action Chunking with Transformers (ACT) to analyze and improve the system's performance by implementing strategies like distractor augmentation and attention regularization. Their key finding is that targeted interventions significantly enhance robustness and accuracy in selecting objects or destinations, demonstrating the importance of addressing visual distractions in policy learning.

### 2. CUA-Universe: A Scalable and Dynamic Environment for Hybrid GUI+CLI Agents
**Authors:** Haoting Shi, Wenhao Wang, Weicheng Fang, Yaozhong Liang, Tian Jin, Pengxiang Zhao, Guangyi Liu, Siheng Chen, Yanfeng Wang
**Link:** https://arxiv.org/abs/2609.05374v1
**Summary:** CUA-Universe addresses the limitations of existing computer-use agents that primarily rely on graphical user interfaces (GUIs) and often execute tasks inefficiently. It presents a scalable environment that integrates both GUI and command-line interface (CLI) capabilities, enabling agents to perform tasks more effectively by coordinating visual and command-based operations. The approach resulted in a significant improvement in agent performance, with enhanced success rates and reduced interaction steps and resource usage across various benchmarks.

### 3. When LLM Decompilers Recompile More and Preserve Less
**Authors:** Chang Liu, Edward Raff, Kristopher Micinski
**Link:** https://arxiv.org/abs/2609.05370v1
**Summary:** The paper addresses the issue that LLM-based decompilers, while producing clean and compilable code, can misrepresent function behavior, potentially omitting vulnerabilities. To tackle this, the authors introduce Decompile-Diverge, a novel method that synthesizes tests to compare original and decompiled code behavior. Their findings reveal that even when decompiled code successfully recompiles and passes standard tests, it can still diverge in behavior by nearly 5% overall, highlighting the gap between recompilability and actual functional accuracy.

### 4. Design Docs Are All You Need: An AI-native Machine-Learning Performance Tool
**Authors:** Samuel Kushnir, Kimia Noorbakhsh, Kavya Sreedhar, Liqun Cheng, Ming Liu, Parthasarathy Ranganathan, Mohammad Alizadeh, Fred Kjolstad, Suvinay Subramanian
**Link:** https://arxiv.org/abs/2609.05364v1
**Summary:** The paper presents SMART, a performance modeling tool for machine learning systems that addresses the issue of ongoing technical debt and code refactoring caused by rapidly evolving models. Instead of relying on traditional code, SMART utilizes self-contained natural-language design documents to guide coding agents in generating implementations, ensuring that the framework remains robust and up-to-date. The key contribution is demonstrating that these design docs can effectively replace code as the primary artifact for co-designing ML systems, achieving precise performance reproduction comparable to hand-audited models.

### 5. Distill Globally, Adapt Locally: Reasoning Distillation and Product-Type Test-Time Training for Scalable Trade-Up Recommendation
**Authors:** Siliang Liu, Mohammad Ghasemi, Sapan Patel, Amin Banitalebi-Dehkordi
**Link:** https://arxiv.org/abs/2609.05363v1
**Summary:** The paper addresses the challenge of making scalable trade-up recommendations, which involve suggesting better alternatives for products customers are interested in. The authors propose a two-level method where a large language model (LLM) first generates structured reasoning for recommendations, which is then distilled into a lightweight classifier that efficiently handles product comparisons without additional LLM usage. This approach significantly increases speed and cost-effectiveness; the distilled model achieved a high accuracy (AUC 0.941) on test data, while being around 5,000 times faster and 10,000 times cheaper than direct LLM inference.

### 6. Who Should Grade My Work? Student Perspectives on Transparent AI-Assisted Writing Assessment in Higher Education
**Authors:** Rayed AlGhamdi
**Link:** https://arxiv.org/abs/2609.05346v1
**Summary:** The paper examines how students perceive AI-generated feedback in writing assessments within higher education, specifically focusing on their understanding of its usefulness and authority. Through a qualitative study with undergraduate computing students, it was found that while students valued AI feedback for its practical suggestions, they maintained that human instructors should remain the ultimate evaluative authority. This highlights a key distinction in students' views between the utility of feedback and the legitimacy of grading.

### 7. Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability
**Authors:** Ankit Goyal, Jaideep Ray
**Link:** https://arxiv.org/abs/2609.05339v1
**Summary:** This study investigates how well an agent's memory can be transferred when upgrading to a new model, revealing that different memory formats affect performance during migration. Researchers tested various memory storage methods, including long-context reading, retrieval-augmented generation, compressed notes, and structured knowledge graphs, using synthetic histories. The key finding is that structured knowledge graphs maintain accuracy during migration, while compressed notes suffer significant performance drops, emphasizing the importance of careful migration strategies and retaining original memory data.

### 8. Variational Continuation for Double Pendulum Periodic Orbits
**Authors:** Leo Yao, Ziming Liu, Max Tegmark
**Link:** https://arxiv.org/abs/2609.05337v1
**Summary:** This paper addresses the challenge of numerically tracking periodic orbits in dynamical systems, specifically for double pendulums. The authors introduce a Hessian-based technique that automates the computation of necessary derivatives using automatic differentiation, allowing for efficient identification of these orbits and their bifurcations. A significant contribution is the discovery of previously unreported periodic orbits where both pendulum masses never come to rest simultaneously.

### 9. The History Is the Detector: Executing CVE Patch History, End-to-End
**Authors:** Qiushi Wu, Kevin Eykholt, Youngja Park, Xiaokui Shu, Dhilung Kirat, Douglas Lee Schales, Ian Molloy
**Link:** https://arxiv.org/abs/2609.05335v1
**Summary:** The paper addresses the challenge of utilizing historical vulnerability data to identify and fix software flaws that remain undetected in existing code. The authors introduce BUGSTONE-E2E, a framework that automatically generates executable detection rules from past CVE patch histories and systematically scans software to apply these rules. Their approach successfully extracted over 1,000 detection rules from a large dataset, leading to 644 actionable findings across multiple programs, showcasing the feasibility of transforming CVE history into a practical detection and repair workflow.

### 10. Lightweight Vision Transformer Compression for On-Device Plant Disease Detection in Resource-Constrained Agricultural Field Conditions
**Authors:** Mahadev Sunil Kumar, Bhavika Gondi, Desaisetty Venkata Satya Sai Swapnith, Gangireddy Rahul Jogi, Sudheesh Manalil, Arnab Raha, Amitava Mukherjee, Parthasarathy Seethapathy, G. Gopakumar
**Link:** https://arxiv.org/abs/2609.05334v1
**Summary:** The paper addresses the challenge of deploying Vision Transformers for detecting diseases in chillies, particularly in resource-limited agricultural settings, where existing models are too large. It introduces a comprehensive compression framework combining methods like pruning, quantization, and knowledge distillation, which improves model efficiency while maintaining accuracy. The key result shows that the proposed approach can significantly reduce model size by up to 54.5 times while achieving comparable accuracy to the original model, making it feasible for on-device application in agriculture.
