---
## 2026-11-18

### 1. Ambient LLMs: Data-Efficient Supervised Fine-tuning via Temperature Matching
**Authors:** Giannis Daras, Marios Papachristou, Adam Klivans, Antonio Torralba, Constantinos Daskalakis
**Link:** https://arxiv.org/abs/2611.23229v1
**Summary:** The paper addresses the challenge of collecting large and high-quality datasets for fine-tuning language models, which can lead to overfitting. The authors propose Ambient SFT, a method that uses a "frozen" pre-trained model as a noisy teacher to help guide the fine-tuning process by matching their predictions at different temperature levels. Their approach shows significant improvements over standard fine-tuning methods, achieving up to 21% better performance in various tasks.

### 2. Spool: Low-Latency Streaming Inference for Hybrid Vision-Language Models
**Authors:** Rui Ning, Om Chabra, Hari Balakrishnan
**Link:** https://arxiv.org/abs/2611.23228v1
**Summary:** The paper presents Spool, a novel framework designed to enhance the efficiency of hybrid vision-language models (VLMs) for low-latency streaming inference on recent video content. By caching and composing state transformations for each frame, Spool eliminates the need to re-process expired frames, significantly speeding up the model while preserving accuracy. As a result, it achieves a 6.6 times faster time-to-first-token across various benchmarks compared to existing solutions.

### 3. StringQFT: A Multiuse Textbook Resource for AI-Assisted Theoretical Physics
**Authors:** Xingyang Yu
**Link:** https://arxiv.org/abs/2611.23225v1
**Summary:** The paper introduces StringQFT, a comprehensive open-access textbook that integrates string theory with quantum field theory, designed to support AI-assisted theoretical physics. It includes a vast collection of resources, such as section records and calculation tools, enabling automated checks and retrieval-augmented generation for educational and research purposes. The key contribution is the creation of a structured, multiuse resource that facilitates learning and problem-solving in theoretical physics through AI technologies.

### 4. An inexact stochastic variance-reduced gradient method for constrained convex finite-sum optimization
**Authors:** Zhaosong Lu, Yifeng Xiao
**Link:** https://arxiv.org/abs/2611.23221v1
**Summary:** This paper addresses constrained convex finite-sum optimization problems, where solutions must closely adhere to hard constraints. The authors present an improved inexact stochastic variance-reduced gradient method that enhances the efficiency of finding $ε$-surely feasible stochastic optimal solutions, with a lower complexity in gradient evaluations compared to existing approaches. Their method also extends to a deterministic first-order technique for standard convex conic optimization, demonstrating superior performance in scenarios where evaluating constraint gradients is more efficient than evaluating the objective gradient.

### 5. Do LLM Agents Still Need to Be Told How to Self-Improve?
**Authors:** Shobhita Sundaram, Cansu Sancaktar, Phillip Isola
**Link:** https://arxiv.org/abs/2611.23219v1
**Summary:** The paper examines whether advanced LLM agents can autonomously determine their own self-improvement strategies without external guidance. By allowing a static LLM agent to experiment with its self-learning algorithm in a gameplay setting, the authors found that these agents could effectively optimize their performance, echoing established theories of self-regulated learning. The study also highlights that the agents' self-generated learning artifacts enhance their capabilities across varied game scenarios and challenges.

### 6. What Does a Bias Head Measure? Non-Identifiability in Head-Level Bias Attribution
**Authors:** S. M Seefat Alam
**Link:** https://arxiv.org/abs/2611.23218v1
**Summary:** The paper investigates the effectiveness of methods that identify and remove social bias in large language models by focusing on individual attention heads. Through an audit of the Qwen-2.5 and Llama-3 models, the authors demonstrate that the metrics used to attribute bias are confounded by factors like prompt identity and response length, making it unclear if the heads truly measure bias. Ultimately, they find that no head set successfully reduces unfairness, challenging the validity of current bias mitigation techniques in these models.

### 7. Higher-Scoring Coding Models Did Not Get More Work Done
**Authors:** Yining Hua
**Link:** https://arxiv.org/abs/2611.23216v1
**Summary:** This study investigates whether higher scores on coding benchmarks correlate with increased productivity in real-world coding tasks, using a natural experiment involving the temporary suspension of the Fable 5 coding model. By analyzing GitHub pull requests from developers before, during, and after the suspension, the researchers found no significant difference in merge rates or productivity between users of Fable 5 and those on a lower-scoring model, Opus 4.8. The key contribution is the finding that higher benchmark scores do not necessarily lead to greater work output in practical coding scenarios.

### 8. Multimodal Masked Diffusion Autoencoder for Modeling Impaired Driving
**Authors:** John Gideon, Anshul Gupta, Megan Applegate-Kenton, Kayli Battel, Todd J Rowell, Patricio Reyes Gomez, Laporsha Dees, Emily Sumner, Avinash Balachandran, Guy Rosman
**Link:** https://arxiv.org/abs/2611.23211v1
**Summary:** The paper addresses the challenge of predicting human cognitive impairments while driving, which is difficult due to the lack of extensive labeled data. The authors propose a multimodal masked-diffusion autoencoder called ID-MAE, which not only predicts impairment levels but also reconstructs gaze and driving trajectories from various types of inputs. Their approach significantly improves impairment detection accuracy on a new driving dataset, achieving a paired AUC of 0.706 compared to 0.590 without reconstruction loss, indicating a robust method for understanding driver behavior under different impairment conditions.

### 9. Distortion-Free Semantic Watermarks for Black-Box Generative Models
**Authors:** Aviv Yossef, Or Patashnik, Or Zamir
**Link:** https://arxiv.org/abs/2611.23208v1
**Summary:** The paper addresses the challenge of watermarking outputs from black-box generative models in a way that doesn't degrade the quality of the generated content, especially against transformations like cropping or resizing. The authors introduce a generic watermarking algorithm that only requires sampling and semantic embedding access, ensuring the watermarks remain robust and detectable despite content-preserving alterations. The key contribution is a specially trained image encoder that effectively balances the need for stability under transformations with the ability to distinguish between separate generations, demonstrating strong watermark detection across different generative models.

### 10. Reading Scene States: Uncovering Safety Failures in Vision-Language Models
**Authors:** Tongxi Wu, Yuyang Cheng, Jiacheng Xian, Menglin Yang, Kai Chen, Jian Zhang, Yang Gao
**Link:** https://arxiv.org/abs/2611.23206v1
**Summary:** The paper addresses the safety vulnerabilities of vision-language models (VLMs) that can provide harmful assistance based on visual inputs, even without explicit harmful requests. The authors introduce a benchmark called SceneSafetyBench and develop a systematic attack method, S3TA, to exploit these vulnerabilities, achieving a high attack success rate of 71.2% across multiple VLMs. This research underscores the importance of enhancing safety measures in models that interpret visual information to prevent dangerous outcomes.
