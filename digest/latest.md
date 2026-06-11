---
## 2026-06-11

### 1. Reroute, Don't Remove: Recoverable Visual Token Routing for Vision-Language Models
**Authors:** Cheng-Yu Yang, Shao-Yuan Lo, Yu-Lun Liu
**Link:** https://arxiv.org/abs/2606.12412v1
**Summary:** The paper addresses the inefficiency in vision-language models caused by the high computational costs of processing visual tokens during decoder inference. Instead of permanently removing low-ranking tokens, the authors propose a "Reroute" approach that allows tokens to be temporarily bypassed and reconsidered later, which helps improve grounding performance while still reducing overall computational load. This method demonstrates that visual token reduction can be effectively done through recoverable routing rather than irreversible pruning, enhancing model effectiveness without sacrificing performance.

### 2. Context-Driven Incremental Compression for Multi-Turn Dialogue Generation
**Authors:** Yeongseo Jung, Jaehyeok Kim, Eunseo Jung, Jiachuan Wang, Yongqi Zhang, Ka Chun Cheung, Simon See, Lei Chen
**Link:** https://arxiv.org/abs/2606.12411v1
**Summary:** The paper addresses the inefficiencies and errors caused by traditional methods of handling long dialogue histories in conversational agents. It introduces a new method called Context-Driven Incremental Compression (C-DIC) that organizes conversation threads and allows for dynamic information sharing across dialogue turns, improving both memory efficiency and accuracy. The results show that C-DIC significantly enhances performance and maintains consistent response times and quality over extended interactions.

### 3. FACTR 2: Learning External Force Sensing for Commodity Robot Arms Improves Policy Learning
**Authors:** Steven Oh, Jason Jingzhou Liu, Tony Tao, Philip Han, Kenneth Shaw, Satoshi Funabashi, Ruslan Salakhutdinov, Deepak Pathak
**Link:** https://arxiv.org/abs/2606.12406v1
**Summary:** The paper addresses the challenge of enabling force-sensitive manipulation in low-cost robotic arms, which typically lack dedicated force sensors. The authors introduce a method called Neural External Torque Estimation (NEXT) that estimates external joint torques using only brief free-motion data, along with an innovative training technique called Force-Informed Re-Sampling Training (FIRST) that improves robotic policy learning. The key contribution is that this approach significantly enhances the performance of robot arms in complex tasks without requiring additional sensing hardware, achieving over 17% better task progress compared to previous methods.

### 4. DIRECT: When and Where Should You Allocate Test-Time Compute in Embodied Planners?
**Authors:** Jadelynn Dao, Milan Ganai, Yasmina Abukhadra, Ajay Sridhar, Mozhgan Nasr Azadani, Katie Luo, Clark Barrett, Jiajun Wu, Chelsea Finn, Marco Pavone
**Link:** https://arxiv.org/abs/2606.12402v1
**Summary:** The paper addresses the challenge of efficient test-time computation in Vision-Language Models (VLMs) for embodied agents, which often leads to increased costs and latency without guaranteed performance improvements. The authors propose DIRECT, a routing framework that strategically allocates compute resources based on multimodal scene context, resulting in significant efficiency gains. Their experiments show that DIRECT achieves comparable or better success rates in robotic tasks while reducing average latency by up to 65%, demonstrating a more effective approach to utilizing test-time compute in embodied planning.

### 5. Doc-to-Atom: Learning to Compile and Compose Memory Atoms
**Authors:** Xingjian Diao, Wenbo Li, Yashas Malur Saidutta, Avinash Amballa, Lazar Valkov, Srinivas Chappidi
**Link:** https://arxiv.org/abs/2606.12400v1
**Summary:** The paper addresses the challenge of efficiently handling long input sequences for document comprehension in Large Language Models, which typically struggle with memory and speed due to the quadratic cost of attention. The authors introduce Doc-to-Atom, a method that breaks documents into semantically distinct "knowledge atoms," each represented by an independent micro-LoRA adapter. This approach allows for more targeted and efficient retrieval at inference time, leading to improved performance on question-answering tasks while minimizing memory usage compared to previous methods.

### 6. Redesign Mixture-of-Experts Routers with Manifold Power Iteration
**Authors:** Songhao Wu, Ang Lv, Ruobing Xie, Yankai Lin
**Link:** https://arxiv.org/abs/2606.12397v1
**Summary:** The paper addresses the challenge of optimizing router matrices in Mixture-of-Experts (MoE) models, which need to effectively represent and connect to the underlying expert matrices. The authors introduce a new design method called Manifold Power Iteration (MPI), which aligns router rows with the principal direction of the associated experts to enhance token-expert affinity. Their experiments show that this approach leads to more effective MoE models, improving performance across various scales.

### 7. System Report for CCL25-Eval Task 5: New Dataset and LoRA-Fine-Tuned Qwen2.5
**Authors:** Haotao Xie
**Link:** https://arxiv.org/abs/2606.12392v1
**Summary:** The paper addresses the challenges in translating and interpreting classical Chinese poetry, which has been overlooked in previous research. To enhance performance in this area, the authors created a specialized dataset called CCPoetry-49K and fine-tuned the Qwen2.5 model using Low-Rank Adaptation (LoRA), resulting in the development of a new model named PoetryQwen. The key finding is that PoetryQwen outperforms its predecessor by 9.7% on a relevant benchmark, demonstrating significant improvements in translation precision and emotional understanding of poetry.

### 8. TAHOE: Text-to-SQL with Automated Hint Optimization from Experience
**Authors:** Zhiyi Chen, Jie Song, Peng Li
**Link:** https://arxiv.org/abs/2606.12387v1
**Summary:** The paper presents Tahoe, a system designed to enhance Text-to-SQL performance by optimizing prompts dynamically to handle complex SQL dialects and user preferences. It utilizes an error-driven hint learning approach that builds a structured Hint Bank from debugging traces and feedback, enabling the model to better navigate SQL generation tasks. Key improvements include raising the pass rate for Text-to-SQL queries from 61.95% to 79.42% and achieving a 100% pass rate for Snowflake syntax, all without needing to retrain the underlying language model.

### 9. ATLAS: Active Theory Learning for Automated Science
**Authors:** Noémi Éltető, Nathaniel D. Daw, Kimberly L. Stachenfeld, Kevin J. Miller
**Link:** https://arxiv.org/abs/2606.12386v1
**Summary:** The paper presents ATLAS, an active learning framework that automates the process of designing experiments to uncover interpretable behavioral models in cognitive science. By generating diverse mechanistic hypotheses and selectively conducting experiments, ATLAS significantly improves sample efficiency—by 5-10 times—compared to random experimentation. The results demonstrate its potential to advance scientific inquiry by efficiently discovering and validating behavioral models.

### 10. Which Models Are Our Models Built On? Auditing Invisible Dependencies in Modern LLMs
**Authors:** Sanjay Adhikesaven, Haoxiang Sun, Sewon Min
**Link:** https://arxiv.org/abs/2606.12385v1
**Summary:** The paper addresses the challenge of uncovering the complex and often hidden dependencies that modern large language models (LLMs) have on other models in their training and operation. It introduces ModSleuth, a system designed to systematically identify and reconstruct these dependencies from publicly available sources, tackling issues like inconsistent documentation. The key contribution is the generation of extensive dependency graphs revealing important insights into licensing obligations and discrepancies, which enhance transparency in the development of LLMs.
