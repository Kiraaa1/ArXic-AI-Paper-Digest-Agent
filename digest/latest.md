---
## 2026-11-12

### 1. ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows
**Authors:** Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, Rohith Nama, Arushi Gupta, Carlos D. Castillo, Prathap Ramachandra, Xiaofan Jiang, Francesco Carbone
**Link:** https://arxiv.org/abs/2611.14492v1
**Summary:** ReTrace addresses the inefficiency of relying on Large Language Model (LLM) agents to execute Standard Operating Procedures (SOPs) by distilling these procedures into reusable workflows that can operate without continual LLM calls. By extracting and consolidating the conditions behind each step from logged agent runs, ReTrace generates efficient, executable workflows tailored for various orchestration platforms. The key results show that ReTrace workflows achieve near-completion rates at significantly lower costs and faster runtimes compared to traditional agent-based approaches.

### 2. TimeSeek: Multi-Task and Multi-Domain Pretraining for Generalized Time Series Analytics
**Authors:** Peng Chen, Yihang Wang, Zhongwen Rao, Yang Shu, Yuying Qiu, Yuxuan Chen, Lujia Pan, Bin Yang, Chenjuan Guo
**Link:** https://arxiv.org/abs/2611.14491v1
**Summary:** The paper presents TimeSeek, a novel model designed to enhance time series analytics by addressing the limitations of existing time series foundation models that struggle with diverse data across multiple domains and tasks. TimeSeek utilizes a Multi-Domain Feature Extractor and multi-task collaborative training to effectively capture complex patterns and unify various tasks during pre-training. The key contribution is its ability to achieve state-of-the-art performance in forecasting, anomaly detection, and classification tasks, even in few-shot and zero-shot scenarios, while maintaining efficient inference.

### 3. Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game
**Authors:** Muhan Gao, Hangxiao Zhu, Xinqi Su, Yu Zhang, Daniel Khashabi, Kuan-Hao Huang
**Link:** https://arxiv.org/abs/2611.14487v1
**Summary:** The paper addresses the challenge of understanding how large language models (LLMs) generate and refine research ideas through an iterative process. The authors introduce a game called Re-Search, where LLMs must rediscover the core idea of a research paper by asking yes-or-no questions, revealing that most progress occurs within the first 30 questions, and identifying key limitations in the models’ ability to generate original questions. The study concludes that enhancing ideation systems with external ideas may be more beneficial than solely improving the models' generation capabilities.

### 4. Mechanistic Interpretability Needs a Logic of Inference
**Authors:** Zhimin Hu, Chen Jiang, Hanbo Xie, N. Apurva Ratan Murty, Sashank Varma
**Link:** https://arxiv.org/abs/2611.14483v1
**Summary:** The paper addresses the challenge of interpreting neural networks by establishing a systematic framework for mechanistic interpretability (MI) that enhances our understanding of how their internal workings relate to their behavior. By drawing parallels with neuroscience, the authors propose five principles that guide the inference of mechanisms from complex systems, aiming to turn localized insights into broader, testable hypotheses. The key contribution is a recursive logic that aids in constructing a more rigorous procedure for understanding and verifying the mechanisms behind neural models.

### 5. Pterodactyl: Pushing the Limits of Efficient Automated Translation Evaluation
**Authors:** Evelyn Y. Garland, Carola F. Berger
**Link:** https://arxiv.org/abs/2611.14480v1
**Summary:** The paper presents Pterodactyl, an automated evaluation system designed for assessing translation quality at the segment level and identifying error-free segments. Utilizing a Large Language Model (LLM) to make binary classifications, the system incorporates prompt engineering and model optimization based on ROC analysis to enhance its performance. The contribution lies in its customizable and cost-effective design, tailored to improve automated translation evaluation tasks.

### 6. FERN: Cross-Benchmark Table Retrieval for Text-to-SQL with Frozen Retrievers and Learned Ranking
**Authors:** Arjun Rao, Nishant Gopinath
**Link:** https://arxiv.org/abs/2611.14477v1
**Summary:** The paper presents FERN, a system designed to improve table retrieval for text-to-SQL tasks across various benchmark datasets, aiming to enhance the performance compared to existing models. Instead of relying on generative language models, FERN combines three fixed retrievers, enriches the candidate tables with features, and uses a trained ranking model to optimize selection. Notably, FERN achieves competitive recall rates and significantly improves the chances of retrieving relevant tables in top rankings, showing particular strength on the Spider and BIRD datasets despite some challenges on Fiben.

### 7. C$^2$-Routing: Complementary Cropping and Compression for Efficient Vision-Language Inference
**Authors:** Guorui Lu, Qinyu Chen
**Link:** https://arxiv.org/abs/2611.14469v1
**Summary:** The paper addresses the high computational costs associated with Visual Question Answering (VQA) by introducing C$^2$-Routing, a method that adaptively selects between cropping images for small targets and compressing whole images for context preservation based on the input image and question. This approach successfully reduces the computational load by an average of 36.53% in end-to-end FLOPs and 42.36% in visual tokens while maintaining a minimal impact on accuracy, demonstrating its effectiveness across multiple vision-language models and diverse datasets.

### 8. Bayesian inverse problems and epidemic-threshold uncertainty for a heterogeneous SIS reaction-diffusion model
**Authors:** Duc-Lam Duong
**Link:** https://arxiv.org/abs/2611.14468v1
**Summary:** This paper addresses the challenge of using early observations to infer persistence in a heterogeneous SIS (susceptible-infected-susceptible) epidemic model, despite uncertainties in individual transmission and recovery rates. The authors establish a Bayesian framework that demonstrates how these rates influence epidemic threshold dynamics and persistence, revealing that early prevalence can effectively inform about long-term epidemic outcomes. Key results include a novel method for quantifying convergence of posterior distributions and error bounds for persistence probabilities, alongside numerical examples that validate their findings.

### 9. A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference Resets
**Authors:** Audrey Huang, Nan Jiang, Sham M. Kakade, Sadhika Malladi, Akshay Krishnamurthy, Dylan J. Foster
**Link:** https://arxiv.org/abs/2611.14467v1
**Summary:** This paper addresses the challenge of optimizing language model policies during post-training, specifically tackling the issue of "coverage collapse" where optimal responses can become highly unlikely even as overall rewards improve. The authors propose a method called Approximate Policy Mirror Descent (APMD) that includes reference resets to the most recent policy, which helps to restore the likelihood of generating optimal responses and ensures convergence to the best possible policy. The key contribution is the establishment of global convergence guarantees for coverage-preserving algorithms, clarifying the impact of regularization and algorithm design on the efficiency of post-training optimization.

### 10. A Theory of Cross-Validation Variance
**Authors:** Nathaniel S. O'Connell, Jaime L. Speiser
**Link:** https://arxiv.org/abs/2611.14463v1
**Summary:** The paper addresses the variability in cross-validation estimates of predictive performance by establishing a theoretical framework that precisely quantifies their variance based on how observations impact training and evaluation in different roles. By deriving an exact identity for this variance, the authors demonstrate that K-fold cross-validation is optimal in minimizing variance, while also identifying that leave-one-out and leave-pair-out schemes yield the lowest variance for specific metrics. This work provides a solid theoretical basis for understanding and improving the selection of cross-validation methods for reliable model evaluation.
