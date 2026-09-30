---
## 2026-09-30

### 1. Skill-Space Shooting for Autonomous Robot Policy Improvement
**Authors:** Zihang Rui, Renhao Wang, Haoxu Huang, Yang Gao
**Link:** https://arxiv.org/abs/2609.38178v1
**Summary:** The paper addresses the challenge of enabling robots to autonomously improve their task performance in real-world settings without the need for constant human supervision. The authors propose a method called skill-space shooting, which leverages reusable skills identified by foundation models to explore and implement corrective actions for robot policies. The key contribution is that this approach allows robots to learn from their experiences and progressively enhance their performance across various tasks, demonstrating effective policy improvement through real-world experiments.

### 2. Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering
**Authors:** Jaewoo Jung, Hyeonseo Yu, Honggyu An, Jisang Han, Mungyeom Kim, Minkyeong Jeon, Heeseong Shin, Wonjun Moon, Federico Tombari, Daniel Barath, Marc Pollefeys, Seungryong Kim, Sunghwan Hong
**Link:** https://arxiv.org/abs/2609.38177v1
**Summary:** The paper addresses the challenge of helping Multimodal Large Language Models (MLLMs) effectively reason about 3D scenes from multiple images, which they struggle with compared to humans. The authors propose Imagine3D-LLM, which learns to create a simplified 3D representation of a scene using summary tokens and a reconstruction loss, rather than relying solely on detailed geometric cues. This approach allows the model to outperform previous methods in spatial reasoning tasks, demonstrating that visualizing the scene can be more beneficial than precise geometric information.

### 3. Breakdown of Local Denoising as Semantic Speciation
**Authors:** Guangkuo Liu, Mert Okyay, Yifan F. Zhang, Fangjun Hu, Rahul Nandkishore, Xun Gao
**Link:** https://arxiv.org/abs/2609.38176v1
**Summary:** This paper investigates the relationship between two phases in generative models—when a sample commits to a semantic class (speciation window) and when local contexts become insufficient for generation (nonlocality window). The authors propose a "common cause" hypothesis to show that the nonlocality window is influenced by the semantic labels of tokens, and they establish conditions under which these two windows converge as system size increases, identifying a "phase transition" in semantic structure emergence. Their findings connect the dynamics of semantic information with model behavior in generative contexts.

### 4. STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization
**Authors:** Bingchen Yao, Haobo Xu, Haokun Lin, Yichen Wu, Ziyu Guo, Renrui Zhang, Zhichao Lu, Zhenan Sun, Ying Wei
**Link:** https://arxiv.org/abs/2609.38169v1
**Summary:** The paper addresses the issue of memory inefficiencies in linear attention models due to large recurrent states, which can degrade accuracy when quantized. The authors introduce STEPQuant, a post-training quantization framework that intelligently allocates precision based on the impact of quantization errors over time and across different state components. Their experiments demonstrate that STEPQuant can achieve high accuracy comparable to full precision with significantly reduced memory usage, outperforming traditional uniform quantization methods.

### 5. LeapQuant: Efficient Linear Attention with Accurate Recurrent State Quantization
**Authors:** Yi Pan, Haocheng Xi, Kan Zhu, Xingyang Li, Yibo Wu, Mayank Mishra, Hongtao Zhang, William X. Zheng, Baris Kasikci, Song Han, Kurt Keutzer, Rishabh Iyer, Ion Stoica
**Link:** https://arxiv.org/abs/2609.38166v1
**Summary:** The paper addresses the inefficiency of state updates in linear attention models during inference by introducing LeapQuant, a method for 8-bit quantization of recurrent states that minimizes quality loss. By employing per-window quantization and retaining high-precision tokens for outliers, LeapQuant significantly reduces both memory and computational costs. The results indicate that it achieves speedups of 2.05–3.70 times at the kernel level and 1.47 times for overall inference, while maintaining accuracy comparable to the standard 32-bit floating-point models.

### 6. Cropland PAtteRNS: Parallel Dimensional Attention Networks and Attention to Dataset Disparity for Crop Segmentation in Satellite Imagery Time Series Data
**Authors:** Joseph Metcalfe, Sara Sharifzadeh, Fabio Caraffini
**Link:** https://arxiv.org/abs/2609.38165v1
**Summary:** The paper addresses the challenge of accurately segmenting crops in satellite imagery time series data, highlighting issues with dataset disparities and boundary delineation quality. The authors introduce Cropland PAtteRNS, a novel hybrid model that employs parallel dimensional attention mechanisms to effectively process the temporal, spectral, and spatial aspects of the data. Their findings demonstrate that this model outperforms existing approaches in crop segmentation metrics, particularly in parcel delineation, and emphasize the need for standardized practices in dataset construction to enhance model training and evaluation.

### 7. A Spectral Theory of Distortion in LLM Graph Reconstruction: Sharp Bounds and Empirical Characterization
**Authors:** Jianru Shen
**Link:** https://arxiv.org/abs/2609.38161v1
**Summary:** This paper addresses the challenge of evaluating how accurately language models reconstruct graphs by focusing on the spectral distance between the original and reconstructed graphs. The authors establish sharp bounds for this distance, linking it to changes in edge counts, and demonstrate that these bounds can reveal whether the model primarily edits by adding or removing edges. Their analysis of 135 graph reconstructions shows that models differ significantly in their editing strategies, and the framework they provide allows for a deeper understanding of these differences beyond simple aggregate metrics.

### 8. EmoRES-TTS: Residual-Enhanced Vector Steering for Emotional Speech Generation
**Authors:** Kuan-Po Huang, Haohe Liu, Puyuan Peng, Haibin Wu, Zhaoheng Ni, Hung-yi Lee, Jinwon Lee, Neha Chachra
**Link:** https://arxiv.org/abs/2609.38157v1
**Summary:** The paper addresses the issue of inconsistent emotional expression in text-to-speech models, which often struggle to convey the requested emotion reliably. The authors introduce EmoRES, a method that enhances the control of emotional speech generation by decomposing emotion vectors into shared and residual components, allowing for improved steering of a fixed model. Their approach significantly outperforms traditional methods, showing substantial improvements in emotion accuracy and listener preference for naturalness.

### 9. Beyond the Timeline: Augmenting Long-Video Memory with Grounded Entity Biographies
**Authors:** Hui Ren, Lei Fan, Henry Pao, Han Guo, Zeeshan Zia, Ying Chen, Alexander Schwing, Gang Hua
**Link:** https://arxiv.org/abs/2609.38155v1
**Summary:** The paper addresses the challenge of tracking and answering questions about the same objects across long videos, where traditional methods often fail to maintain consistent identities. The authors propose Grounded Entity Biographies (GEB), a framework that groups observations of the same entity into a coherent "biography" while retaining contextual information. Their approach shows significant improvements in question answering accuracy, achieving a 72.0% accuracy rate on the EgoLifeQA benchmark, surpassing prior methods by effectively linking entity identities across events.

### 10. Pretraining Latent Information Feedback Transformers with Teacher Supervision
**Authors:** Dor Tirosh, Ido Amos, Mor Geva
**Link:** https://arxiv.org/abs/2609.38149v1
**Summary:** The paper addresses the limitation of traditional Transformer language models, which do not allow feedback of deep-layer representations to shallower layers, resulting in inefficiencies. The authors present the LIFT (Latent Information Feedback Transformer) architecture, which enables models to propagate information across generations by pairing input tokens with state representations derived from another pretrained model. Their experiments demonstrate that LIFT outperforms standard Transformers on various language modeling and reasoning tasks, proving that deep-to-shallow feedback can be effectively utilized in pretrained models through teacher supervision.
