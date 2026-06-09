---
## 2026-06-09

### 1. OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics
**Authors:** Mingxian Lin, Shengju Qian, Yuqi Liu, Yi-Hua Huang, Yiyu Wang, Wei Huang, Yitang Li, Fan Zhang, Zeyu Hu, Lingting Zhu, Xin Wang, Xiaojuan Qi
**Link:** https://arxiv.org/abs/2606.09826v1
**Summary:** The paper introduces OmniGameArena, a benchmark designed to evaluate vision-language model (VLM) agents in various game types, addressing shortcomings in existing evaluation methods that typically provide a single score for agents. It features twelve Unreal Engine 5 games and utilizes the Improvement Dynamics Curve (IDC) to track the evolution of agent performance over multiple attempts. The key contribution is the provision of detailed performance insights beyond initial scores, revealing how agents improve and adapt to different game scenarios.

### 2. An Agency-Transferring Model-Free Policy Enhancement Technique
**Authors:** Anton Bolychev, Georgiy Malaniya, Sinan Ibrahim, Pavel Osinenko
**Link:** https://arxiv.org/abs/2606.09825v1
**Summary:** This paper addresses the challenge of improving reinforcement learning (RL) efficiency by leveraging existing suboptimal baseline policies during training. It introduces a method that gradually shifts control from the baseline to a trainable policy, allowing the latter to enhance its performance while maintaining high success rates in reaching goals from the start of training. The key contribution is that this approach not only leads to a stronger final policy that operates independently but also achieves impressive results in continuous-control tasks, outperforming other competitive methods.

### 3. Causally Evaluating the Learnability of Formal Language Tasks
**Authors:** Vésteinn Snæbjarnarson, Anej Svete, Josef Valvoda, Reda Boumasmoud, Brian DuSell, Ryan Cotterell
**Link:** https://arxiv.org/abs/2606.09822v1
**Summary:** The paper addresses the challenge of determining how much data is needed for language models to learn specific tasks, particularly in complex natural language settings where tasks can intermix. To tackle this, the authors use formal languages generated from probabilistic finite automata to create a controlled environment and introduce a new algebraic tool, the binning semiring, for causal analysis. Their findings reveal that traditional correlational methods can lead to misleading conclusions about task learnability, underscoring the importance of causal evaluation in understanding data requirements for language learning.

### 4. Rethinking the Divergence Regularization in LLM RL
**Authors:** Jiarui Yao, Xiangxin Zhou, Penghui Qi, Wee Sun Lee, Liefeng Bo, Tianyu Pang
**Link:** https://arxiv.org/abs/2606.09821v1
**Summary:** The paper addresses the challenges of stable optimization in reinforcement learning for large language models (LLMs), particularly due to issues with off-policy training and distributional shifts in vocabularies. The authors introduce a new method called Divergence Regularized Policy Optimization (DRPO), which uses a smooth regularization approach instead of a hard clipping mask, allowing for better handling of policy updates when crossing trust-region boundaries. Experimental results demonstrate that DRPO enhances both the stability and efficiency of LLM reinforcement learning training compared to existing methods.

### 5. Weighted universal approximation of differentiable maps on infinite-dimensional manifolds
**Authors:** Philipp Schmocker, Josef Teichmann
**Link:** https://arxiv.org/abs/2606.09820v1
**Summary:** This paper extends the universal approximation theorem for functional input neural networks (FNNs) to cover differentiable maps, incorporating the ability to approximate their derivatives. The authors prove a weighted Nachbin theorem, establishing a universal approximation theorem that is applicable beyond compact sets and includes non-anticipative functionals. A significant contribution is demonstrating that linear functions of the signature can approximate path space functionals along with their directional derivatives.

### 6. PTL-Diffusion: Manifold-Aware Diffusion with Periodic Terminal Laws
**Authors:** Danqi Zhuang, Jisui Huang, Xiaoyue Xi, Andrew Kiggins, Xiaojie Wang, Ke Chen, Yue Wu
**Link:** https://arxiv.org/abs/2606.09816v1
**Summary:** The paper addresses the limitations of standard diffusion models that rely on a single Gaussian distribution, which struggles to capture the complex structures of data concentrated along low-dimensional manifolds. The authors propose PTL-Diffusion, a new framework that uses a periodic family of Gaussian terminal distributions in the forward noising process, allowing for better integration of geometric and semantic information from the data. Their experiments demonstrate that this approach significantly improves distribution matching and reduces errors compared to traditional methods, suggesting that structured terminal laws could enhance the modeling of complex data landscapes.

### 7. AHA-WAM:Asynchronous Horizon-Adaptive World-Action Modeling with Observation-Guided Context Routing
**Authors:** Jisong Cai, Long Ling, Shiwei Chu, Zhongshan Liu, Jiayue Kang, Zhixuan Liang, Wenjie Xu, Yinan Mao, Weinan Zhang, Xiaokang Yang, Ru Ying, Ran Zheng, Yao Mu
**Link:** https://arxiv.org/abs/2606.09811v1
**Summary:** The paper presents AHA-WAM, an innovative model that improves robot manipulation by decoupling world prediction and action execution, addressing the inefficiencies of existing world-action models. Using a dual Diffusion Transformer architecture, AHA-WAM allows for asynchronous processing, enabling the robot to effectively plan with long-term scene context while executing actions in real-time. The approach demonstrates significant performance improvements, achieving a 92.80% success rate on simulated tasks and 78.3% on real-world tasks, with a notable speed advantage in control execution.

### 8. Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting
**Authors:** Avijit Ghosh, Anka Reuel, Jenny Chim, Wm. Matthew Kennedy, Srishti Yadav, Jennifer Mickel, Yanan Long, Andrew Tran, Anastassia Kornilova, Damian Stachura, Kevin Klyman, Felix Friedrich, Jeba Sania, Max Lamparth, Jan Batzner, Anoop Mishra, Eliya Habba, Yixiong Hao, Nathan Heath, Shalaleh Rismani, Usman Gohar, Andrea Loehr, David Manheim, Ruchira Dhar, Sree Harsha Nelaturu, Aarush Sinha, Leshem Choshen, Drishti Sharma, Ishan Khire, Amit Saha, Subramanyam Sahoo, Michael Hardy, Michael Alexander Riegler, Kabir Manghnani, Michelle Lin, Yanan Jiang, Yilin Huang, Asaf Yehudai, Jessica Ji, Aris Hofmann, Mubashara Akhtar, Nuno Moniz, Yacine Jernite, Stella Biderman, Zeerak Talat, Sanmi Koyejo, Mykel Kochenderfer, Irene Solaiman
**Link:** https://arxiv.org/abs/2606.09809v1
**Summary:** The paper addresses the inconsistent reporting of AI evaluation results that makes it difficult for readers to compare findings across different sources. The authors introduce \EvalCards{}, a structured reporting framework that combines various evaluation data into a unified format, and they develop interpretive signals to aid understanding for different audiences. Their implementation revealed widespread gaps in current reporting practices across a large number of AI models and benchmarks.

### 9. Topological Neural Operators
**Authors:** Lennart Bastian, Samuel Leventhal, Mustafa Hajij, Tolga Birdal
**Link:** https://arxiv.org/abs/2606.09806v1
**Summary:** The paper presents Topological Neural Operators (TNOs), a new framework for learning mathematical operators on complex shapes by using features defined on topological cells of different dimensions. By integrating Discrete Exterior Calculus, TNOs enable effective modeling of interactions across these cells while maintaining the physical integrity of data. The results show that TNOs, especially through Hierarchical TNOs (HTNOs), significantly enhance the accuracy of solutions for various partial differential equations (PDEs), particularly in irregular geometries.

### 10. Echo-Memory: A Controlled Study of Memory in Action World Models
**Authors:** Wayne King, Zeyue Xue, Yuxuan Bian, Jie Huang, Haoran Li, Yaowei Li, Yaofeng Su, Yuming Li, Haoyu Wang, Shiyi Zhang, Songchun Zhang, Yuwei Niu, Sihan Xu, Junhao Zhuang, Haoyang Huang, Nan Duan
**Link:** https://arxiv.org/abs/2606.09803v1
**Summary:** The paper addresses the issue of memory failures in action-conditioned world models, which often lose track of scene details after a camera moves away. The authors introduce Echo-Memory, a systematic framework to evaluate various memory mechanisms by controlling all factors except for how memory is stored and retrieved. Their key finding is that while raw context significantly enhances the model's ability to recall scenes, more compact memory solutions compromise key details, and a specific state-space recurrence strategy proves to be the most effective for maintaining accurate scene representation in open-domain scenarios.
