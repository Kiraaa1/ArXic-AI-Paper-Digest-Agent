---
## 2026-11-23

### 1. Optimal Linear Regression Without a Variance
**Authors:** Artin Tajdini, Jasper C. H. Lee, Jonathan Scarlett, Kevin Jamieson
**Link:** https://arxiv.org/abs/2611.27983v1
**Summary:** The paper addresses the challenge of performing linear regression in scenarios where the noise has infinite variance but finite conditional moments, which complicates traditional estimation methods. The authors present a versatile approach that transforms standard finite-variance regression techniques into effective methods for weak-moment scenarios through a process called empirical residual pruning. As a key result, they establish that under certain conditions, the proposed method can achieve reliable parameter estimation with high probability, even without knowledge of the noise characteristics, while also providing a computationally efficient solution.

### 2. A Methodologically Rigorous Benchmark of Linear Regression,RNN, and LSTM for S&P 500 Forecasting:Identifying Sources of Performance Inflation in Financial DeepLearning
**Authors:** Hari Sitaula, Joseph Opitz
**Link:** https://arxiv.org/abs/2611.27978v1
**Summary:** This paper addresses the challenge of accurately forecasting the S&P 500 closing level one day ahead by comparing linear regression, RNNs, and LSTMs using a comprehensive dataset and standardized evaluation methods. The authors conducted a rigorous analysis of existing methodologies in financial deep learning, identifying issues that can inflate performance results, and they proposed corrected benchmarks to assess model effectiveness more reliably. Key findings include a more accurate portrayal of model performance, emphasizing the importance of controlling for methodological biases in stock prediction studies.

### 3. MemOnce: A Scalable Memory Architecture for Large Language Models
**Authors:** Chang Nie, Chaoyou Fu, Songlin Liu, Yiqing Hu, Caifeng Shan
**Link:** https://arxiv.org/abs/2611.27973v1
**Summary:** The paper presents MemOnce, an innovative memory architecture designed to improve the efficiency of large language models (LLMs) during long interactions by addressing issues of memory usage and computational complexity. It achieves this by utilizing a memory encoder-decoder to store compact representations of hidden states and a sparse attention mechanism for effective memory retrieval. The key contributions include a dramatic reduction in GPU memory usage and prefill latency, while also increasing throughput and performance compared to existing architectures.

### 4. On the Complete Feature Set for ADHD Classification in Children and Adolescents Based on EEG Signals
**Authors:** Javier Sanchis, Álvaro Navarro, Jorge García-Carrasco, Tahar Kechadi, Juan Trujillo
**Link:** https://arxiv.org/abs/2611.27970v1
**Summary:** The paper addresses the challenge of standardizing EEG feature comparisons for ADHD classification in children and adolescents by curating a comprehensive dataset from existing recordings. It provides a well-documented resource linking EEG signals to various feature definitions, ensuring consistent signal preparation and quality checks. The key contribution is a publicly available dataset that facilitates analysis, alongside preliminary findings showing robust recruitment-group discrimination in specific task conditions, though without establishing diagnostic validity.

### 5. Non-penetrating World Models
**Authors:** Yuhang Dai, Yinwei Wu, Ziyue Lin, Han Ji, Xingyi Yang
**Link:** https://arxiv.org/abs/2611.27963v1
**Summary:** The paper addresses the issue of preventing object penetration in interactive video world models, revealing that existing models often fail to do so despite having the necessary predictive information. The authors introduce a framework called NoPeWorld, which uses hidden states from diffusion transformers to predict and replace unsafe actions with safe alternatives, significantly reducing penetration incidents from 74% to 16%. Their method also demonstrates impressive generalization capabilities across various scenarios, and they provide open access to their code and benchmark tools.

### 6. Model Carving: Training Transformers That Optimize Their Own Topology
**Authors:** Kaden Zheng, Pratyusha Sharma
**Link:** https://arxiv.org/abs/2611.27962v1
**Summary:** The paper addresses the inefficiency of fixed Transformer architectures in machine learning by introducing a method called Model Carving, which allows a model to learn its own optimal architecture during training. By using learnable gates to remove unnecessary components, the approach results in smaller, more efficient models that perform better than traditional dense models, even surpassing those obtained through pruning or distillation. Key findings demonstrate that carved models not only achieve lower validation losses but also significantly reduce computational costs and increase decoding speed without compromising quality.

### 7. Ranking-Preserving Coreset Selection for Efficient Evolutionary Hyperparameter Optimization
**Authors:** Mamoona Tasadduq, Maryam Bashir
**Link:** https://arxiv.org/abs/2611.27959v1
**Summary:** The paper addresses the challenge of high computational costs in hyperparameter optimization (HPO) when evaluating numerous configurations on large datasets. It introduces a ranking-preserving coreset selection framework that efficiently identifies a smaller subset of data that retains the ranking of configurations from the full dataset. The method significantly accelerates HPO processes with various algorithms, achieving speedups of 1.14x to 8.80x while maintaining comparable accuracy, thereby demonstrating that the coreset selection effectively preserves performance rankings even beyond the selected configurations.

### 8. Topology Hub Optimal Transport: Eliminating Long Context Dilution at Flash Speed
**Authors:** Dylan Forde
**Link:** https://arxiv.org/abs/2611.27951v1
**Summary:** The paper addresses the challenge of efficiently retrieving relevant information from long-context models while minimizing the dilution of important signals among numerous distractors. The authors propose Topology Hub Optimal Transport (THOT), a method that employs bounded-support capacity gating and a novel Sinkhorn scaling technique to enhance recall performance. THOT achieves impressive zero-shot recall rates in large contexts, outperforming traditional attention mechanisms and demonstrating significant speed improvements in processing over conventional methods.

### 9. The Optimal Sample Complexity of Agnostic PAC Learning for Partial Concept Classes
**Authors:** Liang-Yu Zou
**Link:** https://arxiv.org/abs/2611.27946v1
**Summary:** This paper addresses the problem of learning from a partial concept class with finite VC dimension in a setting where the learner must work under agnostic conditions. The authors present a deterministic agnostic PAC learning algorithm that achieves the optimal sample complexity using a number of examples proportional to the VC dimension and the desired accuracy. The key contribution is that their sample complexity result matches a previously established lower bound, confirming the efficiency of their approach.

### 10. BioEmu2: Scalable Emulation of Biomolecular Dynamics
**Authors:** Michael Gastegger, Adam E. Foster, José Jiménez-Luna, Tim Hempel, Sarah Lewis, Yu Xie, Lixin Sun, Iryna Zaporozhets, J. Thorben Frank, Yaoyi Chen, Michael Plainer, Ludwig Winkler, Pedro B. P. S. Reis, Sven H. Giese, Roberto Sordillo, Victor García Satorras, Eray Inanc, Kacper Kapuśniak, Soojung Yang, Rishwanth Raghu, Rachel Kim, Gabriel Dernbach, Deniz Gunceler, Hannes Schulz, Bonnie Kruft, Marwin Segler, Christopher M. Bishop, Cecilia Clementi, Ryota Tomioka, Frank Noé
**Link:** https://arxiv.org/abs/2611.27924v1
**Summary:** BioEmu2 addresses the challenge of modeling biomolecular motions and interactions at scale, which is crucial for understanding biomolecular function. It is a generative model that combines structure prediction, equilibrium sampling, and time evolution to sample biomolecular dynamics significantly faster than traditional molecular dynamics methods. The key contributions include high accuracy in structure prediction, effective simulation of megadalton complexes, and the ability to generate long-timescale dynamics while maintaining close agreement with established molecular dynamics references.
