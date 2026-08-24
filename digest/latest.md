---
## 2026-08-24

### 1. Primal Acceleration of Newton's Method
**Authors:** Nikita Doikov
**Link:** https://arxiv.org/abs/2608.21359v1
**Summary:** This paper presents a new accelerated Newton method for minimizing convex functions that have a Lipschitz continuous Hessian, focusing on using only primal variables and requiring just one linear system solve per iteration. The method achieves a global convergence rate of \(O(1/k^3)\), which is noteworthy as it's the first of its kind in this setting without needing auxiliary subproblems or dual corrections. Additionally, the approach can be applied in a Hessian-free manner and is extended to more complex optimization problems.

### 2. VIALS: A Benchmark for Visual Interpretation of Artifacts in the Life Sciences
**Authors:** Elaine Lau, Thanuka Udumulla, Lee Izhaki-Tavor, Francisco Guzmán, Nicholas Magazine, Jonas Mueller
**Link:** https://arxiv.org/abs/2608.21357v1
**Summary:** The paper introduces VIALS, a benchmark designed to evaluate how well AI models can interpret various visual artifacts commonly used in life sciences, such as microscopy images and gel blots. The authors highlight that while advanced vision-language models perform well with natural images, they struggle with these scientific images, demonstrating a lack of necessary domain knowledge and reasoning skills. The key contribution is the establishment of a set of 161 tasks that can help assess and improve AI's ability to interpret critical artifacts in life sciences workflows.

### 3. AI with Authority, from Application to Silicon
**Authors:** Jason Hickey
**Link:** https://arxiv.org/abs/2608.21356v1
**Summary:** The paper addresses the significant overhead costs associated with machine verification in AI development, traditionally only feasible for exceptional cases. The authors present the Salt method, which employs generative AI to automate the verification process, allowing a researcher to successfully direct a fleet of AI agents to develop a RISC-V processor without human-reviewed proofs or manual RTL coding. The key contribution is demonstrating that AI-driven verification can enhance productivity and reliability in chip design, with a comprehensive error ledger showing zero incorrect proofs.

### 4. PerturbRx: Learning Treatment-Conditioned Latent Transitions for Patient Drug Response Prediction
**Authors:** Yoshitaka Inoue, Minoh Jeong, Alfred Hero, Rui Kuang, Augustin Luna
**Link:** https://arxiv.org/abs/2608.21349v1
**Summary:** The paper addresses the challenge of predicting how individual cancer patients will respond to treatments, which is complicated by limited data and tumor variability. The authors introduce PerturbRx, a framework that learns how treatments change molecular profiles and uses these changes to enhance predictions about patient-drug responses, without needing post-treatment data. Their approach shows strong performance in various benchmarks, demonstrating that these learned transitions provide valuable insights for improving treatment predictions.

### 5. Truthful Calibration Measures for Sequential Prediction
**Authors:** Anagha Gokul, Jason Hartline, Lunjia Hu, Jonathan Ullman, Yifan Wu
**Link:** https://arxiv.org/abs/2608.21348v1
**Summary:** The paper addresses the challenge of developing calibration measures for sequential binary prediction that meet the criteria of truthfulness, completeness, and soundness. The authors demonstrate that achieving exact truthfulness is impossible in this context, but they propose two methods to create approximately truthful calibration measures, including an improved multiplicative measure that offers better guarantees than previous work. This advancement enhances the understanding of calibration in probabilistic forecasting.

### 6. Asymmetric Capacity Allocation in Self-Refinement Pipelines
**Authors:** Zhuoyi Yang, Ian G. Harris, Salar Hashemitaheri, Cassie Huang, Yuangang Li, Hyunwoo Oh, Paul Dourish, Tony Givargis, Mohsen Imani, Li Zhang
**Link:** https://arxiv.org/abs/2608.21345v1
**Summary:** The paper addresses the issue of inefficient resource allocation in self-refinement pipelines for language models, which involve generation, critique, and revision stages. By systematically studying the impact of different model sizes on these stages across various benchmarks, the authors found that larger models enhance the generation and revision processes, while a smaller, underperforming refiner can hurt performance. Notably, they discovered that the size of the critique stage has minimal impact, suggesting that optimized model size distribution across the stages can lead to more efficient language model systems.

### 7. TurboBias 2.0: Streaming Context-Biasing for Production-Efficient ASR Systems
**Authors:** Vladimir Bataev, Lilit Grigoryan, Andrei Andrusenko, Nikolay Karpov, Vitaly Lavrukhin, Boris Ginsburg
**Link:** https://arxiv.org/abs/2608.21343v1
**Summary:** TurboBias 2.0 addresses the challenge of accurately recognizing user-provided phrases in real-time for automatic speech recognition (ASR) systems, especially under tight latency constraints. The framework enhances the existing TurboBias technique by enabling personalized context biasing for multiple users simultaneously, using a GPU-accelerated system that allows for efficient processing of independent context lists. The key result is an improvement in phrase recognition accuracy while maintaining low latency and high throughput, making it suitable for production environments.

### 8. Across-Design Uncertainty in Short Pricing Panels: Evidence from Simulated Price Trajectories
**Authors:** Pedro Cadahia Delgado
**Link:** https://arxiv.org/abs/2608.21334v1
**Summary:** This paper addresses the challenge of estimating uncertainty in short pricing panels that have many observations but limited price movements. The researchers employed a synthetic data-generating process to distinguish between errors arising from a specific price trajectory and those from different trajectories under the same pricing regime. The key finding is that most estimation error variance is due to differences across these trajectories, suggesting that more effective data designs should focus on generating independent variations rather than relying on fixed panels.

### 9. Anatomy-Informed Neural Networks: Encoding Anatomic Priors in Loss and Architecture, with an SE(3) Formulation of Guidewire-Induced Aortoiliac Deformation
**Authors:** David P. Stonko
**Link:** https://arxiv.org/abs/2608.21332v1
**Summary:** This paper addresses the challenge of creating deep-learning models that accurately reflect anatomical structures while improving generalization in scenarios with limited data, particularly in the context of aortoiliac tree deformation during endovascular procedures. The authors propose Anatomy-Informed Neural Networks (AINN), which incorporate both soft and hard anatomical priors into the loss function and network architecture, ensuring that invalid anatomical predictions cannot occur. Their approach is validated through a clinical case, leveraging optimal transport methods to align predictions with 2D angiogram observations, laying the groundwork for future applications with real patient scans.

### 10. Move by Move: Measuring and Steering How LLMs Conduct Psychotherapy
**Authors:** Afonso Baldo, Hugo Pitorro, Areti Vassilopoulos, Anabela C. Areias, Maya D'Eon, Fabíola Costa, Ricardo Rei, Nuno M. Guerreiro
**Link:** https://arxiv.org/abs/2608.21325v1
**Summary:** This paper addresses the lack of understanding regarding how large language models (LLMs) conduct psychotherapy interactions, specifically focusing on their conversational styles compared to human therapists. The authors developed a framework consisting of ten therapeutic moves, validated by psychologists, to analyze and compare the interactions of LLMs with those of human clinicians. They found that LLMs excessively rely on inquiry, underutilize psychoeducation, and improve alignment with human therapists' styles significantly when this framework is applied, without needing any model adjustments.
