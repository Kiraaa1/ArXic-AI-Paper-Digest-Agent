---
## 2026-10-05

### 1. Less Decoder is More Encoder: Geometric Representation Learning from Novel View Synthesis
**Authors:** Keerthi Kaashyap, Dennis Anthony, Akshay Krishnan, Nhi Ngoc Nguyen, Jeremy Collins, James Hays, Shreyas Kousik, Animesh Garg
**Link:** https://arxiv.org/abs/2610.03717v1
**Summary:** The paper addresses the challenge of improving geometric representation learning through Novel View Synthesis (NVS), which typically struggles with existing methods due to ineffective architectural choices. The authors introduce SNAP, a self-supervised encoder-decoder transformer that employs a pose-conditioned local decoder and a latent-space reconstruction objective to enhance representation learning. The key finding is that SNAP achieves competitive performance across various tasks while maintaining more transferable geometric structures, effectively improving robustness under different camera perspectives compared to traditional 2D representation methods.

### 2. 4DCodeBench: Benchmarking Agents on Inverse Graphics of Dynamic Scenes
**Authors:** Ruihong Shen, Žiga Kovačič, Peter Kulits, Xingrui Wang, Zizhang Li, Joshua B. Tenenbaum, Alan Yuille, Jieneng Chen, Jiajun Wu
**Link:** https://arxiv.org/abs/2610.03715v1
**Summary:** The paper presents 4DCodeBench, a new benchmark designed to assess how effectively AI agents can reconstruct dynamic scenes from videos by generating executable graphics code. It involves translating visual inputs into compact scene representations and assessing capabilities across various physical phenomena. The key finding shows that while agents perform well with static scenes, they struggle with accurately reconstructing complex dynamic behaviors, highlighting a gap in current AI models' understanding of dynamic environments.

### 3. What Should World Models Forget? Stratified Retention for Continual Adaptation
**Authors:** Nishit Anand, Ramani Duraiswami, Dinesh Manocha
**Link:** https://arxiv.org/abs/2610.03713v1
**Summary:** The paper addresses the challenge of continual learning in world models, where knowledge must be updated as environments change while also maintaining certain core truths. It proposes a method called differential retention that stratifies knowledge retention based on how stable certain information is over time, allowing for accurate revision of outdated facts without confusing it with forgetting crucial invariants. This approach improves evaluation metrics for world models by distinguishing between successful knowledge updates and catastrophic forgetting.

### 4. RNADyn: A Benchmark for Generating and Understanding RNA Dynamics
**Authors:** Yiming Huang, Lennart Bastian, Hanqun Cao, Luis Vollmers, Tolga Birdal
**Link:** https://arxiv.org/abs/2610.03712v1
**Summary:** The paper addresses the challenge of understanding RNA dynamics, which involves conformational changes not captured by static structures. To tackle this, the authors introduce RNADynBench, a comprehensive benchmark of RNA molecular dynamics trajectories, and develop RNADynNet, a unified model for both generating trajectories and extracting dynamic characteristics from a single RNA conformer. Their approach demonstrates strong performance, achieving high correlations in generated dynamics and showing that the model's predictions align well with traditional molecular dynamics data.

### 5. EyeRobot 2.0: Active Gaze for Precise Manipulation without Wrist Cameras
**Authors:** Kush Hari, Justin Kerr, Nidhya Shivakumar, Samarth Mahapatra, Carmelo Sferrazza, Jiahui Lei, Jitendra Malik, C. Karen Liu, Ken Goldberg, Angjoo Kanazawa
**Link:** https://arxiv.org/abs/2610.03710v1
**Summary:** The paper presents EyeRobot 2.0, a framework that allows robots to perform precise bimanual manipulation using active gaze with just a single stereo camera, rather than relying on wrist-mounted cameras. By employing a technique called Active Visual Fixation (AVF), the system focuses on critical features by adjusting its gaze during tasks and trains through reinforcement learning. The key finding is that EyeRobot 2.0 significantly improves task success rates in both real-world and simulated environments, outperforming traditional methods that use additional cameras, particularly in scenarios where the objects being manipulated obstruct the view.

### 6. From Mixing to Tearing: Graph Decomposition in Decentralized Optimization via Message Passing
**Authors:** Kuangyu Ding, Gesualdo Scutari
**Link:** https://arxiv.org/abs/2610.03709v1
**Summary:** This paper addresses the challenge of minimizing sums of strongly convex functions distributed across agents in an undirected graph, focusing on improving decentralized optimization methods that rely on local communication. The authors introduce a novel framework called GATE, which designs a cooperative structure for optimization and communication based on the graph's topology, using a message-passing approach that involves updating variables at each edge. The key contribution is the establishment of a convergence rate that highlights the relationship between the functions' properties, the network's structure, and the optimization design, supported by numerical experiments that demonstrate the effectiveness of the proposed algorithms.

### 7. LESSER: Post-Training Data Selection with Output-Layer Gradients
**Authors:** Lyuxin David Zhang, Eric Wong, Surbhi Goel, Anton Xue
**Link:** https://arxiv.org/abs/2610.03702v1
**Summary:** The paper addresses the challenge of selecting effective training data for large language models without the heavy computational cost of calculating full gradients. The authors introduce LESSER, a method that uses output-layer gradients, which can be computed more efficiently with just a forward pass, to approximate the performance of traditional full-gradient data selection. Their approach significantly reduces computational costs while maintaining performance alignment in data selection, achieving a reduction in computing resources by up to 9.7 times.

### 8. Language Models that Play Chess and Explain Their Moves
**Authors:** Adithya Bhaskar, Jeffrey Cheng, Danqi Chen
**Link:** https://arxiv.org/abs/2610.03695v1
**Summary:** The paper addresses the challenge of combining the superhuman playing strength of chess engines with the natural language explanation capabilities of language models. The authors introduce a 4B-parameter chess-language model named Queen, which utilizes a novel framework that integrates a chess encoder with a language model, allowing it to play at Grandmaster level while providing coherent explanations for its moves. The key contribution is that Queen significantly improves its playing strength and explanation quality through iterative learning, achieving a substantial Elo rating increase and producing explanations comparable to advanced language models.

### 9. Transcriptome-informed multi-modal AI for predicting neoadjuvant therapy response from breast cancer biopsies
**Authors:** Jungkyu Park, Dhruva Biswas, Joseph Cappadona, Cerise Tang, Ken G. Zeng, Bartosz Machura, Chuwen Liu, Paolo Tarantino, Coral Omene, Francisco J. Esteva, Rohit Bhargava, Marcin Braun, Kamila Paździerz, Jakub Czerwiński, Hanna Romańska-Knight, Albert Grinshpun, Bareket Daniel, Michele Buchinger, Frederick Howard, Piotr Wysocki, Brie Chun, Freya Schnabel, Rich Caruana, Jan Witowski, Krzysztof J. Geras
**Link:** https://arxiv.org/abs/2610.03693v1
**Summary:** The paper addresses the challenge of limited labeled data in developing deep learning biomarkers for predicting responses to neoadjuvant therapy in breast cancer. The authors propose a two-stage AI model that first learns gene expression patterns from histopathology data and then predicts treatment responses using these learned patterns alongside clinical variables. The model demonstrates strong predictive performance with an AUROC of 0.79 across different patient cohorts, highlighting its effectiveness in using biologically informed data compression to improve precision oncology outcomes.

### 10. Simulation-Free Learning of Population Dynamics with Wasserstein Lagrangian Residuals
**Authors:** Fedor Sergeev, Markus Heinonen, Daniel Waxman, Tim Cooijmans, Ricardo Baptista, Dmitry Batenkov, Eli Bingham
**Link:** https://arxiv.org/abs/2610.03679v1
**Summary:** The paper addresses the challenge of modeling the dynamics of probability distributions in systems like cells and fluids without relying on costly simulations. The authors introduce a new method called Double-Stitch that learns these dynamics by focusing on minimizing the residuals of the equations governing motion, based on a Clebsch variational principle. This approach demonstrates superior performance compared to traditional gradient-flow methods, achieving training speeds that are 4 to 14 times faster.
