---
## 2026-11-19

### 1. Jailbreak Detection on Large Language Models via Contrastive Prototype Structures
**Authors:** Yan Qiu, Yuanyuan Li
**Link:** https://arxiv.org/abs/2611.24936v1
**Summary:** The paper addresses the challenge of detecting jailbreak attempts and harmful prompts in large language models by proposing a method called Jailbreak Detection with Prototype Inference (JDPI). This approach leverages contrastively learned representations and binary safety labels to create harmful and benign prototypes, allowing for effective detection without needing to train a separate classifier. Key results show that JDPI improves detection accuracy by 9.1-18.0 percentage points compared to traditional methods and demonstrates strong performance across multiple datasets, even outperforming existing baselines.

### 2. Knowing What You Know: A Trait Theory of Reviewer Value in Human-AI Cognitive Systems
**Authors:** Priyanka Sinha, Sugam Pandey
**Link:** https://arxiv.org/abs/2611.24932v1
**Summary:** The paper addresses the problem of determining which human reviewers add value when working alongside AI models in decision-making processes, focusing specifically on the concept of metacognitive calibration, or the alignment of a reviewer's confidence with the actual correctness of their judgments. The authors propose a trait theory of reviewer value based on extensive data from an AI-assisted accounting system, revealing that traditional measures of reviewer skill can misidentify overconfident novices as more capable than true experts. Notably, they find that individual calibration is crucial for identifying valuable reviewers, and that the effectiveness of both humans and AI can be optimized based on this calibration.

### 3. Mapping the AI Supply Chain: Dependencies, Vulnerabilities, and Market Concentration in the AI Ecosystem
**Authors:** Sarah H. Cen, Lindsey A. Gailmard, Joohan Kim, Rishi Bommasani, Daniel E. Ho, Percy Liang
**Link:** https://arxiv.org/abs/2611.24927v1
**Summary:** The paper addresses the lack of comprehensive documentation on the relationships and dependencies within the AI supply chain, which includes various organizations contributing to AI development. The authors present a pipeline for mapping this supply chain, resulting in a large-scale, multilayered dataset of actors and their interconnections in the AI ecosystem. The main contribution is this dataset, which provides critical insights into industry dynamics, including power concentration and vulnerabilities, and is publicly accessible for further exploration and analysis.

### 4. Agentic Harness Engineering Beta: Requirement-Centered Evolution of Agent Harnesses
**Authors:** Jiahang Lin, Jiahao Chen, Yiding Wang, Shichun Liu, Chengjun Pan, Shihan Dou, Honglin Guo, Yuyang Hu, Changhao Jiang, Zhenhua Han, Hang Yan, Qi Zhang, Tao Gui, Xuanjing Huang
**Link:** https://arxiv.org/abs/2611.24924v1
**Summary:** The paper addresses the issue of harness evolution in AI systems, which often neglects implicit user requirements, leading to suboptimal performance. The authors propose a new method called Agentic Harness Engineering Beta (AHE-Beta), which incorporates user feedback to drive the modification and selection of changes in harnesses in a more generalizable manner. AHE-Beta significantly improves the performance of AI agents while reducing the number of tokens used, demonstrating that focusing on user requirements creates better alignment between AI systems and real-world needs.

### 5. Decomposing SGD Dynamics in Neural Networks: Teacher-Induced Spikes and Variance Inflation
**Authors:** Samet Demir, Zafer Dogan
**Link:** https://arxiv.org/abs/2611.24908v1
**Summary:** This paper investigates how the training dynamics of two-layer neural networks using stochastic gradient descent (SGD) affect generalization, particularly through the impact of weights that are not aligned with the target model (teacher). The authors decompose the first-layer weights into components that align with the teacher and those that do not, revealing that SGD updates cause an increase in variance in the non-aligned weights, which negatively affects generalization. The key contribution is the introduction of a new framework, Decomposed Dynamics, that provides insights into how feature learning outside the target subspace can impair performance, ultimately demonstrating that freezing certain weight directions can lead to better generalization outcomes.

### 6. Equivariant Modeling with Polynomial Features via Minimal Homogeneous Generators
**Authors:** Michael Liaofan Liu, Joe Kileel
**Link:** https://arxiv.org/abs/2611.24896v1
**Summary:** This paper addresses the challenge of modeling equivariant functions in the context of finite dimensional group representations. The authors propose a novel framework that utilizes equivariant polynomial features, which are derived from minimal generators of invariant algebras, allowing for efficient learning of these functions. A key contribution is the development of a Python package that automates the computation of these features and demonstrates effective model training with fewer parameters, as evidenced by successful numerical experiments.

### 7. On Evaluating User Simulators for Interactive Agents
**Authors:** Hengguang Zhou, I-Hung Hsu, Li Chen, Priyanshi Shrivastava, Anastasios Angelopoulos, Wei-Lin Chiang, Ion Stoica, Cho-Jui Hsieh
**Link:** https://arxiv.org/abs/2611.24892v1
**Summary:** This paper addresses the challenge of accurately evaluating the quality of user simulators used for testing interactive agents, which often fail to reliably detect errors in simulated user behavior. The authors propose a new evaluation framework that assesses both the collective behavior of user simulations and the individual goals and constraints of users. Their findings reveal that existing evaluation methods overlook critical failures, whereas their new suite successfully identifies all types of induced user behavior errors, highlighting the importance of thorough fidelity assessment.

### 8. Cap-and-Track: Optimizing LLM Inference Request Dispatch Across Shifting Capacity
**Authors:** Benjamin Novotny, Doug Szeto, Chang Wang, Shicheng Chen, George Zhihua Yuan, Bob Kamma, Michael Ge, John Xin Zhou, Andrea Olgiati
**Link:** https://arxiv.org/abs/2611.24891v1
**Summary:** The paper addresses the challenge of optimizing inference request dispatch for large language models (LLMs) as server capacity and request sizes fluctuate, emphasizing the limitations of fixed dispatch rates. It introduces Cap-and-Track, an asynchronous inference system that adapts to changes in capacity by using refusal signals to adjust request handling without needing output-length predictions. Key results demonstrate that this approach can significantly reduce resource usage, serving requests more efficiently compared to traditional fixed-rate systems while maintaining high throughput.

### 9. Who are you? The Personal Imitation Game
**Authors:** Muhammad Rizky Wellyanto, Hajara-Yasmin Isa, Kexin Xue, Vishal Ravichandran, Wenpeng Lu, Jerry O. Talton, Ranjitha Kumar
**Link:** https://arxiv.org/abs/2611.24888v1
**Summary:** The authors introduce the Personal Imitation Game, a more difficult version of Turing's Imitation Game, where the challenge is for a machine to mimic a specific individual's conversational style rather than a generic human. They developed a system using a large language model trained on a decade's worth of personal communication data, demonstrating it could convincingly imitate one of the authors, as judged by participants. The results showed no significant difference in the ability of interrogators to distinguish between the author and the machine, highlighting important considerations for personal AI agents and privacy.

### 10. Ground, Iterate, Trace: Decomposing AI Research Ideation
**Authors:** Samson Yu, Qiran Zou, Jing Yu Lim, Rushi Shah, Anirudh Goyal, Dianbo Liu
**Link:** https://arxiv.org/abs/2611.24887v1
**Summary:** The paper addresses the challenge of generating effective research ideas using large language models by introducing the Creative AI Researcher (CAR), a framework that combines literature grounding, iterative development, and specific conceptual operators to enhance ideation. CAR constructs a semantic knowledge graph from relevant literature and employs operators to facilitate idea refinement while ensuring traceability of the ideation process. Key results show that CAR achieves higher methodological novelty in generated ideas compared to traditional prompting methods, though the advantage of using explicit operators over iterative approaches is not statistically significant.
