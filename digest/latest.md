---
## 2026-06-26

### 1. DanceOPD: On-Policy Generative Field Distillation
**Authors:** Wei Zhou, Xiongwei Zhu, Zelin Xu, Bo Dong, Lixue Gong, Yongyuan Liang, Meng Chu, Leigang Qu, Lingdong Kong, Wei Liu, Tat-Seng Chua
**Link:** https://arxiv.org/abs/2606.27377v1
**Summary:** The paper addresses the challenge of integrating diverse image generation capabilities, such as text-to-image and various editing functions, which often conflict and degrade performance. The authors propose DanceOPD, a framework that utilizes on-policy generative field distillation, allowing a model to selectively learn from different capability fields while maintaining high-quality outputs. The key contribution is showing that this approach enhances the model's ability to compose multiple capabilities effectively without sacrificing overall image generation quality.

### 2. Reinforcement Learning without Ground-Truth Solutions can Improve LLMs
**Authors:** Yingyu Lin, Qiyue Gao, Nikki Lijing Kuang, Xunpeng Huang, Kun Zhou, Tongtong Liang, Zhewei Yao, Yi-An Ma, Yuxiong He
**Link:** https://arxiv.org/abs/2606.27369v1
**Summary:** The paper addresses the limitation of reinforcement learning methods for training language models (LLMs) that rely on ground-truth solutions, which are often unavailable in practice. It introduces a new framework called RiVER that utilizes deterministic feedback with calibrated rewards based on relative scoring, allowing LLMs to improve their performance on coding tasks without needing explicit correct answers. The key finding is that RiVER significantly enhances the models' performance, achieving up to a 9.4% increase in ranking on benchmark coding tasks while also improving performance on exact-solution tests, showcasing the effectiveness of score-based training without ground-truth solutions.

### 3. Autoregressive Boltzmann Generators
**Authors:** Danyal Rehman, Charlie B. Tan, Yoshua Bengio, Avishek Joey Bose, Alexander Tong
**Link:** https://arxiv.org/abs/2606.27361v1
**Summary:** The paper addresses the challenge of efficiently sampling molecular systems at thermodynamic equilibrium, which is crucial in statistical physics. It introduces Autoregressive Boltzmann Generators (ArBG), a new framework that enhances scalability and efficiency by moving away from traditional flow-based methods. The key result is the development of a 132 million parameter model, Robin, which significantly improves sampling accuracy compared to previous models, achieving over a 60% reduction in energy error for 8-residue peptide systems.

### 4. When are likely answers right? On Sequence Probability and Correctness in LLMs
**Authors:** Johannes Zenn, Jonas Geiping
**Link:** https://arxiv.org/abs/2606.27359v1
**Summary:** The paper investigates the connection between sequence probability—how likely a language model predicts a sequence to be—and the correctness of its outputs, focusing on how this relationship varies across different decoding methods, hyperparameters, and prompts. Through extensive analysis, the authors find that while higher sequence probability often correlates with correctness in a dataset, tweaking decoding strategies doesn't consistently enhance accuracy, and probability alone is unreliable for evaluating responses to the same prompt. These insights offer practical guidance for improving language model outputs.

### 5. Error-Conditioned Neural Solvers
**Authors:** Haina Jiang, Liam Wang, Peng-Chen Chen, Min Seop Kwak, Seungryong Kim, Brian Bell, Jeong Joon Park
**Link:** https://arxiv.org/abs/2606.27354v1
**Summary:** The paper addresses the challenge of neural surrogate models for solving partial differential equations (PDEs), which often struggle to correct their own errors and perform poorly outside their training conditions. The authors propose an innovative approach called error-conditioned Neural Solvers (ENS), which uses the residuals of the PDE as direct input to the model, allowing it to learn how to adjust its predictions iteratively. This method significantly improves prediction accuracy, especially in complex scenarios like turbulent flow, achieving up to ten times better performance compared to traditional hybrid methods while avoiding their computational drawbacks.

### 6. Mapping Political-Elite Networks in Europe with a Multilingual Joint Entity-Relation Extraction Pipeline
**Authors:** Kirill Solovev, Jana Lasser
**Link:** https://arxiv.org/abs/2606.27347v1
**Summary:** The paper addresses the challenge of mapping complex political elite networks in Europe, which are often hidden and difficult to analyze due to their informal nature. The authors propose an open-source, multilingual pipeline that combines named-entity recognition with a sophisticated linking and relationship extraction model to build structured knowledge graphs from large amounts of news data. Their approach demonstrates high accuracy in extracting relationships and successfully applies this method to analyze political dynamics in Austria and Poland, showcasing its potential for empirical research in comparative politics.

### 7. Understanding Domain-Aware Distribution Alignment in Budgeted Entity Matching
**Authors:** Nicholas Pulsone, Gregory Goren, Roee Shraga
**Link:** https://arxiv.org/abs/2606.27342v1
**Summary:** The paper addresses the challenge of Entity Matching (EM), where the goal is to determine if records from different sources refer to the same real-world entity, especially in low-resource settings. It evaluates the performance of a state-of-the-art method called BEACON, focusing on how various factors like data availability influence its effectiveness in domain-aware EM tasks. The study reveals important insights into the importance of distribution alignment and the decision-making process within the BEACON framework.

### 8. Language-Based Digital Twins for Elderly Cognitive Assistance
**Authors:** Mohammad Mehdi Hosseini, Mohammad H. Mahoor, Hiroko H. Dodge
**Link:** https://arxiv.org/abs/2606.27334v1
**Summary:** This paper addresses the challenge of early detection of Mild Cognitive Impairment (MCI) in the elderly by creating a language-based digital twin framework that uses large language models to mimic seniors' conversational behavior. The authors developed a conditional variational autoencoder to evaluate how well this digital twin replicates individual speech patterns and predicts cognitive health scores. Their findings demonstrate that this approach effectively maintains personal identity traits and achieves performance on par with real data, showcasing its potential for ongoing cognitive health monitoring.

### 9. Empowering GUI Agents via Autonomous Experience Exploration and Hindsight Experience Utilization for Task Planning
**Authors:** Tianyi Men, Zhuoran Jin, Pengfei Cao, Yubo Chen, Kang Liu, Jun Zhao
**Link:** https://arxiv.org/abs/2606.27330v1
**Summary:** The paper addresses the challenge of enhancing the task planning capabilities of small multimodal language models (MLLMs) in performing GUI tasks, which typically struggle with comprehension and cross-website generalization. The authors introduce a method called Planning Experience Exploration and Utilization (PEEU), which autonomously explores tasks to build a library of experiences and cleverly uses this hindsight to generate high-quality training data. Key results show that their approach significantly improves performance, with their 7B model achieving 30.6% accuracy, surpassing the larger 32B model, indicating the importance of leveraging experience for better out-of-distribution planning abilities.

### 10. Hallucination in World Models is Predictable and Preventable
**Authors:** Nicklas Hansen, Xiaolong Wang
**Link:** https://arxiv.org/abs/2606.27326v1
**Summary:** The paper addresses the problem of hallucination in generative world models, where simulated rollouts become visually fluent but deviate from reality, particularly in areas of low data coverage. The authors introduce a new dataset, MMBench2, and identify three types of hallucinations while developing predictive signals to detect and mitigate these issues. Their key contribution is a novel approach that uses coverage-aware sampling and curiosity-driven data collection, enabling models to efficiently adapt to new environments with minimal real-world data.
