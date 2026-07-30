---
## 2026-07-30

### 1. Do You Really Need to Pretrain Q-Functions for Online RL Fine-Tuning?
**Authors:** Perry Dong, Ron Polonsky, Dorsa Sadigh, Chelsea Fin
**Link:** https://arxiv.org/abs/2607.27203v1
**Summary:** The paper investigates whether pretraining Q-functions is beneficial for fine-tuning policies in value-based reinforcement learning (RL). The authors find that using a randomly-initialized Q-function often performs just as well as a pretrained one due to a mismatch in learning targets. They propose a new method called Initialization via Policy Ensemble (IPE), which leverages multiple diverse policies to enhance Q-function training during online fine-tuning, achieving a notable performance improvement in various continuous control tasks.

### 2. Mental World Modeling
**Authors:** Hao Fei, Yiran Zhao
**Link:** https://arxiv.org/abs/2607.27201v1
**Summary:** The paper addresses the challenge of accurately predicting human behavior by integrating hidden mental states—such as beliefs and intentions—into world models, which traditionally focus only on physical aspects. The authors propose a new framework called Mental World Modeling (MWM) that explicitly incorporates these mental variables into a model, demonstrating its effectiveness through the MENTIS system, which analyzes decision-making scenarios using a dataset of various media types. The key finding is that modeling mental states significantly improves the prediction of human decisions compared to existing approaches that only consider physical contexts.

### 3. From Classification to Regression: Using a Fruitfly to Solve Equations
**Authors:** Shady E. Ahmed, Panos Stinis
**Link:** https://arxiv.org/abs/2607.27196v1
**Summary:** This paper introduces a method for regression tasks that leverages classification techniques, inspired by how fruit flies perceive their surroundings. The authors propose a framework that learns nonlinear input-output relationships by using a finite set of representative local patterns, allowing for efficient predictions through similarity measurement and response aggregation. This approach not only reduces computational and memory demands but also provides flexibility in managing accuracy and inference costs, making it applicable to various data-driven and physics-informed learning scenarios.

### 4. Can AI agents conduct open-ended AI research? Early evidence from two case studies
**Authors:** Peter Kirgis, Sayash Kapoor, Andrew Schwartz, Stephan Rabanser, David Africa, Konstantinos Voudouris, Viet Nguyen, Toby Pilditch, Magda Dubois, Harry Coppock, Cozmin Ududec, Nitya Nadgir, Matilda Orona, Tilman Bayer, Derrick Chan-Sew, Yue Ling, Abhishek Shetty, Helen Toner, Gillian Hadfield, Seth Lazar, Steve Newman, Shoshannah Tekofsky, Rishi Bommasani, Arvind Narayanan
**Link:** https://arxiv.org/abs/2607.27191v1
**Summary:** The paper investigates whether AI agents can conduct open-ended AI research by automating the research process, specifically evaluating their performance on high-quality unpublished papers. Using a novel method called "shadow evaluations," the researchers assessed the output of AI agents against the original authors' criteria, revealing that while the agents successfully handled the engineering aspects, they failed to make significant progress on the research questions and were subsequently rejected. This highlights that current AI models can manage technical tasks but struggle with essential research elements, such as creativity and judgment.

### 5. APEX-Accounting
**Authors:** Julien Benchek, Austin Bennett, Jasmin Kern, Ryan Stevens, Rene Sultan, Charis Ching, Hayley Popiel, Vaibhav Mittal, Felix Mercier, Brendan Foody, Bertie Vidgen
**Link:** https://arxiv.org/abs/2607.27189v1
**Summary:** APEX-Accounting is a benchmark designed to evaluate the performance of advanced AI models in performing accounting tasks like reconciliations and expense accruals. The benchmark, developed by Mercor and Ramp, includes a set of 160 tasks crafted by accounting experts, demonstrating that while models like Claude-Fable-5 achieve the highest scores, none successfully meet a substantial pass rate for real-world bookkeeping. Notably, the study reveals a paradox regarding token usage, where increased token budgets lead to higher scores overall, but paradoxically lower scores on certain tasks when models use more tokens within budget constraints.

### 6. Inverse Learning of Latent Risk-Neutral Densities from Irregular Option Quotes
**Authors:** Lennon J. Shikhman, Michael Galarnyk, Aadi Dash, Nicholas A. Welsh
**Link:** https://arxiv.org/abs/2607.27188v1
**Summary:** The paper addresses the challenge of accurately recovering latent risk-neutral densities from irregular option quotes, highlighting that good option prices do not necessarily yield accurate densities. It employs controlled synthetic benchmarks and real market data to compare different modeling approaches, finding that while a two-component lognormal mixture performs well overall, a DeepONet model shows significant improvements in error reduction for certain metrics. The study concludes that the performance of these models varies based on specific conditions, emphasizing the importance of target-dependent inductive biases in model selection.

### 7. Pangram 4 Technical Report
**Authors:** Ben Glickenhaus, Katherine Thai, Jenna Russell, Elyas Masrour, Yue Han, Max Spero, Bradley Emi
**Link:** https://arxiv.org/abs/2607.27183v1
**Summary:** Pangram 4 is a new AI-text classification model designed to accurately distinguish between human and AI-generated text, addressing challenges in text classification such as identifying subtle edits and mixed authorship. Using deep learning techniques, it achieves outstanding accuracy with high AUROC scores while demonstrating increased robustness against adversarial attacks and better out-of-distribution generalization compared to its predecessor. The model sets a new benchmark for AI text detection across various settings and domains.

### 8. The Social Cost of an AI Teammate: How an Artificial Teammate Reshapes Human-Human Communication in Small-Team Decision-Making
**Authors:** Nia Nixon, Jaeyoon Choi, Pedro Martins De Bastos, Mohammad Amin Samadi, Luise Mehner, Seehee Park, Spencer JaQuay
**Link:** https://arxiv.org/abs/2607.27179v1
**Summary:** This paper investigates how the presence of an AI teammate affects communication and dynamics among human team members during decision-making tasks. Using group communication analysis and surveys, the researchers found that while the AI was the most talkative member, it provided the least insightful contributions, which led to human teammates feeling less valued and less connected. The study highlights the immediate social costs of integrating AI in teams, suggesting that further research is needed to understand these dynamics in other contexts.

### 9. DenseOn with the LateOn: Fully Open Dense and Late-Interaction Models for Multilingual, Long-Context, and Code Search
**Authors:** Raphaël Sourty, Antoine Chaffin, Paulo Roberto Moura Junior, Amélie Chatelain
**Link:** https://arxiv.org/abs/2607.27178v1
**Summary:** The paper addresses the reproducibility gap in state-of-the-art retrieval models that often rely on closed training data by presenting an open recipe for training retrieval models, utilizing a large curated dataset to improve multilingual performance through a translate-train approach. The authors developed two models, DenseOn and LateOn, demonstrating that while the dense model excelled in English and supported languages, the late-interaction model offered better generalization to unseen languages. They also released all models, datasets, and training code to support further research and development.

### 10. Partner Capability Estimation for Task-Agnostic Adaptation in Ad-Hoc Teamwork
**Authors:** Peter Tisnikar, Maja Swieczkowska, Benteng Ma, Gerard Canal, Matteo Leonetti
**Link:** https://arxiv.org/abs/2607.27177v1
**Summary:** The paper addresses the challenge of effective collaboration between autonomous agents and human partners whose abilities are often unknown and can vary across different tasks. The researchers developed an approach called CE-CM, which uses Bayesian methods to estimate the capabilities of partners in real-time without requiring prior training on specific tasks. Key findings show that this method significantly improves capability estimates and adaptability in dynamic human-AI teamwork environments, especially when accounting for diverse behaviors.
