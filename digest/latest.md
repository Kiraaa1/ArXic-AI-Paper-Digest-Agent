---
## 2026-09-24

### 1. On the Diffusibility of High-Dimensional Latents
**Authors:** Chao Feng, Zhiyang Xu, Bowei Chen, Yuanjun Xiong, Xiyao Wang, Jui-Hsien Wang, Richard Zhang, Zhe Lin, Andrew Owens, Yijun Li
**Link:** https://arxiv.org/abs/2609.28473v1
**Summary:** The paper addresses the issue that standard pretrained visual encoders may lose fine visual details when used in diffusion models, leading to inefficiencies in optimizing high-dimensional representations. To solve this, the authors propose using a clean data parameterization method that focuses on the actual signal manifold rather than the noise directions. Their key finding is that this approach consistently enhances the performance of text-to-image generation across various strong-reconstruction encoders.

### 2. Contrastive Learning for Authorship Verification
**Authors:** Peter Kirby
**Link:** https://arxiv.org/abs/2609.28471v1
**Summary:** The paper addresses the problem of authorship verification, determining whether a piece of text is written by a specific author. It employs a contrastive learning approach, which is shown to outperform traditional classification methods. The authors develop a ModernBERT Bi-Encoder model that achieves an impressive accuracy of 98.4% on the PAN21 authorship verification task, highlighting key factors that enhance model performance.

### 3. StudentBench: AI and human tutoring yield equivalent GRE learning gains
**Authors:** Curtis Northcutt, Inaara Hasmani, Kevin Feng, Trevor Khangi, Andreas Plesner, Jonas Mueller
**Link:** https://arxiv.org/abs/2609.28470v1
**Summary:** The paper presents StudentBench, a platform designed to evaluate and compare AI tutoring with human tutoring by analyzing over 175,000 student-AI interactions. The study found that AI tutoring can produce learning gains equivalent to those from expert human tutoring on GRE subjects, and in some cases, the AI outperformed human tutors while being significantly more cost-effective. This indicates the potential of AI systems to effectively support educational outcomes.

### 4. Where Should I Join? Robot Group Joining via Language-Guided Goal Prediction
**Authors:** Zilin Fang, Zishuo Wang, Gim Hee Lee, David Hsu
**Link:** https://arxiv.org/abs/2609.28467v1
**Summary:** The paper addresses the challenge of robot group joining, which involves determining where a robot should enter a group based on observing the group's activity and using natural language descriptions. The authors propose a method that combines structured group analysis with a language-informed model to predict socially appropriate joining positions, achieving high accuracy in both simulations and real-robot experiments. The key contribution is the effective integration of language and visual data to enhance the robot's ability to navigate social settings and join groups seamlessly.

### 5. Even Sharper Bounds for Transductive Learning and Its Applications
**Authors:** Yingzhen Yang
**Link:** https://arxiv.org/abs/2609.28459v1
**Summary:** This paper develops a new method called Sharper Transductive Local Complexity (STLC) for improving transductive learning, which involves making predictions based on a small set of labeled data without replacement. The authors prove sharper excess risk bounds derived from concentration inequalities and entropy techniques, achieving results similar to classical inductive methods but with tighter confidence intervals. The key contribution is that STLC matches standard inductive rates while remaining close to the optimal lower bounds, and further enhances bounds for transductive kernel learning.

### 6. Can LLMs Reason About Runtime Behavior? A Repository-Level Dynamic Benchmark
**Authors:** Hamed Taherkhani, Mohammad Abdollahi, Melika Sepidband, Hridya Dhulipala, Tien N. Nguyen, Hadi Hemmati
**Link:** https://arxiv.org/abs/2609.28449v1
**Summary:** The paper addresses the gap in evaluating large language models' (LLMs) ability to reason about dynamic code execution in real-world applications, as existing benchmarks primarily focus on static code understanding. The authors propose SWE-Flux, a new benchmark consisting of 480 execution-grounded questions derived from real Python repositories, with answers obtained from actual code execution rather than manual input. Evaluation of various LLMs demonstrates that this reasoning task remains challenging, with the best model achieving only 37% accuracy, particularly struggling with complex dataflow and inter-procedural logic.

### 7. Nonequilibrium Phases of Repulsive Self-Attention: Chaos, Attention Condensation, and Emergent Locality
**Authors:** Qucheng Gao, Zuyi Yang, Xiao Chen
**Link:** https://arxiv.org/abs/2609.28448v1
**Summary:** This paper investigates the dynamic behavior of a simplified self-attention transformer model under nonequilibrium conditions, where repulsive forces between tokens lead to complex patterns of interaction. By analyzing the system's behavior as various parameters are adjusted, the authors uncover distinct phases characterized by chaotic motion, attention condensation, and emergent spatial localization. The key contribution is demonstrating that even sparse attention mechanisms can support ongoing dynamic behavior rather than becoming static, revealing the rich collective phenomena that arise from these interactions.

### 8. Order-Invariant Answers, Order-Sensitive Representations in Mathematical Reasoning
**Authors:** Zhixu Silvia Tao
**Link:** https://arxiv.org/abs/2609.28442v1
**Summary:** The paper examines whether internal representations in language models are affected by the order of mathematical rules when the answer remains unchanged. By testing 16 language models on synthetic multi-step problems presented in different rule orders, the authors found that models which performed better on reordered problems had clearer internal representations of those orders. This suggests a significant distinction between maintaining the correct answer and having invariant internal representations, highlighting a new perspective on mathematical reasoning in AI.

### 9. Minimal-Norm Univariate Two-Layer ReLU Classification: Exact Solutions and Global Optimality with Skip Connections
**Authors:** Karolina Drabik, Ben Lewis, Antoni Puch, Etienne Boursier, Piotr Hofman, Matthias Englert, Ranko Lazić
**Link:** https://arxiv.org/abs/2609.28438v1
**Summary:** This paper addresses the problem of finding minimal-norm classifiers using univariate two-layer ReLU networks for binary classification. The authors provide a detailed geometric analysis of classifier solutions, demonstrating that including biases in the model affects regularization outcomes and sparsity. A key finding is that adding skip connections greatly enhances the optimization landscape, ensuring that all KKT points are globally optimal, which isn't guaranteed without these connections.

### 10. Cross-Scale Transfer Learning for Depression Severity Prediction: From PHQ-8 to HAMD-17 Across Languages and Clinical Paradigms
**Authors:** Wenjie Feng, Sahba Zojaji, Satoshi Nakamura
**Link:** https://arxiv.org/abs/2609.28430v1
**Summary:** The paper addresses the challenge of predicting continuous depression severity scores from clinical interview transcripts, particularly when data is limited. The authors propose a novel transfer learning approach that fine-tunes a language model on an English dataset before adapting it to a Chinese dataset with different severity scales. Key results indicate that this method outperforms traditional training on the target dataset alone, achieving better predictive accuracy metrics.
