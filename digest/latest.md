---
## 2026-08-07

### 1. Learning When to Trust via Selective Context Preference Optimization
**Authors:** Xian Sun, Wei Chow, Yingshuo Wang, Junhao Liu, Wei Gao, Qing Wu, Lingdong Kong
**Link:** https://arxiv.org/abs/2608.06377v1
**Summary:** The paper addresses the challenge of language models being misled by external context signals, which can cause correct answers to become wrong. The authors introduce a benchmark called MIST to evaluate how models respond to different types of context, and propose a method called SCOPE that optimizes model performance by focusing on preference pairs across varied contexts. The key contribution is a significant reduction in susceptibility to misleading signals while maintaining accuracy with valid context, highlighting the importance of selective trust in model evaluation.

### 2. The Bitter Lesson of Tool Calling
**Authors:** Ishan Patel, Sahil Sen, Elias Lumer, Vamse Kumar Subbiah
**Link:** https://arxiv.org/abs/2608.06370v1
**Summary:** The paper addresses the challenge of improving how language models use tools to perform tasks beyond their training data, particularly through a method called programmatic tool calling (PTC), which allows models to interact with tools using typed Python scripts instead of rigid JSON commands. By comparing PTC to traditional JSON tool calling across 14 language models, the authors found that PTC performs as well or better in most cases, with notable improvements in efficiency and stability, particularly with the latest model generation. This establishes PTC as a robust alternative for enhancing the capabilities of code-capable language models in real-world applications.

### 3. Tracing the Heart: An Evidence-Linked Pipeline for Heart-Failure Feature Engineering
**Authors:** Soorya Ram Shimgekar, Michelle Hu, Dorisa Shehi, Daniel Kang, Roy Ka-Wei Lee, Koustuv Saha, Christian Poellabauer, Christopher Lee, Sajeev Singh, Piyum Zonooz, Navin Kumar, Zeeshan Ahmed, Priyadarshini Kachroo
**Link:** https://arxiv.org/abs/2608.06366v1
**Summary:** The paper addresses the challenge of feature engineering in heart failure research, which is time-consuming and often relies on fragmented electronic health record (EHR) data. The authors developed the Nimblemind Multi-Agent System (nMAS), an automated pipeline that creates structured features from EHR data while maintaining evidence traceability. Their approach significantly improved predictive performance for heart failure phenotyping, demonstrating the potential for automated and auditable feature engineering in this clinical area, although further validation is needed beyond a single institution.

### 4. Investigating Artificial Intelligence Digital Sovereignty in Mobile Shopping Apps: A Case Study of Nigeria
**Authors:** George Grispos, Sajda Qureshi
**Link:** https://arxiv.org/abs/2608.06364v1
**Summary:** This study investigates the impact of Artificial Intelligence in mobile shopping apps on digital sovereignty in Nigeria, focusing on how transparent these platforms are about their AI features. By analyzing selected Android applications and relevant documents, the researchers found that while AI is widely used in these apps, there is a significant lack of transparency regarding their operation. The research highlights the challenges users face in maintaining control over their digital interactions in an increasingly AI-driven marketplace.

### 5. An Optimal Agnostic PAC Algorithm
**Authors:** Markus Engelund Mathiasen, Jian Qian, Nikita Zhivotovskiy
**Link:** https://arxiv.org/abs/2608.06363v1
**Summary:** The paper addresses the problem of agnostic PAC learning, which involves minimizing the binary risk associated with a hypothesis class of finite VC dimension. The authors present an algorithm that achieves the statistically optimal risk bound for a learner based on an i.i.d. sample. Their key contribution is the establishment of a sample complexity result that aligns with existing lower bounds, proving the algorithm's effectiveness in achieving optimal performance across varying scenarios of risk.

### 6. AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping in Imperfect-Information Games
**Authors:** Boning Li, Yu Chen, Longbo Huang
**Link:** https://arxiv.org/abs/2608.06362v1
**Summary:** The paper addresses the challenge of efficiently evaluating agent performance in imperfect-information games, where the number of games required to differentiate skill from luck is unpredictable. The authors introduce the anytime-valid AIVAT (AV-AIVAT), which combines advanced variance-reduction techniques with continuously monitored confidence sequences to allow for early stopping in evaluations while maintaining statistical validity. Key results show that AV-AIVAT can significantly reduce the number of games needed, achieving a median reduction of 74 times compared to traditional methods, thereby providing an efficient and auditable evaluation process.

### 7. The Low Frequency Trap: Video Language Models Fail at Simple Event Bookkeeping
**Authors:** Sarvesh Baskar, Zikui Cai, Shayan Shabihi, Anirudh Satheesh, Muhammad R. Islam, Udari Madhushani Sehwag, Tom Goldstein, Furong Huang
**Link:** https://arxiv.org/abs/2608.06361v1
**Summary:** The paper addresses the issue of video language models struggling to accurately count and represent events, particularly when events occur frequently or are transient. To tackle this, the authors introduced a new method called trace-grounded parametric profiling, which evaluates models using controlled tasks and executable event traces. The key finding is that while certain models can reliably count persistent events, they perform poorly with transient events, and increasing the sampling rate or changing prompting strategies does not significantly improve accuracy, highlighting the limitations of these systems in capturing temporal dynamics.

### 8. Resourced Authority A Mechanism-Design Model for Participatory Governance of Deployed AI Agents
**Authors:** Praphul Chandra, Sujit Gujar, Ganesh Ghalme
**Link:** https://arxiv.org/abs/2608.06353v1
**Summary:** The paper presents a formal model for the participatory governance of deployed AI agents, focusing on how resource allocation can enforce control over these agents. By introducing a governance mechanism that allows verified human stakeholders to contribute to decision-making through a unique governance currency, the authors aim to ensure safe AI operation by managing compute budgets. A key contribution is the identification of challenges related to potential manipulation by the AI agents of the governing process, which remains an open issue in the field.

### 9. CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks
**Authors:** Fanzhe Meng, Guoxin Chen, Jiale Zhao, Shuang Sun, Zhiyu Lin, Wayne Xin Zhao, Ruihua Song, Ji-Rong Wen, Kai Jia
**Link:** https://arxiv.org/abs/2608.06352v1
**Summary:** The paper addresses the challenge of creating effective training tasks for terminal agents that are not only solvable but also appropriately challenging for learning. The authors introduce CalibForge, a system that synthesizes tasks by utilizing verified solver behaviors to calibrate candidates through two innovative strategies. Key results show that the calibrated tasks significantly improve model performance across multiple benchmarks, demonstrating the effectiveness of solver-relative task design for agent training.

### 10. Challenges in Evaluating Explanation Methods for Static and Evolving Data
**Authors:** Jerzy Stefanowski
**Link:** https://arxiv.org/abs/2608.06351v1
**Summary:** The paper addresses the inadequate evaluation of Explainable AI (XAI) methods, focusing on the DetoxAI system for bias detection and concept unlearning in image recognition. It presents a human-centered evaluation of explanation methods and discusses strategies for adapting these explanations to evolving data streams with concept drift, particularly through the use of counterfactuals. The key contribution is highlighting the need for better tracking of the co-evolution of data, models, and explanations in XAI.
