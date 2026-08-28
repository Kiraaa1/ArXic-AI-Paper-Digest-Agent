---
## 2026-08-28

### 1. CritICL: Inference-Time Weak-to-Strong Generalization from Small Language Model Failure Modes
**Authors:** Yufan Wu, Yinghui He, Zhengyi Hu, Lang Wei, Ruichen Li, Qifan Yang, Ting Zhu
**Link:** https://arxiv.org/abs/2608.27455v1
**Summary:** The paper introduces CritICL, a new framework designed to enhance the reasoning abilities of large language models (LLMs) during inference by efficiently leveraging their failure modes as guidance. CritICL operates by using either dynamic predictions or a static profile of common failure patterns to provide helpful critiques, ultimately leading to better performance with fewer required outputs compared to traditional methods. Experimental results demonstrate that CritICL not only surpasses standard in-context learning but also competes effectively with more resource-intensive scaling techniques.

### 2. WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution
**Authors:** Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng, Andrew Tomkins, Da-Cheng Juan, Tu Vu
**Link:** https://arxiv.org/abs/2608.27454v1
**Summary:** The paper addresses the challenge of systematically reusing and refining knowledge gained from AI agents' experiences to improve their skills. The authors introduce WikiSkill, a framework that organizes this knowledge into a persistent wiki, allowing for the continuous evolution of agent skills based on accumulated experience. Their key finding is that this method consistently surpasses existing approaches in skill development and shows that larger models benefit more from these evolved skills, while smaller models with skills can outperform much larger models lacking them.

### 3. SWE-Prime: Fewer Trajectories, Better Performance
**Authors:** Dewu Zheng, Ruizhe Ye, Yanlin Wang, Yang Ye, Hongyu Zhang, Ensheng Shi, Xilin Liu, Yuchi Ma, Jianxing Yu, Zibin Zheng
**Link:** https://arxiv.org/abs/2608.27449v1
**Summary:** The paper addresses the challenge of improving large language models' performance in resolving real-world software issues, which can be hampered by noisy supervision from successful but flawed training data. The authors introduce SWE-Prime, a two-stage data selection method that filters training trajectories and their segments based on quality and relevance. Their experiments show that utilizing only 10% of high-quality trajectories selected by this method leads to significant performance improvements over training with the entire dataset.

### 4. TTPO: Test-Time Policy Optimization
**Authors:** Aozhe Wang, Zhengxi Lu, Jianze Wang, Shangke Lv, Ying Liu, Weiming Lu, Jun Xiao, Yueting Zhuang, Hua Yang, Qianglong Chen, Yongliang Shen
**Link:** https://arxiv.org/abs/2608.27448v1
**Summary:** The paper addresses the challenge of optimizing large language models at test time without relying on ground-truth labels, which can lead to error propagation through pseudo-labeling. The authors introduce Test-Time Policy Optimization (TTPO), an approach that combines On-Policy Self-Distillation with Grouped Reinforcement Learning to selectively distill correct outputs while minimizing the impact of incorrect ones. Key results show that TTPO achieves performance comparable to supervised methods on various benchmarks, significantly improving the Qwen3 model's test-time capabilities and demonstrating effective generalization across tasks.

### 5. From Static to Dynamic: Benchmarking Real-World Code Review with MCR-Bench
**Authors:** Dewu Zheng, Yanlin Wang, Xiwen Wang, Kefeng Duan, Hongyu Zhang, Xilin Liu, Yuchi Ma, Zibin Zheng
**Link:** https://arxiv.org/abs/2608.27442v1
**Summary:** The paper introduces MCR-Bench, a new benchmark for evaluating automated code review systems that captures the complex multi-round interactions between developers and reviewers, which are often overlooked in existing models. By analyzing 2,269 real-world code review tasks across various programming languages, the authors find that current large language models struggle significantly with defect detection and lifecycle tracking, especially as the number of interaction rounds increases. Key insights include that their performance varies greatly by defect type and severity, highlighting the limitations in handling complex defects and suggesting areas for improvement in LLM design.

### 6. RedEvoAgent: Automatic Red-Teaming Agent with Experience-Driven Skill Evolution
**Authors:** Junjie Zhang, Hui Liu, Kecheng Chen, Xianbo Mo, Changsheng Chen, Haoliang Li
**Link:** https://arxiv.org/abs/2608.27439v1
**Summary:** The paper introduces RedEvoAgent, an advanced red-teaming agent designed to address the risk of harmful tool use in large language models (LLMs) by automatically evolving attack strategies based on their effectiveness. Unlike traditional methods that rely on static attack patterns, RedEvoAgent distills and updates attack skills using a profiling system and performance validation, resulting in improved efficiency and adaptability across various targets. Testing indicates that RedEvoAgent outperforms existing red-teaming approaches, demonstrating greater versatility and effectiveness in real-world scenarios.

### 7. Mechanistic Reaction Prediction via Discrete Flow Matching on Graph-Structured Electron Occupation
**Authors:** Nguyen Xuan-Vu, Octavian Susanu, Daniel Armstrong, Philippe Schwaller
**Link:** https://arxiv.org/abs/2608.27429v1
**Summary:** The paper addresses the challenge of predicting chemical reactions by focusing on the transformations of electron distributions rather than merely generating product molecules or modifying molecular structures. It introduces a novel method called MAELLE, which treats reaction mappings as discrete flow matching processes over electron occupation vectors, utilizing techniques from Continuous-time Markov Chains and Optimal Transport. The key contribution is MAELLE's ability to outperform existing models on benchmark tests while demonstrating robustness in challenging scenarios, and it also provides mechanistic insights into reaction pathways and potential side products.

### 8. Stochastic Estimation of Transduced Language Models
**Authors:** Vésteinn Snæbjarnarson, Samuel Kiegeland, Manuel de Prada Corral, Ryan Cotterell, Tim Vieira
**Link:** https://arxiv.org/abs/2608.27428v1
**Summary:** The paper addresses the challenge of accurately estimating the probability of target prefixes in transduced language models (TLMs), which can involve an overwhelming number of source strings. The authors propose a novel method that involves resampling source prefixes without replacement and reweighting them, resulting in an unbiased estimator for target prefix probabilities. Their approach significantly reduces computational time while maintaining estimation accuracy, making it particularly effective for long target strings, such as in DNA-to-amino-acid transduction tasks.

### 9. Persona-Execution Separation: An Architecture Pattern for Evolving LLM Agents under Execution Audit
**Authors:** Yisen Xi
**Link:** https://arxiv.org/abs/2608.27427v1
**Summary:** The paper addresses the challenge of allowing the persona of large language model (LLM) agents to evolve while maintaining a traceable and auditable execution process in regulated environments. To solve this, the authors propose the Persona-Execution Separation (PES) architecture, which separates persona and execution into different trust domains connected by controlled interfaces, ensuring that execution remains faceless and traceable. The key contribution is a framework that enables persona flexibility and execution accountability, demonstrated through a pilot case that highlights the architecture's effectiveness in maintaining isolation between persona and execution without compromising governance.

### 10. Beyond F1: Evaluating Coverage and Failure Recovery in AI Model Security Scanners
**Authors:** Qianlong Lan, Vinothini Pandurangan, Anuj Kaul, Indranil Sanyal
**Link:** https://arxiv.org/abs/2608.27424v1
**Summary:** The paper addresses the limitations of conventional evaluation metrics for static security scanners used in assessing machine learning artifacts, which typically overlook cases where scanners fail to provide usable security judgments. The authors evaluate three scanners—ModelScan, ModelAudit, and Fickling—using a benchmark of 170 synthetic artifacts, revealing that while ModelAudit achieved complete security decisions across all labeled families, ModelScan and Fickling demonstrated varying degrees of efficacy, with ModelScan excelling in precision conditional on making a judgment. The study emphasizes the importance of differentiating between the accuracy of judgments and their availability, advocating for more comprehensive evaluation methods in model security scanning.
