---
## 2026-07-16

### 1. Leveraging unlabelled data for generalizable neural population decoding
**Authors:** Ximeng Mao, Nanda H. Krishna, Avery Hee-Woon Ryoo, Matthew G. Perich, Guillaume Lajoie
**Link:** https://arxiv.org/abs/2607.14086v1
**Summary:** The paper addresses the challenge of training neural decoders for interpreting spike-based neural data without relying solely on labeled datasets. It introduces a new framework called MOJO, which combines self-supervised learning and supervised learning to improve model performance. The results show that MOJO significantly enhances decoding accuracy, especially when labeled data is scarce, and demonstrates generalizability across different species and neural recording modalities.

### 2. Linear Independent Component Analysis via Optimal Transport
**Authors:** Ashutosh Jha, Michel Besserve, Simon Buchholz
**Link:** https://arxiv.org/abs/2607.14081v1
**Summary:** The paper addresses the challenge of recovering independent source signals from their mixtures in Linear Independent Component Analysis (ICA). Instead of traditional methods that maximize non-Gaussianity through proxy measures, the authors introduce a new approach using the squared Wasserstein distance to a standard Gaussian. Their proposed OT-ICA algorithm demonstrates superior performance over existing methods in various applications, including EEG artifact removal and economic analysis, without relying on specific distributional assumptions.

### 3. MetaPerch: Learning from metadata for bioacoustics foundation models
**Authors:** Mustafa Chasmai, Vincent Dumoulin, Jenny Hamer
**Link:** https://arxiv.org/abs/2607.14072v1
**Summary:** The paper introduces MetaPerch, a bioacoustic foundation model that enhances species identification by utilizing recording metadata—like location and time—as additional signals during training. This approach leverages the correlations between species and their metadata to improve the model's representation, leading to better performance in diverse environments. The study demonstrates that integrating nine types of metadata across seventeen datasets significantly enhances the model's robustness and generalization in real-world monitoring scenarios.

### 4. Screening of Biosecurity Features in Metagenomic Data with Evo 2 Probes
**Authors:** Jeremy Guntoro, Alexander Dack, Dylan Danno, Michaela Jančovičová, Križan Jurinović, Vanessa Smilansky
**Link:** https://arxiv.org/abs/2607.14070v1
**Summary:** The paper addresses the challenge of biosecurity screening in metagenomic data, specifically focusing on detecting antimicrobial resistance (AMR) and bacterial virulence. The authors utilize Evo 2 genomic representation models to train linear and attention probes on the model's activations, achieving high discrimination rates for AMR detection (up to ROC-AUC 0.977) without fine-tuning. The results indicate that these probes can efficiently identify relevant biosecurity signals, making them a promising tool for rapid metagenomic biosurveillance.

### 5. Hindcast: Replaying Prediction Markets to Evaluate LLM Forecasters
**Authors:** Xiao Ye, Jacob Dineen, Evan Zhu, Shijie Lu, Kevin Song, Ben Zhou
**Link:** https://arxiv.org/abs/2607.14051v1
**Summary:** The paper addresses the issue of evaluating large language models (LLMs) in forecasting, which often suffer from leaks that allow models to access post-event information. The authors introduce "Hindcast," a method that evaluates LLMs by replaying prediction markets while using only historical data available at a specific past date, effectively closing these leaks. The key finding is that while retrieval helps models in cases where relevant discussions existed before the event, it can be detrimental when the available information was purely speculative.

### 6. Deep Interaction: An Efficient Human-AI Interaction Method for Large Reasoning Models
**Authors:** Hefeng Zhou, Jinxuan Zhang, Jiong Lou, Yuxin Liu, Chaochao Lu, Jingjing Qu, Jie Li
**Link:** https://arxiv.org/abs/2607.14049v1
**Summary:** The paper addresses the issue of correcting errors in large language models' Chain-of-Thought reasoning, which often results in repeated mistakes. The authors introduce a method called Deep Interaction, which allows users to directly edit responses to fix errors while maintaining correct reasoning steps. Their approach shows a significant improvement, achieving over 25% higher success in corrections and reducing token usage by about 40% on STEM-related tasks compared to existing methods.

### 7. Earthquaker-AI: A Retrieval-Augmented Generation Framework with Rubric-Based Assessment for Primary School Earthquake Education
**Authors:** Xanthi Kokkinou, Chaido Mizeli, Nafsika Koulaxidou, Marina Delianidi, Konstantinos Diamantaras
**Link:** https://arxiv.org/abs/2607.14046v1
**Summary:** The paper introduces Earthquaker-AI, an educational framework designed to improve earthquake preparedness among primary school students by combining robotics, AI, and rubric-based assessments. It enhances learning through interactive simulations using Lego WeDo2, while a conversational AI assistant provides guided learning and feedback tailored to students' cognitive levels. The key contribution is the effective integration of hands-on activities and reflective learning processes, which fosters technological literacy and self-regulation in emergency situations.

### 8. AI-accelerated End-to-End Framework for Rapid Professional Upskilling
**Authors:** Tam Nguyen, Hung Nguyen, Robert Ogburn
**Link:** https://arxiv.org/abs/2607.14044v1
**Summary:** This paper addresses the urgent need for effective reskilling and upskilling in the workplace, where the time to close skills gaps has significantly increased. The authors propose an AI-driven framework that enhances all stages of the learning process, from knowledge acquisition to assessment, and demonstrate its effectiveness through external validation and successful learner outcomes. Key results include approval from a professional board for a related program and the rapid success of learners in achieving certification in a complex area of AI.

### 9. Multi-Expert Routing for Multi-Domain Low-Resource OCR: A Manchu Case Study
**Authors:** Zhan Chen, Jiqiao Ma, Chih-wen Kuo
**Link:** https://arxiv.org/abs/2607.14041v1
**Summary:** The paper addresses the challenge of optical character recognition (OCR) for the historical Manchu language, which features diverse writing styles and limited labeled training data. It introduces a multi-expert system that utilizes multiple fine-tuned models as specialists, combined with a lightweight classifier to route pages according to their visual style. The key results show that this approach achieves a high level of accuracy, with 99.3% page-level domain accuracy and competitive character error rates across different writing styles.

### 10. Can an Old Dog Be Taught New Tricks? Taking LLMs Beyond Sentence Level Translation
**Authors:** Alaina Brandt
**Link:** https://arxiv.org/abs/2607.14040v1
**Summary:** This paper explores whether large language models (LLMs) can be employed for whole-document translation instead of the traditional sentence-by-sentence method, recognizing the importance of contextual and cultural differences in translation. The authors introduced PAT, a system that utilizes a comparable corpus to inform translations and enhance reformulation for specific Spanish-language contexts. The findings indicate that while LLMs can be adapted to produce more cohesive translations, challenges remain in achieving effective reformulations consistently.
