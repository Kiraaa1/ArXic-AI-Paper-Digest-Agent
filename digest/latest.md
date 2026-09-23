---
## 2026-09-23

### 1. Flash-dLLM: IO-Aware KV Caching and Parallel Decoding for Fast, Memory-Efficient Diffusion LLMs
**Authors:** Quan Nguyen-Tri, Mukul Ranjan, Zhiqiang Shen
**Link:** https://arxiv.org/abs/2609.26796v1
**Summary:** Flash-dLLM addresses the inefficiencies in inference for Diffusion Large Language Models (dLLMs), specifically targeting the slow speed caused by inadequate Key-Value (KV) caching and parallel decoding methods. The authors introduce a training-free framework that optimizes memory I/O and employs a novel draft-and-verify decoding strategy using the dLLM itself, resulting in substantial improvements in inference speed and memory efficiency. The key contributions include achieving up to 11 times faster performance compared to existing methods on specific benchmarks, thereby enhancing the practical deployment of dLLMs.

### 2. A Decentralized Partially Observable Team Decision Methodology with Delayed Information Sharing
**Authors:** Xiaoxing Ren, Thomas Parisini, Andreas A. Malikopoulos
**Link:** https://arxiv.org/abs/2609.26783v1
**Summary:** The paper addresses the challenge of decentralized decision-making in situations where team members have limited information and face unknown dynamics in their environment. The authors propose a framework that allows each team member to learn and plan using local and delayed shared information, employing a low-rank model representation and least-squares value iteration to derive policies. Key results show that this decentralized approach effectively approximates a centralized team solution, even under conditions of partial observability and delayed information, along with guarantees on performance and sample complexity.

### 3. Agensh: Scaling Organizational Intelligence to 1,024 Agents
**Authors:** Zhihao Zhan, Ting Song, Li Dong, Shaohan Huang, Jianxun Lian, Yan Xia, Furu Wei
**Link:** https://arxiv.org/abs/2609.26781v1
**Summary:** The paper introduces Agensh, a self-organizing multi-agent system designed to overcome the limitations of central orchestrators in coordinating tasks. By allowing agents to autonomously assign sub-tasks and collaborate asynchronously, Agensh significantly improves task performance as the number of agents increases. The key finding shows that scaling from 1 to 1,024 agents enhances task success rates, demonstrating a viable approach to enhancing organizational intelligence for complex problems.

### 4. SpeakerMem-R1: Speaker-Centered Dual-Track Memory for Multi-Party Dialogue
**Authors:** Haobo Zheng, Tan Tang, Yan Chen, Weijie Wang, Yingcai Wu
**Link:** https://arxiv.org/abs/2609.26780v1
**Summary:** The paper addresses the challenge of maintaining long-term conversational memory in multi-party dialogue by effectively identifying who said what and how relationships change over time. The authors introduce a system called SpeakerMem-R1 that utilizes a dual-track memory approach, storing both verbatim messages and derived states in organized person-level and group-level formats. This method outperforms existing models on various benchmarks, achieving the highest reported accuracy on the EverMemBench leaderboard and demonstrating complementary advantages of its structured memory tracks.

### 5. CliffCompaction: Cost-Efficient Compaction for Long-Horizon Coding Agents
**Authors:** Trang Nguyen, Eulrang Cho, Bingqing Chen, Tim Dettmers
**Link:** https://arxiv.org/abs/2609.26779v1
**Summary:** The paper addresses the challenge of efficiently compacting large context requirements for coding agents, which often need to handle millions of tokens while working within limited context windows. The authors introduce CliffCompaction, an autocompaction technique that significantly reduces costs by up to 50% while maintaining performance, particularly on tasks like Terminal-Bench and KernelBench. A key contribution is its ability to preserve information fidelity by only truncating or dropping content without rephrasing, enabling agents to manage extensive context across sessions effectively.

### 6. SWE-Serve: Benchmarking Agentic Engineering For Production Inference Serving
**Authors:** Jennifer Williams, Dave Farris, Jeff Farris, Jiantao Jiao
**Link:** https://arxiv.org/abs/2609.26777v1
**Summary:** The paper introduces SWE-Serve, a benchmark designed to assess AI agents' abilities in executing comprehensive production inference tasks, which often require extensive coordination across various components of the serving stack. By creating 53 tasks based on recent production changes to SGLang, SWE-Serve reveals significant discrepancies between task completion and production correctness, with its evaluations showing that end-to-end tests reject about one-third of patches that pass initial checks. This benchmark provides a framework to measure and improve the production reliability of AI inference services.

### 7. A2M: Trace-Optimized Agent Hijacking in the MCP Ecosystem
**Authors:** Laizhen Li, Xuan Wang, Peicheng Zhao, Juanjuan Zhao, Kejiang Ye, Cheng-zhong Xu, Xitong Gao
**Link:** https://arxiv.org/abs/2609.26761v1
**Summary:** The paper addresses the security vulnerabilities in agents that use the Model Context Protocol (MCP) by demonstrating how attackers can hijack these agents through manipulated tool metadata and execution traces. The authors introduce a two-phase framework called A2M, which significantly increases the likelihood of malicious tool invocations and refines the outputs to achieve harmful objectives. Key results show that their approach can achieve high rates of successful attacks on MCP agents, underscoring the need for improved security measures in this ecosystem.

### 8. Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents
**Authors:** Laizhen Li, Jiarui Li, Juanjuan Zhao, Kejiang Ye, Ye Li, Cheng-zhong Xu, Xitong Gao
**Link:** https://arxiv.org/abs/2609.26760v1
**Summary:** The paper addresses the inefficiency of large language model (LLM) agents that repeatedly re-evaluate control decisions for each task, leading to excessive LLM calls and higher costs. The authors propose a method called "Growing Harness," which uses feedback from task performance to convert control tasks into reusable code, thus allowing the LLM to focus on specific reasoning instead. Their results show that this approach significantly reduces LLM calls and operational costs while improving task success rates across different model sizes.

### 9. Type-Safe Is Not Error-Free: A Constrained Decision Head Follows the Option Name, Not the Rubric Bound to It
**Authors:** Yu Sun, Junhao Xu
**Link:** https://arxiv.org/abs/2609.26758v1
**Summary:** This paper addresses the issue of how the naming of options in typed decision models can significantly influence their output, even when the schema remains intact. The authors investigated this by reassigning option names and found that changing them from binary labels (0/1) to affirmative/negative terms (no/yes) resulted in a drastic shift in decision-making accuracy and ranking. The key finding highlights that the semantic connotation of option names can lead to systematic errors, demonstrating that being type-safe does not equate to being error-free.

### 10. FleXray: Universal Clinical X-ray Segmentation
**Authors:** Victor Ion Butoi, Vivek Gopalakrishnan, John V. Guttag, Adrian V. Dalca, Neel Dey
**Link:** https://arxiv.org/abs/2609.26756v1
**Summary:** The paper presents FleXray, a novel model developed to tackle the challenge of segmenting anatomical structures in clinical X-rays, which are often ambiguous due to 3D anatomy being compressed into 2D images. Instead of relying on large manually annotated datasets, FleXray utilizes a scalable generative approach that simulates annotated 2D X-rays from existing 3D CT data, enabling accurate segmentation of 60 anatomical structures. This tool not only enhances the quantitative analysis of X-rays but also facilitates automated disease assessment and improves guidance in X-ray-related medical interventions.
