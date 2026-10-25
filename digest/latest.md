---
## 2026-10-25

### 1. Beyond Best-of-$k$: Prior-Consistent DAPS for Ambiguous Nonlinear Inverse Problems
**Authors:** Merve Kocabas, Benjamin A. Burns, Andreas Geiger, Kent Gauen, Sara Fridovich-Keil
**Link:** https://arxiv.org/abs/2610.31592v1
**Summary:** The paper addresses the challenge of solving ambiguous nonlinear inverse problems, such as phase retrieval, where multiple solutions are measurement-consistent but differ based on prior knowledge. The authors present a new method called Prior-Consistent DAPS (PC-DAPS), which improves sampling by maintaining multiple candidate solutions and selectively pruning them based on how well they align with the prior, without needing ground-truth comparisons. The key finding is that PC-DAPS reduces the likelihood of generating prior-inconsistent samples, leading to better sample quality in nonlinear inverse problems while still performing well on linear ones.

### 2. VERA: A Responsible AI Dashboard for Assessing LLM Deployments in Light of the EU AI Act
**Authors:** Robin Quériaux, Solveig Bachellery, Léa Déléris, Saurabhsingh Rajput, Mariam Barry, Tushar Sharma, Jérôme Lebecq
**Link:** https://arxiv.org/abs/2610.31588v1
**Summary:** The paper presents VERA, an open-source dashboard designed to streamline the assessment of large language model (LLM) deployments in compliance with the EU AI Act, which requires evidence of responsible AI practices. By allowing non-engineering staff to easily evaluate models against specific benchmarks and track their environmental impact, VERA significantly reduces the assessment time from 56 seconds to 30 seconds on average. The dashboard received a high usefulness rating of 4.36 out of 5 from users, and both the dashboard and the study materials are publicly available for broader use.

### 3. Would an LLM Match into a Residency? Uncertainty, Reasoning and Image Use of Open Language Models on the Spanish MIR Examination
**Authors:** Miguel Fernandez-de-Retana, Unai Zulaika, Ruben Sanchez-Corcuera, Aritz Bilbao-Jayo, Aitor Almeida
**Link:** https://arxiv.org/abs/2610.31586v1
**Summary:** The paper investigates how well open language models perform on the Spanish MIR medical residency exam by assessing their accuracy, confidence in responses, and reasoning abilities. Four models with varying parameters were tested on 1,552 questions, revealing that while they scored competitively, their confidence levels did not correlate well with accuracy, and they often made clinically unsound decisions. Additionally, fine-tuning the models improved their confidence but reduced overall accuracy, and image context provided during the exam did not significantly affect their performance.

### 4. Action Learning for Scientific Simulations
**Authors:** Sarah Liaw, Yuanqi Du, Yilun Du
**Link:** https://arxiv.org/abs/2610.31585v1
**Summary:** The paper addresses the challenge of understanding and controlling the evolution of dynamical systems by focusing on how to effectively learn from trajectory observations. The authors introduce a method called LEAP, which retrieves a stochastic action by comparing observed trajectories to a reference process, allowing for the capture of complex time-dependent relationships. The key contribution is that this approach enables robust scientific inference and control by providing a flexible, reusable framework for optimizing and ranking trajectories across various stochastic systems.

### 5. Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse of Trust Calibration
**Authors:** Deepthika S, Pawni Yadav, B. Sankar
**Link:** https://arxiv.org/abs/2610.31579v1
**Summary:** This study investigates whether users of confident, assertive large language models (LLMs) like GPT-5-mini are prone to adopt incorrect information provided by the model. Through an experimental setup, participants were exposed to various versions of the model, some containing factual inaccuracies, and their responses were analyzed in quizzes. The results showed that users frequently accepted false information as correct, highlighting a dangerous collapse in trust calibration, where confidence in the model did not correspond to factual accuracy, indicating the need for improved transparency in human-AI interactions.

### 6. What Makes a Good Unmasking Policy? A Controlled Study of Learned Unmasking in Diffusion Language Models
**Authors:** Jinya Sakurai, Xun Xu, Jaehong Yoon
**Link:** https://arxiv.org/abs/2610.31576v1
**Summary:** The paper addresses the challenge of improving the efficiency of masked diffusion language models by optimizing unmasking policies, which determine which predictions can be confidently committed. The authors develop a trajectory-contraction approach that leverages model confidence and hidden states, resulting in a more effective policy that reduces the number of function evaluations needed for accurate outputs. Their best-performing 856K-parameter policy significantly enhances throughput and accuracy across various benchmarks, demonstrating superior performance compared to existing methods.

### 7. Rethinking Sequence Compression with Test-time Regression
**Authors:** Sihan Yang, Jie Huang, Hanxuan Li, Yifan Guo, Weigao Sun, Yiran Zhong, Weiyang Liu
**Link:** https://arxiv.org/abs/2610.31574v1
**Summary:** The paper addresses the inefficiency of current sequence compression techniques in language and multimodal models. It introduces TTR-Compressor, which uses a novel test-time regression approach to compute compressed representations of input tokens efficiently. The results show significant performance improvements, with TTR-Compressor enhancing model capabilities while reducing the number of visual tokens needed for processing.

### 8. Social-HUMINT: An LLM-Augmented Unified Framework for Measuring Social Media Exposure
**Authors:** Pellegrino Casoria, Simon Pietro Romano
**Link:** https://arxiv.org/abs/2610.31573v1
**Summary:** The paper addresses the issue of assessing the risk of social engineering attacks based on social media profiling, highlighting how easily user attributes can be inferred from their online presence. It introduces a unified framework that combines Social Media Intelligence (SOCMINT) and Cyber Human Intelligence (Cyber-HUMINT) to quantify user exposure and susceptibility through a multi-agent pipeline enhanced by Large Language Models (LLMs). The key contribution is a validated taxonomy of capabilities that significantly improves the accuracy of user profiling and susceptibility assessments, enabling defenders to better understand their vulnerabilities before attackers do.

### 9. On the Token Collapse Phenomenon in Textual Graph Soft Prompting
**Authors:** Andrea Giuseppe Di Francesco, Rishabh Jain, Franco Maria Nardini, Nicola Tonellotto, Pietro Liò, Fabrizio Silvestri
**Link:** https://arxiv.org/abs/2610.31572v1
**Summary:** The paper investigates the issue of "token collapse" in graph soft prompting for language models, where graph-specific tokens become nearly indistinguishable across different inputs, undermining their intended purpose of conveying relational information. The authors analyze the G-Retriever method and find that it often performs poorly, suggesting that learned tokens act more like generic prompts rather than effectively using graph data. They propose a two-stage procedure to produce non-collapsed tokens while maintaining performance, emphasizing the need for better evaluation of graph-token alignment in prompts beyond just accuracy metrics.

### 10. When to Follow the Teacher: Advantage-Based On-Policy Distillation
**Authors:** Mahdi Sabbaghi, George Pappas, Hamed Hassani, Adel Javanmard
**Link:** https://arxiv.org/abs/2610.31563v1
**Summary:** The paper addresses the problem of inefficient teacher-student relationships in Online Policy Distillation (OPD), where students are trained to follow teachers at all times, even when it may not be beneficial. The authors propose Advantage-Based On-Policy Distillation (AOPD), which selectively reinforces teacher actions based on their expected advantages for the student, using a novel estimator that requires no additional rollouts. This approach improves the effectiveness of the distillation process, demonstrating superior performance in various tasks compared to traditional methods.
