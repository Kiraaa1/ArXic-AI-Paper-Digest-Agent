---
## 2026-08-15

### 1. Exponential quantum advantage for learning signals with a single qubit
**Authors:** Ishaan Kannan, Sridhar Prabhu, Saeed A. Khan, Mandar M. Sohoni, Xingrui Song, Saswata Roy, Alen Senanian, Valla Fatemi, Peter L. McMahon, Jordan Cotler
**Link:** https://arxiv.org/abs/2608.13521v1
**Summary:** This paper addresses the challenge of efficiently learning classical signals through measurement, which is typically resource-intensive. The authors demonstrate that by coupling a single qubit with a conventional sensor, they can significantly reduce the required measurements—up to 10 million times less—for tasks like learning Fourier coefficients and analyzing time-varying signals. Their approach, based on a new theoretical framework called Quantum Phase-Space Inference (QΨ), not only highlights the capabilities of near-term quantum technology but also provides a systematic method to identify and leverage quantum advantages in practical applications.

### 2. The data geometry of masking diffusion: Certified-optimal schedules via unmasking growth complexity
**Authors:** Martin J. Wainwright
**Link:** https://arxiv.org/abs/2608.13520v1
**Summary:** This paper addresses the challenge of improving sampling efficiency in masking diffusion by introducing a new measure called unmasking growth complexity (UGC), which assesses data geometry. The authors develop optimized sampling schedules that adapt to the underlying data structure and demonstrate that their method leads to samplers that can achieve low errors in Kullback-Leibler divergence effectively. A key contribution is the demonstration of significant performance improvements, particularly in high-dimensional settings, through a certified-optimal approach to sampling.

### 3. Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology
**Authors:** Yunsung Chung, Yingshuo Liu, Abboud F. Hassan, Han Feng, Mary M. Maleckar, Nassir Marrouche, Jihun Hamm
**Link:** https://arxiv.org/abs/2608.13518v1
**Summary:** The paper addresses the challenge of predicting post-operative outcomes in cardiology, particularly after atrial fibrillation ablation, where recovery processes are complex and irregular. It introduces an intervention-aware clinical world model that tracks a patient's recovery through a structured latent state updated by various clinical events and measurements over time. The model demonstrated effective prediction of recurrence risk, achieving an area under the receiver operating characteristic (AUROC) of 0.756, and it also provided insights into recovery dynamics without needing follow-up MRI data during inference.

### 4. DFM Mimir v1: An Open HRM Delivering Frontier Performance at 1B Parameters Using Only Permissible Post-Training Data
**Authors:** Peter Schneider-Kamp, Jacob Nielsen, Gianluca Barmina, Kenneth Enevoldsen, Lukas Galke Poech
**Link:** https://arxiv.org/abs/2608.13517v1
**Summary:** The paper presents Mimir v1, a 1-billion-parameter language model developed to overcome the challenges of training models on non-permissible datasets by relying solely on ethically sourced post-training data. Using the Hierarchical Reasoning Model architecture, Mimir v1 achieves state-of-the-art performance in Danish and competitive results in English, surpassing existing models like HRM-Text 1B and challenging larger models. The model is available for use on the Hugging Face Hub, promoting accessibility in open-source research.

### 5. Measuring Task-Agnostic Training Data Influence Across Language Model Pretraining
**Authors:** Yuto Nishida, Hirokazu Kiyomaru, Yusuke Oda, Takashi Kodama, Chaoran Liu, Daisuke Kawahara, Yusuke Miyao, Max Müller-Eberstein, Masaru Isonuma
**Link:** https://arxiv.org/abs/2608.13515v1
**Summary:** The paper addresses the challenge of measuring how training data influences language model performance during pretraining, without relying on specific downstream tasks. The authors propose a novel method that evaluates an example's influence based on its impact on reducing the distance to final model parameters, using intermediate checkpoints. They find that the influence of certain data types shifts over the course of training, with literature-related data being more influential early on and STEM data gaining importance later, revealing a dynamic relationship between training data and model progression.

### 6. Bagging Robustly Learns VC Classes with Linear Sample Complexity
**Authors:** Omar Montasser
**Link:** https://arxiv.org/abs/2608.13514v1
**Summary:** The paper addresses the challenge of creating predictors that are robust to adversarial examples at test time, proving that such predictors can be learned from a number of training samples that scales linearly with the VC dimension. The authors leverage a straightforward approach that combines bagging with robust empirical risk minimization, achieving a significant improvement over previous methods. Their findings also establish a lower bound indicating that this linear sample complexity is optimal for this type of learning task.

### 7. TabSOM: A tabular-to-image encoding method based on self-organizing maps
**Authors:** David Chushig-Muzo, María Ángeles Rodríguez de Cara, Eva Milara, Francisco J. Lara-Abelenda, Luis Zhinin-Vera, Diego H. Peluffo-Ordóñez
**Link:** https://arxiv.org/abs/2608.13513v1
**Summary:** The paper introduces TabSOM, a new method for converting tabular data into images to enhance the performance of deep learning models like convolutional neural networks and vision transformers. Unlike existing methods that only consider individual feature values, TabSOM preserves the relationships between features using a Self-Organizing Map to create meaningful visual representations. The approach outperforms twelve prior methods in predictive accuracy and provides improved interpretability, making it a significant advancement in applying deep learning to tabular data.

### 8. On the Structural Limits of Machine Learning Decision Systems: An Information-Theoretic, Interaction-Based, and Stochastic-Dynamical Perspective
**Authors:** Nestor R. Barraza, Gabriel Pena
**Link:** https://arxiv.org/abs/2608.13510v1
**Summary:** This paper addresses the limitations of machine learning decision systems by analyzing how intrinsic structural properties of data affect their performance, rather than just focusing on algorithmic advancements. It employs an information-theoretic framework to establish bounds on classification errors and estimation precision, highlighting that these limits are influenced more by the underlying data model than by the algorithms used. The authors emphasize that understanding these constraints is essential for improving predictive capabilities and integrating decision systems more effectively.

### 9. Equivariant learning of a transferable three-dimensional classical density functional
**Authors:** Bingqing Cheng
**Link:** https://arxiv.org/abs/2608.13506v1
**Summary:** The paper addresses the challenge of predicting liquid behavior under varying conditions without requiring separate atomistic simulations for each scenario. The authors developed a method to directly learn a three-dimensional free-energy functional from equilibrium density fields while maintaining symmetry and consistency. Their key contribution is a single learned functional that successfully transfers across different temperatures and system sizes, allowing it to predict important liquid properties such as phase behavior and interfacial interactions without needing specific training data.

### 10. Intern-S2-Preview: Scientific Agentic Foundation Model
**Authors:** Lei Bai, Jiaqi Cao, Chiyu Chen, Guanzhou Chen, Kai Chen, Guangran Cheng, Erfei Cui, Xuanlang Dai, Shengyuan Ding, Shangheng Du, Yanhui Duan, Yue Fan, Youqing Fang, Quan Gan, Yuanyuan Gao, Jiaye Ge, Lixin Gu, Yuzhe Gu, Qipeng Guo, Junjun He, Xin Hong, Ming Hu, Zhouqi Hua, Haian Huang, Junhao Huang, Zixian Huang, Minxi Jin, Lingkai Kong, Alexander Lam, Zehao Li, Zonglin Li, Tianhao Liang, Dahua Lin, Junyao Lin, Tianyang Lin, Zhouhan Lin, Jiangning Liu, Jin Liu, Kuikun Liu, Wenran Liu, Yifei Liu, Yuhong Liu, Yuhong Liu, Zhoumianze Liu, Ziyan Liu, Ziyu Liu, Haijun Lv, Han Lv, Chengqi Lyu, Le Ma, Ningsheng Ma, Zerun Ma, Haoyang Peng, Runyu Peng, Jifei Shan, Zixin Shang, Kou Shi, Xiang Shi, Qisheng Su, Xuerui Su, Hao Sun, Xiao Sun, Yanan Sun, Yu Sun, Huanze Tang, Yinghao Tang, Wenhui Tian, Zhongbo Tian, Bingli Wang, Haomin Wang, Jiarui Wang, Jingzhi Wang, Rui Wang, Xiquan Wang, Yi Wang, Zhecan Wang, Ziyi Wang, Zun Wang, Rubin Wei, Lianyi Wu, Wen Wu, Yue Wu, Yuhan Wu, Zhenyu Wu, Zijian Wu, Shuhao Xing, Jun Xu, Xingle Xu, Xuenan Xu, Xiangchao Yan, Ziang Yan, Bowen Yang, Danni Yang, Lin Yang, Zhiqi Yang, Qian Yao, Haochen Ye, Peng Ye, Jinhui Yin, Jiashuo Yu, Dingbo Yuan, Fei Yuan, Yuhang Zang, Bo Zhang, Chao Zhang, Chen Zhang, Hongjie Zhang, Junming Zhang, Wenlong Zhang, Wenwei Zhang, Yiming Zhang, Zhuo Zhang, Ziyang Zhang, Haiteng Zhao, Penghao Zhao, Yibo Zhao, Zhonghan Zhao, Zhihang Zhong, Bowen Zhou, Peiheng Zhou, Xin Zhou, Xinyu Zhou, Yunhua Zhou, Dongsheng Zhu, Yicheng Zou
**Link:** https://arxiv.org/abs/2608.13505v1
**Summary:** The paper presents Intern-S2-Preview, a series of advanced AI models designed to enhance scientific reasoning and discovery by processing various types of scientific data and tools over extended tasks. The models are pretrained using a diverse range of scientific documents and then fine-tuned through innovative training techniques, which lead to improved performance on scientific and multimodal benchmarks. Notably, the approach significantly enhances time series analysis and forecasting capabilities, demonstrating superior results in specific scientific tasks.
