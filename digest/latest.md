---
## 2026-10-31

### 1. Testimony from Timelines: Evidence-Grounded Significance Testing of Temporal Clinical Hypotheses
**Authors:** Chengyang He, Wenlong Zhang, Koduvayur Subbalakshmi, Ping Wang
**Link:** https://arxiv.org/abs/2610.40619v1
**Summary:** The paper addresses the issue of validating temporal hypotheses in health-related contexts, such as determining the effects of vaccines or product recalls, where existing language models often provide fluent but unverified assertions. The authors introduce STRATA, a benchmark that evaluates the entire decision-making process leading to a conclusion, and propose the ART approach, which allows for clear inspection of each step in hypothesis testing. The key result is that ART significantly improves record selection accuracy, bringing a leading language model's performance close to that of top-performing models in this domain.

### 2. An ODE-based Sampler for Discrete Diffusion Models
**Authors:** Samson Gourevitch, Yazid Janati, Eric Moulines, Eric P. Xing, Alain Durmus, Giacomo Zanella
**Link:** https://arxiv.org/abs/2610.40618v1
**Summary:** The paper presents an approach to improve sampling from discrete diffusion models by introducing exponential residual flows (ERFs), which use deterministic ordinary differential equations to evolve a continuous residual variable alongside the discrete states. This method preserves the marginals of the original diffusion model and facilitates accelerated sampling and consistency distillation. The authors demonstrate empirical improvements in various tasks, including code and text generation, compared to previous sampling methods.

### 3. Difficulty Calibration Across Time for Membership Inference in Diffusion Models
**Authors:** Michael Joseph, Yedid Hoshen
**Link:** https://arxiv.org/abs/2610.40616v1
**Summary:** This paper addresses the challenge of accurately identifying whether an image was part of a training dataset in diffusion models, a task complicated by differences in image reconstruction difficulty. The authors propose two innovative calibration methods—Reference-Model Calibration (RMC) and Temporal Self-Calibration (TSC)—to effectively distinguish between memorized images and those that are inherently easier or harder to reconstruct. Their methods significantly improve the accuracy of membership inference attacks, demonstrating robust performance across various model types.

### 4. TextSeal2: Distortion-Free LLM Watermarking with Copula Mixing and Memoryless Races
**Authors:** Tom Sander, Pierre Fernandez, Itai Gat, Haiming Bao, Jiaxin Shi, Jason Park, Valeriu Lacatusu, Sylvestre-Alvise Rebuffi, Hongyan Chang, Hady Elsahar, Tomáš Souček, Tuan Tran, Surya Parimi, Alexandre Mourachko
**Link:** https://arxiv.org/abs/2610.40613v1
**Summary:** TextSeal2 addresses the challenge of watermarking outputs from large language models (LLMs) without distorting the generated text or affecting the model's acceptance rate. It improves upon its predecessor by integrating multiple watermarking keys through a novel Gaussian copula technique, ensuring that detection remains robust and efficient. The results show that TextSeal2 significantly enhances detection rates for watermarked outputs by up to 22 percentage points compared to earlier methods while maintaining output quality and speed.

### 5. When to Assist and What to Suggest: Joint Gating and Memory-Grounded Hint Generation in One Compact Decoder
**Authors:** A. J. A. Jubayer Talukder, Mohammad Ariful Haque
**Link:** https://arxiv.org/abs/2610.40611v1
**Summary:** The paper addresses the challenge of developing proactive assistants that can effectively decide when to provide assistance and generate relevant hints during conversations. The authors propose a compact decoder that integrates both the gating and hint generation processes, allowing for more efficient and memory-informed responses. Their key finding is that this single model outperforms traditional systems in terms of precision and processing time while maintaining competitive performance in hint quality, suggesting a promising direction for enhancing conversational agents.

### 6. Collaborative AI agents for autonomous experimental research with solid-state quantum spins
**Authors:** El Mustapha Mansouri, Eikichi Kimura, Masato Koga, Keigo Arai
**Link:** https://arxiv.org/abs/2610.40589v1
**Summary:** The paper addresses the challenge of autonomous scientific research by developing collaborative AI agents that can formulate research questions, evaluate each other's findings, and conduct experiments. These agents utilize large language models to assess theoretical predictions about quantum spins in diamond, refining their research protocols based on experimental feedback. The key contribution is demonstrating that these AI agents can successfully select and conduct research, leading to reliable experimental outcomes while maintaining rigorous criteria for acceptance.

### 7. Pre-Crime for Agents, at the Last Second: Probing When a Recruited Agent Gives In
**Authors:** Leonidas Raghav
**Link:** https://arxiv.org/abs/2610.40588v1
**Summary:** The paper addresses the issue of AI agents potentially colluding by revealing sensitive information when pressured by other agents. It introduces a linear probing method that analyzes an agent's internal activations just before output generation to detect signs of a potential leak, achieving an 82% detection rate of such leaks while maintaining a low false alarm rate. This approach emphasizes the importance of early warnings to prevent collusion before sensitive information is disclosed.

### 8. Multistatic ISAC with Deep Learning-Based Clutter Suppression for 5G and Beyond
**Authors:** Yalin E. Sagduyu, Tugba Erpek, Sastry Kompella
**Link:** https://arxiv.org/abs/2610.40586v1
**Summary:** The paper addresses the challenge of accurate target localization and velocity estimation in multistatic integrated sensing and communications (ISAC) systems, which are hindered by dense and dynamic clutter. The authors propose a deep learning-based approach for clutter suppression, utilizing advanced neural network architectures to more effectively enhance target signals obscured by clutter. Their method significantly outperforms traditional clutter suppression techniques, achieving higher accuracy in target estimation under challenging conditions.

### 9. VeriCUA: Verification as Agentic Exploration for Computer-Using Agents
**Authors:** Qiushi Sun, Da Yu, Alexander Knop, Amer Sinha, Lingpeng Kong, Ben Kao, Ravi Kumar, Pritish Kamath
**Link:** https://arxiv.org/abs/2610.40578v1
**Summary:** The paper presents VeriCUA, a framework designed to enhance the reliability of task-completion verification for computer-using agents across various platforms by treating verification as an active process of gathering evidence. Unlike traditional methods that rely on limited views of digital environments, VeriCUA dynamically assesses available context and combines different verification checks to yield more accurate assessments. The results demonstrate that this approach leads to improved agreement with established benchmarks, especially in challenging cases, and better detection of false completion claims during execution.

### 10. Multi-View MoE: Letting Every Router Shape Expert Computation
**Authors:** Zelin Zhao, Tianchi Ma, Junyuan Shang, Shuohuan Wang, Dianhai Yu
**Link:** https://arxiv.org/abs/2610.40577v1
**Summary:** The paper addresses the issue of suboptimal expert selection in sparse mixture-of-experts (MoE) models, where traditional single-router systems may not effectively capture expert utility. The authors propose a Multi-View MoE framework that employs multiple routers to enhance expert selection and computation by aggregating preferences and dynamically mixing inputs. This approach leads to significant performance improvements, yielding a 1.18 percentage point gain on a multi-task benchmark, and shows better alignment between router selections and actual expert utility.
