---
## 2026-11-03

### 1. Pixel-UMI: Learning Environment-Aware Whole-Body Manipulation from Sensorized Human Demonstrations
**Authors:** Jason Jingzhou Liu, Tony Tao, Deepak Pathak, Ruslan Salakhutdinov
**Link:** https://arxiv.org/abs/2611.03647v1
**Summary:** The paper addresses the challenge of transferring human manipulation skills to robots, taking into account differences in body structure and environment. The authors propose Pixel-UMI, a method that combines scene information and human motion to develop policies for robotic whole-body manipulation while correcting for errors and incorporating feedback from human demonstrations. Key results show that Pixel-UMI significantly enhances a robot's ability to perform complex manipulation tasks, achieving an impressive 87.0% average task progress across various scenarios.

### 2. Pixel: A Co-Designed Full-Stack Robot System for Learning General-Purpose Mobile Manipulation
**Authors:** Tony Tao, Jason Jingzhou Liu, Ruslan Salakhutdinov, Deepak Pathak
**Link:** https://arxiv.org/abs/2611.03648v1
**Summary:** The paper addresses the challenge of general-purpose mobile manipulation in robotics, which is often hindered by the independent development of various system components. The authors introduce Pixel, a fully integrated robot system that combines a humanoid robot, advanced control mechanisms, and a unified learning pipeline for efficient data collection and policy learning. Their approach successfully demonstrates the robot's ability to perform complex tasks involving dexterity, navigation, and coordination, showcasing the effectiveness of a co-designed system that aligns hardware and learning processes.

### 3. From Natural Language to Exact Cover: A Neuro-Symbolic Approach to Zebra Puzzles
**Authors:** Paulius Skaisgiris, Thomas Pammer, Veronika Semmelrock, Mykyta Ielanskyi, Maximilian Heisinger, Erich Kobler
**Link:** https://arxiv.org/abs/2611.03641v1
**Summary:** The paper addresses the limitations of Large Language Models (LLMs) in solving logical reasoning tasks, particularly in the context of Zebra puzzles, by combining neural semantic parsing with deterministic exact cover reasoning. The authors propose a neuro-symbolic framework that translates natural language puzzles into structured formats that symbolic solvers can understand, enabling accurate and efficient problem-solving. Their empirical results show that this hybrid approach significantly outperforms traditional neural methods and other recent neuro-symbolic techniques.

### 4. WebHarbor: Docking Real Websites for Evolving GUI Agent Environments
**Authors:** Zhaoyang Wang, Qianhui Wu, Boyu Gou, Demi Wang, Jiacheng Zhang, Peichun Hua, Qize Li, Shi Qiu, Yifan Jiang, Yifan Zhang, Zexu Jin, Baolin Peng, Bolin Shen, Chetan Bansal, Dehan Kong, Deren Lei, Dongshen Peng, Fengqing Jiang, Hao Cheng, Haoqing Wang, Jiaming Shan, Jicheng Wang, Jingguang Zhou, Jixuan He, Kaide Zeng, Kangyu Zhu, Lama Moukheiber, Mufan Qiu, Peng Xia, Qihan Sun, Qingwei Lin, Qiushi Sun, Ruichen Zhang, Shuqing Luo, Si Qin, Sicheng Fan, Tao Xiong, Wenlin Yao, Xinyu Zhang, Xinyue Zeng, Xuanrui Li, Xuchao Zhang, Yian Wang, Yichao Liu, Yiming Liang, Yiyang Zhou, Yizhu Jiao, Yuetai Li, Yurun Chen, Yuxuan Zhang, Zheyuan Yang, Zhiyuan Yao, Zhongyang Li, Zihao Li, Zili Wang, Jianfeng Gao, Huaxiu Yao
**Link:** https://arxiv.org/abs/2611.03634v1
**Summary:** The paper presents WebHarbor, a collection of 153 dockerized website environments designed to provide realistic and stable training and evaluation settings for GUI web agents, addressing issues like changing online content and limited access to complex tasks. By combining human input and automated coding, these environments cover a wide range of tasks, including those often overlooked by other methods. The key finding shows that a GUI agent trained in WebHarbor successfully generalizes to new tasks and performs well compared to leading open-source alternatives.

### 5. Pretraining Data Scale Reverses the Muon-AdamW Fine-Tuning Gap
**Authors:** Catherine Li, Jingchu Gai, Andrej Risteski, Jacob Mitchell Springer, Aditi Raghunathan
**Link:** https://arxiv.org/abs/2611.03633v1
**Summary:** The paper investigates the performance of two optimizers, Muon and AdamW, in training large language models, specifically focusing on their effectiveness during the fine-tuning phase after pretraining. It finds that while Muon is faster at minimizing pretraining loss, AdamW eventually outperforms Muon in fine-tuning when large amounts of pretraining data are used. The study introduces the margin-to-spread ratio as a key concept to explain this phenomenon, demonstrating how the relative performance of the two optimizers shifts with increasing data.

### 6. Not All Reasoning Generalizes: A Case Study on Learning Generalizable Reasoning Strategies in RLVR
**Authors:** Ziqi Pang, Yu-Xiong Wang
**Link:** https://arxiv.org/abs/2611.03627v1
**Summary:** This paper addresses the challenge of generalizing reasoning strategies in reinforcement learning with verifiable rewards (RLVR) when faced with out-of-distribution tasks. The authors investigate this using a framework of equation-solving, discovering that models trained under RLVR often struggle to adapt their reasoning methods to more complex scenarios, resorting to ineffective brute-force solutions. To enhance generalization, they introduce a co-training approach with bijective inversion tasks, which helps maintain effective reasoning strategies even under challenging conditions, ultimately improving accuracy and robustness in varied contexts.

### 7. FADE: Factored Ability--Difficulty Filtering for Online RLVR Scheduling
**Authors:** Tomas Duncun, Jonah Ellison, Mateo Ruiz, Hanae Fujita, Ingrid Solberg
**Link:** https://arxiv.org/abs/2611.03625v1
**Summary:** The paper addresses the challenge of efficiently scheduling prompts in group-based reinforcement learning with verifiable rewards (RLVR) by separating the ability of the policy and the difficulty of prompts. The authors propose FADE (Factored Ability--Difficulty Estimation), a bilinear state-space filtering method that dynamically updates the policy's competence across reasoning skills without affecting the intrinsic difficulty of prompts. The key contribution is that FADE enhances accuracy and calibration in results across various benchmarks while maintaining low computational overhead.

### 8. Thought-deciphering via hierarchical EEG-to-text alignment
**Authors:** Xiaopeng Mao, Morten Mørup, Xin Xu, Sang Wan Lee, Sadasivan Puthusserypady
**Link:** https://arxiv.org/abs/2611.03623v1
**Summary:** This paper addresses the challenge of enabling effective communication for individuals with disabilities by developing a brain-computer interface that decodes thoughts into text, specifically at the sentence level using EEG. The authors introduce a hierarchical alignment framework that enhances the retrieval of sentences based on EEG data and contextual information. Their key contribution is demonstrating the potential for improved sentence classification, which is crucial for better communication in non-invasive BCI systems.

### 9. D&A: Decoupling Description and Assessment Enables VLMs as Zero-Shot Robotic Reward Models
**Authors:** Marius Memmel, Shawn Yin, Urvi Rutia, Angad Wadhwa, Eldon Li, Gavin Angeloff, Ankit Goyal, Jesse Zhang, Dieter Fox, Fabio Ramos, Anqi Li, Abhishek Gupta
**Link:** https://arxiv.org/abs/2611.03622v1
**Summary:** The paper addresses the issue of confirmation bias in zero-shot video task-progress estimation for robots, where existing models often inaccurately assess progress during failed executions. The authors propose a novel method called D&A (Describe & Assess) that separates the evaluation process into two phases: first generating a clear textual description of expected success, and then assessing based on that description, thus anchoring evaluations to external criteria. This approach not only improves the accuracy of progress estimation but also outperforms existing post-training reward models, making it applicable across various tasks without requiring extensive retraining.

### 10. Strategist: Evolving Reasoning with Agents
**Authors:** Taiming Lu, Qi Xu, Zhigang Hua, Zhuang Liu
**Link:** https://arxiv.org/abs/2611.03618v1
**Summary:** The paper introduces Strategist, a system designed to evolve inference strategies for AI agents, which typically require manual coding and do not benefit from previous experiences. By utilizing a library of reusable blueprints, Strategist automatically generates, tests, and refines these strategies across various tasks. The results demonstrate that Strategist outperforms strong baseline models in terms of accuracy while substantially reducing inference costs, and its strategies can be adapted to new tasks and models without additional effort.
