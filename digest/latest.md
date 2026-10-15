---
## 2026-10-15

### 1. Modeling and Understanding Neural Weights of Humanoid Policies with Diffusion
**Authors:** Huixuan Cheng, Bike Zhang, Shankar Sastry, Koushil Sreenath
**Link:** https://arxiv.org/abs/2610.20606v1
**Summary:** The paper addresses the challenge of understanding and modeling the weights of humanoid control networks, which are typically trained using conventional methods. The authors propose a latent diffusion framework combining a linear autoencoder and a Diffusion Transformer to generate effective control networks directly from their weights. They find that the first-layer weights reveal a structural principle related to the robot's kinematic capabilities, indicating a shared knowledge across different training methods, and they successfully generate networks capable of executing complex motions in the real world.

### 2. Hierarchical Residual Policy Learning for Real-World Mobile Manipulation with Sparse Human Guidance
**Authors:** Zhefei Gong, Hefeifei Jiang, Zehao Wang, Jiachen Li
**Link:** https://arxiv.org/abs/2610.20607v1
**Summary:** The paper addresses the challenges of fine-tuning mobile manipulation robots in real-world settings, where there are complex action spaces and interactions between different robotic modules. The proposed HiRe-MoMa framework uses a Hierarchical Residual Architecture to adjust a base policy while minimizing interference and enhancing sample efficiency through sparse human guidance. The key result shows that this approach significantly improves task performance in just 30 minutes of real-world interaction, making fine-tuning of robots more practical in dynamic environments.

### 3. Co-Evolving Acting and Forecasting for Language Agents
**Authors:** Haofei Yu, Yixing Chen, Yining Zhao, Xuyan Ye, Yuxiang Liu, Zhigang Hua, Yan Xie, Shuang Yang, Jiaxuan You
**Link:** https://arxiv.org/abs/2610.20597v1
**Summary:** The paper addresses the challenge of efficiently training language agents in reinforcement learning, which is often hindered by the high costs of long-term predictions. The authors propose a novel method called \name that incorporates multi-step action targets to enhance the learning process, allowing the agent to improve both its acting and forecasting capabilities simultaneously. Key results show that \name outperforms existing methods in terms of overall performance and sample efficiency without adding extra models or complexity during inference.

### 4. Your Transformer Is Secretly Elastic
**Authors:** Walter Simoncini, Dheeraj Varghese, Gertjan J. Burghouts, Cees G. M. Snoek
**Link:** https://arxiv.org/abs/2610.20588v1
**Summary:** The paper addresses the inflexibility of current transformer models, which only come in fixed sizes, making them suboptimal for varying computational demands. The authors propose a novel method that allows a single transformer model to adaptively adjust its complexity without needing retraining, by jointly ranking individual components based on their importance. This approach enables efficient pruning of models to achieve significant reductions in size and increases in processing throughput, demonstrating impressive performance on various tasks with minimal accuracy loss.

### 5. Price of Anarchy of First-Price Auctions in Agentic Markets
**Authors:** Shubhendu Trivedi, Jacob Eisenstein, Alekh Agarwal, Ian Gemp, Michael Kaisers, Adam Fisch
**Link:** https://arxiv.org/abs/2610.20587v1
**Summary:** The paper addresses the issue of welfare loss in first-price auctions within decentralized AI markets, where agents bid to claim user prompts. By examining the dynamics of competition among bidders and the nature of their bid values, the authors demonstrate that certain market features can significantly reduce the price of anarchy, leading to improved welfare outcomes. Their results indicate that under certain conditions, the efficiency can approach nearly optimal levels, surpassing the standard limits commonly observed in such auction settings.

### 6. Continuum Attention
**Authors:** Afshin Khadangi
**Link:** https://arxiv.org/abs/2610.20586v1
**Summary:** The paper introduces Continuum Attention (CA), a new attention mechanism for Transformers that replaces the standard discrete key and value lookup with a continuous memory integration approach. This method allows for more efficient attention calculations and achieves improved performance, demonstrating significant reductions in validation negative log likelihood compared to traditional softmax and focal attention methods. The results suggest that continuous integration could be a valuable alternative for attention mechanisms in deep learning models.

### 7. Learnable Hodge-Laplacian Driven Mixture of Experts for Steady-PDE Surrogates on Coarse Unstructured Meshes
**Authors:** Stavros Nousias, Akis Nousias, Konstantinos Gkrispanis
**Link:** https://arxiv.org/abs/2610.20585v1
**Summary:** The paper addresses the challenge of creating surrogate models for steady partial differential equations (PDEs) on unstructured meshes, where traditional methods use a single mixing strategy. The authors introduce a new architecture that utilizes transformer experts focused on different spectral scales, guided by a discrete Hodge-Laplacian to assess high-frequency content. Their method shows significant improvement, reducing relative L2 error by 31% and interior mean squared error by 47% compared to existing techniques.

### 8. Player-1: Learning to Play from Synthetic Experience
**Authors:** Mingyu Ouyang, Yiran Wang, Siyuan Hu, Xingyilang Yin, Huiqiang Sun, Guangzhi Wang, Junfu Pu, Cheng Cheng, Honghao Chen, Ying Shan, Mike Zheng Shou, Hwee Tou Ng
**Link:** https://arxiv.org/abs/2610.20584v1
**Summary:** The paper addresses the challenge of training agents to control games with rich visuals and diverse mechanics, which traditional methods struggle to fully cover. The authors introduce Player-1, a framework that allows agents to learn from synthetic experiences using a novel action space and specialized environments, leading to substantial improvements in game performance. Notably, their approach resulted in a significant increase in success rates across various games, outperforming existing models and demonstrating enhanced generalization capabilities.

### 9. Latent Compaction with Test-Time Training
**Authors:** Yingfa Chen, Xingyu Shen, Chaojun Xiao, Xu Han
**Link:** https://arxiv.org/abs/2610.20582v1
**Summary:** The paper addresses the challenge of efficiently compressing key-value (KV) caches used in long-context generation models, which consume excessive memory and attention resources. The authors introduce Latent Compaction, a technique that optimizes a compact, document-specific cache through test-time training without changing the model weights, leading to significant improvements in retrieval accuracy even under aggressive compression. Notably, their method achieves 96.7% accuracy at 32× compression on the RULER benchmark, far outperforming existing approaches.

### 10. One Task, Many Interfaces: Simple Cross-Interface Consistency Training Improves LLM Agent Robustness
**Authors:** Artin Tajdini, Manpreet Kaur, Peng Qi
**Link:** https://arxiv.org/abs/2610.20576v1
**Summary:** The paper addresses the issue of large language model (LLM) agents becoming less effective when faced with changes to their training interface, such as altered action names. The authors propose a method called Cross-Interface Policy Regularization (CIPR), which uses a self-supervised approach to train the agent on two equivalent interfaces, encouraging consistency in its actions. The results show that CIPR significantly improves the agent's robustness, recapturing about 10.5% of the accuracy lost due to interface changes while maintaining performance on the original interface.
