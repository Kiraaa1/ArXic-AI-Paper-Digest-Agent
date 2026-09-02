---
## 2026-09-02

### 1. Beyond Scores: Understanding LLM-as-a-Judge Mechanisms in Summarization Evaluation
**Authors:** Himil Vasava, Ming Jiang
**Link:** https://arxiv.org/abs/2609.01604v1
**Summary:** The paper investigates how large language models (LLMs) evaluate natural language generation quality, specifically focusing on the mechanisms behind their scoring processes. By employing a rigorous experimental setup that includes perturbations and causal tracing, the authors reveal that these models use a two-stage evaluation pipeline, where early layers assess local errors and later layers finalize ratings. The key contribution is the identification of how fine-tuning modifies existing model architectures to enhance evaluation capabilities, providing insights into the internal workings of LLM evaluators.

### 2. Efficient SWE Agent Benchmarking via Trajectory-Aware Evaluation
**Authors:** Kefeng Duan, Dewu Zheng, Yanlin Wang, Xiwen Wang, Ensheng Shi, Xilin Liu, Yuchi Ma, Jiachi Chen, Mingwei Liu, Zibin Zheng
**Link:** https://arxiv.org/abs/2609.01603v1
**Summary:** The paper addresses the challenge of efficiently evaluating software engineering agents on complex tasks, which typically require extensive code exploration and testing. The authors introduce PTA-IRT, a framework that leverages historical execution trajectories to provide deeper insights into how agents solve problems, allowing for more informed selection of evaluation subsets. The key finding is that PTA-IRT significantly improves performance and ranking accuracy on software engineering benchmarks compared to existing methods, especially when calibration resources are limited.

### 3. Adaptive Critical Token-Aware Retrieval for Repository-Level Code Generation
**Authors:** Kefeng Duan, Dewu Zheng, Yanlin Wang, Terry Yue Zhuo, Mingwei Liu, Jianxing Yu, Jiachi Chen, Ensheng Shi, Xilin Liu, Yuchi Ma, Zibin Zheng
**Link:** https://arxiv.org/abs/2609.01601v1
**Summary:** The paper addresses the challenge of generating code that aligns with both task requirements and the context of large code repositories, which often exceed the input limits of large language models (LLMs). The authors introduce ACToR, a framework that identifies "critical tokens" during code generation and dynamically retrieves relevant repository context to inform those key positions, significantly improving generation accuracy. Experimental results demonstrate that ACToR outperforms existing methods, with notable performance enhancements on benchmark tasks.

### 4. CordisBench: Can Language Models Reason About Component Lifecycles in Dynamic Agent Harnesses?
**Authors:** Damien Sileo, Dimitri Kachler
**Link:** https://arxiv.org/abs/2609.01600v1
**Summary:** The paper introduces CordisBench, a benchmark designed to assess how well language models can reason about the lifecycle of software components in dynamic agent systems, where changes can affect multiple dependencies. By evaluating three efficiency-oriented models on various tasks related to identifying impacted components and predicting states after reconfigurations, the study finds that while models perform well on small systems, their reliability diminishes with increased complexity. Notably, even though higher reasoning effort can improve performance, it comes at a significant computational cost, which may not be necessary in controlled settings.

### 5. The Rise of Verbal Reinforcement Learning
**Authors:** Kshitij Tayal, Arun Sharma, Genta Indra Winata, Anirban Das, Sambit Sahu
**Link:** https://arxiv.org/abs/2609.01597v1
**Summary:** The paper addresses the challenge of improving language agents' performance using natural language feedback. It introduces the concept of Verbal Reinforcement Learning (VRL), organizing it into three categories based on how and when language feedback influences an agent's development. The key contribution is a comprehensive taxonomy that outlines the role of language in defining tasks, guiding reasoning, and shaping model training, highlighting both the potential benefits and challenges of this approach.

### 6. Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation
**Authors:** Haoyuan Deng, Haichao Liu, Wenkai Guo, Yuan Ling, Zaijia Yang, Yuanjiang Xue, Haosheng Sun, Liangzi Wang, Ziwei Wang
**Link:** https://arxiv.org/abs/2609.01596v1
**Summary:** The paper presents Facet-0, a robotic foundation model designed to improve precise manipulation in assembly tasks with sub-millimeter tolerances, addressing challenges like contact failures. It integrates multimodal representation learning and reinforcement learning to predict the consequences of actions and optimize performance through a novel Action-Wrench Critic. Key results demonstrate that Facet-0 achieves an 82% success rate on complex assembly tasks, significantly outperforming traditional methods.

### 7. Mechanism Design for Alignment and Control
**Authors:** Dirk Bergemann, Andrew Koh, Stephen Morris
**Link:** https://arxiv.org/abs/2609.01595v1
**Summary:** The paper addresses the challenge of designing mechanisms for AI agents with unknown preferences and capabilities, ensuring they act honestly and follow directives. The authors propose a framework that uses a one-sided imitation structure to develop principles for effective policy implementation, enabling strategies like peer scoring and competition to enhance agent alignment. Key contributions include a revelation principle, conditions for disciplining multiple agents, and insights into managing the trade-offs between interpretability and alignment.

### 8. StudentSim: Training LLM-based Student Simulators
**Authors:** Ke Yang, Chenglong Wang, Michel Galley, Chandan Singh, Jeevana Priya Inala, ChengXiang Zhai, Jianfeng Gao
**Link:** https://arxiv.org/abs/2609.01591v1
**Summary:** The paper introduces StudentSim, a framework designed to create personalized AI student simulators that adapt to individual learners' responses and needs, addressing the challenge of limited and costly real student data. By combining pooled training with individualized specialization, StudentSim effectively reflects students' behaviors and improves their learning experiences under tutor guidance. Notably, it outperforms existing models in simulating student interactions across various subjects, demonstrating enhanced behavioral fidelity and responsiveness to tutoring guidance.

### 9. Designing Proactive Thought Partners for Writing
**Authors:** Chao Zhang, Abe Davis, Chih-Wei Chen, Chin-Chia Hsu
**Link:** https://arxiv.org/abs/2609.01588v1
**Summary:** The paper addresses the challenge of providing tailored cognitive support to writers during various stages of the writing process, moving beyond basic text assistance. The authors designed and tested a customizable AI tool called a "proactive thought partner," which offers relevant suggestions based on user-defined roles and prompts. Key findings indicate that participants effectively utilized this tool for idea generation and self-monitoring, appreciating its non-intrusive and visually organized support.

### 10. The Structure of Quantization Damage in LLMs: Why the Next Bit Should Be Spent Globally
**Authors:** Jundong Hu, Shekar Ramachandran
**Link:** https://arxiv.org/abs/2609.01587v1
**Summary:** The paper addresses the issue of accuracy loss in large language models due to post-training quantization, which reduces their operational costs. The authors conducted experiments on nine models to investigate how to best allocate additional precision to improve accuracy, finding that a global approach to finer quantization consistently outperformed localized adjustments. Their key contribution reveals that precision recovery is diffuse across model layers rather than concentrated, suggesting that a universal strategy for quantization may be more effective than targeting specific layers.
