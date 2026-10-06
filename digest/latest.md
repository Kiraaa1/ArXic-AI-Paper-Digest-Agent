---
## 2026-10-06

### 1. One Figure, Every Canvas: Editable Flowchart Relayout via Agentic Pipeline
**Authors:** Shih-Chen Tseng, Chih-Hsuan Chen, Ryan Yang, Hsi-An Chen, Chun-Wei Tuan Mu, Yu-Lun Liu
**Link:** https://arxiv.org/abs/2610.06852v1
**Summary:** The paper addresses the challenge of adapting flowchart figures in machine learning papers to various aspect ratios without compromising their structure or content. The authors propose an innovative agentic pipeline that involves parsing, styling, and layout stages, ensuring that the flowchart’s connectivity is preserved and editable in formats like draw.io. Their method significantly outperforms existing techniques with a content fidelity score of 68.6%, compared to 11.2-41.4% for previous approaches, demonstrating a major advancement in flowchart relayout.

### 2. Base Models Can Reason By Taking a Cue From Training Data
**Authors:** Sophie L. Wang, Amil Dravid, Rulin Shao, Kevin Farhat, Sewon Min, Alexei A. Efros
**Link:** https://arxiv.org/abs/2610.06851v1
**Summary:** The paper investigates how specific starting tokens in prompts can influence the reasoning abilities of base models, showing that carefully chosen cues can significantly enhance performance in tasks like math and coding. By analyzing the effects of these tokens and their relationships with training data, the authors find that certain cues can match or even exceed the performance of models fine-tuned with reinforcement learning. The research highlights that manipulating these cues can alter reasoning behavior and compliance in language model responses.

### 3. BiasFlow: Geometric Monitoring and Backbone Regularization for Spurious Feature Reliance
**Authors:** Haojin Deng, Zhiping Lin, Yimin Yang
**Link:** https://arxiv.org/abs/2610.06846v1
**Summary:** The paper addresses the issue of spurious feature reliance in machine learning models, specifically how traditionally trained predictors perform when new tasks are introduced. The authors introduce BiasFlow, a toolkit that monitors class-attribute relationships and proposes BiasFlow Regularization (BFR), a method to align centroids conditionally based on classes. Key results show that integrating BFR improves worst-group accuracy significantly, demonstrating its effectiveness in mitigating bias during retraining of predictor heads on biased data.

### 4. Learning to Read the Contextual Tokens in Diffusion Transformers
**Authors:** Omer Dahary, Etai Sella, Hadar Averbuch-Elor, Daniel Cohen-Or, Or Patashnik
**Link:** https://arxiv.org/abs/2610.06844v1
**Summary:** This paper addresses the challenge of understanding how contextual tokens in Multimodal Diffusion Transformers (MM-DiTs) encode information during image generation. The authors developed a framework that utilizes a lightweight network to interpret these tokens, allowing a frozen Large Language Model to extract information about the evolving images. They found that contextual tokens contain significant semantic information early in the generation process, and improved training techniques based on this understanding can enhance the quality of generated images.

### 5. Recursive Video In-Context Learning for Agentic Robot
**Authors:** Wenrui Bao, Xinxin Liu, Bingxin Xu, Yuzhang Shang
**Link:** https://arxiv.org/abs/2610.06843v1
**Summary:** This paper addresses the challenge of enhancing robot performance in task execution by improving how demonstration videos are utilized for learning. The authors propose Recursive Video In-Context Learning (RV-ICL), a method that organizes a demonstration into a hierarchy of sub-events, allowing the robot to access detailed information as needed during task execution. This approach significantly increases the success rates of the robots, achieving improvements from 92.6% to 96.5% on the LIBERO-PRO dataset and from 86.7% to 95.8% on LIBERO-Plus.

### 6. Direct Intermediate Initialization for Tilted Diffusion Samplers
**Authors:** Gregory D. Bellchambers
**Link:** https://arxiv.org/abs/2610.06834v1
**Summary:** The paper addresses the challenge of efficiently sampling from diffusion posteriors in tilted diffusion samplers by introducing a method called Direct Intermediate Initialization for the sequential Monte Carlo sampler, MCGDiff. This approach involves using an approximate solver to sample from a softened clean-space posterior, which is then mapped to the tilted target via a Gaussian bridge, thus improving sampling performance. The key contribution is that this method significantly enhances the accuracy of the sampler, demonstrating up to a twofold improvement in performance metrics like sliced Wasserstein distance, especially in scenarios where the target mode is rare.

### 7. Towards Looped Models Done Right, Part II: Rethinking at Fixed Points
**Authors:** Benhao Huang, Chufan Shi, Junlin Chen, Shicheng Wen, Zhengzhong Liu, Eric Xing, Xuezhe Ma
**Link:** https://arxiv.org/abs/2610.06833v1
**Summary:** The paper addresses inefficiencies in looped language models, particularly caused by recurrent states that approach fixed points, which can complicate training and decoding processes. The authors propose improvements in training through a learned depth prior and a new orthogonal injection method that enhance efficiency while maintaining accuracy. Key results show that their techniques reduce model perplexity across various parameter scales and achieve performance comparable to more resource-intensive methods, significantly lowering the computational costs of training and inference.

### 8. UniSlider: Perceptually Uniform Sliders for Continuous Image Editing
**Authors:** David Serrano-Lozano, Duygu Ceylan, Yannick Hold-Geoffroy, Iliyan Georgiev, Javier Vazquez-Corral, Anna Frühstück
**Link:** https://arxiv.org/abs/2610.06831v1
**Summary:** UniSlider addresses the problem of inconsistent perceptual changes in continuous image editing sliders, which often fail to provide a smooth editing experience. The authors propose a lightweight approach that trains a model to create a slider that maintains a linear relationship between slider value and perceptual distance from the input image. The key result shows that UniSlider significantly outperforms previous methods in uniformity and user preference when evaluated on a benchmark for continuous edits.

### 9. MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents
**Authors:** Haozhen Zhang, Haodong Yue, Quanyu Long, Jianzhu Bao, Qingyuan Liu, Tao Feng, Bohan Liu, Weida Liang, Wenya Wang
**Link:** https://arxiv.org/abs/2610.06830v1
**Summary:** The paper introduces MemPilot, a framework that enhances memory management for language model (LLM) agents by allowing for on-demand curation of multimodal information tailored to specific queries. Using reinforcement learning, it optimizes a policy that balances performance, cost, and latency by intelligently deciding when to access memory and how to curate information. The experiments demonstrate that MemPilot achieves better trade-offs in performance and resource use compared to existing systems, showcasing its potential for flexible memory management in LLM applications.

### 10. CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling
**Authors:** Yifan Zhang, Yutong Dai, Viraj Prabhu, Zhiyuan Hu, Ran Xu, Zeyuan Chen
**Link:** https://arxiv.org/abs/2610.06829v1
**Summary:** The paper introduces CLIFT, a method to enhance the training and testing of open-source web agents by enabling them to verify their own performance using natural language questions, instead of relying on expensive external judges. CLIFT utilizes a self-verification mechanism to improve training efficiency and allows agents to make decisions during testing without external input, achieving state-of-the-art performance in various benchmarks. This approach effectively transforms costly feedback into a reusable training signal, thereby improving agent capabilities.
