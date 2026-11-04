---
## 2026-11-04

### 1. DreamX: Video Diffusion Model is a Universal Latent Action Learner
**Authors:** Jisoo Kim, Chaehyun Kim, Junsu Kim, Jiho Park, Seongchan Kim, Eunbeen Hong, Soowon Son, Fu-En Yang, Seungryong Kim
**Link:** https://arxiv.org/abs/2611.05377v1
**Summary:** The paper presents DreamX, a novel model designed to learn universal action representations from videos, effectively addressing the challenge of distinguishing actions from irrelevant visual variations. By leveraging a pretrained video diffusion model, DreamX compresses video frames and captures action dynamics in a shared latent space, allowing seamless transfer of actions across different settings, such as humans and robots. The key contribution is achieving state-of-the-art performance on action modeling benchmarks and enabling efficient policy learning in a compact action representation.

### 2. From Autonomous Agents to Cognitive Symbionts: Toward AI-Augmented Human Intelligence
**Authors:** Hao Fei
**Link:** https://arxiv.org/abs/2611.05376v1
**Summary:** The paper addresses the limitations of current AI systems that operate independently, highlighting the need for AI to actively augment human intelligence rather than just perform tasks on their own. It proposes the concept of a "cognitive symbiont," a supportive AI that continuously learns about an individual to assist them in real-time by understanding their context and needs. The authors outline a design framework for this symbiotic relationship and discuss potential risks associated with its implementation, emphasizing the importance of governance in the deployment of such AI systems.

### 3. Aligning Language Models with General Preferences: An Empirical Study of Direct Nash Optimization
**Authors:** Austin Tsai, Saurav Nanda, Ganapathy Parthasarathy, Bhuvnesh Kumar, Parivesh Choudhary
**Link:** https://arxiv.org/abs/2611.05373v1
**Summary:** The paper addresses the challenge of aligning language models with broader human preferences through a method called Direct Nash Optimization (DNO), which simulates a preference game between two players. By implementing a practical variant called DNO-Prct on various instruct models, the authors demonstrate significant improvements in win rates against a leading model (GPT-4o), indicating that their approach effectively enhances model alignment with human-like responses. Key findings highlight that robust performance can be maintained even with non-proprietary annotators, and specific configurations of the algorithm significantly influence the outcomes.

### 4. PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning
**Authors:** Yuhan Liu, Xinqi Liu, Zixuan Dong, Keith W. Ross, Shenji Wan
**Link:** https://arxiv.org/abs/2611.05372v1
**Summary:** The paper addresses the challenge of achieving high-precision inverse kinematics for robot arms, which is complicated by issues like redundancy and the need for fine-tuned controllers. The authors present PolicyIK, a goal-conditioned reinforcement learning method that effectively updates joint positions based on feedback to minimize errors in arm movements. The key contribution is its demonstrated success in both simulation and on a physical robot, achieving over 98% accuracy in task execution compared to traditional methods.

### 5. GUILD: Guided Iterative Data Collection for Imitation Learning
**Authors:** Shivin Dass, Kevin Nguyen, Rohan Yelandur, Junhong Xu, Roberto Martín-Martín
**Link:** https://arxiv.org/abs/2611.05368v1
**Summary:** The paper presents GUILD, a new method for improving the efficiency of data collection in imitation learning for robotics, which traditionally relies on unguided teleoperation and can lead to uninformative data. GUILD iteratively proposes specific tasks for data collection based on semantic insights and evaluates how well the collected data enhances policy performance, thereby optimizing future data collection. The results show that this guided approach significantly outperforms passive data collection strategies in both simulations and real-world scenarios.

### 6. Suppressing Misaligned Behaviors in Language Models, Durably
**Authors:** Luxi He, Pengcheng Jiang, Jifan Zhang, Jiawei Han, Danqi Chen
**Link:** https://arxiv.org/abs/2611.05358v1
**Summary:** This paper addresses the challenge of suppressing undesired behaviors in language models, which can emerge during training. The authors develop a new approach called Prefix-Expanded Adversarial Reinforcement Learning (PEARL) to effectively suppress these behaviors while maintaining general performance and durability against further training. Key results show that PEARL achieves strong immediate suppression of misaligned actions, especially for more broadly triggered misbehavior, outperforming standard methods.

### 7. Reading Why: Born-Measured Attention with Exact Word Evidence on Light and Qubits
**Authors:** Teerawat Tongloy, Jiraporn Pongsopa, Rangsan Jomtarak
**Link:** https://arxiv.org/abs/2611.05355v1
**Summary:** The paper introduces a novel transformer model that utilizes Born measurements to directly quantify why a language model generates specific answers, improving the interpretability of its decisions. By encoding attention through a polynomial derived from word amplitudes, the model achieves comparable accuracy to traditional softmax transformers while demonstrating a significant ability to identify critical words influencing its outputs. The approach bridges concepts from optics and quantum computing, illustrating its compatibility with qubits and potential for implementation on quantum hardware.

### 8. Agnostic Learning by Imitating
**Authors:** Sílvia Casacuberta, Parikshit Gopalan, Varun Kanade, Omer Reingold, Konstantinos Stavropoulos, Pranay Tankala
**Link:** https://arxiv.org/abs/2611.05346v1
**Summary:** This paper explores the equivalence between two challenging tasks in machine learning: training a model to distinguish between positive and negative examples and training a generative model that produces data indistinguishable from real samples. The authors demonstrate a new efficient method for reducing the generative task to the discriminative task, providing insights into how adaptive queries can enhance learning capabilities. Their key contribution is showing that multiaccuracy oracles, which perform well across a class of models, can yield effective solutions for a broader range of learning objectives than previously understood.

### 9. Adversarial Speculative Reasoning Improves Long Horizon Agents
**Authors:** Hongyin Luo, Wei Fang, Lijie Yang, Owen Stepan, Daniel Suit, Jeff Krapf, Dana Wensberg, Jack O'Brien
**Link:** https://arxiv.org/abs/2611.05345v1
**Summary:** The paper addresses the challenge of improving the reasoning accuracy of long-horizon agents using speculative decoding, which is typically seen as a speed optimization rather than a behavior modifier. The authors propose a method that enhances this process by training draft models to reject less precise reasoning points, effectively reducing numerical noise and improving the output at critical decision junctures. Their approach significantly boosts the success rate of agents on complex tasks without altering the target model itself.

### 10. A Circuit for In-Context Learning
**Authors:** Andrew Gao, William Gao
**Link:** https://arxiv.org/abs/2611.05344v1
**Summary:** The paper addresses the mechanism behind in-context learning (ICL) in large language models, detailing how these models can effectively classify sentences with arbitrary labels without needing parameter updates. The authors describe a specific circuit within transformer architectures that utilizes a key-value memory system for label identification and retrieval based on previous demonstrations. Their key contribution is identifying and establishing the causal roles of different activation heads in this process, revealing that ICL functions as a gated associative lookup that replicates reliably across different model sizes.
