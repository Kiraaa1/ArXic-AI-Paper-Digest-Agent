---
## 2026-08-14

### 1. AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design
**Authors:** Yaxin Luo, Haobin Jiang, Jialv Zou, Xu Huang, Wenhao Yan, Haodong Li, Zhengrong Yue, Jing Li, Xiaofu Chen, Xiaohan Zhao, Jiacheng Liu, Jiacheng Cui, Zhiqiang Shen, Xiaotong Li
**Link:** https://arxiv.org/abs/2608.13560v1
**Summary:** The paper addresses the challenge of transforming academic papers into effective conference posters by proposing AutoDesign, a framework that uses a meta-harness optimizer to improve a code agent's design capabilities through iterative feedback. This approach significantly outperforms existing commercial solutions, achieving a high average quality of poster outputs while demonstrating strong human preference in evaluations. Key results include a substantial improvement in performance on the provided PosterBench dataset, indicating the effectiveness of AutoDesign in automating long-horizon design tasks.

### 2. OmniScientist: An Omni-Modal Omni-Discipline AI Scientist
**Authors:** Bobo Li, Hao Fei, Tianjie Ju, Mong-Li Lee, Wynne Hsu
**Link:** https://arxiv.org/abs/2608.13558v1
**Summary:** The paper introduces OmniScientist, an AI system designed to automate full research workflows in science by integrating and reasoning over diverse types of raw data (such as images, audio, and numerical datasets) rather than relying on pre-processed summaries. It features a structured approach with separate agents for ideation, experimentation, and writing, enabling the AI to adapt its research questions and methods based on real-time observations. The results show that OmniScientist successfully completed full research projects across multiple disciplines, outperforming existing methods by leveraging direct perception of data.

### 3. HumanTracker: Towards Comprehensive and Human-Aligned Motion Tracking Benchmark
**Authors:** Dairu Liu, Zekun Qi, Jiayu Zeng, Ruixi Yu, Yu Guan, Yintianrun Zhang, Xuchuan Chen, Sikai Liang, Zekai Li, Chenghuai Lin, Xinqiang Yu, Wenyao Zhang, He Wang, Li Yi
**Link:** https://arxiv.org/abs/2608.13555v1
**Summary:** The paper addresses the limitations of current humanoid motion tracking evaluations, which are often misaligned with human perceptions and fail to account for critical physical issues like instability and incorrect contacts. The authors introduce the HumanTracker benchmark, featuring a large dataset of motion trajectories organized by motion types and accompanied by a new metric called HumanScore, which better aligns with human preferences and highlights failures that traditional metrics overlook. The key contribution is the creation of a more comprehensive and perceptually relevant evaluation framework for motion tracking.

### 4. Defensive Boosting for Online Probabilistic Forecasting
**Authors:** Georgy Noarov, Aaron Roth
**Link:** https://arxiv.org/abs/2608.13554v1
**Summary:** The paper addresses the challenge of online probabilistic forecasting in situations where the predictors may not consistently perform well, particularly against an adaptive adversary. The authors introduce a novel algorithm called the Defensive Booster, which effectively combines two different boosting guarantees: it competes well with the best available predictions while also reducing classification errors when certain conditions are met. Their approach is highly efficient, requiring only a single weak learner and demonstrating superior performance in both speed and accuracy compared to existing methods.

### 5. Exponential Convex Calibration Dimension for the Multi-Label Jaccard Measure
**Authors:** Mingyuan Zhang
**Link:** https://arxiv.org/abs/2608.13549v1
**Summary:** This paper addresses the challenge of calibrating multi-label classification metrics, specifically the Jaccard score, which has an exponential number of possible outcomes as the number of labels increases. The authors develop a mathematical framework using a MinHash Gram representation and Boolean Möbius inversion to prove bounds on the calibration dimension required for convex surrogates of the Jaccard measure. A key contribution is demonstrating that achieving exact calibration necessitates an exponential number of prediction coordinates, while also presenting polynomial-dimensional alternatives that maintain small regret in Jaccard scoring.

### 6. QuoteBench: How Matched Scores Can Hide Command-Path Failures
**Authors:** Shangao Li, Yao Zhang, Volker Tresp, Yuanyuan Yang
**Link:** https://arxiv.org/abs/2608.13547v1
**Summary:** The paper introduces QuoteBench, a framework designed to evaluate the effectiveness of large language model (LLM) coding agents in executing Bash commands while identifying errors that occur during command generation versus execution. By conducting experiments that assess how different configurations affect command success rates, the study reveals that matched execution scores can obscure significant failures, indicating the need for a detailed reporting of the model’s configuration and evaluation conditions. The key finding is that replaying generated commands through a modified parser can drastically reduce success rates, highlighting the importance of distinguishing between initial command generation and subsequent execution errors.

### 7. LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure
**Authors:** Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel
**Link:** https://arxiv.org/abs/2608.13545v1
**Summary:** The paper addresses the challenge of studying how language models acquire knowledge given their training on diverse and expansive data. To tackle this, the authors created LITTLECURRICULUM, a specially curated dataset focused on U.S. elementary school material, and trained a new language model, LITTLELEARNER, on this limited scope. The key contribution is the establishment of a controlled environment that allows for systematic exploration of knowledge acquisition and representation, demonstrating that while new knowledge can be integrated, it does not extend the model's capabilities beyond the predefined scope.

### 8. SAEVerbalizer: Generating Explanations for Sparse Autoencoder Features via Representation Verbalization
**Authors:** Weihan Meng, Hongzhu Guo, Yi Jing, Dewen Liu, Zijun Yao, Xiaozhi Wang, Lei Hou, Juanzi Li
**Link:** https://arxiv.org/abs/2608.13538v1
**Summary:** The paper addresses the challenge of explaining features extracted by sparse autoencoders, which typically rely on external observations for insights. The authors propose SAEVerbalizer, a framework that fine-tunes a large language model to generate natural-language explanations directly from the decoder directions of the sparse autoencoder. Key results demonstrate that this approach not only provides explanations for unseen features but also allows for flexible adaptation to features from different models.

### 9. DARTree: Speculative Diffusion Decoding with Autoregressive Draft Trees
**Authors:** Tianyi Li, Yaxin Luo, Xinyi Shang, Zhiqiang Shen
**Link:** https://arxiv.org/abs/2608.13524v1
**Summary:** The paper presents DARTree, a method designed to enhance the speed of autoregressive language models by efficiently decoding multiple token proposals in parallel. By leveraging a tree structure for candidate generation instead of relying on a single draft chain, DARTree significantly increases the number of acceptable tokens in each verification round while decoupling the inference process from time-consuming operations. The results show that DARTree achieves a substantial lossless speedup, accepting nearly 99% more tokens per round compared to existing methods and up to 9.73 times faster than traditional autoregressive decoding.

### 10. Vero: Can AI Agents Build Formally Verified Software Repositories?
**Authors:** Zhe Ye, Hantao Lou, Yuechun Sun, Peiyang Song, Zhengxu Yan, Timothe Kasriel, Qingyang Zhang, Kaiyu Yang, Soonho Kong, Jingxuan He, Dawn Song
**Link:** https://arxiv.org/abs/2608.13522v1
**Summary:** The paper introduces Vero, a benchmarking framework designed to evaluate AI agents' ability to generate both code and formal proofs in large software repositories. By testing agents on 43 curated multi-module instances from real-world applications, Vero aims to bridge the gap in verified code generation at the repository level. The key finding indicates that even the most advanced coding agents struggle, fully solving only 27 of 43 tasks, highlighting the current limitations in achieving reliable verified software synthesis.
