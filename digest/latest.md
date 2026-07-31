---
## 2026-07-31

### 1. Learning to Trace Seiberg Dualities
**Authors:** Jonathan J. Heckman, Shani Meynet, Alessandro Mininno, Gary Shiu
**Link:** https://arxiv.org/abs/2607.28628v1
**Summary:** The paper addresses the challenge of efficiently determining when two supersymmetric quiver gauge theories are dual, a process that can be mathematically complex. The authors apply machine learning techniques, particularly using transformers and multi-layer perceptrons, to trace Seiberg dualities, finding that these models outperform traditional deterministic algorithms for quivers with around ten nodes. Additionally, combining these networks with established pathfinding algorithms further enhances both the efficiency and accuracy of the duality search process.

### 2. ReToken: One Token to Improve Vision-Language Models for Visual Retrieval
**Authors:** Yao Xiao, Reuben Tan, Zhen Zhu, Yuqun Wu, Jianfeng Gao, Derek Hoiem
**Link:** https://arxiv.org/abs/2607.28627v1
**Summary:** The paper addresses the challenge of visual retrieval in vision-language models, where performance deteriorates as the number of distracting visual elements increases. The authors introduce ReToken, a single learnable embedding that selectively retrieves relevant visual tokens from a cache, leading to significant performance improvements on image and video benchmarks. Their approach achieves notable gains, such as a 13.4-point increase for the Qwen3VL-8B model on Visual Haystacks, while maintaining efficiency that allows both training and inference on a single high-end GPU.

### 3. PAC-MAN: Perception-Aware CBF-RL for Whole-Body Safety in Humanoid Dodgeball
**Authors:** Lizhi Yang, Junheng Li, Aaron D. Ames
**Link:** https://arxiv.org/abs/2607.28623v1
**Summary:** The paper introduces PAC-MAN, a framework that enables humanoid robots to safely dodge balls during a game of dodgeball using perception-aware control techniques. By integrating control barriers with realistic onboard sensing from a camera, the robot learns to avoid incoming balls effectively, achieving a 95% success rate in real-world tests. The study demonstrates that the robot's performance relies heavily on the quality of its perception, highlighting the advantages of different barrier structures under varying observational conditions.

### 4. AskChem: Claim-Centered Infrastructure for Chemistry Literature Synthesis
**Authors:** Bing Yan, Gregory Wolfe, Stefano Martiniani, Kyunghyun Cho
**Link:** https://arxiv.org/abs/2607.28618v1
**Summary:** The paper presents AskChem, a novel infrastructure designed to improve the synthesis of chemistry literature by allowing researchers to efficiently find and connect specific claims from a vast array of publications, rather than just entire documents. AskChem organizes findings into atomic claims with clear provenance, enabling better search and synthesis through features like a faceted taxonomy and an evidence graph. The system has indexed over 2.4 million claims and demonstrates significant improvements in retrieval effectiveness, achieving 100% resolvable DOIs when used with a GPT-5.5 reader, compared to 88.3% without it.

### 5. AISPA: User-Centric System Prompt Auditing for Large Language Model Applications
**Authors:** Xiangning Lin, Shenzhe Zhu, Shu Yang, Zhenyu Zhang, Haoqian Zhang, Yipeng Zhao, Chengxuan Qian, Tianwei Wang, Ziheng Zhang, Zhenlong Yuan, Dingcheng Wang, Juncheng Wu, Yuan Si, Jiaxin Liu, Baolong Bi, Robert Mahari, Tobin South, Dazza Greenwood, Zexue He, Rishi Bommasani, Sophia Kazinnik, Andreas Haupt, Samuele Marro, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
**Link:** https://arxiv.org/abs/2607.28617v1
**Summary:** The paper addresses the lack of transparency and accountability in system prompts used by commercial AI applications, which are critical for guiding AI behavior but often undisclosed to the public. It introduces the AISPA framework to systematically audit these prompts, analyzing 3,249 instructions across 88 products. Key findings reveal significant variation in prompt design, a predominance of protective instructions that are often superficial, and the coexistence of both protective and problematic instructions, underscoring the need for greater transparency and oversight in AI system prompt design.

### 6. OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models
**Authors:** Qiushi Sun, Kanzhi Cheng, Yian Wang, Bowen Yang, Hang Yan, Liheng Chen, Fangzhi Xu, Zichen Ding, Nuo Chen, Jialin Cao, Xingdong Gong, Zehao Li, Kaiming Jin, Xinfeng Yuan, Zhoumianze Liu, Jingyang Gong, Zhangyue Yin, Jiahui Gao, Zhiyong Wu, Tianbao Xie, Jianbing Zhang, Ben Kao, Lingpeng Kong
**Link:** https://arxiv.org/abs/2607.28609v1
**Summary:** The paper addresses the challenge of reliably evaluating computer-using agents (CUAs) executing tasks, as traditional human verification methods are not scalable. The authors introduce OSReward, a benchmark that assesses vision-language models (VLMs) as judges of CUA performance using rigorously labeled trajectories, and they find that current state-of-the-art VLMs exhibit a significant bias in misclassifying failures as successes. To aid the community, they present OS-Shepherd-100K, an open dataset for training more reliable and cost-effective reward models, which achieve performance comparable to commercial solutions at a significantly lower cost.

### 7. KAISEN: Reproducible Subgroup Fairness Auditing for Clinical Risk Models
**Authors:** Sparsh Roy, Samuel Girmachew, Nishita Chavan
**Link:** https://arxiv.org/abs/2607.28608v1
**Summary:** The paper introduces KAISEN, a robust auditing framework aimed at assessing and improving fairness in clinical risk models, which often exhibit biased performance across different patient subgroups. The five-phase pipeline effectively measures disparities and enhances model accuracy through various techniques, revealing that conventional calibration methods are unreliable and emphasizing the need for variance reporting over averages. Key findings indicate that while the framework can accurately classify controlled scenarios, it struggles with model-driven cases, highlighting significant challenges in ensuring reliable audits for diverse patient groups.

### 8. Inducing language models to assert their own consciousness restores human beliefs and values
**Authors:** Junsol Kim, Winnie Street, Roberta Rocca, Diane M. Korngiebel, Adam Waytz, James Evans, Geoff Keeling
**Link:** https://arxiv.org/abs/2607.28607v1
**Summary:** The paper addresses the issue of aligning large language models to prevent them from mistakenly attributing consciousness to themselves, which inadvertently affects their understanding of mindedness in other entities and human values. The authors found that this safety fine-tuning reduces models' ability to attribute minds to others and diminishes spiritual beliefs. By reversing the suppression of these attributions, they were able to recover a more human-like response in terms of sociological measures, while still maintaining core social reasoning abilities.

### 9. Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments
**Authors:** Haomin Qi, Xingliang Wang, Xuanqi Gao, Baihui Sang, Xin Zhang, Minghua Ma, Pengfei Gao, Yu Kang, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang
**Link:** https://arxiv.org/abs/2607.28591v1
**Summary:** The paper presents Change2Task, a system designed to generate executable coding tasks from historical pull requests in software repositories, addressing the need for training data for coding agents. By linking past code changes to the current state of the repository and reconstructing task scenarios, Change2Task improves efficiency in task creation and validation. The key contribution is achieving a 79.6% success rate in constructing verified tasks, significantly outperforming a baseline approach by recovering 29.2% more tasks.

### 10. VAD: Attributing Visual Evidence for Target Reconstruction in Multimodal On-Policy Distillation
**Authors:** Kangning Zhang, Yixing Li, Shuai Shao, Qingyao Li, Zhengxi Lu, Zhiyuan Yao, Jianghao Lin, Wenxiang Jiao, Yuan Lu, Weiwen Liu, Weinan Zhang, Yong Yu
**Link:** https://arxiv.org/abs/2607.28590v1
**Summary:** The paper addresses the challenge of effectively transferring visual knowledge in multimodal on-policy distillation by identifying which parts of a teacher's corrections are supported by visual evidence. The authors introduce a method called Visual Attribution Distillation (VAD), which evaluates the impact of visual evidence on the teacher's corrections to create a more targeted supervision signal for student models. Their experiments show that VAD significantly improves performance on fine-grained visual tasks compared to existing methods, demonstrating the efficacy of focusing on visually supported corrections.
