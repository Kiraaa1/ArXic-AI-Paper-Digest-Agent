---
## 2026-08-05

### 1. ParVL: Parallel Scaling and Expandable Compute Allocation for Multimodal LLMs
**Authors:** Yang Yang, Qinyu Zhao, Mouxiang Chen, Xiaohui Li, Lixin Gu, Wenhai Wang, Hongjie Zhang, Wenwei Zhang
**Link:** https://arxiv.org/abs/2608.04010v1
**Summary:** The paper addresses the limitations of existing scaling strategies in Multimodal Large Language Models (MLLMs), which often lead to inefficient memory use and fixed computation distribution between vision and language components. The authors propose a new framework called ParVL that allows for flexible, parallel computation by sharing backbone parameters across multiple vision and language branches and optimizing their allocation based on task requirements. Key results demonstrate that ParVL outperforms traditional single-branch models and shows that the optimal distribution of resources varies depending on the specific task.

### 2. SocietyBench: Forecasting Counterfactual Social-World Evolution
**Authors:** Zhenran Wang, Zhonghan Bian, Jinsong Li, Zhangyang Qi
**Link:** https://arxiv.org/abs/2608.04009v1
**Summary:** The paper introduces SocietyBench, a benchmark designed to evaluate how well large language models (LLMs) can forecast social events, a capability that has been largely overlooked compared to task completion abilities. This benchmark creates counterfactual timelines from real-world events and presents various forecasting questions, revealing that even the best models scored only 75 out of 100, indicating significant limitations in their predictive abilities. The authors emphasize the importance of evaluating models across multiple events, as performance gaps can vary widely.

### 3. WorldCup Arena: Prospective, Leakage-Free Evaluation of Frontier LLMs on a Live Tournament
**Authors:** Zhenran Wang, Zhonghan Bian, Jinsong Li, Zhangyang Qi
**Link:** https://arxiv.org/abs/2608.04008v1
**Summary:** The paper addresses the challenge of evaluating the forecasting abilities of large language models (LLMs) without the risk of using prior knowledge or memorization by conducting live predictions during the 2026 FIFA World Cup. The researchers asked six advanced LLMs to predict outcomes for matches in real-time, resulting in 4,494 predictions that showed average accuracy comparable to bookmakers. A key finding was that while the models agreed with each other more often than they were correct, they struggled particularly with closely contested matches and tended to favor certain outcomes, leading to consistently narrow performance margins among them.

### 4. TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning
**Authors:** Changle Qu, Sunhao Dai, Hengyi Cai, Yuqi Zhou, Xinran Chen, Simon, Jun Xu
**Link:** https://arxiv.org/abs/2608.04007v1
**Summary:** The paper presents TurnSight, a novel framework designed to enhance Tool-Integrated Reasoning in large language models (LLMs) by improving fine-grained credit assignment through turn-level hindsight self-distillation. Instead of relying on traditional trajectory-level supervision, TurnSight utilizes multiple hindsight perspectives derived from the agent's executions, allowing for more accurate learning signals. Experimental results demonstrate that this approach significantly boosts the performance of LLMs on complex tasks involving iterative tool interactions.

### 5. PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents
**Authors:** Shuhan Xue, Zixin Ding, Yichen Shen, Yinjie Wang, Zhenfei Yin, Yingcheng Wu, Yuxin Chen, Mengdi Wang, Ling Yang
**Link:** https://arxiv.org/abs/2608.04003v1
**Summary:** The paper introduces PAST-Bench, a benchmarking framework that tests how effectively personal AI agents improve their performance by using their past experiences during tasks. By systematically evaluating agents across various scenarios with and without retained experience, the study discovers that while agents do show improvement, it varies based on their capabilities. The authors also present Hermes+, an enhanced agent model that implements targeted interventions to boost learning from experience, demonstrating significant improvements in specific tasks.

### 6. Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility
**Authors:** Mohsen Hariri, Weicong Chen, Nahal Shahini, Vikash Singh, Kai Ye, Amirhossein Samandar, Debargha Ganguly, Sreehari Sankar, Yanyan Zhang, Shouren Wang, Jerry Peng, Biyao Zhang, Michael Hinczewski, Vipin Chaudhary
**Link:** https://arxiv.org/abs/2608.04001v1
**Summary:** The paper addresses the challenge of comparing different inference algorithms used in large language models, particularly regarding their performance during test-time scaling. The authors propose a systematic framework that classifies these algorithms based on their structures, establishes clear evaluation principles to improve reproducibility, and facilitates better reporting of computational costs and outcomes. As a key contribution, they also provide a comprehensive dataset of over 2 billion reasoning traces to support future research and benchmarking in this area.

### 7. Agogic: Performance-Timed Music Tokens for LLM-Native Text-to-Symbolic-Music Generation
**Authors:** Junhao Chen, Mingjin Chen, Jingjia Mao, Lin Chen, Saining Zhang, Minglin Chen, Ruocheng Wu, Liaoyuan Fan, Wenyi Li, Mingju Gao, Henghaofan Zhang, Zhihao Li, Hao Zhao, Yufei Wang, Ruqi Huang
**Link:** https://arxiv.org/abs/2608.03999v1
**Summary:** The paper addresses the challenge of how to effectively tokenize music for text-to-music language models, a decision that influences model performance. By systematically replacing tokenization methods while keeping the model and other factors constant, the authors demonstrate that the choice of music representation significantly impacts how well the model generates music, with their new performance-resolution tokenization achieving superior results compared to traditional methods. They provide extensive resources, including trained models and datasets, to facilitate further research in this area.

### 8. When Attention Goes Blind: Numerical Failure in ALiBi Positional Encodings
**Authors:** Christopher Schröder, Lukas Gienapp, Ferdinand Schlatt, Martin Potthast, Gerhard Heyer
**Link:** https://arxiv.org/abs/2608.03994v1
**Summary:** The paper addresses a critical issue with ALiBi positional encoding, where the linear bias scaling leads to floating-point precision underflows, causing many attention weights to be zeroed out and affecting model performance. The authors analyze this failure mode, test four mitigation strategies, and find that using log-scaled distances significantly improves token retrieval while maintaining strong performance in standard benchmarks. They offer practical recommendations for training models utilizing ALiBi to enhance retrieval tasks.

### 9. Assessment of Conditional Diffusion Model for Synthetic Histopathology Image Generation
**Authors:** Seyed Kahaki, Shijie Li, Weijie Chen, Nicholas Petrick
**Link:** https://arxiv.org/abs/2608.03990v1
**Summary:** This paper addresses the challenge of evaluating the quality of synthetic histopathology images, which are essential for overcoming data shortages in computational pathology. The authors propose improved evaluation metrics based on domain-specific features, utilizing foundation models trained on digital pathology data, and demonstrate that these metrics correlate better with the performance of downstream tasks, specifically nuclei segmentation, than conventional metrics. Their key finding emphasizes that diversifying the generated training data is more beneficial for segmentation model performance than simply enhancing the visual fidelity of individual images.

### 10. string2string Studio: An Interactive, In-Browser Platform for String-to-String Algorithms
**Authors:** Mirac Suzgun, James Zou, Stuart M. Shieber, Dan Jurafsky
**Link:** https://arxiv.org/abs/2608.03984v1
**Summary:** string2string Studio is an interactive web platform designed for analyzing string-to-string algorithms relevant to fields like natural language processing and computational biology. It features optimized C++ algorithms compiled to WebAssembly, allowing for high-speed local computations without installation, and provides detailed output that makes algorithms transparent and easy to debug. The platform achieves significant performance improvements over prior methods, with internal benchmarks showing speedups up to 2,500 times, and offers accurate homology search results comparable to established tools like NCBI BLAST+.
