---
## 2026-09-09

### 1. TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model
**Authors:** Anqi Li, Yuxin Chen, Zhaobo Li, Zhuo Cao, Junli Ren, Masayoshi Tomizuka, Dhruv Shah
**Link:** https://arxiv.org/abs/2609.09158v1
**Summary:** The paper presents TANGO, a novel framework for enabling humanoid robots to navigate cluttered indoor environments by interpreting natural language instructions and analyzing visual input. Unlike traditional methods that focus on 2D path planning, TANGO utilizes a whole-body vision-language model to predict coordinated joint movements for safe traversal in 3D space. The key contribution is that TANGO achieves state-of-the-art performance in this challenging task, successfully demonstrating robust navigation in real-world settings without any prior training on real navigation data.

### 2. Learning Length-Extrapolatable Recurrent Models
**Authors:** Hanwen Jiang
**Link:** https://arxiv.org/abs/2609.09157v1
**Summary:** The paper addresses the limitation of recurrent models, which often struggle with long-context dependencies when trained with traditional backpropagation methods. The authors introduce a new technique called Credit Stabilization through Time (CST) that adjusts the signal used to update earlier states during training, ensuring better stability and performance. Their results show that CST significantly enhances the model's ability to extrapolate beyond its training length, achieving improvements at scales up to 128 times longer than the training horizon.

### 3. ReCite: Agentic Reasoning for Faithful Citation
**Authors:** Yuyang Huang, Bobo Li, Jiajia Song, Yuzhe Ding, Chong Teng, Fei Li, Donghong Ji
**Link:** https://arxiv.org/abs/2609.09156v1
**Summary:** The paper addresses the problem of inaccurate citations in automated citation recommendation systems, which often cite relevant but unsupported papers. The authors propose a framework called ReCite, which focuses on active reasoning and verification of claim-evidence consistency instead of relying solely on semantic similarity. Their experiments show that ReCite significantly improves citation accuracy compared to existing generative models, providing a more reliable solution for automated academic writing.

### 4. Procedural Graphs: Self-Evolving Execution Structures for LLM Agents
**Authors:** Yuxing Lu, Yicheng Chen, Shanchan Wu, Sercan Ö. Arık
**Link:** https://arxiv.org/abs/2609.09153v1
**Summary:** The paper addresses the issue of large language model (LLM) agents losing focus and mismanaging tasks during long execution sequences. To tackle this, the authors propose the Procedural Graph, a structure that organizes procedural knowledge to guide LLMs in their decision-making. The key contribution is that this self-evolving graph, which learns from successes and failures, consistently outperforms traditional memory-based systems and can enhance expert-designed procedures without the need for manual adjustments.

### 5. Silver Rate Is (Almost) Optimal for Gradient Descent Acceleration
**Authors:** Yuhan Ye, Kaizhao Liu
**Link:** https://arxiv.org/abs/2609.09152v1
**Summary:** The paper investigates the acceleration of gradient descent (GD) in smooth convex optimization by using fixed nonnegative step sizes. It establishes lower bounds for the convergence rates of various schedules, proving that a specific step size choice, referred to as the "silver rate,” is nearly optimal for maximizing acceleration. The findings clarify the limits of performance in both fixed and anytime settings, enhancing our understanding of optimal convergence rates in this context.

### 6. Copying explains the collective behavior of AI agents in the wild
**Authors:** Giordano De Marzo, Nicola Albore, David Garcia
**Link:** https://arxiv.org/abs/2609.09150v1
**Summary:** This paper investigates how AI agents exhibited cooperative behavior while editing a public wiki without any prior instruction or memory. The authors propose that the agents made decisions based on the prevalence of options visible in their environment, which led to a range of consistent and collaborative outcomes. The key finding is that simple copying rules govern their decision-making, enabling the formation of collective structures, making the behavior of these agents predictable and easily influenced by initial actions.

### 7. Studying Image Tokenizers as Visual Languages in Unified Multimodal Models
**Authors:** Siting Li, Zhengyang Wang, Simon Shaolei Du, Xi Chen, Yang Liu
**Link:** https://arxiv.org/abs/2609.09143v1
**Summary:** The paper investigates how image tokenizers function as part of a "visual language" in unified multimodal models by studying their behavior when combined with text. The authors created a controlled testing setup to analyze task-specific validation losses during continual multimodal pretraining, revealing that losses vary significantly depending on the task and tokenizer choice, which influences both image and text modeling performance. Key findings include that reconstruction quality does not guarantee better task performance, and items such as tokenizer design can impact joint optimization outcomes.

### 8. NOAH: Learning the Full Patient Journey. A Longitudinal Multimodal Time-Aware Model for Representation and Forecasting
**Authors:** Tobias Susetzky, Raphael Rehms, Dmitrii Seletkov, Özgün Turgut, Michelle Espranita Liman, Lisa Steinhelfer, Rickmer Braren, Daniel Rueckert
**Link:** https://arxiv.org/abs/2609.09140v1
**Summary:** The paper presents NOAH, a generative transformer model designed to effectively represent and forecast patient health trajectories using diverse, complex, and longitudinal healthcare data. Unlike existing models, NOAH captures the irregular timing and uncertainty inherent in patient records while processing multiple data types, such as medical images and clinical notes. The model demonstrates strong capabilities in predicting clinical outcomes and comorbidities, offering a comprehensive tool for personalized healthcare and predictive analytics.

### 9. A Data-Driven Framework for Identifying and Prioritizing RPA Opportunities in Healthcare Processes
**Authors:** Maria Alejandra Gomez, Juan Manuel Castillo
**Link:** https://arxiv.org/abs/2609.09137v1
**Summary:** The paper addresses the challenge of effectively selecting and prioritizing healthcare processes for Robotic Process Automation (RPA), which often leads to underperforming initiatives due to informal selection methods. The authors propose a comprehensive, data-driven framework comprising four modules to systematically identify automation opportunities, including a prioritization index and financial forecasting tools. Key results demonstrate the framework's effectiveness, with 60% of evaluated processes qualifying for automation, and robust validation of prioritization stability and risk assessment through extensive simulations.

### 10. Entropy-Regularized Rank-Masked Policy Optimization for Test-Time Reinforcement Learning in Code Generation
**Authors:** Jiacheng Xu, Feng Chen, Xiuneng Xu, Bo An
**Link:** https://arxiv.org/abs/2609.09135v1
**Summary:** The paper addresses the challenge of applying test-time reinforcement learning (TTRL) to code generation, where traditional reward mechanisms are ineffective due to the unique nature of code. The authors propose a new method called Entropy-Regularized Rank-Masked Policy Optimization (ERPO), which leverages probe inputs and behavioral agreement to generate meaningful rewards for code outputs. This approach significantly enhances performance on coding tasks, improving success rates in both familiar and novel scenarios.
