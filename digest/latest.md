---
## 2026-08-03

### 1. TokTier: Exact Stateful Tokenization for Agentic LLM Serving
**Authors:** Zhenyu Zhang, Zhichao Cao
**Link:** https://arxiv.org/abs/2607.29678v1
**Summary:** The paper presents TokTier, a stateful tokenization service designed to improve the efficiency of large language model (LLM) serving systems by minimizing re-tokenization when appending text. By using a specialized method that allows for tokenization of only the new additions while maintaining consistency with standard tokenization, TokTier dramatically speeds up processing times. Key results show it can reduce time to first token by 16-34% and achieve up to 1,821 requests per second, vastly outperforming current tokenization methods.

### 2. ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction
**Authors:** Boyang Zhang, Adrian Lyjak, Eli Stewart, Zhaoqi Li, Simon Suo
**Link:** https://arxiv.org/abs/2607.29677v1
**Summary:** ExtractBench addresses the challenge of schema-guided document extraction in enterprise workflows, where agents need to accurately extract information based on user-defined schemas. The authors created a comprehensive benchmark that evaluates extraction performance across multiple metrics, including accuracy and grounding, using a curated dataset of 4,869 pages from various document types. Their key finding is that while commercial visual language models (VLMs) excel with short documents, the LlamaExtract Agentic Plus outperforms others in terms of accuracy and cost efficiency on longer documents.

### 3. Differentially Private Nonparametric Modal Learning with Applications to Regression and Clustering
**Authors:** Arkajyoti Bhattacharjee, Arnab Auddy
**Link:** https://arxiv.org/abs/2607.29675v1
**Summary:** The paper addresses the challenge of estimating density modes of multimodal distributions while ensuring strong differential privacy. The authors introduce DP-GRAMS, a method that combines a noisy mean-shift algorithm with privacy-preserving techniques, enabling reliable mode recovery under certain smoothness conditions. Key contributions include theoretical guarantees for high-probability mode recovery and asymptotic error rates, along with practical extensions for private regression and clustering, supported by experimental results that demonstrate an effective balance between privacy and utility.

### 4. Sign compression for Muon: SignMuon, MuonSign, and the Limits of Error Feedback
**Authors:** Maria Smirnova, Alexey Kravatskiy
**Link:** https://arxiv.org/abs/2607.29674v1
**Summary:** The paper addresses the challenge of efficiently compressing gradient updates in optimization algorithms using a method called SignMuon, which reduces updates to a single bit per parameter by utilizing the sign of each gradient element. Despite its theoretical limitations—it can ascend on linear functions and struggles with error feedback—experiments reveal that a simpler heuristic of applying the sign after the optimization step yields better practical performance across various tasks like CIFAR-10 and nanoGPT. This suggests that the practical effectiveness of compression techniques can sometimes outweigh their theoretical guarantees in real-world applications.

### 5. Freeze, Then Select: Structured Field Adapters and Stability-Validated Weak Selection for PDE Discovery from Sparse Observations
**Authors:** Juncheng Zhong, Chenghuang Shen, Jianfeng Liu, Zhengdong Xiao, Longjiu Luo, Qianrong Wang, Wenjun Xu, Wenlian Lu
**Link:** https://arxiv.org/abs/2607.29665v1
**Summary:** The paper addresses the challenge of discovering partial differential equations (PDEs) from sparse observational data, where it can be difficult to identify the correct equation structure. The authors propose a "freeze-then-select" method that first extracts spatial features and temporal coefficients before identifying the relevant terms in the equations using a stability-validated selection process. This approach outperforms classical and neural methods in accurately recovering the true equation structures, particularly excelling in complex scenarios like Kuramoto-Sivashinsky dynamics.

### 6. GQ-FSL: Green Quantized Federated Split Learning
**Authors:** Idan Roth, Lutz Lampe
**Link:** https://arxiv.org/abs/2607.29659v1
**Summary:** The paper addresses the challenges of deploying deep neural networks on resource-limited mobile devices by proposing a green quantized federated split learning framework (GQ-FSL). It leverages stochastic quantization for both local training and data transmission, allowing for different precision levels between client and server models to optimize energy consumption while maintaining convergence. The key contribution is a method that significantly enhances energy efficiency in large-scale DNN deployments without compromising accuracy compared to existing approaches.

### 7. Development of FDD-ON: an Ontology for VAV HVAC System Fault Detection and Diagnostics
**Authors:** Yimin Chen, Brian Fricke, Bo Shen, Jamie Lian, Mingkan Zhang, James Lo, Yun Zhang, Shi Ye, Jiajing Huang, Han Hu, Chujie Lu, Rui Tang, George Zhuang
**Link:** https://arxiv.org/abs/2607.29657v1
**Summary:** The paper addresses the challenge of fault detection and diagnosis (FDD) in variable air volume (VAV) HVAC systems, which often struggle with data interpretation and interoperability. The authors developed an ontology called FDD-ON, which organizes and represents key components, fault types, and symptoms in a structured manner. The key contribution is that FDD-ON enables better querying of diagnostic knowledge and supports the creation of interoperable FDD applications, ultimately enhancing reliability and efficiency in HVAC systems.

### 8. Evolving language compositionality in a frequency-structured meaning space
**Authors:** Fabio De Ponte, Eloise Gaines-White, Conor Houghton, Seth Bullock
**Link:** https://arxiv.org/abs/2607.29642v1
**Summary:** The paper investigates how the frequency of meanings influences the evolution of language compositionality in an iterated learning model. The authors found that high-frequency meanings can develop independently of grammatical structures when they are learned holistically, but that imposing frequency on smaller components disrupts language transmission. This highlights the importance of frequency distribution over complete form-meaning units in supporting stable language evolution.

### 9. AgentHPOBench: A Benchmark For Evaluating LLM Agents as Sequential Hyperparameter Optimizers
**Authors:** Tianyu Huai, Tingshuo Fan, Xinchi Chen, Yining Zheng, Yuxin Wang, Shuang Chen, Jie Zhou, Xuanjing Huang
**Link:** https://arxiv.org/abs/2607.29626v1
**Summary:** The paper presents AgentHPOBench, a new benchmark designed to evaluate the ability of large language model (LLM) agents to optimize hyperparameters in a sequential manner across various machine learning tasks. Unlike existing benchmarks that focus on static outputs, this one measures how well agents can interpret results and guide their next steps based on experimental evidence. The findings indicate that while current agents demonstrate some competence in optimizing experiments, they still struggle with iterative refinement, diagnostic complexity, and consistent performance improvement.

### 10. The Theoretical Foundation of Socratic Tests: Dynamic, Multimodal, Conversational Examinations
**Authors:** Ilya Mikhelson
**Link:** https://arxiv.org/abs/2607.29624v1
**Summary:** The paper addresses the limitations of traditional assessment methods, which can hinder student performance and obscure feedback. It proposes the "Socratic Test," an automated conversational assessment that utilizes Dynamic Assessment principles and combines various educational frameworks to better gauge student understanding. The key contribution is a novel grading system that emphasizes mastery and provides more reliable measurement of a student's cognitive abilities while reducing biases linked to anxiety and power dynamics.
