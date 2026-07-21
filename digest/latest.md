---
## 2026-07-21

### 1. The Many Senses of Visual Similarity: A Text-Prompted Image Perceptual Metric
**Authors:** Sheng-Yu Wang, Yotam Nitzan, Aaron Hertzmann, Jun-Yan Zhu, Eli Shechtman, Alexei A. Efros, Richard Zhang
**Link:** https://arxiv.org/abs/2607.18237v1
**Summary:** The paper addresses the limitation of existing visual similarity metrics, which oversimplify human judgments by providing only a single score that fails to capture the nuanced ways people perceive similarity in images. The authors introduce a dataset of human similarity assessments across various aspects, and develop the Text-Prompted Image Perceptual Similarity (TPIPS) metric by fine-tuning a vision-language model to consider these nuances based on text prompts. The key contribution is that TPIPS better aligns with human perception of visual similarity and enhances tasks like text-guided retrieval and evaluation of generative models.

### 2. Patch Policy: Efficient Embodied Control via Dense Visual Representations
**Authors:** Gaoyue Zhou, Zichen Jeff Cui, Ada Langford, Bowen Tan, Yann LeCun, Lerrel Pinto
**Link:** https://arxiv.org/abs/2607.18236v1
**Summary:** The paper introduces Patch Policy, a new architecture that allows robotic control systems to efficiently utilize dense visual features from pre-trained Vision Transformers without the heavy computational cost of large vision-language models. By employing a block-causal attention mechanism, Patch Policy effectively manages spatial information and temporal causality, leading to a 40% improvement in performance over traditional global pooled representations and outperforming a fine-tuned model with only 0.7% of its parameters. This approach provides a way for the robotics field to harness advanced visual representation techniques while maintaining operational efficiency.

### 3. Automated Discovery Has No Universally Superior Harness
**Authors:** Akshat Gupta, Jermaine Lei, Alexander Lu, Gopala Anumanchipalli, Leshem Choshen
**Link:** https://arxiv.org/abs/2607.18235v1
**Summary:** The paper addresses the issue that existing autonomous discovery systems often fail to provide universally superior performance due to inherent variability in their design and execution. The authors systematically analyze various components of the OpenEvolve and TTT-Discover systems by evaluating 30 different harnesses across multiple problem scenarios using extensive trials. They find that no single harness consistently outperforms others, advocating for a tailored approach to harness selection based on specific tasks, and introducing a method for adaptive allocation of resources that enhances discovery outcomes.

### 4. It's Not What You Say, It's How You Say It: Evaluating LLM Responses to Expressions of Belief
**Authors:** Kevin Du, Clara Kümpel, Michelle Wastl, Alex Warstadt
**Link:** https://arxiv.org/abs/2607.18232v1
**Summary:** The paper addresses how large language models (LLMs) interpret and respond to users' expressions of belief, which can vary in linguistic style and impact how models prioritize context versus prior information. The authors developed a typology of these expressions and assessed 16 different LLMs to see how their responses vary based on the linguistic framing used. Key findings indicate that larger and instruction-tuned models are generally less responsive to contextual beliefs, highlighting important patterns that can inform prompt design and increase model robustness.

### 5. Simple Domain Generalization for Strong Pixel-Level Image Tampering Detection in Modern VLMs
**Authors:** Yi Tang, Xinyi Shang, Jiacheng Cui, Sondos Mahmoud Bsharat, Jiacheng Liu, Xiaohan Zhao, Tran Dinh Tien, Ahmed Elhagry, Salwa K. Al Khatib, Tianjun Yao, Yonina C. Eldar, Jing-Hao Xue, Hao Li, Salman Khan, Zhiqiang Shen
**Link:** https://arxiv.org/abs/2607.18230v1
**Summary:** This paper addresses the challenge of detecting pixel-level image tampering in outputs from modern vision-language models (VLMs), which can vary significantly across different models and distributions. The authors propose a practical training framework that includes a balanced minibatch sampling method and a late-injection strategy to enhance robustness and adaptability without overfitting. Their approach achieves significant improvements, outperforming the previous state-of-the-art by over 26% in localization accuracy metrics across several VLMs.

### 6. Logical Judgments Under Pressure: Diagnosing Syllogistic Stability with Learned Soft Prefixes
**Authors:** Brian K Chen
**Link:** https://arxiv.org/abs/2607.18228v1
**Summary:** The paper investigates how learned soft prefixes can influence correct logical judgments in syllogistic reasoning tasks. By applying these prefixes to a benchmark dataset while keeping the models fixed, the authors found that prefixes can divert many correct answers and exhibit significant effects even with unseen data variations. The main contribution is revealing that these prefixes evoke a broad preference for certain answers across different models, highlighting varying levels of logical stability and biases in the models' responses.

### 7. Causal Discovery on Irregular Time Series
**Authors:** Martim Penim, Ricardo Ribeiro Pereira, Jacopo Bono, Hugo Ferreira, Mário A. T. Figueiredo, Pedro Bizarro
**Link:** https://arxiv.org/abs/2607.18226v1
**Summary:** The paper addresses the challenge of causal discovery in irregularly sampled time series data, which traditional methods struggle to handle due to their reliance on regular sampling. The authors propose an extension of the PCMCI+ method, allowing it to aggregate causal influences over defined time windows instead of fixed lags. Their evaluations demonstrate that this modified approach effectively recovers causal structures in synthetic data and significantly outperforms the standard PCMCI+ method when applied to irregularly sampled datasets.

### 8. Vector Search As Nearest Neighbor Matching: RAG-based Policy Learning in Causal Inference
**Authors:** Masahiro Kato, Taka Kato
**Link:** https://arxiv.org/abs/2607.18225v1
**Summary:** The paper addresses the challenge of policy learning in causal inference by integrating retrieval-augmented generation (RAG) with nearest-neighbor matching. The authors propose both one-step and two-step methods, where the two-step approach utilizes vector search to gather action-specific evidence and estimates expected outcomes to inform action selection. A key contribution is the decomposition of regret in the two-step method, which is analyzed using bounds from nearest-neighbor estimators, enhancing understanding of its performance relative to traditional methods.

### 9. GigaPath-Flash and GigaTIME-Flash: Efficient Pathology Foundation Models for Whole-Slide and Tumor Microenvironment Analysis
**Authors:** Naoto Usuyama, Jeya Maria Jose Valanarasu, Sicong Yao, Hanwen Xu, Jaspreet Bagga, Guanghui Qin, Robert E. Kramer, Cliff Wong, Soohee Lee, Hao Qiu, Theodore Zhengde Zhao, Racheli Ben Shimol, Angela Crabtree, Kevin Matlock, Eduardo Alejandro Lozano Garcia, Naiteek Sangani, Alberto Santamaria-Pang, Jason Entenmann, Alexandra Q. Bartlett, Bill J. Wright, Bernard A. Fox, Brian Piening, Sheng Zhang, Sheng Wang, Tristan Naumann, Carlo Bifulco, Hoifung Poon
**Link:** https://arxiv.org/abs/2607.18218v1
**Summary:** The paper presents GigaPath-Flash and GigaTIME-Flash, two efficient foundation models aimed at improving whole-slide analysis in computational pathology and tumor microenvironment prediction from histopathology data. These models significantly reduce computational requirements while maintaining high performance, with GigaPath-Flash achieving 97% of a larger model's performance with 50 times less compute, and GigaTIME-Flash offering better predictions than its predecessor while being faster and more memory-efficient. The authors also provide open-access models, promoting wider use in clinical and research settings.

### 10. SWE-Pruner Pro: The Coder LLM Already Knows What to Prune
**Authors:** Yuhang Wang, Yuling Shi, Shaoqiu Zhang, Jialiang Liang, Shilin He, Siyu Ye, Yuting Chen, Kai Cai, Xiaodong Gu
**Link:** https://arxiv.org/abs/2607.18213v1
**Summary:** The paper addresses the challenge of efficiently managing long context in coding agents by improving context pruning methods. The authors introduce SWE-Pruner Pro, which utilizes the agent's internal representations to determine which parts of tool outputs to prune, eliminating the need for a separate code classifier. This approach achieves significant reductions in token usage—up to 39%—while maintaining high task quality and even improving performance on certain benchmarks.
