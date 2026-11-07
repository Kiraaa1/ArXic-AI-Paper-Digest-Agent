---
## 2026-11-07

### 1. Label-Wording Augmentation in a Typed-Decision Encoder: Gains on Unfamiliar Words, Not on Abbreviations or Codes
**Authors:** Vladimir Beskorovainyi
**Link:** https://arxiv.org/abs/2611.08439v1
**Summary:** The paper addresses the problem of improving the accuracy of typed-decision models, which score options based on label wordings that developers cannot control. The authors compare two versions of a multilingual cross-encoder, focusing on an augmented version that presents labels in various surface forms. The key finding is that this augmentation benefits accuracy with unfamiliar words, especially jargon and slang, but does not improve performance on abbreviations or opaque codes, revealing specific scenarios where the enhancement is effective.

### 2. Understanding AI from the Inside: The State of Mechanistic Interpretability for AI Safety
**Authors:** Fazl Barez, Tung-Yu Wu, Hunar Batra, Gabriele Dominici, Florent Draye, Yanai Elazar, Damiano Fornasiere, Antía García, Abir Harrasse, Riley Harris, Sara Hooker, Michael Lan, Belinda Z. Li, Aaron Maiwald, Narmeen Fatimah Oozeer, Naomi Saphra, Or David Shafran, Adi Simhi, Robert Trager, Shriyash Kaustubh Upadhyay, Ziyu Yao, Yu Zhao, Shay B. Cohen, Mor Geva, Yoshua Bengio, Stella Biderman, Hassan Sajjad
**Link:** https://arxiv.org/abs/2611.08438v1
**Summary:** The paper addresses the challenge of ensuring AI safety as neural networks become more powerful and autonomous. It explores mechanistic interpretability, which involves studying the internal workings of these models to better predict and control their behavior. The authors propose a unified framework for evaluating interpretability efforts, highlight its potential benefits for AI safety, and provide practical resources for researchers to experiment with mechanistic understanding.

### 3. MedGraph: Maintaining Patient State with Graph Memory for Long-Term Medical Dialogue
**Authors:** Donghua Zhang, Zizheng Wang, Ze Dong, Yiding Feng, Siyu Qian
**Link:** https://arxiv.org/abs/2611.08433v1
**Summary:** The paper addresses the challenge of maintaining an accurate and updated patient state in long-term medical dialogues for AI assistants. The proposed solution, MedGraph, utilizes a graph memory system that organizes and retrieves patient information, ensuring that outdated or incorrect data is minimized by attributing facts to the correct patient and maintaining links between related medical records. The key finding shows that MedGraph significantly outperforms existing memory systems in accuracy, achieving up to 10.5 points higher on a benchmark test.

### 4. The Power of Meta Access in the Software of the Future --- Demonstrated on LLM Chat UIs and Chat AI
**Authors:** Julian Kunkel, Ali Doosthosseini
**Link:** https://arxiv.org/abs/2611.08428v1
**Summary:** The paper addresses the limitation of current chat interfaces for large language models (LLMs) by introducing "meta access," which provides structured access to the interface and its settings. This approach enables users to navigate, organize, and operate their workspace more effectively within a single chat client while managing risks related to privacy and control. The key contribution is the development of the Meta Chat prototype, which enhances chat interfaces by exposing application states in a way that supports advanced interactions and greater user empowerment.

### 5. Failure Prediction and Classification in Vision-Language-Action Models Via Calibrated Latent Probing
**Authors:** Michal P. Podolinsky, Yunhao Yang, Daniel Little, Hong Lu, Rohan Siva, Olin Goudey, Neel P. Bhatt, Matthias Scheutz, Ufuk Topcu
**Link:** https://arxiv.org/abs/2611.08425v1
**Summary:** The paper addresses the challenge of failure prediction in Vision-Language-Action models, which can struggle under unforeseen conditions. The authors introduce VLA-Tug, a lightweight probing technique that enhances early failure detection while maintaining low computational overhead. Their approach significantly improves detection rates and accuracy in identifying failure modes, demonstrating a substantial increase in performance compared to existing methods, and they provide a dataset for further research in this area.

### 6. Data-driven discovery of intrinsic Lie point symmetries of differential equation systems
**Authors:** Ilker Gurcan, Kadir Ustun, Ramazan Gokberk Cinbis
**Link:** https://arxiv.org/abs/2611.08421v1
**Summary:** The paper addresses the challenge of discovering continuous symmetries in differential equations directly from data, which can aid in model reduction and scientific machine learning. The authors develop an operator-theoretic framework to identify relevant symmetry generators from sampled data while filtering out redundant or trivial components. Their key contribution is demonstrating that their method can accurately recover the full set of intrinsic symmetry generators and their associated structure from both exact and approximate differential systems.

### 7. On the limitations of molecular representations
**Authors:** Acer Blake, Fergus Imrie, Charlotte M. Deane
**Link:** https://arxiv.org/abs/2611.08420v1
**Summary:** The paper investigates the effectiveness of different molecular representations, such as fingerprints and learned embeddings, used in cheminformatics and machine learning for small molecules. Through a systematic analysis, the authors found that current advanced embedding models do not outperform traditional fingerprints or physicochemical descriptors in capturing important molecular properties, and highlight significant issues with non-unique representations in large molecular databases. The findings underscore the need for improved molecular encoding techniques for better performance in applications like virtual screening.

### 8. Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks
**Authors:** E. Kelly Buchanan, Crystal Zhou, Scott W. Linderman, Christopher Ré
**Link:** https://arxiv.org/abs/2611.08417v1
**Summary:** The paper addresses the issue of "benchmark maintenance debt," where outdated benchmarks fail to accurately reflect the capabilities of advanced coding agents, resulting in misleading evaluations. To tackle this, the authors propose a continuous-validation workflow that incorporates community feedback and automated checks, which they applied to the Terminal-Bench benchmark. Their findings revealed significant issues in about 30% of the benchmark, leading to updates that improved accuracy by over 10 percentage points and altered leaderboard positions, highlighting the importance of regularly re-evaluating both benchmarks and their resource settings as models evolve.

### 9. Spectral and Subspace Dynamics of LoRA in Supervised Fine-Tuning and Reinforcement Learning
**Authors:** Chenruo Liu, Zihan Wang, Yijun Dong, Qi Lei
**Link:** https://arxiv.org/abs/2611.08414v1
**Summary:** The paper investigates how Low-Rank Adaptation (LoRA) operates differently in supervised fine-tuning (SFT) versus reinforcement learning (RL), revealing that RL focuses learning on specific spectral distributions and rotates subspaces more quickly than SFT. By analyzing the dynamics and effects of group-mean baseline subtraction, the authors propose tailored LoRA update strategies for each context, leading to improved performance in mathematical reasoning tasks. The key contribution lies in adapting LoRA updates to optimize learning behavior specific to SFT and RL settings, resulting in enhanced outcomes across multiple models.

### 10. The Gold Rush in AI4Math, II: What are signatures of AI-assisted Proofs?
**Authors:** Yuanchuan Guo, Jiashun Jin, Zheng Tracy Ke, Bingcheng Sui
**Link:** https://arxiv.org/abs/2611.08412v1
**Summary:** This paper addresses the challenge of identifying whether a mathematical proof has been assisted by AI, separate from the AI's role in writing. The authors developed ProofTrace, a framework that analyzes the structure of proofs as graphs, allowing them to extract features that reveal the extent of AI involvement. Key findings include distinct characteristics of AI-generated proofs, such as different citation patterns and connectivity, along with ProofTrace's ability to effectively distinguish between human-written and AI-assisted papers, even after AI rewording.
