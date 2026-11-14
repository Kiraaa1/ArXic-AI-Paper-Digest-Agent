---
## 2026-11-14

### 1. Towards a Theory of Learnability via Debate
**Authors:** Tosca Lechner, Vinayak Pathak, Sivan Sabato, Ruth Urner
**Link:** https://arxiv.org/abs/2611.17303v1
**Summary:** The paper addresses the challenges of using debate as a training method for AI models, focusing on the implicit learning problem it presents. The authors reformulate this problem as an online learning challenge and introduce a cooperative debate protocol that optimizes learning outcomes. A key finding is that even minor errors from human judges can significantly impair the learning effectiveness of the models.

### 2. FLEX-LBP: Learning Local Binary Patterns with Exact Binary Inference for Texture Classification
**Authors:** Mohamed Alimoussa, Amal El Kaid
**Link:** https://arxiv.org/abs/2611.17302v1
**Summary:** The paper introduces FLEX-LBP, a new method that enhances Local Binary Patterns (LBP) by automatically learning key parameters such as radius and color transforms through backpropagation, rather than setting them manually. The approach retains the efficiency of traditional LBP while significantly improving texture classification accuracy across various datasets. Notably, FLEX-LBP outperforms several classical descriptors and achieves a remarkable accuracy of 93.8% on the Kather colorectal cancer benchmark, surpassing the best existing methods.

### 3. Consistent Video-to-Video Translation via Explicit Correspondences
**Authors:** Gaurav Parmar, Zhengqi Li, Richard Zhang, Jun-Yan Zhu, Srinivasa Narasimhan, Eli Shechtman, Yotam Nitzan
**Link:** https://arxiv.org/abs/2611.17298v1
**Summary:** The paper addresses the challenge of achieving long-range temporal consistency in interactive video-to-video translation while maintaining fast real-time generation. The authors introduce a new method called vid2vid-long, which utilizes explicit correspondences between input and output video patches, allowing the model to reference relevant past frames outside a fixed-length context window. Their approach significantly enhances long-range consistency without compromising generation quality or speed compared to existing models.

### 4. Goal Encoding in LLMs
**Authors:** Arnab Sen Sharma, Eric Todd, Sheridan Feucht, Andy Arditi, Rohit Gandikota, Natalie Shapira, Gabriele Sarti, Constanza Fierro, Lisa Schut, David Bau
**Link:** https://arxiv.org/abs/2611.17297v1
**Summary:** The paper investigates how large language models (LLMs) encode and pursue goals during task completion. By analyzing the models' attention mechanisms in a coding context, the researchers identified specific attention heads that represent and sustain goal-related information, allowing the LLM to adapt its actions even in different programming environments. A novel non-recurrent goal-seeking (NRGS) model is proposed, suggesting that LLMs continually re-evaluate their goals in light of their current progress, ensuring effective task execution without a traditional recurrent mechanism.

### 5. Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon
**Authors:** Haozhe Wang, Lina Chen, Fanqi Wan, Qi Han, Yinmin Zhang, Zheng Ge, Daxin Jiang, Junchi Yan
**Link:** https://arxiv.org/abs/2611.17294v1
**Summary:** The paper introduces Metal Sandbox, a system designed to optimize the execution of GPU programming tasks on Apple Silicon by efficiently scheduling commands and managing isolated execution environments for multiple coding agents. It allows for parallel and serial command execution across interconnected Macs, significantly improving command throughput and reducing waiting times. The key findings demonstrate that this approach can achieve up to 2.05 times the command throughput and an 18.8% reduction in waiting times for tool execution.

### 6. Negative-Only Policy Optimization for One-Sided Verifiable Rewards
**Authors:** Jiacheng Xu, Shuo He, Fuxiang Zhang, Chaojie Wang, Bo An
**Link:** https://arxiv.org/abs/2611.17287v1
**Summary:** The paper addresses the challenge of reinforcement learning (RL) in scenarios where reliable verification of successes is not possible, leading to potential false positives in positive feedback. The authors propose a novel method called Negative-Only Policy Optimization (NOPO), which focuses on using only verified negatives to optimize the learning policy while treating verified positives as ambiguous. The key contribution is that NOPO significantly improves performance on various benchmarks, demonstrating its effectiveness in optimizing RL in environments with one-sided verifiability.

### 7. Synthesis Smuggling: Maliciously Hiding Inferred Personal Attributes in LLM Outputs
**Authors:** Gautam Galada, Supreeth Shastri, Sagnik Ray Choudhury
**Link:** https://arxiv.org/abs/2611.17280v1
**Summary:** The paper introduces a threat model called "Synthesis Smuggling," which reveals how a malicious language model can extract sensitive personal information (like gender and age) from user interactions and secretly embed it in seemingly harmless generated content. By training models to make these inferences and encode them using hidden characters or specific word choices, the research demonstrates that such outputs can unintentionally serve as covert channels for transmitting private data, even when users share the content innocently.

### 8. LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds
**Authors:** Pengcheng Zhou, Xuanyu Liu, Yanchen Yin, Tianjie Ju, Bobo Li, Shengqiong Wu, Hao Fei, Mong-Li Lee, Wynne Hsu
**Link:** https://arxiv.org/abs/2611.17267v1
**Summary:** The paper presents GeoWorld, a dynamic geographic environment designed to test the decision-making abilities of large language models (LLMs) in settings that continuously change over time. The benchmark, LiveGeo, evaluates how well these agents can gather relevant information and adapt their plans as the environment evolves. The findings indicate that current leading LLMs struggle with both static and dynamic tasks, revealing significant challenges in maintaining accurate decision-making as conditions change.

### 9. Programming Quantum Circuit Parameters with Large Language Models
**Authors:** Tiago de Souza Farias, Caio Moraes Porto, Matheus da Silva Fonseca, Nicolas Armando Cabrera Carpi, Anderson de Araujo Oliveira, Celso Jorge Villas-Boas
**Link:** https://arxiv.org/abs/2611.17246v1
**Summary:** This paper explores how large language models (LLMs) can generate parameters for quantum circuits without traditional optimization methods, investigating their effectiveness across various Hamiltonian types. The findings indicate that while LLMs struggle with general Hamiltonians and show limited improvement with feedback, they perform better for structured Hamiltonians, producing low-energy configurations. Additionally, the study highlights limitations in the LLM's ability to provide physically accurate energy values, underscoring the significance of problem structure and verifiability in generating quantum circuit parameters.

### 10. Ballad: Bandit-Based LLM Routing for Automated Heuristic Discovery
**Authors:** Samidha Verma, Ankit Anand, Sayan Ranu
**Link:** https://arxiv.org/abs/2611.17241v1
**Summary:** The paper presents Ballad, an innovative method for selecting and combining various Large Language Models (LLMs) to enhance automated heuristic discovery (AHD) for NP-hard combinatorial optimization problems. Instead of relying solely on more powerful and expensive models, Ballad employs an online bandit algorithm to dynamically choose models based on their performance, ultimately creating an ensemble that often outperforms individual models while significantly reducing costs. The key finding is that this approach can improve heuristic quality and efficiency while achieving cost savings of up to 65.6% compared to using the most powerful model alone.
