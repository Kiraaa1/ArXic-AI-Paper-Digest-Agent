---
## 2026-10-03

### 1. Hierarchical Continuous Diffusion Language Models
**Authors:** Hui Ren, Zihan Li, Chang Liu, Huidong Liu, Alexander Schwing
**Link:** https://arxiv.org/abs/2610.02193v1
**Summary:** The paper introduces Hierarchical Continuous Diffusion Language Models (HC-DLM) to improve the generation of language by effectively coupling discrete token generation with a continuous latent state. This approach addresses the limitations of existing models that sample independent tokens, enhancing performance in structured reasoning, mathematical planning, and language modeling tasks. The key contributions demonstrate that HC-DLM outperforms both discrete and continuous diffusion baselines in accuracy and perplexity for specific applications.

### 2. The Missing Primitive: Diagnosing and Repairing Mathematical Reasoning in Large Language Models
**Authors:** Shuo Xing, Zilin Dai, Chengyuan Qian, Fangzhou Lin, Wenjing Chen, Ping He, Pan Lu, Alvaro Velasquez, Mohit Bansal, Zhengzhong Tu
**Link:** https://arxiv.org/abs/2610.02191v1
**Summary:** This paper addresses the issue of understanding how well Large Language Models (LLMs) grasp mathematical concepts beyond just producing correct answers. The authors introduce a benchmark called \hlei{} to evaluate different aspects of mathematical reasoning and find that a lack of discovery skills is a major limitation in LLM performance. They then propose a new framework, \abs{}, that enhances LLMs' mathematical reasoning abilities by focusing on improving these discovery skills, showing significant performance gains across various model scales and benchmarks.

### 3. Trust the Direction, Search the Step: Zero-and-First-Order Methods for LLM Fine-Tuning
**Authors:** Cristian McGee, El Houcine Bergou, Aritra Dutta
**Link:** https://arxiv.org/abs/2610.02190v1
**Summary:** The paper addresses the challenge of selecting step sizes in large-scale neural network optimization, which can either slow convergence or destabilize training. The authors propose a novel framework called Zero-and-First-Order (ZFO) that separates the selection of optimization direction from step size, using a trusted first-order optimizer for direction and zeroth-order evaluations to determine the optimal step size. Their approach demonstrates significant improvements in optimization efficiency and performance for language model fine-tuning compared to traditional fixed-step methods.

### 4. Generative modeling of intrinsically disordered protein regions by reinforcing sparse autoencoder features
**Authors:** Jason X. Liu, Sebastian Ibarraran, Frank Hu, Soojung Yang, Xinyu A. Feng, Abigail Park, Anagha Aneesh, Lacramioara Bintu, Alexander R. Dunn, Grant M. Rotskoff
**Link:** https://arxiv.org/abs/2610.02189v1
**Summary:** The paper addresses the challenge of designing intrinsically disordered protein regions (IDRs), which are crucial for various cellular processes but difficult to model. The authors introduce IDiom, a specialized autoregressive protein language model trained on a vast dataset of predicted IDRs, and enhance it with a reinforcement learning approach that uses sparse autoencoder features to generate sequences that meet specific functional criteria. The key finding is that this method significantly improves the ability to produce IDRs that accurately reflect their natural functional properties and facilitates the combination of diverse biological features within single sequences.

### 5. DMAD: Distribution Matching as Adversarial Distillation for Fast Visual Generation
**Authors:** Zhengming Yu, Junkun Yuan, Haotian Yang, Gordon Guocheng Qian, Yizhi Wang, Angtian Wang, Yiding Yang, Bo Liu, Xin Li, Wenping Wang, Chongyang Ma
**Link:** https://arxiv.org/abs/2610.02188v1
**Summary:** The paper presents DMAD, a novel approach for fast visual generation that improves upon Distribution Matching Distillation (DMD) by using adversarial training to directly learn log-density ratios instead of relying on an auxiliary diffusion model. By employing two discriminator heads to distinguish between real and generated samples, DMAD eliminates the need for additional memory and computation while achieving state-of-the-art performance. The key results show significant improvements in generation quality, measured by Fréchet Inception Distance (FID) and human preference rates, outperforming previous methods in both single and multi-step generation tasks.

### 6. Higher-Order Molecular Grammars for Generative and Foundation Models in Chemistry
**Authors:** Yiming Huang, Yujie Zeng, Vijay Prakash Dwivedi, Simone Foti, Jianmin Wang, Jure Leskovec, Tolga Birdal
**Link:** https://arxiv.org/abs/2610.02186v1
**Summary:** The paper addresses the limitations of existing molecular learning models in accurately representing complex molecular structures, particularly those with higher-order topology. It introduces a new framework called Higher-order Grammar Representation (HGR) that encodes these structures in a compact and computationally efficient manner using context-free grammars. The authors demonstrate that HGR-based models achieve 100% validity in molecular generation while outperforming existing methods in representation learning benchmarks, thereby proving its effectiveness for generating valid molecules and improving transfer learning in chemistry.

### 7. Decoding Looped Transformers Better for (Almost) Free
**Authors:** Weihao Liu, Huangjie Zheng, Tianrong Chen, Rohit Dilip, Richard He Bai, Yizhu Jiao, Yuyang Wang, Ruixiang Zhang
**Link:** https://arxiv.org/abs/2610.02185v1
**Summary:** The paper addresses the inefficiency in traditional decoding methods used in Looped Transformers, which typically discard earlier states during token prediction. The authors introduce LoopCD, a framework that enhances decoding by contrasting final predictions with earlier recurrent states, either in logit space or hidden-state space. This approach significantly improves decoding performance while allowing for a reduction in the number of required loops, leading to a substantial decrease in computational cost without sacrificing accuracy.

### 8. SoftServe: A Scalable Quasi-Newton Method for Deep Learning
**Authors:** Joohwan Ko, Tetiana Parshakova, Diana Cai, Robert M. Gower
**Link:** https://arxiv.org/abs/2610.02182v1
**Summary:** The paper presents SoftServe, a new family of quasi-Newton methods designed to improve optimization in deep learning, particularly for non-convex problems with large parameter sizes. By deriving positive-definite curvature estimates without the need for line searches and using GPU-friendly matrix operations, SoftServe effectively addresses challenges in training deep networks, outperforming established optimization baselines on various ill-conditioned tasks.

### 9. Generative Cinematographer: Composing Camera and Object Motion in 3D
**Authors:** Jiahan Zhang, Chaohao Yang, Namitha Guruprasad, Vivekjyoti Banerjee, Trong-Tung Nguyen, Alan Yuille, Anand Bhattad
**Link:** https://arxiv.org/abs/2610.02180v1
**Summary:** The paper addresses the challenge of accurately controlling 3D object and camera motions in video generation, which can be ambiguous with existing 2D motion controls. The authors introduce the Generative Cinematographer (GenCine), a system that creates an editable 3D scene from a single image, allowing artists to manipulate both camera paths and object motions using intuitive 3D handles. The key contribution is a method that produces consistent camera-relative motion and improves geometric accuracy in generated videos, enhancing the control artists have over dynamic 3D scenes.

### 10. From Gradients to Capabilities: Understanding Multi-Teacher On-Policy Distillation
**Authors:** Siqi Zhu, Suozhi Huang, Kaixuan Zhang, Yuheng Yang, Zhanyang Jin, Yihang Sun, Jiaxuan You
**Link:** https://arxiv.org/abs/2610.02179v1
**Summary:** The paper examines how to effectively combine the strengths of multiple reinforcement learning (RL) teachers into a single student model using a method called multi-teacher on-policy distillation (MOPD). By analyzing the impacts of various factors such as loss averaging and optimizer updates on model training, the authors found that certain strategies for combining teacher signals can significantly affect the learning performance of the student, revealing complexities in how teacher gradients influence final outcomes. Their findings indicate that different averaging methods can lead to notable differences in task performance, emphasizing the importance of signal manipulation in multi-teacher settings.
