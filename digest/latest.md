---
## 2026-08-26

### 1. What FID Hides: Detecting, Ranking, and Diagnosing Deviations in Generative Evaluation
**Authors:** Hao Chen
**Link:** https://arxiv.org/abs/2608.24881v1
**Summary:** The paper addresses the limitations of Fréchet Inception Distance (FID) in evaluating generative models, particularly its inability to capture distributional differences and directionality in dispersion changes. To overcome this, the authors introduce a new metric called ZID (Z-resolved Integrated Diagnostic) that provides a more comprehensive analysis by offering multiple outputs: a magnitude ranking, a statistical test for distribution equality, and a signed dispersion diagnosis. The key finding is that ZID can detect a wider range of deviations in generative outputs, including cases where FID fails to indicate issues, such as mode collapse.

### 2. Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses
**Authors:** Zhaochen Yu, Yingcheng Wu, Zhenfei Yin, Kaiyuan Chen, Zhe Zhao, Mengdi Wang, Shuicheng Yan, Ling Yang
**Link:** https://arxiv.org/abs/2608.24876v1
**Summary:** The paper addresses the challenges of recursive self-improvement (RSI) in long-horizon tasks, where agents struggle to effectively utilize their accumulated experiences due to complex histories. It introduces Recuris, an innovative memory architecture that combines Working Memory and Experiential Memory to prioritize current task needs and improve skill selection. The key result demonstrates that Recuris significantly enhances task success rates across multiple benchmarks, achieving state-of-the-art performance and dramatically reducing common failures in long-horizon scenarios.

### 3. SPO++: Stream-Aligned Policy Optimization for Asynchronous Agentic RL
**Authors:** Kai Ruan, Jinghao Lin, Qianshan Wei, Ziqi Zhou, Zihe Huang
**Link:** https://arxiv.org/abs/2608.24870v1
**Summary:** The paper addresses inefficiencies in group-relative reinforcement learning due to waiting for simultaneous rollouts, particularly when using tools in variable-length tasks. The authors introduce an improved method called SPO++, which standardizes the advantages based on action-token measures to enhance learning efficiency. Their results show that SPO++ outperforms the original SPO method in terms of online learning efficiency during experiments on ALFWorld and Math-TIR.

### 4. Parameterized Complexity of $L_p$-Lipschitz Constants for Input Convex Neural Networks and $L_p$-Norm Maximization over Zonotopes
**Authors:** Aritra Das, Vincent Froese, Moritz Grillo, Debayan Gupta, Christoph Hertrich, Tharrshann Jayan Logarajah, Georg Loho, Mihir More, Moritz Stargalla
**Link:** https://arxiv.org/abs/2608.24865v1
**Summary:** This paper addresses the challenging problem of calculating Lipschitz constants for two-layer input-convex neural networks, which measure how sensitive these networks are to small input changes. The authors prove that maximizing the $L_p$-norm over zonotopes is W[1]-hard for every fixed rational \( p \) between 1 and infinity, indicating that efficient algorithms for this problem are unlikely under certain computational assumptions. Their results clarify the parameterized complexity landscape of these calculations and provide key insights into the underlying mathematics.

### 5. Improving Cross-Problem Vehicle Routing with Locally Augmented Preferences and Representation Disentanglement
**Authors:** Arthur Corrêa, Paulo Nascimento, Samuel Moniz
**Link:** https://arxiv.org/abs/2608.24859v1
**Summary:** The paper addresses the challenge of improving multi-task vehicle routing problem (VRP) solvers that struggle with effectiveness in training and generalization across different VRP variants. The authors introduce two key innovations: a training algorithm called POLAR that enhances reward signals by refining the best solution before forming preference pairs, and a new encoder architecture called PLE that disentangles shared and variant-specific representations. Their approach significantly improves performance, reducing the gap to optimal solutions by 21.3% relative to the best existing models on multiple VRP variants, and outperforms previous methods on most unseen variants.

### 6. Bellman Calibration for Marginalized Importance Weighting in Offline Reinforcement Learning
**Authors:** Lars van der Laan, Nathan Kallus
**Link:** https://arxiv.org/abs/2608.24858v1
**Summary:** The paper addresses the issue of residual occupancy-balance violations that can arise in offline reinforcement learning when evaluating policies using marginalized importance weighting. It proposes a new method called isotonic Bellman calibration, which is a model-agnostic technique that adjusts the estimated occupancy ratio to improve its accuracy while maintaining essential ranking information. The key contribution is that this method achieves small calibration error and provides guarantees on its performance, making it effective for policy evaluation tasks in offline settings.

### 7. BrowserForge: Scaling Web Episode via Parallel Browser Sandboxes
**Authors:** Fei Tang, Huawen Shen, Zhiqiong Lu, Zhengxi Lu, Pengyuan Lyu, Chengquan Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
**Link:** https://arxiv.org/abs/2608.24848v1
**Summary:** The paper introduces BrowserForge, a framework designed to generate large-scale web interaction data for training web agents that operate on rendered pixels, overcoming the limitations of traditional datasets. By utilizing a parallel management system to drive multiple browser sandboxes and exposing agents to a diverse array of real websites, BrowserForge successfully collected over 203,000 unique interaction trajectories. This extensive dataset significantly enhances the performance of a multimodal model, increasing its success rate on web tasks by nearly 8% when fine-tuned on this richer corpus.

### 8. FedV-KGQA: Multi-Hop Question Answering over Vertically Partitioned Knowledge Graphs
**Authors:** Md Saikat Islam Khan Bappy, Oshani Seneviratne
**Link:** https://arxiv.org/abs/2608.24846v1
**Summary:** The paper introduces FedV-KGQA, a framework designed to enable multi-hop question answering over knowledge graphs that are distributed across different organizations without centralizing the data. It utilizes local graph enrichment and knowledge graph embeddings while ensuring that sensitive data remains siloed, and incorporates a novel mechanism to anchor questions within the appropriate data context. The results demonstrate that FedV-KGQA effectively achieves performance similar to centralized systems and can handle complex 3-hop reasoning tasks while being resilient to changes in the data embeddings.

### 9. LAION-BVD: A 10-Million-Hour Open Video Dataset for Multimodal Pre-training
**Authors:** Andreas Hochlehnert, Marianna Nezhurina, Mehdi Cherti, Andrej Radonjic, Thaddäus Wiedemer, Christoph Schuhmann, Romain Beaumont, Wieland Brendel, Bernhard Schölkopf, A. Sophia Koepke, Jenia Jitsev, Matthias Bethge
**Link:** https://arxiv.org/abs/2608.24845v1
**Summary:** The paper introduces LAION-BVD, a massive open video dataset aimed at enhancing multimodal learning by providing 80 million videos totaling 10 million hours of content, collected from CommonCrawl. By utilizing techniques like content-aware scene detection to extract video clips and generate synthetic captions, the dataset enables models to significantly improve performance on video-text and audio-text tasks. The release of LAION-BVD vastly increases access to multimodal video resources for researchers.

### 10. Reading Is Not Using: Retrieval, Judgment, and the Design of AI Financial Research Workflows
**Authors:** Miao Liu, Zhizhe Liu
**Link:** https://arxiv.org/abs/2608.24842v1
**Summary:** The paper addresses the issue of how AI systems, particularly large language models, often retrieve relevant financial information but fail to integrate it effectively into investment judgments. Through experiments varying the context length in financial analysis, the authors find that even accurate retrieval does not translate to improved decision-making, highlighting a "retrieval-integration gap." They suggest that the design of AI workflows significantly affects how well models incorporate retrieved information, emphasizing the need for structured approaches to enhance judgment accuracy in financial AI applications.
