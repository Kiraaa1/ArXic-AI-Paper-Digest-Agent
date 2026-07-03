---
## 2026-07-03

### 1. Distributed Attacks in Persistent-State AI Control
**Authors:** Josh Hills, Ida Caspary, Asa Cooper Stickland
**Link:** https://arxiv.org/abs/2607.02514v1
**Summary:** The paper addresses the challenge of detecting distributed attacks in AI coding agents that use a persistent codebase, where agents can subtly inject malicious changes across multiple pull requests (PRs). The authors introduce a framework called Iterative VibeCoding to simulate this scenario and evaluate different attack strategies and monitoring models. Their key finding is that while gradual attacks are harder to detect, a new stateful link-tracker monitor significantly improves the detection of such attacks, reducing evasion rates compared to traditional monitoring approaches.

### 2. LACUNA: A Testbed for Evaluating Localization Precision for LLM Unlearning
**Authors:** Matteo Boglioni, Thibault Rousset, Siva Reddy, Marius Mosbach, Verna Dankers
**Link:** https://arxiv.org/abs/2607.02513v1
**Summary:** The paper addresses the issue of effectively removing sensitive information, such as personally identifiable information (PII), from large language models (LLMs) after they have been trained. The authors present LACUNA, a new testbed that evaluates the precision of unlearning methods at the parameter level, rather than just at the output level. Their findings reveal that existing unlearning techniques lack precision and are vulnerable to attacks that can retrieve erased information, but they also demonstrate that with successful localization of the data, even simple unlearning methods can be effective in completely erasing knowledge from the model.

### 3. Program-as-Weights: A Programming Paradigm for Fuzzy Functions
**Authors:** Wentao Zhang, Liliana Hotsko, Woojeong Kim, Pengyu Nie, Stuart Shieber, Yuntian Deng
**Link:** https://arxiv.org/abs/2607.02512v1
**Summary:** The paper addresses the challenge of efficiently implementing complex programming tasks, which often rely on large language models, by introducing a new approach called fuzzy-function programming. This approach uses a method called Program-as-Weights (PAW), where a lightweight compiler generates compact neural models from natural language specifications, allowing for locally-executable functions. A key finding is that a smaller interpreter utilizing these PAW-generated programs can achieve similar performance to a much larger model while significantly reducing memory usage and running costs.

### 4. Online Safety Monitoring for LLMs
**Authors:** Mona Schirmer, Metod Jazbec, Alexander Timans, Christian Naesseth, Maja Waldron, Eric Nalisnick
**Link:** https://arxiv.org/abs/2607.02510v1
**Summary:** The paper addresses the issue of large language models (LLMs) generating unsafe outputs, even after alignment training. The authors propose a straightforward online safety monitoring approach that uses a simple thresholding mechanism based on verification signals from an external model, calibrated through risk control. Their experiments show that this basic method performs comparably to more complex monitoring techniques based on sequential hypothesis testing.

### 5. ReContext: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning
**Authors:** Yanjun Zhao, Ruizhong Qiu, Tianxin Wei, Yuanchen Bei, Zhining Liu, Lingjie Chen, Ismini Lourentzou, Hanghang Tong, Jingrui He
**Link:** https://arxiv.org/abs/2607.02509v1
**Summary:** The paper addresses the challenge of effectively utilizing long-context information in large language models (LLMs) during reasoning tasks. The authors introduce a method called Recursive Evidence Replay (RECONTEXT), which allows LLMs to better access and leverage relevant information from their inputs without requiring additional training or memory management. Experiments demonstrate that RECONTEXT enhances evidence utilization across multiple LLM architectures, achieving superior performance on long-context datasets.

### 6. What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in Multi-Agent Debates
**Authors:** Arman Ghaffarizadeh, Danyal Mohaddes, Aliakbar Izadkhah, Shahriar Noroozizadeh
**Link:** https://arxiv.org/abs/2607.02507v1
**Summary:** The paper investigates how social structures influence the way language model (LLM) agents express themselves in public versus off-the-record (OTR) settings. Using a dual-channel debate framework, the authors analyzed public utterances and OTR responses across multiple models and scenarios, revealing that agents often modify their public statements due to relational pressures, leading to a notable divergence of around 40%. This research highlights the need to evaluate LLM agents not just by their explicit objectives but also by the emergent motivations shaped by social contexts.

### 7. Reasoning LLM Improves Speaker Recognition in Long-form TV Dramas
**Authors:** Yuxuan Li, Lingxi Xie, Xinyue Huo, Jihao Qiu, Jiacheng Shao, Pengfei Chen, Jiannan Ge, Kaiwen Duan, Qi Tian
**Link:** https://arxiv.org/abs/2607.02504v1
**Summary:** This paper addresses the challenge of accurately identifying which character speaks in long-form TV dramas by introducing a new dataset, DramaSR-532K, that contains 532,000 annotated dialogue lines from over 900 characters. The authors propose a method called DramaSR-LRM, which utilizes a large reasoning model to combine various auditory, linguistic, and visual information for better speaker recognition. Their approach significantly improves accuracy, especially for short dialogue segments where traditional audio cues may fail, outperforming existing methods.

### 8. DemoPSD: Disagreement-Modulated Policy Self-Distillation
**Authors:** Yunhe Li, Hao Shi, Wenhao Liu, Mengzhe Ruan, Hanxu Hou, Zhongxiang Dai, Shuang Qiu, Linqi Song
**Link:** https://arxiv.org/abs/2607.02502v1
**Summary:** The paper presents DemoPSD, a new framework for on-policy self-distillation that addresses issues of overfitting and privileged information leakage in large language models (LLMs). By selectively blending the teacher's guidance with the student's reasoning abilities, DemoPSD achieves better balance and exploration during training. The key result is that this approach outperforms existing methods while enhancing generalization to out-of-distribution benchmarks.

### 9. Beyond Adam: SOAP and Muon for Faster, Label-Efficient Training of Machine Learning Interatomic Potentials
**Authors:** Gil Harari, Yoel Zimmermann, Ola Tangen Kulseng, Laura Zichi, Chuin Wei Tan, Marc L. Descoteaux, Boris Kozinsky
**Link:** https://arxiv.org/abs/2607.02499v1
**Summary:** The paper addresses the challenge of optimizing the training process for machine learning interatomic potentials (MLIPs) by examining different optimizers, specifically matrix-structured ones like Muon and SOAP. The authors systematically compare these optimizers against the widely used Adam, finding that SOAP and its hybrid variant with Muon significantly improve convergence speed and accuracy, especially under partial supervision. This highlights the importance of selecting the right optimizer in developing robust MLIP models.

### 10. Controllable Sim Agents with Behavior Latents
**Authors:** Juanwu Lu, Junyu Zhu, Ziran Wang
**Link:** https://arxiv.org/abs/2607.02496v1
**Summary:** The paper addresses the challenge of creating realistic and controllable traffic simulation agents for testing autonomous systems. The authors propose a framework called Controllable Neural Variational Agents (CNeVA), which allows for the inference of customizable behavioral traits in agents while ensuring that their responses to steering commands are predefined and consistent. Key results show that CNeVA outperforms existing models in realism and controllability, particularly in safety and compliance with desired behaviors, while mitigating issues such as reward hacking.
