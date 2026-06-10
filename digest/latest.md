---
## 2026-06-10

### 1. When to Align, When to Predict: A Phase Diagram for Multimodal Learning
**Authors:** Ilay Kamai, Hugues Van Assel, Aviv Regev, Hagai B. Perets, Randall Balestriero
**Link:** https://arxiv.org/abs/2606.11190v1
**Summary:** The paper addresses the lack of systematic understanding in multimodal representation learning regarding when to use cross-modal alignment versus cross-modal prediction. The authors propose a unified linear framework that categorizes multimodal problems into four regimes based on their characteristics, helping practitioners identify the most effective approach for their specific datasets. Key findings demonstrate that certain conditions can make cross-modal training counterproductive, thus providing a tool for better decision-making before training models.

### 2. A Unifying Lens on Supervised Fine-Tuning Through Target Distribution Design
**Authors:** Tong Xie, Yuanhao Ban, Yunqi Hong, Sohyun An, Yihang Chen, Cho-Jui Hsieh
**Link:** https://arxiv.org/abs/2606.11189v1
**Summary:** The paper addresses the limitations of traditional supervised fine-tuning (SFT), which typically attempts to match observed tokens without considering their uniqueness or alignment with the model's prior knowledge. The authors introduce a new framework called Q-target that redefines SFT as a matter of designing target distributions, leading to a method called Target-SFT that adapts training objectives based on these distributions. Their findings demonstrate that this approach consistently outperforms existing methods across various reasoning tasks, highlighting a more foundational principle for effective SFT training.

### 3. EEVEE: Towards Test-time Prompt Learning in the Real World for Self-Improving Agents
**Authors:** Weixian Xu, Shilong Liu, Mengdi Wang
**Link:** https://arxiv.org/abs/2606.11182v1
**Summary:** The paper presents EEVEE, a novel framework for enabling large language model (LLM) agents to learn from multiple datasets in real-world scenarios, where tasks and inputs can vary widely. EEVEE introduces a smart routing mechanism to organize incoming data and optimize prompt configurations through a co-evolution learning strategy. The framework significantly enhances model performance and robustness across diverse datasets, achieving notable improvements in benchmark scores compared to existing state-of-the-art methods.

### 4. Data Journalist Agent: Transforming Data into Verifiable Multimodal Stories
**Authors:** Kevin Qinghong Lin, Batu EI, Yuhong Shi, Pan Lu, Philip Torr, James Zou
**Link:** https://arxiv.org/abs/2606.11176v1
**Summary:** The paper presents the Data Journalist Agent (Data2Story), a multi-agent framework designed to automate the process of transforming raw data into trustworthy, multimodal news stories. This system improves on traditional reporting by ensuring that claims are anchored in verifiable evidence and uses various media formats to enhance reader engagement. The evaluation shows that while Data2Story produces competitive and transparent stories, human journalists still excel in creative decision-making and design aspects.

### 5. The Role of Feedback Alignment in Self-Distillation
**Authors:** Semih Kara, Oğuzhan Ersoy
**Link:** https://arxiv.org/abs/2606.11173v1
**Summary:** The paper explores how to improve self-distillation in language models by optimizing the feedback context they receive during training. It compares three types of feedback structures—binary rewards, reference solutions, and step-by-step critiques—and finds that step-aligned critiques significantly enhance performance by effectively targeting specific reasoning failures without altering correct responses. This indicates that aligning feedback with the model's reasoning structure is crucial for effective self-distillation.

### 6. Predicting Future Behaviors in Reasoning Models Enables Better Steering
**Authors:** Evgenii Kortukov, Piotr Komorowski, Florian Klein, Paula Engl, Gabriele Sarti, Seong Joon Oh, Sebastian Lapuschkin, Wojciech Samek
**Link:** https://arxiv.org/abs/2606.11172v1
**Summary:** The paper addresses the challenge of controlling the outputs of large reasoning models (LRMs) that often produce unexpected results. It introduces a new technique called Future Probe Controlled Generation (FPCG), which uses specially trained activation probes to predict future behaviors based on intermediate reasoning steps, rather than relying on detection of behavior in generated text. This approach significantly improves steering effectiveness while maintaining output quality, demonstrating the importance of distinguishing between detection and prediction features in controlling LRM behavior.

### 7. Algorithmic and Minimax Complexities in Kernel Bandits
**Authors:** Yunbei Xu
**Link:** https://arxiv.org/abs/2606.11171v1
**Summary:** This paper reconciles two different methods in kernel bandit learning—Gaussian-process upper confidence bounds (GP-UCB) and decision-estimation coefficients (DEC)—by framing them within a shared algorithmic-information perspective. The authors propose a unified framework that combines the strengths of both approaches and demonstrate that algorithmic complexity can offer more insights than traditional minimax bounds in certain overparameterized scenarios. The key contribution is establishing that these two concepts provide distinct insights into the performance of bandit algorithms, particularly in the context of kernel methods.

### 8. Piper: A Programmable Distributed Training System
**Authors:** Megan Frisella, Shubham Tiwari, Andy Ruan, Yi Pan, Parker Gustafson, Mat Jacob, Gilbert Bernstein, Stephanie Wang
**Link:** https://arxiv.org/abs/2606.11169v1
**Summary:** The paper presents Piper, a programmable distributed training system designed to simplify the development and adaptation of large-scale model training by decoupling high-level parallelism strategies from their low-level execution. Piper allows users to easily define their training strategies using annotations and directives that transform a unified intermediate representation. The key contribution is that Piper achieves performance parity with existing methods while enhancing efficiency and enabling new parallelism strategies, demonstrating improved compute and communication scheduling.

### 9. Multi-Faceted Interactivity Alignment in Full-Duplex Speech Models
**Authors:** Atsumoto Ohashi, Neil Zeghidour, Alexandre Défossez, Eugene Kharitonov
**Link:** https://arxiv.org/abs/2606.11167v1
**Summary:** The paper addresses the issue of interactivity in full-duplex spoken dialogue models, which struggle with problems like excessive silence and poor turn-taking during conversations. The authors propose a post-training reinforcement learning approach that focuses on improving four aspects of interactivity—pause handling, turn-taking, backchanneling, and user interruption—using specific reward functions derived from human conversation data. Their method is tested on two models, resulting in significant enhancements in conversational interactivity during both offline evaluations and real-time dialogue interactions.

### 10. Flaws in the LLM Automation Narrative
**Authors:** George Perrett, Javae Elliott, Jennifer Hill, Marc Scott
**Link:** https://arxiv.org/abs/2606.11166v1
**Summary:** This paper critiques the narrative that large language models (LLMs) can match human experts in knowledge-based tasks, highlighting flaws in existing benchmarking methods that overstate LLM performance. The authors introduce a new benchmarking task that involves writing code for data analysis and compare LLM outputs to those of human experts, finding that humans outperform LLMs with more consistent results. The study emphasizes the need for evaluating the reliability and error rates of LLMs in high-stakes contexts.
