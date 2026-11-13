---
## 2026-11-13

### 1. Unbundling Multimodal Vision Encoding
**Authors:** Ellis Brown, Chris Hoang, Shengyi Qian, Shang-Wen Li, Mike Lewis, Marjan Ghazvininejad, Luke Zettlemoyer, Lucas Beyer, Mengye Ren, Jakob Verbeek, Saining Xie, Hu Xu
**Link:** https://arxiv.org/abs/2611.17334v1
**Summary:** The paper addresses the ongoing debate about how multimodal language models should integrate visual input, particularly whether to use pretrained vision encoders or train them from scratch. The authors conducted experiments using a controlled framework to compare various encoding strategies, ultimately finding that the key factor for effective visual understanding is dedicated vision capacity rather than a pretrained visual prior. They concluded that joint training of the visual encoder with the language model leads to comparable performance as using a separate pretrained encoder, especially when the vision capacity is strategically placed within the model architecture.

### 2. ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research
**Authors:** Jie Wang, Tong Zhu, JiaHao Kuang, Zhe Xu, Yunkai Chai, Dehong Zheng, Yu Cheng, Tao Ji, ZhouHan Lin, Qi Zhang, Bowen Zhou
**Link:** https://arxiv.org/abs/2611.17332v1
**Summary:** ArchSpace addresses the lack of documentation and review in LLM architecture research, which often leads to missed insights in both industry and academia. The platform allows researchers to record their architectural proposals along with experimental results, review them via community input, and reference them in future work. By leveraging scaling laws to predict model performance from smaller experiments, ArchSpace aims to facilitate the development of a wider array of architectural innovations for next-generation models.

### 3. Internalizing Investment Mandates: A Neurosymbolic RL Approach to Portfolio Allocation
**Authors:** Zeynep Yıldız, Satchit Chatterji, Ercan Atam, Erman Acar
**Link:** https://arxiv.org/abs/2611.17329v1
**Summary:** This paper addresses the challenge of enforcing investment policy constraints in portfolio allocation using deep reinforcement learning (RL). The authors introduce a neurosymbolic approach that integrates symbolic rules directly into the learning process, enabling the RL agent to learn compliance without needing post-hoc corrections. Their method significantly reduces violations of investment rules from as high as 98% to just 4.8%, demonstrating its effectiveness in real-world applications.

### 4. AgentSSL: Can MLE Agents Leverage Unlabeled Data?
**Authors:** Ethan Lin, Akanksha Sarkar, Ziang Liu, Kristin Branson, Jennifer J. Sun
**Link:** https://arxiv.org/abs/2611.17323v1
**Summary:** The paper addresses the challenge of leveraging abundant unlabeled data for machine learning by introducing Agentic Semi-Supervised Learning (AgentSSL), which frames the problem as a search for optimal programs. The researchers found that agents can effectively synthesize code that integrates existing semi-supervised learning techniques, achieving better performance than traditional human-engineered methods in many scenarios. However, they also identified program selection as a significant hurdle, leading to a dedicated benchmark to evaluate and improve this aspect.

### 5. Learning When Diffusion Language Models Should Regenerate
**Authors:** Minhae Oh, Jeonghye Kim, Jinwoo Koo, Yeongoon Kim, Jimin Seo, Minsik Seol, Jungwoo Lee
**Link:** https://arxiv.org/abs/2611.17320v1
**Summary:** This paper addresses the challenge of improving the accuracy of diffusion language models when generating text by identifying when errors occur and how to correct them. The authors introduce DiVR, a verifier that assesses the likelihood of a generated sequence being correct, enabling it to decide which parts should be regenerated. The results show that DiVR significantly boosts accuracy on reasoning tasks while being more cost-effective than traditional search methods.

### 6. CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation
**Authors:** Peiwen Li, Harshit Verma, Sophia Zhou, Haiwen Wang, Ngoc Bui, Heng Chang, Fei Fei, David van Dijk, Rex Ying
**Link:** https://arxiv.org/abs/2611.17316v1
**Summary:** The paper addresses the challenge of efficiently managing memory in coding agents that work on successive tasks while minimizing costs associated with reading and writing this memory. The authors introduce CoReMem, a framework that evaluates the future usefulness of memory segments to optimize memory design and actor decision-making. Key results show that CoReMem significantly improves the performance of a 27B actor model on the ChainSWE task, increasing its success rate while reducing effort and resource consumption.

### 7. Linking Rapid Learning to Compositional Structure in Neural Networks: Evidence from Additive Analogies in Meta-Learned Parameter Spaces
**Authors:** Abigail L. Tenenbaum, R. Thomas McCoy
**Link:** https://arxiv.org/abs/2611.17314v1
**Summary:** This paper explores how certain neural networks can learn new tasks quickly by examining their internal structure after being optimized through meta-learning. The authors draw parallels to additive relationships in word embeddings, showing that the parameters of a meta-learned network can be combined to create new representations for functions, allowing the network to effectively implement these functions without additional training. The key finding is that meta-learning organizes a network's learning trajectories in a way that supports rapid learning of related tasks.

### 8. Sketching Language Models for Context Attribution
**Authors:** Christopher Liaw, Aranyak Mehta, Grigoris Velegkas, Felix Zhou
**Link:** https://arxiv.org/abs/2611.17313v1
**Summary:** The paper addresses the problem of context attribution in language models, specifically how removing parts of a prompt affects the model's output. The authors propose a novel algorithm that estimates the leave-one-out attribution values using significantly fewer model evaluations compared to direct computation, achieving a bound of \(O(\sqrt{\log(1/\varepsilon)}/\varepsilon)\) evaluations while maintaining accuracy. Key contributions include demonstrating stability in the estimates and deriving a lower bound that matches their upper bound, based on advanced techniques in sketching and matrix query estimation.

### 9. Classical Energies Learn to Reason 1,000x Faster than Looped Models
**Authors:** Benjamin Hoover, Hugh Blayney, James C. R. Whittington
**Link:** https://arxiv.org/abs/2611.17309v1
**Summary:** The paper addresses the inefficiencies of looped models in solving reasoning tasks by introducing a learned energy-based model called CRAM, which is inspired by Hopfield & Tank's work from the 1980s. CRAM demonstrates significantly faster training times and lower computational demands, achieving near-complete accuracy on puzzles like Sudoku and Maze while being over 1,000 times quicker than traditional looped models. This study highlights the potential of energy-based approaches for reasoning tasks while cautioning against relying on simple benchmarks for assessing the scalability of reasoning techniques.

### 10. Quantifying structural stability of transparent models for general insurance pricing
**Authors:** Félix Côté, Marie-Pier Côté
**Link:** https://arxiv.org/abs/2611.17308v1
**Summary:** This paper addresses the challenge of maintaining structural stability in insurance pricing models, which often undergo significant changes when updated due to the short duration of general insurance contracts. The authors introduce a novel metric called the Mean Squared Shape function distance to evaluate the stability of functionally transparent models, allowing for better understanding and comparison of model changes. Their findings reveal that generalised linear models and explainable boosting machines balance stability and accuracy effectively, and that certain strategies can enhance stability without sacrificing performance.
