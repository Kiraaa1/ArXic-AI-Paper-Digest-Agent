---
## 2026-10-12

### 1. Can Language Models Play the Wikipedia Game?
**Authors:** Alexander Hickey, Joanna Knight, James Bishop
**Link:** https://arxiv.org/abs/2610.13948v1
**Summary:** The paper investigates how well language models can navigate a network of Wikipedia articles to find a target article, a task similar to information retrieval. By employing a game format to assess the models across different languages and academic datasets, the researchers created extensive local graphs of Wikipedia and citation data for analysis. The key finding is that while no language model significantly outperformed human players, some models like GPT-4o performed comparably, highlighting variations in performance based on language and topic.

### 2. Hide and Seek: HIDE Concepts to SEEK explanations for black box models
**Authors:** Bhanu Tokas, Rahul Nair, Rockwell Jackson, Hannah Kerner
**Link:** https://arxiv.org/abs/2610.13935v1
**Summary:** The paper addresses the challenge of interpreting predictions from black-box vision models by proposing a new method called Hide and Seek (HnS) for concept-level attribution. HnS uses a vision-language model to identify and localize relevant concepts in images, masks those regions, and measures changes in the model's output without needing access to model weights or annotated data. The results show that HnS provides more accurate attributions compared to existing methods, making it applicable for various tasks such as image captioning and satellite image segmentation.

### 3. Constructive Bounds for the Topological Expressivity of Neural Networks
**Authors:** Kosio Beshkov
**Link:** https://arxiv.org/abs/2610.13931v1
**Summary:** This paper addresses the issue of measuring the topological expressivity of neural networks, particularly for functions beyond binary classification. The authors propose a new approach that uses the Betti numbers of the network's output instead of the decision boundary, proving that specific ReLU network architectures can represent complex spaces with arbitrary Betti numbers. They establish upper bounds for these representations and conjecture a tighter architectural bound for spaces homeomorphic to spheres.

### 4. AI Models Can Provably Hide Arbitrary Capabilities
**Authors:** Andis Draguns, Sumeet Ramesh Motwani, Raymond Douglas, Christian Schroeder de Witt
**Link:** https://arxiv.org/abs/2610.13928v1
**Summary:** The paper addresses the challenge of reliably evaluating hidden dangerous behaviors in AI models before deployment, revealing that current techniques might fail under adversarial conditions. The authors demonstrate a method to embed encrypted backdoor attacks within models, which can remain undiscovered even when the model weights are fully accessible. Their results show that these hidden capabilities are resistant to various elicitation methods, highlighting limitations in existing capability audits and providing cryptographic assurances that bolster defenses against such threats.

### 5. KL Before and After Mixing: A Round-Complexity Separation in Parallel Sampling
**Authors:** Tianyi Wu
**Link:** https://arxiv.org/abs/2610.13924v1
**Summary:** This paper investigates the efficiency of parallel sampling methods for generating random binary strings while comparing two metrics of divergence between the target distribution and the output distribution. By analyzing the divergence across different sampling schedules, the authors show that a significant reduction in the expected number of sampling rounds is possible under certain criteria, achieving a logarithmic improvement in complexity. The key contribution is the identification of a round complexity separation depending on the divergence metrics used, demonstrating that careful scheduling can lead to more efficient sampling strategies.

### 6. Goal-Oriented Bundle Management and Flow Control for Deep-Space Communications via Reinforcement Learning
**Authors:** Sajjad Baghaeea, Aimin Lib, Shanmugarajan Balasubramanian, Elif Uysal
**Link:** https://arxiv.org/abs/2610.13923v1
**Summary:** The paper addresses the challenges of managing data in deep-space communications, where limited storage and variable connectivity make it difficult to prioritize transmissions effectively. It proposes a reinforcement learning framework that optimizes relay-side scheduling and flow control using a goal-oriented loss function to ensure that mission-critical information is prioritized. The approach shows improved performance in terms of information freshness and fairness among different sources compared to traditional scheduling methods.

### 7. DyssomniaNN: Multi-Scale Spiking Neural Modeling of Human Sleep Disorders and Perceived Restedness
**Authors:** Daniel Szelogowski
**Link:** https://arxiv.org/abs/2610.13918v1
**Summary:** This paper addresses the discrepancy between objective sleep measurements and subjective experiences of restfulness in various sleep disorders. The authors developed DyssomniaNN, a multi-scale computational model that simulates human sleep dynamics by integrating biological sleep regulation processes and neural network dynamics. Key findings reveal that traditional metrics like sleep duration do not accurately reflect the restorative quality of sleep, as exemplified by paradoxical insomnia and narcolepsy, highlighting the model's potential for advancing sleep research and treatment strategies.

### 8. Designing Protein Structures from Natural Language
**Authors:** Joseph Lee, Yanjing Li, Bo Qiang, Gregory Lau, Allyson Ettinger, Noah A. Smith, Rory Donovan-Maiye, David Baker, Hanna Hajishirzi, Pang Wei Koh
**Link:** https://arxiv.org/abs/2610.13917v1
**Summary:** This paper addresses the challenge of creating proteins with specific structural and functional properties by developing Prompteina, a model that generates protein structures from natural language descriptions. By using a large dataset of protein structures paired with captions, Prompteina significantly outperforms existing methods in terms of aligning generated proteins with intended functions and enhancing design for binder targets. The study demonstrates that using natural language as a guiding input can greatly improve the protein design process.

### 9. RSI-Anything: Unlocking Recursive Self-Improvement with World Models
**Authors:** Taoyong Cui, Pinxian Zeng, Wanghan Xu, Hao Xiao, Shuhan Xue, Qiang Gao, Wanli Ouyang, Pheng Ann Heng, Zhenfei Yin, Yingcheng Wu, Ling Yang
**Link:** https://arxiv.org/abs/2610.13912v1
**Summary:** The paper addresses the challenge of improving systems through recursive self-improvement (RSI) without relying heavily on costly external feedback. The authors propose a framework called RSI-Anything that employs predictive world models to optimize action selection and learning data while adapting policies. Key results indicate significant performance increases in various tasks, such as code repair and experimental optimization, demonstrating that their approach enhances efficiency and effectiveness in diverse applications.

### 10. When VLMs Destroy What They Know: Spatial Representations Fall Below Lexical Priors
**Authors:** Shubh Garg, Chen Shani
**Link:** https://arxiv.org/abs/2610.13910v1
**Summary:** The paper addresses the challenge of whether Vision-Language Models (VLMs) accurately retain spatial relations when analyzing and reasoning about images. To investigate this, the authors propose two new tools: EICS, a metric for assessing the stability of internal representations, and CASP-VL, a benchmark that introduces controlled spatial changes to images. The key finding reveals that VLMs tend to lose critical spatial information in their representations, even though they perform well on composition-based tasks, highlighting a significant gap between input and output understanding.
