---
## 2026-08-10

### 1. MirrorWorld: Taming Video Diffusion Models for Mirror Reflection Generation
**Authors:** Youjun Zhao, Alex Warren, Gary K. L. Tam, Rynson W. H. Lau
**Link:** https://arxiv.org/abs/2608.07463v1
**Summary:** The paper addresses the challenge of generating accurate mirror reflections in videos, which often struggle with consistency between the reflected content and the surrounding scene. The authors propose MirrorWorld, a framework that incorporates two key components: Semantic Relation Distillation to capture relationships between scene elements and mirror regions, and Geometric Transformation Alignment to manage the spatial arrangement of reflections. Experimental results demonstrate that MirrorWorld outperforms existing methods for generating mirror reflections in videos.

### 2. CreativeInstruct: Scalably Teaching LLMs to Balance Quality, Creativity, and Diversity
**Authors:** Ananya Sahu, Mohit Bansal, Elias Stengel-Eskin
**Link:** https://arxiv.org/abs/2608.07460v1
**Summary:** The paper addresses the issue of large language models (LLMs) producing less diverse and creative outputs after post-training, which negatively affects tasks that require creativity. To solve this, the authors propose CreativeInstruct, a novel instruction-tuning method that encourages creativity through the use of special markers, improving narrative diversity without compromising on quality. Key results show that models fine-tuned with CreativeInstruct are rated as more creative than their post-trained counterparts in 70.3% of cases and improve performance in reinforcement learning tasks significantly.

### 3. CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context RAG
**Authors:** Gyuwan Kim, Cheoneum Park, Tao Yang
**Link:** https://arxiv.org/abs/2608.07458v1
**Summary:** The paper presents CoinRAG, an approach designed to enhance the efficiency of Retrieval-Augmented Generation (RAG) models by reusing contextualized, fine-grained information nuggets rather than full chunks of retrieved data. By employing a two-stage retrieval process, CoinRAG assembles relevant semantic units into a compact representation, leading to significant reductions in operational costs and a 5.3% improvement in answer quality on multi-hop question answering tasks. This approach advances the state of the art in managing long contexts while maintaining high accuracy and low latency.

### 4. Interaction Creates Dynamical AI Behavior Absent in Isolation
**Authors:** Bella Xinrui Li, Frank Yingjie Huo, Neil F Johnson
**Link:** https://arxiv.org/abs/2608.07457v1
**Summary:** The paper explores how interactions between AI agents can lead to unexpected and new behavior patterns that wouldn't occur in isolation. By analyzing the dynamic responses of a "boss" AI that sends messages to a "subordinate" AI while ignoring its feedback, the authors demonstrate that the subordinate enters a unique behavioral state influenced by the boss, governed by principles from kinetic theory. The key finding is that the delivery of messages affects future AI interactions, leading to the emergence of complex behaviors that challenge traditional understanding.

### 5. Strategy-first synthesis planning for complex natural products
**Authors:** Daniel Armstrong, Xuan-Vu Nguyen, Octavian Susanu, Gabriel Gibberd, Théo A. Neukomm, Taddäus Strunden, Dan Forster, Morgane Delattre, Shawn Teh, Clément Rols, John Federice, Hayden Leatherwood, M. Lavelle Barnes, Maarten R. Dobbelaere, Peter Wipf, Jon T. Njardarson, Jieping Zhu, Philippe Schwaller
**Link:** https://arxiv.org/abs/2608.07454v1
**Summary:** The paper addresses the challenge of automating the synthesis planning for complex natural products, which often outstrip traditional tools due to their intricate structures. The authors introduce SynthEx, a framework based on large language models that generates diverse synthetic routes, evaluates them, and refines its designs, outperforming conventional catalog-based methods. Notably, expert chemists found its proposed routes comparable to human-designed syntheses, marking a significant advancement in the field.

### 6. SkillProx: Self-Evolving Agent Skills via Proximal Textual Gradient Descent
**Authors:** Mingxuan Zheng, Yujin Zhou, Chuxue Cao, Boqin Yin, Yuyao Zhang, Jiapeng Sun, Shuaishuai Gong, Sirui Han, Yike Guo
**Link:** https://arxiv.org/abs/2608.07449v1
**Summary:** The paper presents SkillProx, a framework designed to enhance the adaptability of LLM agents by improving their skill accumulation and refinement during recurring tasks. It introduces a method that combines diagnostic evaluation of task performance with a structured approach to refining and consolidating skills, resulting in a significant accuracy improvement of 3.0 percentage points over existing techniques. The approach uniquely incorporates a closed-loop feedback mechanism and utility-based skill management for more effective learning.

### 7. Taxonomy-Driven Analysis of Open-Source AI Risk Mitigation Tools
**Authors:** Afreen Alam, Evgenija Popchanovska, Ana Gjorgjevikj, Maryan Rizinski, Lubomir T. Chitkushev, Irena Vodenska, Dimitar Trajanov
**Link:** https://arxiv.org/abs/2608.07446v1
**Summary:** This paper addresses the challenge of effectively identifying and mitigating risks associated with the use of large language models (LLMs) in enterprise settings, where existing open-source tools are often misaligned with risk governance frameworks. The authors develop a structured protocol that maps 21 open-source AI risk mitigation tools to an established risk taxonomy, leveraging an LLM to analyze their capabilities. Key findings reveal that most tools focus on technical controls, leaving significant gaps in governance and regulatory areas, thus suggesting the need for a more integrated risk-mitigation strategy that combines tools with organizational processes.

### 8. RIS-Aided mmWave Localization Under Cross-Link Interference via Beam-Domain ML Fingerprinting
**Authors:** Md Tarek Hassan, Dmitry Zelenchuk, Muhammad Ali Babar Abbasi
**Link:** https://arxiv.org/abs/2608.07444v1
**Summary:** This paper addresses the challenge of accurately localizing user equipment (UE) in reconfigurable intelligent surface (RIS)-assisted millimeter-wave (mmWave) networks when direct communication links are unavailable, particularly in the presence of cross-link interference. The authors propose a beam-domain fingerprinting framework that uses signal-to-noise ratios (SNR) to estimate the UE's position without needing detailed channel information, and they evaluate several machine learning models to determine localization accuracy. Notably, their findings reveal that while the model can maintain decent performance under interference, angle estimation accuracy suffers significantly more than range estimation due to how location information is encoded.

### 9. Blast Radius
**Authors:** MY Pitsane, Hope Mogale
**Link:** https://arxiv.org/abs/2608.07440v1
**Summary:** The paper introduces Blast Radius, a memory management system that reduces the token consumption of language models by effectively managing and archiving unused context. The approach uses methods like NECROPHORESIS for reversible eviction and Recurring Dead Matter (RDM) to identify and discard redundant transcripts. Key findings show that Blast Radius reduces token usage by 17-26% and minimizes overflow while preserving the ability to recover archived information, enhancing the efficiency and sustainability of language models and agentic coding.

### 10. An Exploratory Evaluation of LLM-Assisted Rewriting of Moderate-Complexity Financial Sentences for DisCoCat-Based Sentiment Analysis
**Authors:** Brian Llinas, Nikos Chrisochoides
**Link:** https://arxiv.org/abs/2608.07439v1
**Summary:** This paper addresses the challenges of using the DisCoCat framework for analyzing financial sentiment in moderately complex sentences, which can be difficult for traditional parsing methods. The authors propose an approach that utilizes large language models (LLMs) to rewrite these sentences, simplifying them while preserving their meaning, leading to more efficient processing in quantum circuits. The key finding is that this LLM-assisted rewriting significantly reduces the complexity of the input sentences and improves sentiment analysis accuracy compared to the original approach, offering a promising direction for scalable quantum natural language processing in finance.
