---
## 2026-10-28

### 1. Honeycomb-Surfels: Compact Hexagonal Primitives for Efficient Scene Rendering and Reconstruction
**Authors:** Prakhar Kaushik, Soumava Paul, Alan Yuille
**Link:** https://arxiv.org/abs/2610.37668v1
**Summary:** The paper addresses the challenges of memory and computational demands in 3D scene rendering and reconstruction by introducing a new primitive called Hexels, which are hexagonal surface elements designed to represent both 3D scenes and 2D images more efficiently. By utilizing larger, locally planar regions with a first-order color field, Hexels improve image quality while reducing memory usage, achieving significant gains in quality and rendering speed compared to existing methods. The key results show an increase in PSNR and a 28.9% reduction in error for 3D reconstructions, marking Hexels as a valuable advancement in the trade-offs between quality and efficiency.

### 2. ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning
**Authors:** Chaehyun Kim, Chi-Pin Huang, Jisoo Kim, Min-Hung Chen, Yu-Chiang Frank Wang, Seungryong Kim, Fu-En Yang
**Link:** https://arxiv.org/abs/2610.37666v1
**Summary:** The paper addresses the challenge of improving the generalization of Vision-Language-Action models in robotic manipulation, which often struggle due to limited action-labeled training data. The authors introduce a framework called ThinkWorld that uses a concept called Chain-of-Dynamics to represent actions as sequences of motion tokens, allowing the model to learn from both labeled demonstrations and unannotated human videos. Key results show that this approach enhances the transfer of learning from humans to robots and allows the robots to effectively tackle new tasks and environments.

### 3. When Should We Intervene at Test Time?
**Authors:** Jiahao Zhang, Xinling Wen, Liangliang Li, Yu Chen
**Link:** https://arxiv.org/abs/2610.37658v1
**Summary:** The paper addresses the challenge of test-time adaptation for machine learning models, which can perform inconsistently depending on the input batch. The authors propose PORTAL, a controller that intelligently decides when to apply interventions, which inputs to label for feedback, and when to stop querying, enhancing the model's performance by focusing on promising candidates. The key finding is that PORTAL can turn otherwise ineffective interventions into beneficial ones for selected batches, while also maintaining improvements for future inputs with minimal feedback.

### 4. Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness
**Authors:** Igor Shilov, Xiaoxue Yang, Alexander Panfilov, Evgenii Kortukov, Matthieu Meeus, Peter Romov, Wojciech Samek, Jonas Geiping, Yves-Alexandre de Montjoye
**Link:** https://arxiv.org/abs/2610.37657v1
**Summary:** The paper presents Heads of Security (HoS), a novel defense mechanism against prompt injection in language models that enhances security by using learned attention gates to separate trusted from untrusted data. HoS significantly improves robustness against adaptive attacks compared to state-of-the-art defenses, maintaining model performance while achieving a dramatic reduction in attack success rates. Overall, the approach demonstrates a successful balance between security and utility, addressing critical vulnerabilities in language model interactions.

### 5. Attention as Lattice Gauge Theory: Relations Interact Only Through Wilson Loops
**Authors:** Aakash Sarkar, Ananya Mukherjee, Motoshige Sato
**Link:** https://arxiv.org/abs/2610.37656v1
**Summary:** This paper addresses the challenge of modeling relationships in graphs, specifically how entities interact based on their relational structure. The authors present a framework inspired by lattice gauge theory, focusing on "Wilson loops" to define these interactions, leading to a unique method of edge attention that respects the underlying symmetries. Their approach achieves impressive performance in inferring unobserved relationships and identifying corrupted data in sparse graphs, significantly outperforming traditional methods.

### 6. KPPax: preprocess differentiable kinetic ODE for machine learning in atmospheric chemistry
**Authors:** Wenqing Peng, Michael Boy, Zhi-Song Liu
**Link:** https://arxiv.org/abs/2610.37655v1
**Summary:** The paper introduces KPPax, a tool that transforms kinetic ODE chemical mechanisms from KPP into differentiable code suitable for machine learning, allowing for more accurate model training and parameter estimation in atmospheric chemistry. By integrating JAX for efficient computation and automatic differentiation, KPPax enables precise sensitivity analysis and facilitates the use of neural networks for improving emission inventory corrections. Key results show that KPPax predicts identifiable reaction rate coefficients effectively and significantly enhances the accuracy of biogenic emission corrections by leveraging chemical model integrations.

### 7. Pushing Dexterity and Safety for In-Hand Object Pose Reaching That Works Remarkably Well
**Authors:** Ian Chuang, Hiya Shah, Vamsi Chilamkur, Iman Soltani, Claire Tomlin
**Link:** https://arxiv.org/abs/2610.37652v1
**Summary:** The paper addresses the challenge of dexterous in-hand manipulation with multi-fingered robotic hands, focusing on safely reaching diverse object poses without dropping them. The authors developed a training framework that uses simulation to create effective manipulation policies, incorporating innovative methods like varied starting conditions and an adaptive friction curriculum, achieving impressive transfer to real robots. Key results show that their approach allows for high success rates in goal achievement while significantly reducing object drops, demonstrating the potential of these learned skills in practical applications.

### 8. GEPA-Curator: Curated Learning for Self Improving Agents
**Authors:** Zack Yu, Nicholas Lee, Minjae Lee, Lakshya Agarwal, Luca Manolache, Wonjun Kang, Matei Zaharia, Michael W. Mahoney, Kurt Keutzer, Sehoon Kim, Amir Gholami
**Link:** https://arxiv.org/abs/2610.37651v1
**Summary:** The paper presents GEPA-Curator, a framework designed to enhance the performance of Large Language Models (LLMs) in complex task environments by curating the experiences that inform prompt optimization. It filters out potentially misleading tasks and incorporates successful past experiences to guide learning. The approach demonstrated significant performance improvements, achieving up to 20.7% better results compared to existing methods.

### 9. Can LLMs Uncover Hidden Physical Laws through Free Exploration?
**Authors:** Zhen Yang, Wen Wang, Xander Xu, Ying-Cong Chen
**Link:** https://arxiv.org/abs/2610.37649v1
**Summary:** This paper investigates whether large language models (LLMs) can autonomously discover new physical laws by exploring simulated environments with altered physics. The authors introduce a framework called LongChang, which enables LLMs to experimentally investigate these worlds without specific guidance. Among 12 tested LLMs, GPT-6-Astra succeeded in uncovering new insights with a 16.7% discovery rate, highlighting the potential of LLMs for scientific exploration despite the limitations observed in other models.

### 10. Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis
**Authors:** Andrew Szot, Samira Abnar, Omar Attia, Abbas Kazerouni, Michael Kirchhof, Cheng-Yu Hsieh, Raviteja Vemulapalli, Alexander Toshev
**Link:** https://arxiv.org/abs/2610.37648v1
**Summary:** This paper addresses the challenge of training large language model tool-use agents to effectively complete complex, multi-step tasks by examining how the composition of synthetically generated environments influences their performance. The authors introduce the SynthAPI pipeline, which allows them to control the diversity of environments and systematically analyze the impact of various factors on agent training. Their findings indicate that focusing on the diversity of tools and databases is more beneficial than simply increasing the number of tasks, leading to superior agent performance compared to previous methods.
