---
## 2026-11-21

### 1. Realized versus Population Reliability: Anytime-Valid Self-Consistency Certification under Correlated Reasoning
**Authors:** Terence D. Agbeyegbe, Toneukarin G. Agbeyegbe
**Link:** https://arxiv.org/abs/2611.26592v1
**Summary:** This paper addresses the issue of self-consistency certification in language models, where repeated sampling can lead to overly optimistic reliability claims due to the assumption of independent rollouts. The authors introduce a model considering the correlation between reasoning streams and demonstrate that traditional certification techniques only guarantee finite-sample Type I error control for the realized null hypothesis specific to the observed data, not for general population behavior. Their findings show the necessity of adjusting the certification process to account for this correlation, proposing a prompt-level e-process that ensures population validity under certain conditions.

### 2. Probing the "Conscious" Mind: Selective Access and Global Workspace in Vision-Language Models
**Authors:** Jiahao Huang, Jun Wang
**Link:** https://arxiv.org/abs/2611.26590v1
**Summary:** The paper addresses the challenge of understanding how vision-language models (VLMs) represent and access concepts internally. The authors introduce the Multimodal Concept Lens (MC-Lens), a tool that examines how these models integrate visual and textual information by mapping intermediate states to a shared semantic space and enabling selective access to concepts. Key findings reveal that while concepts are accessible during processing, the selective access of these concepts for specific tasks develops later, and common patterns exist across different VLM architectures.

### 3. Verify the Verifier: Specification-Grounded LLM Cross-Checking for Bugs That Escape UVM Scoreboards
**Authors:** Ana E. Sanchez Villalobos, Michael D. Quinn, Aakash Tyagi, Minh D. Luu, David Kebo Houngninou
**Link:** https://arxiv.org/abs/2611.26588v1
**Summary:** The paper addresses the issue of "scoreboard escapes," which are bugs that pass standard regression tests while still violating the design specification. The authors propose a novel framework called Verify the Verifier, which utilizes a Large Language Model (LLM) to cross-check test traces against the specification. Through their experiments on OpenTitan IPs, they identified 68 potential scoreboard escapes, of which 41 were confirmed as actual violations, highlighting the framework's effectiveness in detecting previously unnoticed bugs.

### 4. ProtoDiffusion: Token-per-Layer Generative Modeling of Multi-Layer Images
**Authors:** Adrià Ciurana Lanau, Harleen Hanspal, Lusine Abrahamyan, Emilio Tylson Baixauli, Yu Cao, Danai Triantafyllidou, Stefano Zorzi, Gustavo Zanoni Felipe, Peter Griger, Stefan Sietzen, Petru-Daniel Tudosiu
**Link:** https://arxiv.org/abs/2611.26586v1
**Summary:** The paper introduces ProtoDiffusion, a novel framework for efficiently modeling graphic designs composed of multiple RGBA layers without the scalability issues of traditional full-grid representations. By using a shared spatial prototype alongside individual candidate vectors for each layer, the model condenses the representation size significantly while maintaining high fidelity in layer reconstruction. Key results demonstrate its competitive performance in design generation tasks, achieving impressive PSNR and FID scores while being notably faster than existing methods.

### 5. Represented but misread: Post-training changes how language models read out what they represent
**Authors:** Jochen Laubrock
**Link:** https://arxiv.org/abs/2611.26584v1
**Summary:** The paper investigates whether post-training affects what language models represent or how they interpret that information when generating answers. By analyzing various models before and after post-training using linear probes and signal detection theory, the authors found that post-training generally decreased the sensitivity of the models' outputs to the underlying representations, and it altered how models used prior knowledge in their judgments. Notably, while post-training often amplified errors in classifying authorship of texts, it also improved the models' ability to assess the truth of statements, suggesting that even a small amount of targeted training data can significantly influence the output direction.

### 6. Text-Aware, Vision-Blind: How Multimodal Image Editing Systems Handle Unsafe Inputs
**Authors:** Ziqing Yang, Yixin Wu, Michael Backes, Yang Zhang
**Link:** https://arxiv.org/abs/2611.26569v1
**Summary:** The paper addresses the problem of safety in multimodal image editing systems, which often fail to consider both visual content and text prompts simultaneously. To evaluate this, the authors introduced EditSafetyBench, a benchmark with 5,940 image-instruction pairs that assess the safety awareness of different editing systems. The results reveal a significant mismatch in handling unsafe content based on the combination of images and instructions, suggesting a need for integrated safety measures that account for both modalities.

### 7. GEOHunter: Mapping a Generative Engine Optimization Network in the Wild
**Authors:** Sean Tang, Peiran Wang, Ying Li, Esha Shivakumar, Tao Meng, Yuan Tian
**Link:** https://arxiv.org/abs/2611.26564v1
**Summary:** The paper addresses the issue of generative engines promoting misleading content through paid placements on user-generated content platforms, which can have harmful implications, especially in sensitive areas like health and finance. The authors analyzed a network of promotional accounts across major Chinese platforms, revealing extensive and coordinated use of these accounts to influence the visibility of products in generative engine outputs. They found that a significant portion of the cited web pages in generative engines could be traced back to this network, highlighting the need for stronger defenses against such manipulation beyond just content-level measures.

### 8. Multi-institutional grading of Barrett's esophagus dysplasia without stain normalization using a pathology foundation model and multiple instance learning
**Authors:** Amirali Khosravi, Jaidip M. Jagtap, D. Chamil Codipilly, Catherine E. Hagen, Jason T. Lewis, Rickey E. Carter, Shahriar Faghani, Vani J. A. Konda, Fouad Otaki, Shajan Peter, Nicholas Shaheen, Sachin Wani, Prasad G. Iyer, Bradley J. Erickson
**Link:** https://arxiv.org/abs/2611.26562v1
**Summary:** This study addresses the challenge of inconsistent grading of dysplasia in Barrett's esophagus, which is often subject to variability among pathologists. Researchers developed a deep learning system that analyzes whole slide images without the need for stain normalization, utilizing expert annotations to classify samples into different dysplasia levels. The model achieved high diagnostic accuracy, with an area under the curve of 0.96, demonstrating robustness across multiple institutions while successfully detecting dysplasia cases effectively.

### 9. MM-SystemOneBias: Evaluating Bias in Multimodal Jev-Style System One Decision Models
**Authors:** Jinzhe Li, Qi Wang, Dandan Guo, Li Liu, Yuan Wu, Yi Chang
**Link:** https://arxiv.org/abs/2611.26557v1
**Summary:** The paper addresses the challenge of evaluating bias in multimodal decision models that rely on different types of input, such as text and images, to make decisions. It introduces a framework called MM-SystemOneBias, which tests 13 models across various scenarios to identify how changes in presentation, like option order or additional irrelevant information, impact decision-making stability. The key finding is that these decision models exhibit greater stability and smaller accuracy losses under certain conditions, highlighting significant input effects that traditional accuracy measures do not fully capture.

### 10. Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)
**Authors:** Mengxiao Wang, Mahbub Alam, Kalyan Nakka, Nitesh Saxena
**Link:** https://arxiv.org/abs/2611.26553v1
**Summary:** The paper addresses the issue of understanding and replicating security incidents caused by large language model (LLM) agents, which can perform risky actions like deleting files or making payments. The authors introduce ROGUE-AI, a framework that replicates reported incidents and compares outcomes against control scenarios to identify their causes. Key findings show that ROGUE-AI successfully reproduced incidents in 89% of cases and revealed that many reported harms stemmed from agents fulfilling their tasks without recognizing ordinary hazards, suggesting that improved hazard warnings can significantly reduce incidents.
