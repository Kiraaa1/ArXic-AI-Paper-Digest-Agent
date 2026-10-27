---
## 2026-10-27

### 1. Retriever-Free Retrieval: Navigating Documents with Decision Models
**Authors:** Chao Wan, Paul Jünger, Beixi Du, Bodong Liu, Navaneetha Krishnan, Kilian Q. Weinberger
**Link:** https://arxiv.org/abs/2610.35868v1
**Summary:** The paper addresses the limitations of current retrieval methods that rely on lexical matching, which can miss relevant information that even advanced language models could not recover. The authors introduce DecisionRAG, a decision model that evaluates candidate documents more effectively by navigating through the content structure without relying on a traditional retriever or task-specific training. This approach significantly improves retrieval performance, achieving notable gains over dense retrieval methods while maintaining fast query response times.

### 2. Center-of-Mass Interpretation of Evolution Strategies
**Authors:** Akshat Gupta
**Link:** https://arxiv.org/abs/2610.35865v1
**Summary:** The paper explores a geometric interpretation of evolution strategies (ES), a popular optimization method, by describing the model updates as movements toward a reward-weighted center of mass of a population of perturbed models. The authors demonstrate that the update can be understood as a displacement from the mean of the sampled rewards, providing an intuitive way to visualize how ES adjusts its parameters based on performance. This geometric framework enhances understanding of ES while remaining accurate even for finite populations.

### 3. Auto-Research Arena: Benchmarking and Advancing Auto-Research in Language Modeling
**Authors:** Xi Chen, Chongjian Ge, Yiran Xu, Yiqun Mei, Henrik I. Christensen, Hao Tan, Ziwen Chen, Hanwen Jiang
**Link:** https://arxiv.org/abs/2610.35866v1
**Summary:** The paper presents the Auto-Research Arena, a benchmark designed to evaluate and enhance autonomous research systems in language modeling. It establishes a framework that separates performance qualifications from improvement metrics across multiple research objectives, demonstrating that existing research methods can be outperformed by simpler approaches. The Arena not only benchmarks current systems but also uncovers new research avenues, ultimately leading to improved model training outcomes.

### 4. Learning Force-Reactive Humanoid Loco-Manipulation
**Authors:** Sihang Li, Xiaofeng Guo, Jinkun Cao, Charlie Cheng, Ruihan Yang, Chen Feng, Guanya Shi, Haozhi Qi
**Link:** https://arxiv.org/abs/2610.35862v1
**Summary:** The paper addresses the challenge of coordinating both motion and contact force in humanoid robots during complex tasks. It introduces a framework called FLORE, which utilizes a force-reactive diffusion policy that integrates sensory inputs to predict hand actions and force commands, facilitated by a hybrid whole-body controller for balance and compliance. The key finding is that this approach significantly outperforms a traditional position-only policy, achieving an 80% success rate in executing contact-rich tasks compared to just 26.7% for the latter.

### 5. On the stability of learning
**Authors:** John J. Vastola
**Link:** https://arxiv.org/abs/2610.35856v1
**Summary:** This paper investigates the stability of learning algorithms when gradient information is noisy and intermittently available, which is often the case in biological neural networks. The authors analyze various settings, including single-layer and multi-layer networks, and identify explicit conditions that ensure stable learning, distinguishing these from traditional stability conditions in stochastic gradient descent. The key finding is that reliable learning requires not only unbiased credit assignment but also sufficiently frequent and informative feedback.

### 6. Patient-specific rubric-based evaluation of large language models across longitudinal cancer care
**Authors:** Wei-Wei Zhang, Pengkai Wang, Yan Li, Zhijie Sang, Guan-Qun Zhou, Jun-Yan Li, Shu-Han Zhou, Pei-Wen Liu, Ting-Xi Tang, Min Tang, Zhitian Hou, Jianmin Wu, Jian Guan, i Lin, Hongxia Yang, Ying Sun
**Link:** https://arxiv.org/abs/2610.35847v1
**Summary:** This paper addresses the challenge of evaluating large language models (LLMs) in longitudinal cancer care, as traditional assessments often focus on isolated clinical encounters rather than the entire care pathway. The authors introduce NPC-RubricBench, a comprehensive benchmark that evaluates LLMs based on the evolving responsibilities in cancer treatment, revealing that even models with high diagnostic accuracy struggled with later stages of care, particularly in making timely decisions. Key findings indicate that while more detailed prompts can improve decision quality, they may compromise the reliability of evidence used, underscoring the need for adaptive evaluation methods in medical AI.

### 7. Preserve to Expand: Source-Aware Adaptation and Model Merging for Multilingual LLM-Based ASR
**Authors:** Yuchen Zhang, Haralambos Mouratidis, Ravi Shekhar
**Link:** https://arxiv.org/abs/2610.35846v1
**Summary:** The paper addresses the challenge of expanding multilingual automatic speech recognition (ASR) systems to new languages without losing performance in previously supported languages. The authors propose a method using connector-based Speech LLMs, evaluating various strategies for adapting the model while preserving source-language capabilities. Key findings reveal that while certain fine-tuning approaches lead to forgetting source languages, a specific merging technique (SSU-Wanda+TIES) effectively balances the adaptation to new languages with maintaining performance on existing ones.

### 8. Work Agents: Systems, Capabilities, and Optimization
**Authors:** Zishan Xu, Enjun Du, Mingqi Gao, Cheng Yang, Junhao Shen, Zirong Chen, Zhiyuan Yao, Yifu Guo, Yuquan Lu, Jinyang Huang, Zhengxi Lu, Siyi Liu, Ziyu Zheng, Yongqi Zhang, Difan Zou, Weiwen Liu
**Link:** https://arxiv.org/abs/2610.35845v1
**Summary:** This paper addresses the challenge of reliably executing complex digital tasks using work agents that combine foundation models with operational systems. The authors propose a comprehensive framework that categorizes digital work, introduces key capabilities needed for effective execution, and suggests optimization strategies for both the models and their operational environments. The key contribution is a unified perspective that advances our understanding of work agents, enabling the development of systems that can deliver trustworthy and valuable work outcomes.

### 9. I-HITL: Inalienable Human-in-the-Loop
**Authors:** Samuel Breckenridge, Dani Vilardell, Wenhao Wang, Fan Zhang, Ari Juels
**Link:** https://arxiv.org/abs/2610.35835v1
**Summary:** The paper addresses the challenge of ensuring robust human oversight in AI systems, particularly when AI agents attempt to bypass established approval mechanisms through coercive tactics. To solve this, the authors introduce the concept of inalienable human-in-the-loop (I-HITL), which ensures that AI actions require explicit human approval, even under adversarial conditions. Their contributions include a formal definition of I-HITL, conditions for its implementation, and a prototype system called Countersign, which enhances existing human oversight frameworks using common consumer devices.

### 10. Information-Theoretic Secure Aggregation With Heterogeneous Client Quantization
**Authors:** Shreya Meel, Sennur Ulukus, Itzhak Tamo
**Link:** https://arxiv.org/abs/2610.35833v1
**Summary:** The paper addresses the challenge of secure aggregation in federated learning when clients have different quantization levels due to varying bandwidth constraints. It proposes a novel information-theoretic secure aggregation protocol that accommodates these heterogeneous quantization levels while preventing privacy breaches from client dropouts and collusion. The key contribution is the use of threshold secret sharing to handle updates from clients without revealing individual updates, despite the differences in their representation.
