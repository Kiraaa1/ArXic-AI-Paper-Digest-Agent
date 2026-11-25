---
## 2026-11-25

### 1. OmniAct: One Policy, One Million Embodiments
**Authors:** Xiang Fan, Yuheng Wang, Jiayuan Yan, Bohan Fang, Wisdom Oluchi Ikezogwo, Ainaz Eftekhar, Max Argus, Jason Ren, Jiafei Duan, Ranjay Krishna
**Link:** https://arxiv.org/abs/2611.33158v1
**Summary:** The paper addresses the challenge of creating a single control policy for diverse robots that adapts to each robot's unique physical characteristics while performing manipulation tasks. The authors introduce OmniAct, a policy that utilizes a kinematic graph to tailor behaviors based on the robots' joint configurations and scene interactions. Key results show that OmniAct significantly outperforms existing methods in both simulated environments and on a real-world robot, achieving higher success rates and developing distinct strategies that leverage different robotic morphologies.

### 2. DiaCap: Jointly Learning Who Speaks When for Audiovisual Dialogue Captioning
**Authors:** Binfei Ji, Zhiwen Cao, Anqi Yang, Prem Seetharaman, Shuo Yang, Ratheesh Kalarot, Yingyan Celine Lin, Mingze Xu
**Link:** https://arxiv.org/abs/2611.33153v1
**Summary:** The paper introduces DiaCap, a model designed for effective audiovisual dialogue captioning that generates transcripts, timestamps, and speaker descriptions for video utterances. It combines utterance timing and audiovisual diarization into a single framework, training on a large dataset with synthetic captions and refining performance through reinforcement learning. DiaCap demonstrates strong performance on a benchmark, outperforming existing models like Gemini 4 Argon in timestamp accuracy while maintaining high diarization quality across multilingual videos.

### 3. BioLoom: Scaling Biomedical Vision-Language Models by Learning from the Structure of Scientific Articles
**Authors:** Yuwei Yang, Xiaoxiao Sun, Alejandro Lozano, Yuan-Sen Ting, Yuhui Yuan, Liang Zheng, Serena Yeung-Levy
**Link:** https://arxiv.org/abs/2611.33151v1
**Summary:** The paper addresses the challenge of enhancing biomedical vision-language models by leveraging the structural relationships found in scientific articles, such as figures, captions, and associated text. The authors introduce a new dataset, Loom52M, which incorporates these relationships into a contrastive training approach, allowing models to learn from both exact matches and related content. As a result, their model, BioLoom, significantly improves performance on various classification tasks compared to existing baselines, achieving a mean accuracy of 56.82%.

### 4. CoT-Proxy: Cross-Format Transfer for Distilling Long-Horizon Policies
**Authors:** Dawid J. Kopiczko, Tijmen Blankevoort, Yuki M. Asano
**Link:** https://arxiv.org/abs/2611.33148v1
**Summary:** The paper addresses the challenge of distilling long-horizon policies from strong teacher models whose reasoning processes are inaccessible via APIs. The authors propose a method called CoT-Proxy that allows a student model to learn effectively from the teacher's actions alone, without relying on the teacher's chain-of-thought, leading to improved performance. Key results show that this approach significantly enhances the success rates of the student models on various tasks, with notable increases of up to 48% on specific benchmarks.

### 5. iWAM: Efficient Action Prediction from World Models without Explicit Future Prediction
**Authors:** Vansh Kapoor, Max Sobol Mark, Sreyas Venkataraman, Max Simchowitz, Aviral Kumar
**Link:** https://arxiv.org/abs/2611.33141v1
**Summary:** The paper presents iWAM, a method for efficient action prediction that leverages world-action models without the high computational cost of generating future scenes. It introduces the idea of conditioning action policies on intermediate features derived from a single evaluation of a video-generation model, rather than needing full frame predictions. The key contribution is demonstrating that this approach can retain the predictive performance of traditional world-action models while significantly reducing inference costs, as shown in various simulated benchmarks and real robot applications.

### 6. BriConstrain: Geometrically Constrained Decoding for Autoregressive Brick Assembly Generation
**Authors:** Nadav Magar, Amir Hertz, Ariel Shamir, Or Patashnik
**Link:** https://arxiv.org/abs/2611.33135v1
**Summary:** The paper addresses the issue of generating valid LEGO assemblies from language models, which often produce builds with parts that either collide or are unattached. The authors introduce BriConstrain, a decoding method that dynamically restricts the model's next-token probabilities to focus on valid attachment configurations, significantly improving the rate of collision-free builds from 31% to 91% for one format and from 15% to 65% for another, while operating at a lower cost than traditional rejection sampling methods.

### 7. A Bias in Disguise: Tiny Gradient Edits Stop a Small Language Model's Thinking Loops and Complement a Frontier Model's Weight Edit
**Authors:** Hussamuddin Syed
**Link:** https://arxiv.org/abs/2611.33133v1
**Summary:** The paper addresses the issue of low reasoning accuracy in small language models, specifically the Qwen3.5-0.8B, which struggles to complete thinking tasks effectively. The authors propose a method that combines tiny gradient edits with an existing weight editing technique to significantly improve the model's performance on MATH-500 problems, achieving an accuracy increase from around 15% to over 62% when both approaches are used together. Their findings demonstrate that these edits are mutually beneficial, allowing for enhanced reasoning capabilities in language models.

### 8. Exploratory Midtraining for Robot Policies
**Authors:** Kshitiz, Zheyuan Hu, Robyn Wu, Yizhou Li, Yunchu Zhang, Vattanary Tevy, Kavya Tayal, Shawn Yin, Aykut Onol, Kushal Arora, Dhruv Shah, Abhishek Gupta, Zackory Erickson, Aviral Kumar
**Link:** https://arxiv.org/abs/2611.33130v1
**Summary:** The paper addresses the limitation of robot policies that primarily learn from human demonstrations, which often lack the variety of low-level behaviors necessary for autonomous improvement. The authors propose a midtraining approach using a new dataset, $β$-Data, where human operators are guided by an adversarially perturbed environment, allowing for more diverse behavior exploration. Their method leads to better task execution, improved generalization across manipulation tasks, and more efficient online learning as robots require fewer attempts to successfully complete tasks compared to conventional training methods.

### 9. SAG-Mem-1.0 Technical Report
**Authors:** Yuchao Wu, XingCheng Liang, Xuanze Wang, Yini Huang, Yue Wu
**Link:** https://arxiv.org/abs/2611.33124v1
**Summary:** The paper presents SAG-Mem, a framework for long-term conversational memory that efficiently retrieves relevant facts from past dialogues without losing context or detail. It uses a combination of a lexical index for memory construction and a two-step retrieval process to enhance evidence gathering. The approach achieves the highest performance on established benchmarks, demonstrating its effectiveness in preserving dialogue and expanding retrieval based on evidence.

### 10. MetaFORGE: A Meta-Learning Framework for Harness Optimization in Automated Code Generation for Parallel Computing
**Authors:** Scott Piersall, Yang Gao, Shenyang Liu, Liqiang Wang
**Link:** https://arxiv.org/abs/2611.33119v1
**Summary:** The paper presents MetaFORGE, a meta-learning framework designed to enhance the generation of efficient and correct parallel programs using large language models. By optimizing natural-language specifications through a combination of testing, diagnostics, and performance profiling, MetaFORGE significantly improves program quality and execution efficiency compared to previous methods. The results show that it consistently outperforms zero-shot generation and an iterative baseline, showcasing its effective use of optimization knowledge across various computing tasks.
