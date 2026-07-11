---
## 2026-07-11

### 1. Workflow as Knowledge: Semantic Persistence for LLM-Mediated Workflows
**Authors:** Emanuele Quinto, Carlo Andrea Rozzi, Francesco Zanitti
**Link:** https://arxiv.org/abs/2607.08740v1
**Summary:** This paper addresses the challenge of managing workflows in large language model (LLM) applications by proposing a new conceptual model for representing workflows as persistent knowledge objects. The authors introduce a framework that distinguishes between deterministic computation (derive) and LLM-mediated judgment (infer), allowing workflows to be more inspectable, resumable, and reviewable. This contributes to a better understanding of how workflows can encapsulate knowledge beyond merely producing outputs, setting the stage for future work on formalizing these concepts.

### 2. The Illusion of Equivalency: Statistical Characterization of Quantization Effects in LLMs
**Authors:** Baha Rababah, Cuneyt Gurcan Akcora, Carson K. Leung
**Link:** https://arxiv.org/abs/2607.08734v1
**Summary:** The paper addresses the limitations of traditional accuracy metrics in evaluating post-training quantization of large language models (LLMs), which can mask significant behavioral changes. The authors introduce a new metric, correctness agreement, to assess the alignment of correct predictions between base and quantized models, revealing that noticeable behavioral divergences occur even when accuracy seems unchanged. Key findings include that quantization distorts attention weights variably across different layers, particularly affecting query and key projections, challenging the notion that quantized models can seamlessly match their full-precision counterparts.

### 3. Super Weights in LLMs and the Failure of Selective Training
**Authors:** Shreyas Subramanian, Adewale Akinfaderin, Akarsha Sehwag
**Link:** https://arxiv.org/abs/2607.08733v1
**Summary:** The paper investigates the concept of Super Weights in large language models (LLMs), which are crucial parameters whose removal severely impacts performance. The authors found that training these Super Weights in isolation leads to a dramatic drop in accuracy, suggesting that their significance doesn't translate to effective training. Instead, they emphasize that successful fine-tuning requires a broader, structured approach rather than focusing solely on these seemingly important parameters.

### 4. Validity of LLMs as data annotators: AMALIA on authority
**Authors:** Manuel Pita
**Link:** https://arxiv.org/abs/2607.08731v1
**Summary:** The paper evaluates the effectiveness of Portugal's AMALIA language model in accurately coding the moral foundation of authority compared to trained human coders. By breaking down the coding process into smaller components, the authors found that AMALIA's performance significantly dropped, indicating that it relies more on surface-level correlations than on a deep understanding of the theoretical construct. This study highlights the need for comprehensive testing of language models beyond mere agreement with human coders to ensure they are genuinely capturing the intended concepts.

### 5. Pose-to-Biomechanics: Bridging 3D Human Pose Estimation and Biomechanical Attribute Prediction
**Authors:** Ayda Eghbalian, Kevin Desai
**Link:** https://arxiv.org/abs/2607.08725v1
**Summary:** This paper addresses the challenge of translating accurate 3D human pose estimates into useful biomechanical information for applications in fields like rehabilitation and sports science. The authors introduce BioModule, a flexible tool that connects to existing pose estimators and predicts biomechanical attributes without altering the underlying models. Their findings demonstrate that BioModule effectively bridges the gap between pose estimation and biomechanical analysis, enhancing the practical utility of pose estimation technologies.

### 6. Latent Memory Palace: Reasoning for Control as Autoregressive Variational Inference
**Authors:** Chuning Zhu, Eva Xu, Jose Barreiros, Krishnan Srinivasan, Paarth Shah, Abhishek Gupta
**Link:** https://arxiv.org/abs/2607.08724v1
**Summary:** The paper addresses the challenge of enabling continuous control policies to exhibit adaptive reasoning similar to human decision-making. The authors propose a method called Latent Memory Palace (LMP), which organizes information in an autoregressive latent space and uses variational inference to optimize decision-making processes. The key contribution is that LMP demonstrates strong performance in both simulation and real-world tasks while providing interpretable and flexible compute allocation, as well as improving downstream policy performance with a variable-length action tokenizer.

### 7. Deep Learning for Joint Narrowband Interference Cancellation and Soft Demodulation in OFDM Systems
**Authors:** Emmanouil Kavvousanos, Francky Catthoor, Vassilis Paliouras
**Link:** https://arxiv.org/abs/2607.08717v1
**Summary:** The paper addresses the challenge of narrowband interference (NBI) in orthogonal frequency-division multiplexing (OFDM) systems, which can significantly degrade performance and lead to high error rates. The authors propose a deep learning framework that jointly cancels NBI and performs soft demodulation, using a convolutional network to effectively estimate and remove interference while handling non-Gaussian residuals. Key results show that this approach significantly reduces computational complexity and eliminates error floors, achieving near-optimal performance even under severe interference conditions.

### 8. Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents
**Authors:** Yifan Wu, Lizhu Zhang, Yuhang Zhou, Mingyi Wang, Bo Peng, Serena Li, Xiangjun Fan, Zhuokai Zhao
**Link:** https://arxiv.org/abs/2607.08716v1
**Summary:** The paper addresses the issue of "behavioral state decay," where important decision-making information can be lost in long-horizon tasks. To combat this, the authors propose a proactive memory agent that actively updates and manages a memory bank, reminding the action agent of relevant past experiences as needed. This method significantly improves action agents' performance in benchmark tests, achieving notable gains in decision-making effectiveness.

### 9. LTM: Large-scale Terrain Model for Wildfire-prone Landscapes
**Authors:** Xiao Fu, Yue Hu, Meida Chen, Peter Anthony Beerel, Barath Raghavan
**Link:** https://arxiv.org/abs/2607.08711v1
**Summary:** The paper addresses the challenge of creating accurate 3D terrain maps in wildfire-prone areas, where traditional reconstruction methods are insufficient. The authors propose a multi-modal reconstruction framework that uses old Digital Elevation Models (DEMs) to guide image-based 3D reconstruction, simplifying the process by eliminating costly feature matching. The key contribution is the demonstrated improvement in both reconstruction accuracy and computational efficiency, enabling real-time, high-quality terrain mapping for emergency response.

### 10. MPFlow: Learning Budgeted Max-Flow Optimization on the Lightning Network with Deep Graph Reinforcement Learning
**Authors:** Harrison Rush, Vincent Davis, Simone Antonelli, Vikash Singh, Jesse Shrader, Emanuele Rossi
**Link:** https://arxiv.org/abs/2607.08703v1
**Summary:** The paper addresses the challenge of optimizing liquidity placement in the Bitcoin Lightning Network by determining which channels to open within a fixed budget to maximize routing capacity. The authors developed a lightweight deep graph reinforcement learning agent that employs a message-passing policy network and proximal policy optimization, trained under a curriculum that encourages strategic channel placement. Their approach consistently outperformed conventional heuristic methods in maximizing routing capacity across various scenarios and has been successfully implemented in production, facilitating thousands of channel-opening decisions.
