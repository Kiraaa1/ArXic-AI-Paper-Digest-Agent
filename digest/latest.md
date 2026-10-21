---
## 2026-10-21

### 1. Joints, Camera, Action! Co-Generating 3D Motion and Video for Arbitrary Rigs
**Authors:** Noam Rotstein, Yoad Tewel, Chen Tessler, Haggai Maron, Gal Chechik, Or Litany, Yoni Kasten, Yuval Atzmon
**Link:** https://arxiv.org/abs/2610.28632v1
**Summary:** The paper addresses the challenge of converting realistic video motions into replayable 3D animations for various skeleton rigs, which traditional video models struggle to do. The authors propose a model that separates 3D motion generation from video creation, allowing them to first learn motion patterns and then integrate them with a pretrained video model using cross-attention layers. The key contribution is the successful co-generation of video and 3D motion for arbitrary rigs, enabling accurate animation and scene integration while allowing flexible control and editing of the generated content.

### 2. GBClaw: An agentic AI framework for atomistic grain boundary research and mechanistic discovery
**Authors:** Yazhuo Liu, Kunqing Ding, Xiaoguo Gong, Zifeng Wang, Yichen Yang, Yifeng Che, Wen Chen, Josh Kacher, Olivier Pierron, Shigenobu Ogata, Ting Zhu
**Link:** https://arxiv.org/abs/2610.28629v1
**Summary:** The paper introduces GBClaw, an AI framework designed to automate the investigation of grain boundaries in polycrystalline materials, which are often complex and difficult to study. By integrating large language models with specialized tools and adaptive workflows, GBClaw facilitates both simulations and detailed mechanistic analyses. The study applied this framework to 14 asymmetric tilt grain boundaries in nickel, revealing significant insights into interfacial defects and deformation modes, particularly highlighting the importance of defect hierarchies on shear strength.

### 3. Learning Adaptable Dexterous Skills via Hybrid Dexterous Mimicking
**Authors:** Yuxuan Kuang, Jiashun Wang, Yixuan Sun, Yufei Ye, Sungjae Park, Umar Iqbal, Katerina Fragkiadaki, Shubham Tulsiani
**Link:** https://arxiv.org/abs/2610.28628v1
**Summary:** The paper addresses the challenge of teaching robotic hands to perform versatile and reliable dexterous skills, a task complicated by the trade-offs in existing learning methods. The authors introduce AdaDex, a goal-conditioned reinforcement learning framework that combines human motion data with generalization techniques to train adaptable skills from brief motion capture clips. Their approach enables the resulting robotic policies to execute a range of dexterous tasks effectively, outperforming existing methods in terms of adaptability and functionality across different environments.

### 4. UniWALM: Unified World Action Language Model for Embodied Robot Control
**Authors:** Rahul Sajnani, Diego Romeres, Mingyuan Zhang, Kai Gao, Carl Qi, Baichuan Huang, Srinath Sridhar, Dylan Randle, Lillian J. Ratliff, Jose Barreiros, Manikantan Nambi, Jeroen Vanbaar
**Link:** https://arxiv.org/abs/2610.28626v1
**Summary:** The paper presents UniWALM, a unified model that integrates video, actions, and language for controlling robots, aiming to enhance manipulation tasks by allowing the model to generate and utilize language as a form of memory during action execution. The key innovation lies in its mixture-of-transformers architecture, which processes all three modalities simultaneously without needing separate planning phases, leading to improved performance in various tasks, including a significant increase in success rates in a real-world item-finding challenge from 11.1% to 61.1%.

### 5. Industrial ReMEmbR: Scaling Spatiotemporal Memory to Robot Fleets
**Authors:** Jad Yammine, Malek Wahidi, Abrar Anwar, Yan Chang, Mihir Acharya, Anthony Rizk
**Link:** https://arxiv.org/abs/2610.28624v1
**Summary:** The paper addresses the high computational, communication, and storage costs associated with maintaining reusable semantic memory in warehouse robot fleets that monitor operational conditions. It introduces IndustrialReMEmbR, a spatiotemporal memory system that optimizes this process by generating scene descriptions only when needed and offloading computational tasks between the robots and a server. The key outcome is a more efficient memory retrieval system that maintains functionality while reducing the need for raw data transfer and processing, enabling GDPR compliance by abstracting personally identifiable information.

### 6. Planning under Noise with Neural Operators
**Authors:** Michael Chen, Hong Chul Nam, Xi Deng, Anima Anandkumar
**Link:** https://arxiv.org/abs/2610.28623v1
**Summary:** The paper addresses the challenge of planning in environments where control execution is affected by noise, which complicates navigation. It introduces a method called Planning Under Noise (PUN), which uses neural operators to learn noise-aware value fields and efficiently compute paths that navigate around obstacles while maintaining feedback for planning. The key contribution is that PUN outperforms existing planners by achieving high success rates and faster runtimes, particularly in complex, noisy conditions, making it effective for planning tasks in high-dimensional spaces.

### 7. MindView: Benchmarking Generative Multi-View Spatial Intelligence
**Authors:** Yanbo Wang, Siqi Luo, Siyu Zhang, Chenming Zhu, Wenzhao Zheng, Qian Yu, Juncheng Yan, Bin Fu, Tai Wang, Yu Qiao, Yihao Liu, Jiwen Lu
**Link:** https://arxiv.org/abs/2610.28622v1
**Summary:** The paper introduces MindView, a benchmark designed to evaluate generative models' ability to create spatially consistent views from partial multi-view observations in indoor scenes. By testing eleven generators on the benchmark, the authors discovered a significant performance gap, leading them to fine-tune the BAGEL model, which improved its score markedly across multiple tasks. Additionally, they propose MindCue, a method that enhances evidence utilization in expanded contexts, further demonstrating the utility of learning to generate spatially grounded views for better spatial understanding.

### 8. Adaptive Multi-Token Prediction: How far should we go?
**Authors:** Emile Anand, Mohammed Rehan Parwani, Xinyuan Cao
**Link:** https://arxiv.org/abs/2610.28619v1
**Summary:** The paper addresses the issue of optimizing multi-token prediction in language models, where determining the optimal number of tokens to draft can be context-dependent. The authors propose Adaptive Multi-Token Prediction (AMTP), a lightweight control mechanism that uses feedback from previous predictions to select the most efficient drafting horizon without needing retraining. Their experiments show that AMTP can significantly accelerate decoding—up to 4.1 times faster than traditional methods—while achieving competitive or superior performance across various settings.

### 9. Efficient Edge-aware Attention Network for Graph Generation
**Authors:** Vincent Jung, Alba Carballo-Castro, Yiming Qin, Lonneke van der Plas, Pascal Frossard
**Link:** https://arxiv.org/abs/2610.28618v1
**Summary:** The paper addresses the limitations of existing graph generative models that struggle with scalability due to their reliance on traditional Transformer architectures. The authors introduce an edge-aware attention layer that efficiently incorporates structural information and updates edge representations, leading to significant reductions in GPU memory usage by approximately 65%, while maintaining generation quality and enhancing training and sampling efficiency. This innovative approach represents a significant advancement toward practical scalable graph foundation models.

### 10. NarraSpace: Multimodal Scene-Grounded Evidence for Picture-Description Dementia Classification
**Authors:** Qingming Li, Ruiyan Sun, Satoshi Nakamura
**Link:** https://arxiv.org/abs/2610.28616v1
**Summary:** NarraSpace addresses the challenge of classifying dementia through picture descriptions by analyzing the relationship between spoken words and visual scene elements in the speech data. The approach utilizes a frozen language model to evaluate the narrative structure and timing of speech related to predefined scene events, linking these back to specific utterances. Key results show that this method achieved an accuracy of approximately 80.88% in identifying Alzheimer's disease among participants, providing a clear, evidence-based way for clinicians to review and assess picture descriptions.
