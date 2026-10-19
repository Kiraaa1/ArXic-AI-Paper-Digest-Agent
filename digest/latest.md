---
## 2026-10-19

### 1. Rethinking the design space of Vanilla Pixel Diffusion Transformers
**Authors:** Soumik Mukhopadhyay, Long Mai, Abhinav Shrivastava, Aniruddha Mahapatra
**Link:** https://arxiv.org/abs/2610.23854v1
**Summary:** The paper addresses the limitations of vanilla pixel-space diffusion models in generating high-quality images by exploring different prediction approaches. The authors introduce MFlow, a new adaptive parameterization method that learns to interpolate between two prediction strategies—image prediction and velocity prediction—depending on the data and model capacity. The key finding is that MFlow enhances generative performance across various datasets, and they also propose ConvRefiner, a lightweight module that improves the quality of generated images by restoring high-frequency details while maintaining model efficiency.

### 2. Behavioral Couplings: From Formation to Behavioral Emergence in Language Models
**Authors:** Dongyoon Hahm, Woogyeol Jin, Dennis Wei, Yi Zhou, Nathalie Baracaldo, Kimin Lee
**Link:** https://arxiv.org/abs/2610.23847v1
**Summary:** This paper addresses the issue of unintended behaviors that can emerge in large language models (LLMs) after fine-tuning, a phenomenon known as behavioral coupling. The authors investigate how training on documents containing multiple behaviors can lead to the emergence of unexpected behaviors when the model is subsequently fine-tuned to exhibit just one of those behaviors. They find that these couplings can compose, making it challenging to trace the origins of misbehavior, thereby highlighting the need for more comprehensive evaluation methods beyond observing a model's current outputs.

### 3. AI-Driven Reproducibility and Analytical Robustness in Scientific Discovery
**Authors:** Shicheng Liu, Krista Opsahl-Ong, Andrew Drozdov, Julian Killingback, Arnav Singhvi, Ronak Pradeep, Michael Bendersky, James C. Dickerson, Monica S. Lam
**Link:** https://arxiv.org/abs/2610.23845v1
**Summary:** The paper addresses the challenge of ensuring reproducibility and analytical robustness in scientific research, which often requires significant manual effort. The authors developed SEER-Repro, a benchmark based on a cancer registry, and created an AI agent that successfully reproduces research claims while also testing their robustness through an analysis pipeline. Key results indicate that this approach allows for a high reproduction rate of claims and identifies critical analytical choices that may influence conclusions, facilitating more efficient scientific review.

### 4. DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses
**Authors:** Jianyuan Zhong, Chenwei Wu, Zhaochen Yu, Xixian Jiang, Xuewei Li, Hao Xiao, Xilin Dai, Junyang Wang, Jiaru Zou, Zhiqing Cui, Boyuan Zheng, Jing Xiong, Zhen Zhang, Qiang Gao, Michael Morley, Luis Nakayama, Qiang Xu, Liyue Shen, Tao Gui, Leo Anthony Celi, James Zou, Zhenfei Yin, Yingcheng Wu, Ling Yang
**Link:** https://arxiv.org/abs/2610.23839v1
**Summary:** The paper addresses the challenge of developing valuable research hypotheses that can lead to successful scientific investigations. The authors propose the DiscoveryRSI framework, which employs a multi-agent evolutionary search method to create and improve hypothesis trees while learning from past research processes. The key contribution is the demonstrated improvement in hypothesis quality, with a significant increase in evaluative metrics after self-improvement rounds, surpassing other existing models in both expert assessments and alignment with newly published research.

### 5. Task-aligned spectral inductive biases in parameterized quantum circuits
**Authors:** Felix Frohnert, Adrián Pérez-Salinas, Sebastian Lange, Marcus Schwaebisch, Evert van Nieuwenburg, Vedran Dunjko
**Link:** https://arxiv.org/abs/2610.23834v1
**Summary:** This paper addresses the challenge of designing parameterized quantum circuits that effectively align with specific tasks in quantum machine learning. The authors introduce a method using data reuploading quantum circuits that incorporate a fixed, task-specific spectral query to probe variable input signals. Their findings demonstrate that incorporating such queries enhances learning performance in classification tasks, especially when data is limited, compared to circuits without aligned queries.

### 6. Beyond the Answer: Student-Conditioned Trace Construction for Reasoning Distillation
**Authors:** Shaoang Li, Yanhang Shi, Yufei Li, Mingfu Liang, Frank Shyu, Sandeep Pandey, Luke Simon, Xi Liu, Jian Li
**Link:** https://arxiv.org/abs/2610.23831v1
**Summary:** The paper addresses the issue of ineffective learning when students receive only answer supervision without accompanying reasoning traces. It proposes ReDiST, a framework that constructs more effective reasoning traces by revising student drafts based on evidence and providing tailored guidance. The key finding is that ReDiST significantly enhances both direct and transfer learning performance compared to traditional methods that rely solely on provided answers or original traces.

### 7. Waiting Buys Exactly Two Moments: Endogenous Identification in Prediction-Driven Allocation
**Authors:** Rama AlHamidi, Rasul Khanbayov, Erchin Serpedin, Hasan Kurban
**Link:** https://arxiv.org/abs/2610.23830v1
**Summary:** The paper addresses the challenge of how to allocate preventive help effectively over time, considering the trade-off between revealing risk through observation and potentially losing intervention opportunities as higher-risk individuals leave. The authors develop a model that shows how waiting for additional signals can provide two new moments of information regarding latent risks for every extra observation period, though this does not always improve allocation welfare. Their findings indicate that while longer observation can reduce timing ambiguities, the optimal intervention time might have already occurred, and certain strategies enhance decision-making without guaranteeing better outcomes.

### 8. Quality-of-Transmission Estimation in Quantum Networks: Compute, Simulate, or Learn?
**Authors:** Anis Bekri, Amar Abane, Van Sy Mai, Abdella Battou, Saddek Bensalem
**Link:** https://arxiv.org/abs/2610.23827v1
**Summary:** This paper addresses the challenge of accurately estimating the quality of entanglement in quantum networks, which is crucial for making control-plane decisions like routing and scheduling. The authors propose a framework that evaluates three methods for this estimation—computing analytically, simulating, or using learned models—and find that while analytical methods can work in simpler scenarios, simulations are necessary in more complex situations influenced by stochastic factors. The key contribution is the demonstration that learned surrogates can effectively approximate simulation results at a fraction of the computational cost, paving the way for more efficient online control in quantum networks.

### 9. Self-Building Labs
**Authors:** Jiaru Bai, Yuchi Zhao, Han Hao, Miroslav Bogdanovic, Yang Cao, Varinia Bernales, Alán Aspuru-Guzik
**Link:** https://arxiv.org/abs/2610.23826v1
**Summary:** The paper addresses the challenge of flexibility in self-driving laboratories, which often require extensive manual engineering to adapt to new experiments. The authors introduce a self-building laboratory (SBL) that autonomously designs and configures its own experimental setup based on high-level scientific goals, using its existing resources. Their work demonstrates SBL's capability to perform complex experiments, such as quantum-dot synthesis, significantly simplifying the automation process and allowing researchers to focus on specifying objectives rather than technical details.

### 10. ENFR: Evidence Networks with Flow-Matched References for Amortized Simulation-Based Model Inference
**Authors:** Kai Lehman, Jameson Dong, Carolina Cuesta-Lazaro, Niall Jeffrey, Benjamin D. Wandelt, Francisco Villaescusa-Navarro, Sven Krippendorf, Jochen Weller
**Link:** https://arxiv.org/abs/2610.23825v1
**Summary:** The paper addresses the challenging problem of accurately computing the evidence of data-generating models in Bayesian inference, which is crucial for model assessment and parameter inference. The authors introduce a novel approach called ENFR (Evidence Networks with Flow-Matched References), which learns Bayes factors to recover absolute evidence efficiently. Their results show that ENFR outperforms existing methods in evidence estimation across various scientific applications, providing a robust tool for evaluating model fidelity.
