---
## 2026-09-29

### 1. FurE: Efficient Instance-Specific 3D Fur Reconstruction without Animal-Fur Datasets
**Authors:** Srinjay Sarkar, Prakhar Kaushik, Soumava Paul, Alan Yuille
**Link:** https://arxiv.org/abs/2609.35770v1
**Summary:** The paper introduces FurE, a method for efficiently reconstructing realistic animal fur from multi-view images, addressing the challenge of lacking animal-fur datasets and the intricate details involved. The approach utilizes a latent field optimized for individual fur strands, combined with a PCA-based decoder and local thickness cues for realistic representation. Key results include a tenfold speedup in training time while maintaining high fidelity and versatility across both synthetic and real-world scenarios.

### 2. Telescopic Language Models
**Authors:** Zhilin Guo, Boqiao Zhang, Hakan Aktas, Kyle Fogarty, Nursena Koprucu Aslan, Wenzhao Li, Canberk Baykal, Albert Miao, Siyu Hong, Yixiao Liu, Adam Wu, Ashish Kumar Singh, Sakar Khattar, Chenliang Zhou, Weihao Xia, Cristina Nader Vasconcelos, Cengiz Oztireli
**Link:** https://arxiv.org/abs/2609.35769v1
**Summary:** The paper presents a Telescopic Language Model (TLM) designed to efficiently serve various computational budgets without the need for separate training runs. By using a nested-capacity Transformer trained with stochastic prefix supervision, the model maintains performance across different depths while reducing training costs. The key contribution is a 43-44% reduction in the area under the quality-budget curve compared to traditional fixed-exit models, while also achieving similar performance at full capacity with lower GPU costs.

### 3. PDMD: Projected Distribution Matching Distillation for Video Diffusion Models
**Authors:** Zimo Wang, Junkun Yuan, Angtian Wang, Haotian Yang, Canyu Zhang, Siyuan Yuan, Xingchang Huang, Bo Liu, Yizhi Wang, Yiding Yang, Chongyang Ma, Gordon Guocheng Qian
**Link:** https://arxiv.org/abs/2609.35768v1
**Summary:** The paper addresses the issue of degradation in sample quality during the training of video diffusion models using Distribution Matching Distillation (DMD), which can result in oversaturation and artifacts. The authors propose a new method called Projected Distribution Matching Distillation (PDMD), which filters out errors from the critic during updates, stabilizing training and enhancing sample quality. Key results show that PDMD improves performance on multiple benchmarks, surpassing the original DMD significantly while requiring minimal code changes and additional computational resources.

### 4. Learning Native Reflection in Unified Models with Interleaved Reinforcement Learning
**Authors:** Yijia Fan, Ziqi Huang, Zhongang Cai, Yan Li, Zimo Wen, Wanqi Yin, Haiwen Diao, Ziwei Liu
**Link:** https://arxiv.org/abs/2609.35767v1
**Summary:** The paper addresses the challenge of improving image generation by allowing unified multimodal models to assess and correct their own outputs through a feedback loop. The authors introduce a method called UMM-Reflection, which uses reinforcement learning to jointly optimize the model's reflection and image revision processes across multiple iterations. The key contribution is a substantial improvement in evaluation scores compared to supervised fine-tuning, demonstrating the effectiveness of this approach on various benchmarks without relying on external validation during inference.

### 5. Retrieving Biblical Intertextual References in Karen Blixen's Seven Gothic Tales
**Authors:** András Kovács, Alexander Conroy, Daniel Hershcovich, Jens Bjerring-Hansen
**Link:** https://arxiv.org/abs/2609.35765v1
**Summary:** This paper addresses the challenge of recognizing biblical references in Karen Blixen's *Seven Gothic Tales*, which often employs nuanced paraphrases and allusions. The authors developed a benchmark of annotated references and evaluated various retrieval models, including TF-IDF and BM25, as well as fine-tuned sentence encoders. They found that while models can effectively retrieve known references, their outputs also suggest meaningful additional connections, highlighting their role as tools that assist scholars rather than definitive sources for literary analysis.

### 6. Unifying Distributional Training for One-Step Visual Generation
**Authors:** Chi Zhang, Haoyang Shi, Yueyi Liu, Ruichuan An, Junkang Zhou, Chang Li, Xiuyuan Lu, Yichi Zhang, Bo Wang, Yuhang Wu, Sen Cui, Miao Liu
**Link:** https://arxiv.org/abs/2609.35763v1
**Summary:** The paper addresses the challenge of improving one-step visual generation by proposing a unified framework for distributional training that enhances the connection between feature matching and distribution modeling. This framework led to the development of MGFlow, which effectively uses Gaussian mixtures to model feature distributions and mitigate issues like mode collapse. The key contribution is that MGFlow significantly outperforms existing methods, achieving state-of-the-art results in both image generation and text-to-image generation tasks.

### 7. Scaling Long-Form Story Generation via Narrative State Tracking
**Authors:** Zhennan Wan, Jianfei Chen
**Link:** https://arxiv.org/abs/2609.35759v1
**Summary:** The paper addresses the challenge of maintaining narrative consistency in long-form story generation with large language models (LLMs) as they scale up to full-length novels. The authors introduce NstAgent, a framework that allows LLMs to effectively track key narrative elements such as characters and events without requiring additional training. The key finding is that NstAgent improves both narrative consistency and writing quality for stories ranging from 10,000 to 100,000 words, effectively supporting longer story generation.

### 8. TokenCast: Forecasting Token Consumption During LLM Agent Execution
**Authors:** Chaoqian Ouyang, Ling Yue, Libin Zheng, Huanghui Guo, Shengxiang Xu, YiShu Wang, Ran Li, Jian Yin, Shaowu Pan, Shimin Di
**Link:** https://arxiv.org/abs/2609.35760v1
**Summary:** The paper addresses the unpredictability of token consumption when large language model (LLM) agents execute tasks, which can vary significantly with each run. The authors introduce TokenCast, a method that tracks and predicts token usage by learning a composable representation of execution segments, allowing the model to adjust forecasts based on new information without additional LLM calls. Key results show that TokenCast reduces prediction errors by an average of 14.5% and uses 21.3% fewer tokens compared to traditional budget policies.

### 9. Statistical Learning of Contractive Dynamical Representations for Composite Adaptive Control
**Authors:** Min Kim, José Leonardo Brenes, Fred Hadaegh, Soon-Jo Chung
**Link:** https://arxiv.org/abs/2609.35758v1
**Summary:** The paper addresses the challenge of tracking control in the presence of dynamically coupled disturbances by developing a statistical learning framework that identifies and exploits latent representations of these disturbances. Using a hard expectation-maximization procedure with a Kalman smoother, the method learns to predict disturbance behavior while ensuring stable control. The key contribution is a composite adaptive tracking controller that demonstrates enhanced disturbance prediction and improved performance in experimental tests on various systems, outperforming traditional approaches.

### 10. Neural Harmonic Measure Operator
**Authors:** Jinjin He, Sinan Wang, Yuchen Sun, Bo Zhu
**Link:** https://arxiv.org/abs/2609.35752v1
**Summary:** The paper presents the Neural Harmonic Measure Operator (NHMO), a neural network-based method designed to efficiently solve elliptic partial differential equations (PDEs) on domains with variable shapes. By parameterizing the harmonic measure using a transformer-based approach, NHMO allows for quick adaptations to different boundary conditions without retraining. The results show that NHMO outperforms existing methods on benchmark tests, demonstrating its effectiveness and versatility in solving these types of PDE problems.
