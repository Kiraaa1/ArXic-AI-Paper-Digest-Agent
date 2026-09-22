---
## 2026-09-22

### 1. GameHorizon Suite: Multi-Horizon Data and Evaluation in Gameplay
**Authors:** Yiran Wang, Xingyilang Yin, Junfu Pu, Guangzhi Wang, Kaifeng Li, Mingyu Ouyang, Huiqiang Sun, Lingen Li, Cheng Cheng, Wangbo Yu, Honghao Chen, Xiaodong Cun, Chi-Man Pun, Zhiguo Cao, Ying Shan
**Link:** https://arxiv.org/abs/2609.25001v1
**Summary:** The paper presents the GameHorizon Suite, a comprehensive framework designed to evaluate AI models in video games across multiple time horizons, addressing gaps in existing datasets that lack diverse game coverage and structured language instructions. It includes an automated annotation pipeline, a large-scale gameplay dataset from 21 games, and a benchmarking system for evaluating model performance. The key contribution is the establishment of a standardized method to assess gameplay skills, revealing significant differences in model capabilities through extensive evaluation.

### 2. Critical-State RL: Diagnosing Trainable States for Multi-Turn Tool Use
**Authors:** Zixiang Chen, Wenting Zhao, Zhepeng Cen, Akshara Prabhakar, Jielin Qiu, Jianguo Zhang, Zhiwei Liu, Tulika Manoj Awalgaonkar, Liangwei Yang, Shelby Heinecke, Silvio Savarese, Huan Wang
**Link:** https://arxiv.org/abs/2609.24985v1
**Summary:** The paper addresses the challenge of identifying which specific model calls in multi-turn tool-use tasks can be effectively improved through training, as traditional reward signals may not clearly indicate actionable changes. The authors propose a method called Critical-State RL, which uses nested sampling to distinguish meaningful performance variations from noise and to optimize policy based on identified critical states. Their experiments show that training at these strategically selected states significantly enhances performance, achieving up to a 14 percentage point improvement in specific tasks compared to training alternatives that did not yield such improvements.

### 3. WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory
**Authors:** Wangbo Yu, Kunhao Liu, Wenbo Hu, Shenghai Yuan, Chaoran Feng, Haiyang Zhou, Yukun Huang, Yiran Wang, Wang Zhao, Yingmin Luo, Ying Shan
**Link:** https://arxiv.org/abs/2609.24984v1
**Summary:** WorldCrafter addresses the challenge of maintaining consistency in video world models during long-term exploration of dynamic environments. It utilizes an implicit 3D-aware memory system that adapts to the requested viewpoint, allowing for effective integration of historical observations without requiring explicit depth information. The model demonstrates improved long-horizon consistency and camera control accuracy, enabling seamless scene exploration from just a single image or text prompt.

### 4. onPanda: Efficient Annotation of On-Policy Alignment Data for LLMs and Agents via Token-Level Correction
**Authors:** Lei Yang, Mengyin Liu, Jia Wang, Hangyu Guo, Liang Zhao, Zheng Ge, Kang An, Binxing Jiao, Qi Han, Daxin Jiang, Siqi Shen, Xiangyu Zhang
**Link:** https://arxiv.org/abs/2609.24983v1
**Summary:** The paper introduces onPanda, an interactive tool designed to streamline the annotation of alignment data for large language models and agents by allowing annotators to correct model outputs at the token level. By enabling users to identify and replace inappropriate tokens while maintaining the model's original sampling distribution, onPanda significantly reduces the time needed for annotation—showing a 52% time savings compared to traditional manual methods. In addition, the tool produces high-quality data for training models and provides nuanced supervision via detailed correction logs.

### 5. LoRA-generating hypernetworks for efficient on-device LLM generative personalization
**Authors:** Sean Augenstein, Li Ding, Jihwan Lee, Keith Rush, Andrey Zhmoginov
**Link:** https://arxiv.org/abs/2609.24979v1
**Summary:** This paper addresses the challenge of personalizing large language models (LLMs) on mobile devices, where limited computing resources affect model quality. It introduces a method that utilizes a hypernetwork to create low-rank adaptations (LoRA) tailored to individual users based on their context, allowing for efficient on-device personalization without significant computational overhead. The key contribution is demonstrating that this approach effectively enhances personalization for long-form text generation, outperforming traditional methods like in-context learning and parameter-efficient fine-tuning.

### 6. DexTacWAM: A Visuo-Tactile World-Action Model for Dexterous Manipulation
**Authors:** Haoran Yuan, Zekai Wang, Boning Shao, Haoran Lu, Trevor Darrell, Ismini Lourentzou, Wei Zhan
**Link:** https://arxiv.org/abs/2609.24976v1
**Summary:** The paper introduces DexTacWAM, a model designed to improve dexterous manipulation by integrating both visual and tactile information to better understand contact dynamics. This is achieved by independently encoding fingertip tactile data and combining it with a video model to enhance predictive capabilities in complex manipulation tasks. The key contribution is that DexTacWAM significantly outperforms existing methods in six dexterous manipulation tasks, demonstrating a more effective approach to learning from limited tactile data while maintaining visual prediction accuracy.

### 7. Harness-Zero: Harness Distillation via Agent-as-Harness
**Authors:** Haoran Ye, Yuxing Lu, Haonan Dong, Zhaochen Su, Guojie Song
**Link:** https://arxiv.org/abs/2609.24974v1
**Summary:** The paper presents Harness-Zero, a method for transferring the performance benefits of specialized agent harnesses into a single, more general model for various tasks. By using a harnessing agent to convert the guidance from an optimized harness into training data for a model, it enables the model to internalize behaviors that enhance its performance once the specialized harness is removed. The results show a significant improvement in task success rates, achieving a success rate of 44.3% from a baseline of 23.3%, with the method also recovering key effective behaviors not present in the original model.

### 8. RRSI: Regularized Recursive Self-Improvement of Agent Harnesses
**Authors:** Peng Xia, Rujun Han, Zifeng Wang, Yanfei Chen, Yufan Zhang, Yoonho Lee, Chengsong Huang, Han Yu, Zhongying CuiZhu, Yifei Ming, Huaxiu Yao, Burak Gokturk, Tomas Pfister, Chen-Yu Lee
**Link:** https://arxiv.org/abs/2609.24972v1
**Summary:** The paper addresses the problem of overfitting in the recursive self-improvement of agent harnesses for large language models (LLMs), where agents may excel on training tasks but struggle with new ones. The authors propose a method called Regularized Recursive Self-Improvement of Agent Harnesses (RRSI) that uses regularization techniques to manage the evolution of agent harnesses and encourages exploration of new strategies. The results show that RRSI improves performance on both in-distribution and out-of-distribution benchmarks while reducing the number of policy tokens used by the agent.

### 9. DolphinBench: Mapping the Pareto Frontier of Agent Memory
**Authors:** Soumil Rathi, Deshraj Yadav, Taranjeet Singh
**Link:** https://arxiv.org/abs/2609.24971v1
**Summary:** The paper introduces DolphinBench, a new benchmark designed to evaluate the effectiveness of agent memory by assessing how well agents complete tasks that rely on long-term memory and context recall. Unlike existing benchmarks that focus primarily on accuracy in conversational settings, DolphinBench includes a comprehensive evaluation of agent performance across various tasks while also measuring cost and latency. The contribution lies in its holistic approach to memory system evaluation, enabling a better understanding of trade-offs in memory usage for agents.

### 10. Rare Event Estimation via Iterative Unalignment
**Authors:** Hanming Yang, Daksh Mittal, Jing Dong, Hongseok Namkoong
**Link:** https://arxiv.org/abs/2609.24969v1
**Summary:** The paper addresses the challenge of accurately estimating the probabilities of rare events that can occur during the operation of autonomous agents. The authors propose an innovative importance sampling method that involves perturbing the weights of a differentiable language model to enhance the efficiency of probability estimation. Their approach demonstrates significant efficiency improvements, achieving over 800 times the computational efficiency of traditional Monte Carlo methods for events with very low probabilities, showcasing its effectiveness in handling rare event risk assessment.
