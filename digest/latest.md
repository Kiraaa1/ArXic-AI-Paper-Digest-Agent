---
## 2026-11-26

### 1. Spectrum Adaptation of AI-Native Autoencoder Communications with Transfer Learning
**Authors:** Yalin E. Sagduyu, Tugba Erpek
**Link:** https://arxiv.org/abs/2611.34942v1
**Summary:** This paper addresses the challenge of adapting autoencoder-based communication systems to different channel conditions, particularly when trained on a simpler channel like AWGN and then faced with more complex environments like Rayleigh fading. The authors propose a transfer-learning approach that fine-tunes only a small portion of the encoder and decoder layers while keeping most of the model unchanged, allowing for quick adaptation without significant resource costs. They demonstrate that this method effectively reduces bit error rates and training time while maintaining performance close to fully retrained models.

### 2. Tokenisation is not in APX
**Authors:** Violeta Kastreva, Philip Whittington, Dennis Komm, Tiago Pimentel
**Link:** https://arxiv.org/abs/2611.34938v1
**Summary:** This paper addresses the problem of tokenisation, specifically the challenge of finding an optimal tokeniser that efficiently groups elements in a way that aligns with certain objectives, like compression or likelihood maximization. The authors prove that, unless P=NP, it's impossible to design a polynomial-time algorithm that can produce a tokenisation within a constant factor of the optimal solution, thus establishing that tokenisation is not in the APX complexity class. They also demonstrate that direct tokenisation is APX-hard even for simple cases with unary alphabets, indicating that no polynomial-time approximation scheme exists for this problem.

### 3. Can image generation help visual reasoning? An empirical study
**Authors:** Xueyang Yu, Yifan Jing, Taiming Lu, Linrong Cai, Zhipeng Cai, Yunyang Xiong, Gabriel Sarch, Zhuang Liu
**Link:** https://arxiv.org/abs/2611.34935v1
**Summary:** This paper investigates whether generating images can enhance the ability of multimodal models to answer visual questions. The researchers tested various combinations of vision-language models and image generators but found that using generated images generally decreased accuracy on most tasks. Notably, for some models, repeated image edits produced varying results, indicating that the effectiveness of image generation in visual reasoning is inconsistent.

### 4. Attack Policy Selection can Mislead Monitor Evaluators
**Authors:** Charlie Griffin, Oliver Makins, Asa Cooper Stickland, Alessandro Abate, Yarin Gal, Abby D'Cruz, Xander Davies
**Link:** https://arxiv.org/abs/2611.34934v1
**Summary:** This paper investigates the reliability of AI monitors that detect harmful behavior by evaluating their performance against attack policies, which serve as proxies for dangerous actions. The study finds that the effectiveness of these monitors can vary significantly (from 0.5% to 23% false negative rates) based on how the attack policies are generated and optimized. This variability highlights the risk of overestimating a monitor's robustness, underscoring the need for careful justification of the evaluation methods and their applicability to real-world scenarios.

### 5. A gene informed benchmark for BioScoring of pathology foundation models
**Authors:** Paul Vilars, Vincent Quoc-Huy Trinh, Maria Vakalopoulou, Dimitris Samaras, Stergios Christodoulidis, Mahdi S. Hosseini
**Link:** https://arxiv.org/abs/2611.34930v1
**Summary:** The paper addresses the challenge of evaluating pathology foundation models in a way that reflects their biological relevance, rather than just their performance on classification tasks. It introduces BioScore, a novel benchmark that uses sparse autoencoders to assess how well these models capture specific cell identities based on spatial transcriptomics data. The key finding is that all pathology models outperformed natural image models, highlighting their effectiveness in representing biological features, while also providing detailed insights into which cell identities are well represented by each model.

### 6. Diverse Alternative Reasoning Traces for Hard Math Problems
**Authors:** Lukas Aichberger, Adam Golinski, Arno Blaas, Arwen Bradley, Jacob Springer, Mehrdad Farajtabar, Michael Kirchhof, Sinead Williamson
**Link:** https://arxiv.org/abs/2611.34928v1
**Summary:** The paper addresses the challenge of finding effective reasoning traces for difficult math problems, which are often scarce when sampling randomly from large language models. It introduces a method called Diverse Alternative Reasoning Traces (DART), which refines rejected reasoning traces by breaking them down and creating varied alternative paths. The key finding is that DART recovers 37% more solutions to challenging math problems compared to traditional methods, while also reducing the cost of generating accepted solutions.

### 7. Mixture-of-Loops Transformer
**Authors:** Lianghui Zhu, Shijie Wang, Xinggang Wang, Jinze Bai, Bo Wang, Xiang Bai
**Link:** https://arxiv.org/abs/2611.34923v1
**Summary:** The Mixture-of-Loops Transformer (MoLT) addresses the challenge of balancing expressivity and efficiency in looped Transformers by introducing a new attention mechanism that selectively reuses memory across different processing loops. This approach enhances model performance significantly, achieving greater token efficiency and improved accuracy in various tasks compared to existing models. Notably, the U-shaped version of MoLT (U-MoLT) demonstrates a substantial reduction in computational cost while maintaining competitive inference speeds.

### 8. $μ$-Bench: Benchmarking Multi-User Task Completion in Shared Interaction Voice Agents
**Authors:** Qihao Lin, Guanxu Chen, Shuhang Zheng, Xiaoya Lu, Jingyi Yang, Terumi Chiba, Wenyi Yu, Chao Zhang, Zhuan Shi, Jing Shao
**Link:** https://arxiv.org/abs/2611.34920v1
**Summary:** The paper addresses the challenge of evaluating voice agents in shared environments where multiple users have interdependent requests and varying levels of authority and privacy. The authors introduce $μ$-Bench, a benchmark that simulates user interactions and evaluates joint task completion across various scenarios. Key findings reveal that proprietary voice systems perform better than open-weight models, but overall success rates are limited, particularly in larger groups, highlighting areas for improvement in multi-turn interactions.

### 9. Enhancing Maritime Domain Awareness using Latent Space Representations
**Authors:** Rikard Vinge, Miguel A. Belenguer-Plomer, Isabelle Wittmann, Octavian Dumitru, Michele Lazzarini, Sergio Albani, Conrad M Albrecht
**Link:** https://arxiv.org/abs/2611.34899v1
**Summary:** This paper addresses the challenge of Maritime Domain Awareness (MDA) by using compressed latent-space representations of Earth Observation data, specifically from Sentinel-1 synthetic aperture radar imagery. The authors developed a method that leverages these embeddings to detect, localize, and classify vessels efficiently, achieving a high detection accuracy and releasing a new maritime dataset of approximately 2,000 images paired with AIS signals. The findings highlight both the promise and limitations of using Geospatial Foundation Models for detailed MDA applications.

### 10. What a Drop Reveals: Sim-to-Real Material Estimation for Deformable Objects from Video
**Authors:** Ziyue Peng, Yanxi Hu, Junyoung Kim, Andrew Chen, Jin Yang, Chandrajit L. Bajaj, Etienne Vouga, William T. Freeman, Qixing Huang, Brandon Y. Feng
**Link:** https://arxiv.org/abs/2611.34894v1
**Summary:** The paper addresses the challenge of estimating material properties, such as stiffness and yield stress, of deformable objects based on their behavior when dropped, using only video footage with no material labels. The authors developed a predictor called PhysReader that learns to connect 2D video data to 3D deformation in a simulated environment, while demonstrating that short 2D optical-flow tracklets transfer better to real scenarios than more detailed 3D inputs. The key finding is that PhysReader outperforms other methods in estimating material properties from real video drops, significantly improving accuracy with minimal processing time.
