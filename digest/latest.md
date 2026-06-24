---
## 2026-06-24

### 1. InSight: Self-Guided Skill Acquisition via Steerable VLAs
**Authors:** Maggie Wang, Lars Osterberg, Stephen Tian, Ola Shorinwa, Jiajun Wu, Mac Schwager
**Link:** https://arxiv.org/abs/2606.24884v1
**Summary:** The paper presents InSight, a framework that enhances Vision-Language-Action (VLA) models by enabling them to autonomously acquire new manipulation skills through a self-guided process. It uses an automated method to break down tasks into basic actions and a data-driven approach to identify and practice missing actions, allowing the models to learn and integrate these skills without human input. The key contribution is demonstrating that this "primitive steerability" facilitates continuous skill acquisition, allowing the models to tackle new, complex tasks effectively.

### 2. New Bounds for the Last Iterate of the Stochastic subGradient Method
**Authors:** Guglielmo Beretta, Tommaso Cesari, Roberto Colomboni, Andrea Paudice
**Link:** https://arxiv.org/abs/2606.24879v1
**Summary:** This paper addresses the performance of the last iterate of the stochastic subgradient method (SsGM) when optimizing one-dimensional convex Lipschitz objectives. The authors prove that using fixed step sizes leads to an optimization error of order \(1/\sqrt{n}\), improving on previous bounds that included an undesirable logarithmic factor. However, they also demonstrate that when the additive noise is not independent and identically distributed (i.i.d.), the error can increase to \((\log n)/\sqrt{n}\), indicating that uniformly bounded variance alone is not sufficient for optimality.

### 3. FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation
**Authors:** Haorui Ji, Weizhe Liu, Hongdong Li, Hengkai Guo
**Link:** https://arxiv.org/abs/2606.24874v1
**Summary:** FLUX3D addresses the challenge of generating high-fidelity 3D Gaussian structures from 2D images, which often fail to capture fine visual details. The authors propose a new framework that enhances the representation of 2D features and improves alignment between 2D image data and 3D voxel representations through innovative techniques, leading to superior quality in 3D generated assets. The results show that FLUX3D significantly outperforms existing methods in generating realistic 3D structures.

### 4. OpenThoughts-Agent: Data Recipes for Agentic Models
**Authors:** Negin Raoof, Richard Zhuang, Marianna Nezhurina, Etash Guha, Atula Tejaswi, Ryan Marten, Charlie F. Ruan, Tyler Griggs, Alexander Glenn Shaw, Hritik Bansal, E. Kelly Buchanan, Artem Gazizov, Reinhard Heckel, Chinmay Hegde, Sankalp Jajee, Daanish Khazi, Emmanouil Koukoumidis, Xiangyi Li, Hange Liu, Shlok Natarajan, Harsh Raj, Nicholas Roberts, Ethan Shen, Nishad Singhi, Michael Siu, Ashima Suvarna, Hanwen Xing, Patrick Yubeaton, Robert Zhang, Leon Liangyu Chen, Xiaokun Chen, Steven Dillmann, Saadia Gabriel, Xunyi Jiang, Anurag Kashyap, Boxuan Li, Yein Park, Minh Pham, Sujay Sanghavi, Lin Shi, Ke Sun, Yixin Wang, Zhiwei Xu, Erica Zhang, Siyan Zhao, Wanjia Zhao, Jenia Jitsev, Alex Dimakis, Benjamin Feuer, Ludwig Schmidt
**Link:** https://arxiv.org/abs/2606.24855v1
**Summary:** The paper presents OpenThoughts-Agent (OT-Agent), which addresses the challenge of curating diverse training data for agentic language models that can perform a wide range of tasks. By developing a fully open data curation pipeline and conducting over 100 experiments, the authors created a training set of 100,000 examples that was used to fine-tune the Qwen3-32B model, achieving a notable improvement in accuracy over existing models. The project also demonstrates strong performance scalability and makes all resources available for further research in this area.

### 5. It's Complicated: On the Design and Evaluation of AI-Powered AAC Interfaces
**Authors:** Blade Frisch, Will Wade, Dylan Gaines, Michelle Kinsella, Betts Peters, Tamara Broderick, Keith Vertanen
**Link:** https://arxiv.org/abs/2606.24854v1
**Summary:** This paper addresses the challenges in evaluating AI-powered augmentative and alternative communication (AAC) systems, which struggle to capture the diverse needs of users. The authors explore six complex problem areas in AAC and propose new evaluation methods that better account for the intersectional and nuanced desires of individuals. Their work aims to improve how AI can be integrated into AAC interfaces by providing a more comprehensive framework for assessment.

### 6. Real vs. Complex Spectral Bases for Neural Operators: The Role of Green's Function Alignment
**Authors:** Jason Sulskis, Sathya Ravi
**Link:** https://arxiv.org/abs/2606.24851v1
**Summary:** The paper addresses the efficiency of neural network architectures in learning solutions to partial differential equations (PDEs) by comparing two spectral bases: the complex Fourier domain used in Fourier Neural Operators (FNO) and a purely real approach with Hartley Neural Operators (HNO). The authors introduce HNO, which eliminates complex arithmetic and retains more frequency information, and demonstrate that the best choice of spectral basis depends on the specific properties of the PDE being solved, particularly its phase content. Their findings provide a guideline for selecting the appropriate operator based on the symmetry of the Green's functions associated with the equations.

### 7. IV-CoT: Implicit Visual Chain-of-Thought for Structure-Aware Text-to-Image Generation
**Authors:** Zixuan Li, Haokun Lin, Yicheng Xiao, Zhiwei Li, Xinyang Song, Zelong Zheng, Yong He, Heng Yao, Ke Ding, Chao Yu, Chuan Yuan, Qi Li, Zhenan Sun
**Link:** https://arxiv.org/abs/2606.24849v1
**Summary:** The paper addresses the challenge of ensuring that text-to-image generation models accurately follow structural details in prompts, such as object counts and spatial relationships. To tackle this, the authors introduce Implicit Visual Chain-of-Thought (IV-CoT), a framework that separates structural planning from appearance rendering, thereby allowing for better visual planning through non-extractive sketch supervision. The results indicate that IV-CoT significantly improves generation quality on benchmarks, demonstrating the effectiveness of its structural and semantic query approach.

### 8. World Models in Pieces: Structural Certification for General Agents
**Authors:** Yikai Lu, Yifei Wu, Xinyu Lu, Tongxin Li
**Link:** https://arxiv.org/abs/2606.24842v1
**Summary:** The paper addresses the issue that general agents cannot perform universally across complex environments, leading to ineffective worst-case performance analyses. To tackle this, the authors propose a method called structural certification, which focuses on evaluating agents based on specific transitions in their world model rather than overall performance. The key contribution is the development of algorithms that provide error bounds for agents' goal-conditioned performance, enabling reliable planning in selected scenarios and facilitating the certifiable use of general agents.

### 9. Matching Tasks to Objectives: Fine-Tuning and Prompt-Tuning Strategies for Encoder-Decoder Pre-trained Language Models
**Authors:** Ahmad Pouramini, Hesham Faili
**Link:** https://arxiv.org/abs/2606.24841v1
**Summary:** This paper addresses the challenge of optimizing encoder-decoder pre-trained language models for specific natural language processing tasks, such as generation and question answering. The authors propose the Match Task to Objective (MTO) framework, which automates the selection of pre-training objectives and designs fine-tuning templates that align with those objectives. Their approach demonstrates substantial performance improvements (over 120%) in few-shot settings compared to traditional methods, while also enhancing prompt-tuning strategies.

### 10. Grading the Grader: Lessons from Evaluating an Agentic Data Analysis System
**Authors:** Tian Zheng, Kai-Tai Hsu
**Link:** https://arxiv.org/abs/2606.24839v1
**Summary:** The paper addresses the challenge of evaluating outputs from complex agentic data analysis systems, which produce diverse results beyond simple text responses. The authors implement a three-layer grading system that combines strict regex matching, lenient grading by a language model, and human inspection. They find that this approach achieves high grading precision and significantly improves recall through iterative nudging strategies, effectively enhancing the evaluation process for these sophisticated systems.
