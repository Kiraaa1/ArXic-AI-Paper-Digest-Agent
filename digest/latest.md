---
## 2026-10-07

### 1. QF3: Fast Flow RL with Filtered Q-Gradients
**Authors:** Chung Min Kim, Brent Yi, David McAllister, Hongsuk Choi, Himanshu Gaurav Singh, Jinkun Cao, Ken Goldberg, Pieter Abbeel, Carmelo Sferrazza, Angjoo Kanazawa
**Link:** https://arxiv.org/abs/2610.08789v1
**Summary:** The paper presents QF3, an efficient off-policy reinforcement learning algorithm designed to improve and train flow policies for robot locomotion and manipulation tasks. By leveraging filtered Q-gradients and focusing on reliable update regions, QF3 enables the training of humanoid locomotion policies from scratch and significantly accelerates the training process, achieving a 10-fold speedup compared to previous methods. This approach allows for effective learning of robotic behaviors both from scratch and through fine-tuning of pre-existing policies.

### 2. Conformal Prediction Sets Quantify Information Gain: A Theoretical Perspective
**Authors:** Kevin Zhang, Stephen Bates
**Link:** https://arxiv.org/abs/2610.08785v1
**Summary:** This paper addresses the gap in understanding how the size of conformal prediction sets relates to information gain in uncertainty quantification. The authors propose a new theoretical framework linking the size and coverage of these sets to generalized information measures, demonstrating that the reduction in set size from additional information corresponds to well-established information-theoretic principles. Their findings empirically confirm that the way set size reduction and mutual information rank features can vary, which can impact feature selection processes in classification tasks.

### 3. 4D-HOF: Hand-Object Flow Matching for Feed-Forward 4D Interaction Reconstruction
**Authors:** Shiqi Li, Sean Cho, Yijie Li, Fengzhi Guo, Bowen Wen, Cheng Zhang
**Link:** https://arxiv.org/abs/2610.08782v1
**Summary:** The paper addresses the challenge of reconstructing 4D hand-object interactions without relying on expensive optimization techniques, which can lead to unstable outcomes. The authors present 4D-HOF, a feed-forward framework that improves reconstruction by correcting errors in real-time using a model that matches estimated hand-object states to a specified interaction shape. The key result is that 4D-HOF achieves state-of-the-art performance in producing stable and accurate reconstructions, even in complex real-world scenarios.

### 4. IdeaAnchor: Teaching LLMs to Turn Literature into Research Ideas
**Authors:** Ziyu Chen, Yilun Zhao, Jiashuo Sun, Yiling Ma, Manasi Patwardhan, Arman Cohan
**Link:** https://arxiv.org/abs/2610.08781v1
**Summary:** The paper presents IdeaAnchor, a method for improving how large language models (LLMs) generate research ideas by synthesizing information from existing literature. By using structured specifications to guide the synthesis process, along with techniques like demonstration and reinforcement learning, the authors enhance the models' ability to identify gaps and propose new research directions. The results show that this approach significantly improves the quality of the generated ideas, with the combination of structured training and retrieval methods yielding the best outcomes.

### 5. DepthWorld: 3D World Model for Robot Manipulation
**Authors:** Jai Bardhan, Josef Sivic, Vladimir Petrik
**Link:** https://arxiv.org/abs/2610.08780v1
**Summary:** The paper introduces DepthWorld, a novel 3D world model for robot manipulation that addresses the limitation of existing video-based models that lack consistent 3D geometry. The authors develop a calibration pipeline that integrates learned stereo depth with a shared kinematic model, resulting in a new calibrated 3D dataset called DROID-3D. The key contribution is that DepthWorld can jointly predict RGB images and depth information, leading to improved RGB predictions and accurate metric depth for geometric reasoning—demonstrating enhanced performance over traditional RGB-only models.

### 6. Sherpa: Teaching LLMs to Teach Adaptively
**Authors:** Weixian Xu, Yanzhe Zhang, Zora Zhiruo Wang, Changyu Chen, Diyi Yang
**Link:** https://arxiv.org/abs/2610.08778v1
**Summary:** The paper introduces Sherpa, a reinforcement learning framework designed to train large language models (LLMs) to teach effectively by adapting their instruction based on individual student learning preferences. By simulating different student archetypes, Sherpa significantly enhances the teaching performance of LLMs, resulting in improved student outcomes and higher pedagogy scores. The approach demonstrates a preference for the trained teacher model over traditional LLMs in 79.6% of comparisons, suggesting it aligns more closely with effective human teaching methods.

### 7. Agent in a Bottle: Can LLM Agents Turn Their Capabilities Into Cheap, Scalable Artifacts?
**Authors:** Ankit Sonthalia, Haritz Puerto, Alexander Rubinstein, Martin Gubri, Seong Joon Oh
**Link:** https://arxiv.org/abs/2610.08775v1
**Summary:** The paper addresses the challenge of efficiently handling large workloads with large language models (LLMs) by introducing a method called "bottling," which enables LLM agents to autonomously generate cost-effective, task-specific solutions. The authors introduce a benchmark, BOTTLED, to evaluate agents' abilities to optimize workload completion under budget constraints. Key findings indicate that while LLMs perform well in zero-shot settings, their effectiveness in bottling varies significantly, though the approach can achieve substantial cost savings while maintaining a high level of performance compared to dedicated models for repetitive tasks.

### 8. AdvSim2Real : Training Web Agents Against Adaptive Prompt Injection in a Web World Model
**Authors:** Sarim Hashmi, Mukul Ranjan, Kshitij Mishra, Mikhail Kuznetsov, Praneeth Vepakomma, Nils Lukas
**Link:** https://arxiv.org/abs/2610.08773v1
**Summary:** The paper addresses the issue of web agents being misled by malicious instructions embedded in web pages, which can divert them from completing user tasks. The authors propose a new training framework called AdvSim2Real that simultaneously evolves the agent, the adversarial prompts, and the task curriculum in a controlled web simulation environment. This approach significantly enhances the agent's performance, leading to a 33.6% increase in task completion when faced with unseen adversarial attacks.

### 9. Rapid Fredholm stabilization of the Kuramoto--Sivashinsky equation with unrestricted, spatially-varying anti-diffusion
**Authors:** Luke Bhan, Miroslav Krstic, Yuanyuan Shi
**Link:** https://arxiv.org/abs/2610.08764v1
**Summary:** This paper addresses the challenge of stabilizing the Kuramoto--Sivashinsky equation, which can become uncontrollable due to certain unstable eigenvalues. The authors introduce a novel feedback control design using two distinct boundary inputs to effectively manage these instabilities and ensure controllability. A key contribution is the development of a continuous mapping for approximating control gains, along with a Fourier neural operator that achieves impressive stabilization results and low gain errors in numerical tests.

### 10. VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning
**Authors:** Zewei Zhou, Rachel Luo, Yulong Cao, Chaowei Xiao, Chensheng Peng, Boyi Li, Thomas Tian, Zheng Lian, Yan Wang, Jiaqi Ma, Boris Ivanovic, Marco Pavone, Wenhao Ding
**Link:** https://arxiv.org/abs/2610.08761v1
**Summary:** The paper addresses the challenge of verifying self-improving AI policies in tasks that require embodied reasoning, where traditional fixed judges limit progress. The authors introduce VeriFine, a framework that evolves both the AI policy and its evaluative judge through co-training, allowing for adaptive feedback and human input on complex failure cases. Their experiments demonstrate that this approach leads to significant improvements in both AI capabilities and the judges' ability to evaluate them, facilitating more effective continuous self-improvement.
