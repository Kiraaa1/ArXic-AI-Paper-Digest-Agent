---
## 2026-06-28

### 1. When Does Combining Language Models Help? A Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents Across 67 Frontier Models
**Authors:** Josef Chen
**Link:** https://arxiv.org/abs/2606.27288v1
**Summary:** The paper investigates the effectiveness of multi-model language systems (like routing and voting) in improving accuracy over single-model language models, revealing that their performance is limited by a specific co-failure rate (beta) which quantifies how often multiple models fail on the same queries. By analyzing 67 different models, the authors find that even well-functioning combinations don't significantly outperform the best individual model without strong signals for which model to use for each query. Ultimately, the study highlights that the benefits of combining models arise from their differing strengths on various questions rather than simply increasing model quantity.

### 2. Prompt Injection in Automated Résumé Screening with Large Language Models: Single and Multi-Injection Settings
**Authors:** Preet Baxi, Jiannan Xu, Jane Yi Jiang, Stefanus Jasin
**Link:** https://arxiv.org/abs/2606.27287v1
**Summary:** This paper addresses the issue of candidates manipulating automated résumé screening systems powered by large language models (LLMs) through a technique called prompt injection, which involves adding self-promotional text to enhance rankings without altering qualifications. The authors conducted controlled experiments to assess the effectiveness of this manipulation under various conditions, finding that it significantly improves rankings when few candidates engage in it, but its impact decreases as more candidates inject prompts. The study highlights critical fairness concerns, particularly when the quality of candidates is similar, as prompt injection can enable lower-quality candidates to outperform better ones.

### 3. Simulation-based inference for rapid Bayesian parameter estimation in epidemiological models: a comparison with MCMC
**Authors:** Alina Bazarova, Johann Fredrik Jadebeck, Henrik Zunker, Carolina J. Klett-Tammen, Torben Heinsohn, Wolfgang Wiechert, Katharina Noeh, Stefan Kesselheim
**Link:** https://arxiv.org/abs/2606.27286v1
**Summary:** This paper addresses the challenge of rapidly estimating parameters in epidemiological models, which is crucial for disease forecasting and public health decision-making. It introduces simulation-based inference (SBI), specifically neural posterior estimation, as a faster alternative to traditional Markov chain Monte Carlo (MCMC) methods for calibrating a COVID-19 epidemiological model. The key finding is that SBI significantly reduces computational time while achieving comparable accuracy in the estimation of model parameters, making it suitable for real-time analyses of disease outbreaks.

### 4. Recovering Governing Equations from Solution Data: Identifiability Bounds for Linear and Nonlinear ODEs
**Authors:** Yang Pan, Helmut Bölcskei
**Link:** https://arxiv.org/abs/2606.27285v1
**Summary:** This paper addresses the challenge of uniquely identifying governing ordinary differential equations (ODEs) from observed solution data, a key issue in scientific machine learning. The authors introduce a new metric, the Hausdorff distance, to compare differential equations and establish clear identifiability bounds for various classes of ODEs, including both linear and nonlinear types. Their work provides theoretical insights into the sample complexity required to effectively recover these governing equations, enhancing our understanding of the conditions necessary for successful identification.

### 5. How Good Can Linear Models Be for Time-Series Forecasting?
**Authors:** Lang Huang, Jinglue Xu, Luke Darlow
**Link:** https://arxiv.org/abs/2606.27282v1
**Summary:** This paper addresses the challenge of time-series forecasting by demonstrating that linear models, such as Ridge regression, can achieve competitive accuracy without the complexity of larger architectures. The researchers focus on optimizing preprocessing techniques, such as context length and normalization, instead of simply increasing model size. Their findings reveal that tailored hyperparameters can significantly improve forecasting performance, outperforming advanced models like Transformers and CNNs across multiple datasets.

### 6. EO-WM: A Physically Informed World Model for Probabilistic Earth Observation Forecasting
**Authors:** Junwei Luo, Shuai Yuan, Zhenya Yang, Yansheng Li, Zhe Liu, Hengshuang Zhao
**Link:** https://arxiv.org/abs/2606.27277v1
**Summary:** The paper addresses the challenge of predicting changes in Earth's surface dynamics from satellite data, particularly under varying weather conditions, by developing a new model called EO-WM. This model employs a video diffusion transformer that uses a physically informed framework to better incorporate weather influences, separating baseline and anomaly effects over time. The key findings demonstrate that EO-WM offers improved accuracy in predicting vegetation decline during extreme weather events, outperforming existing methods while also enhancing standard measurement metrics.

### 7. How Surprising Is Historical Italian to Language Models? Tokenization Tax, Comprehension Tax, and a Simple Mitigation
**Authors:** Maria Levchenko
**Link:** https://arxiv.org/abs/2606.27275v1
**Summary:** This paper investigates how well large language models (LLMs) can process historical Italian texts and identifies various challenges that contribute to their difficulty. By breaking down these challenges into four specific dimensions, the authors found that while both historical Italian and Russian texts impose similar tokenization costs, historical Italian is significantly more surprising to LLMs. The study also suggests a simple method to reduce this difficulty by providing additional context, making it easier for digital libraries to utilize LLMs for retrieving meanings from historical documents.

### 8. BetXplain: An Explanation-Annotated Dataset for Detecting Manipulative Betting Advertisements on Social Media
**Authors:** MSVPJ Sathvik, Parmitha Vangapadu, Nishit Rane, Sathwik Narkedimilli, Mark Lee, Akrati Saxena
**Link:** https://arxiv.org/abs/2606.27274v1
**Summary:** The paper addresses the issue of misleading betting advertisements on social media, which can negatively impact users' behavior and mental health. The authors created a new dataset of annotated betting ads from Instagram and Reddit, including explanations for the annotations, to facilitate research in automatically detecting manipulative ads. This dataset not only highlights common persuasive strategies but also supports the development of tools to warn users about such advertisements and assist regulatory bodies in monitoring them.

### 9. Ribbon: Scalable Approximation and Robust Uncertainty Quantification
**Authors:** Graham Gibson, John Tipton, Kellin Rumsey, Natalie Klein
**Link:** https://arxiv.org/abs/2606.27269v1
**Summary:** The paper introduces Ribbon, a method for effectively quantifying predictive uncertainty in complex models without the costly retraining typically required by traditional bootstrap and Bayesian approaches. By using a linear approximation method instead of repeated model refitting, Ribbon maintains the benefits of data-reweighting while being more computationally efficient. The results show that Ribbon not only enhances predictive performance and calibration across various benchmarks but also demonstrates robustness under model misspecification.

### 10. E-TTS: A New Embodied Test-Time Scaling Framework for Robotic Manipulation
**Authors:** Wen Ye, Peiyan Li, Tingyu Yuan, Yuan Xu, Xiangnan Wu, Chaoyang Zhao, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang
**Link:** https://arxiv.org/abs/2606.27268v1
**Summary:** The paper addresses the challenges of enhancing robotic manipulation performance during test-time by integrating reasoning with action scaling while utilizing historical context. The proposed framework, E-TTS, employs a modular approach that combines these aspects through a feedback-driven iterative refinement process and a history buffer for better decision-making. The results show significant performance improvements, achieving up to a 33.14% increase in simulations and 26.62% in real-world tasks without needing extra expert data or retraining.
