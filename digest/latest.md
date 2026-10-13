---
## 2026-10-13

### 1. Revisiting Tabular Deep Regression: Objectives and the Limits of Global Early Stopping
**Authors:** Danil Rudenko, Georgii Bulgakov, Nikolay Kartashev, Ivan Rubachev, Daniil Krasylnikov, Artem Babenko
**Link:** https://arxiv.org/abs/2610.13909v1
**Summary:** This paper investigates the effectiveness of various objective functions for deep learning regression tasks on tabular data, with a specific focus on comparing them to the traditional Mean Squared Error (MSE). The authors find that while quantile loss consistently outperforms MSE, the challenge of varying optimal training epochs for different noise levels leads to limitations in using a single global early-stopping approach. To address this, they propose a novel heteroskedasticity-aware extension of quantile loss, which shows improved performance across multiple neural network architectures.

### 2. Hitting-Time Bounds for Asynchronous Q-Learning
**Authors:** Yang Peng
**Link:** https://arxiv.org/abs/2610.13901v1
**Summary:** This paper investigates the performance of asynchronous Q-learning using a single trajectory from a fixed behavior policy in finite Markov decision processes. The authors establish that zero-initialized Q-learning can achieve a bounded error with high probability if a constant step size is applied, showing a dependency on the effective horizon and the hitting time of the state-action chain. Their approach also includes a method for dynamically selecting a step size, allowing for effective training without needing prior model knowledge.

### 3. Structural Automata for Neural Semantic Parsing
**Authors:** Xiao Zhang
**Link:** https://arxiv.org/abs/2610.13896v1
**Summary:** The paper addresses the challenge of generating well-formed semantic representations in neural semantic parsing, which can suffer from incomplete or invalid outputs due to token dependencies. The authors propose a method called accepting-path decoding (APD) that ensures valid completions within specified output lengths while maintaining the model's preferred token choices. Their results show that APD significantly improves parsing accuracy, outperforming local masking methods and achieving comparable results to approaches that allow token retraction under length constraints.

### 4. Task Context Shapes Component Roles in Language Models
**Authors:** Sovesh Mohapatra, Dani S Bassett
**Link:** https://arxiv.org/abs/2610.13895v1
**Summary:** This paper investigates how large language models utilize the same attention heads for different tasks and how task context influences their roles. By analyzing the interaction of model components through graph-based representations, the authors demonstrate that task changes can significantly redistribute the influence and output of these shared components. The key finding is that modifying early activations can shift which information the model focuses on, revealing a structured mechanism that allows models to adapt their behavior while using shared parameters.

### 5. RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics
**Authors:** Weiliang Chen, Song Liao
**Link:** https://arxiv.org/abs/2610.13889v1
**Summary:** The paper presents RATED, a new framework for reliably retrieving AI tools by considering their availability during execution, rather than just their semantic relevance. By combining a fine-tuned dual-encoder for semantic matching with a dynamic feedback mechanism that adapts to runtime execution conditions, RATED significantly reduces the rate of selecting faulty tools. The main finding shows a 52.2% improvement in retrieval performance and a drastic decrease in fault selection during API outages, while maintaining minimal processing latency.

### 6. X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems
**Authors:** Yeonsung Jung, Zhiyuan Wang, Zifan Wang, Vítor Albiero, Benjamin Newman, Edoardo Debenedetti, Ivan Evtimov, Ninareh Mehrabi
**Link:** https://arxiv.org/abs/2610.13886v1
**Summary:** The paper addresses the issue of personal agents causing unintended harmful outcomes when interacting with web services due to compositional failures. It introduces X-AgentRed, a self-evolving framework that explores and refines harmful tool-call paths by analyzing dependencies among tools and using execution feedback to improve its exploration. The key finding shows that X-AgentRed significantly outperforms existing methods, achieving a higher rate of harmful path discovery and greater tool diversity.

### 7. Prediction Is Not a Sufficient Memory State
**Authors:** Robert Jenkinson Alvarez
**Link:** https://arxiv.org/abs/2610.13881v1
**Summary:** The paper examines the limitations of memory states in learning systems, specifically highlighting that simply reproducing predictions does not ensure the ability to learn from new data. It characterizes conditions under which a fixed-dimensional memory state can facilitate cumulative learning, revealing that polynomial loss functions require a specific number of memory coordinates to maintain learning. The key contribution is a deeper understanding of the interplay between memory states and learning mechanisms, rather than proposing a new learning algorithm.

### 8. Partially Informed Stochastic Optimization via Zeroth-Order Residual Tracking
**Authors:** El Mahdi Chayti, Alireza Mirrokni, Martin Jaggi
**Link:** https://arxiv.org/abs/2610.13871v1
**Summary:** The paper addresses the challenge of optimizing functions when only partial gradient information is available, such as in scenarios involving performative prediction and bilevel optimization. The authors propose a method called Partially Informed Stochastic Optimization (PISO), which combines known gradient components with a running estimate of the unknown parts to reduce variance during optimization. Key results show that PISO achieves leading efficiency in function evaluations while providing convergence guarantees, outperforming existing methods in various applications.

### 9. Finite-Sample Guarantees for Fully Discrete Conditional Diffusion Models
**Authors:** Qiuyun Zhu
**Link:** https://arxiv.org/abs/2610.13851v1
**Summary:** This paper addresses the challenge of ensuring that conditional diffusion models, which are learned from data using a finite number of denoising steps, maintain accuracy in their output distributions. The authors propose a method that connects the training objectives with the sampling process, allowing them to analyze both statistical and numerical errors simultaneously. They derive high-probability bounds for errors in the generated distributions, demonstrating that with appropriately chosen grids, the models can achieve good performance in terms of Kullback-Leibler divergence and total-variation error as the sample size increases.

### 10. Inference-Time Steering Across Scaffolds and Epitopes for Sample-Efficient De Novo Nanobody Design
**Authors:** Mason Minot, Simon Friedensohn, Cédric R. Weber
**Link:** https://arxiv.org/abs/2610.13844v1
**Summary:** The paper addresses the inefficiency in de novo nanobody design, where traditional methods over-generate candidates and filter them afterward. The authors introduce a novel approach that dynamically allocates computation resources during the design process, employing techniques like Global Sequential Monte Carlo and Batched Successive Elimination. Their method improves the efficiency of generating viable nanobody candidates by nearly five times without compromising the diversity of the designs.
