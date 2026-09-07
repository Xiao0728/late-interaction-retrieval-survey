# Late-Interaction Neural Retrieval: Survey and Resources

Companion resources for **[A Survey of Late-Interaction Neural Retrieval: Paradigms, Systems, and Research Frontiers](https://ssrn.com/abstract=7412000)**.

**Xiao Wang · Chuting Yu · Minghan Li · Binci Yang · Hang Li · Ben He**

[Read the preprint](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7412000) · [Citation](#citation) · [Software and benchmarks](docs/resources.md) · [Evaluation guide](docs/evaluation.md) · [Contribute](CONTRIBUTING.md)

Late interaction retains independently encoded local representations and performs fine-grained matching at scoring time. This survey organizes the field around the components of the retrieval pipeline, connecting model design to representation storage, candidate generation, final scoring, and deployment.

The collection contains **120 distinct bibliography records** from the August 2026 survey snapshot, including background work and software. Reading lists follow the actual numbered subsections; the same paper can appear wherever it is cited or discussed. See [coverage and provenance](docs/coverage.md) and the [citation audit](docs/citation-audit.md).

## Start Here

- **Understand the architecture:** ColBERT → ColBERTv2 → PLAID; read survey Sections 2–3 first.
- **Reduce index storage:** residual compression, token pruning, and pooling in Section 5.
- **Reduce query latency:** engines, proxies, and query pruning in Section 6; fused scoring kernels in Section 11.2.
- **Improve query representations:** ColBERT-PRF → CWPRF → PLAID-PRF in Section 8.
- **Explore visual or iterative retrieval:** ColPali and Baleen in Section 10.
- **Run comparable experiments:** [evaluation and reproducibility guide](docs/evaluation.md).

## Survey Navigation

| Survey section | Topic | Repository entry |
| --- | --- | --- |
| 1–2 | Background and boundary cases | [Reading list](#background-and-boundary-cases) |
| 3 | ColBERT Prototype | [Reading list](#section-3) |
| 4 | Scoring and Matching | [Reading list](#section-4) |
| 5 | Lightweight Document Representations | [Reading list](#section-5) |
| 6 | Efficient Retrieval and Execution | [Reading list](#section-6) |
| 7 | Sparse and Hybrid Retrieval | [Reading list](#section-7) |
| 8 | Query Enhancement and PRF | [Reading list](#section-8) |
| 9 | Training, Evaluation, and Infrastructure | [Reading list](#section-9) |
| 10 | Extensions and Applications | [Reading list](#section-10) |
| 11 | Research Frontiers and Evaluation Context | [Reading list](#section-11) |

## Scope

The survey uses four architectural criteria:

1. Query and document representations are computed independently before interaction.
2. Both sides retain multiple local units.
3. Relevance is estimated through lightweight post-encoding local interaction.
4. Retrieval-oriented systems support precomputed document representations and scalable search.

Reranking-only systems can relax the fourth criterion. COIL is lexically gated; XTR modifies retrieval and scoring together; query-conditioned visual scorers relax full document-side independence. Single-vector dense retrieval and pooled sparse retrieval are important comparison classes but are not automatically late-interaction systems.

Three distinctions guide this repository:

- **Scoring model versus execution procedure:** a faster engine need not change the relevance function.
- **Offline reduction versus online approximation:** pruning stored document units differs from pruning query-time work.
- **Candidate loss versus scoring error:** exact reranking cannot recover a relevant document absent from the candidate set.

## Reading Lists

Download [references.bib](references.bib) for the cited literature; use [survey.bib](survey.bib) to cite the survey itself. **Cited** denotes an explicit author–year citation (including table citations); **mentioned** denotes a named discussion whose citation is supplied elsewhere. Parent-section entries cover introductory text; subsections without a new citation or named reference are retained in the outline.

<a id="background-and-boundary-cases"></a>

### Background and boundary cases — §§1–2

Poly-encoders, ME-BERT, MVR, and MLR illustrate the wider multi-vector family. DPR, ANCE, and Contriever supply single-vector baselines. Their inclusion is background context, not a classification as core late interaction. Canonical methods cited in the introduction are listed separately below.

<a id="section-1"></a>

### §1 Introduction

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Argus-Retriever — Argus-Retriever: Vision-LLM Late-Interaction Retrieval with Region-Aware Query-Conditioned MoE for Visual Document Retrieval](https://arxiv.org/abs/2606.04300) | Abdallah et al., 2026 · `abdallah2026` | Cited |
| [ColPali — ColPali: Efficient Document Retrieval with Vision Language Models](https://openreview.net/forum?id=ogjBpZ8uSi) | Faysse et al., 2025 · `faysse2025` | Cited |
| [SPLATE — SPLATE: Sparse Late Interaction Retrieval](https://doi.org/10.1145/3626772.3657968) | Formal et al., 2024 · `formal2024` | Cited |
| [Hydra — Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model](https://arxiv.org/abs/2603.28554) | Georgiou, 2026 · `georgiou2026` | Cited |
| [Single-stage sparse coding — No More K-Means: Single-Stage Sparse Coding for Efficient Multi-Vector Retrieval](https://arxiv.org/abs/2605.30120) | Guo et al., 2026 · `guo2026` | Cited |
| [LEMUR — LEMUR: Learned Multi-Vector Retrieval](https://arxiv.org/abs/2601.21853) | Jääsaari et al., 2026 · `jaasaari2026` | Cited |
| [Voronoi pruning — A Voronoi Cell Formulation for Principled Token Pruning in Late-Interaction Retrieval Models](https://doi.org/10.1145/3805712.3809726) | Kankanampati et al., 2026 · `kankanampati2026` | Cited |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Cited |
| [Signed MaxSim — Quantifying and Expanding the Theoretical Capacity of Late-Interaction Retrieval Models](https://arxiv.org/abs/2607.05803) | Killingback et al., 2026a / Killingback et al., 2026b · `killingback2026a` | Cited |
| [LITTA — LITTA: Late-Interaction and Test-Time Alignment for Visually-Grounded Multimodal Retrieval](https://arxiv.org/abs/2603.26683) | Kim, 2026 · `kim2026litta` | Cited |
| [Nemotron ColEmbed V2 — Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval](https://arxiv.org/abs/2602.03992) | Moreira et al., 2026 · `moreira2026` | Cited |
| [Flash-MaxSim — FLASH-MAXSIM: IO-Aware Fused Kernels for Late-Interaction Retrieval](https://arxiv.org/abs/2605.29517) | Pony et al., 2026a · `pony2026a` | Cited |
| [Col-Bandit — Col-Bandit: Zero-Shot Query-Time Pruning for Late-Interaction Retrieval](https://arxiv.org/abs/2602.02827) | Pony et al., 2026b · `pony2026b` | Cited |
| [Video-ColBERT — Video-colbert: Contextualized late interaction for text-to-video retrieval](https://openaccess.thecvf.com/content/CVPR2025/html/Reddy_Video-ColBERT_Contextualized_Late_Interaction_for_Text-to-Video_Retrieval_CVPR_2025_paper.html) | Reddy et al., 2025 · `reddy2025` | Cited |
| [PLAID — PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Santhanam et al., 2022a · `santhanam2022a` | Cited |
| [ColBERTv2 — ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Santhanam et al., 2022b · `santhanam2022b` | Cited |
| [TileMaxSim — TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization](https://arxiv.org/abs/2606.26439) | Sharma, 2026 · `sharma2026` | Cited |
| [LateOn / mLateOn — DenseOn with the LateOn: Fully Open Dense and Late-Interaction Models for Multilingual, Long-Context, and Code Search](https://arxiv.org/abs/2607.27178) | Sourty et al., 2026 · `sourty2026` | Cited |
| [GEM — GEM: A Native Graph-Based Index for Multi-Vector Retrieval](https://arxiv.org/abs/2603.20336) | Tian et al., 2026 · `tian2026` | Cited |
| [Early ColBERT-PRF — Pseudo-Relevance Feedback for Multiple Representation Dense Retrieval](https://doi.org/10.1145/3471158.3472250) | Wang et al., 2021 · `wang2021` | Cited |
| [ColBERT-PRF — ColBERT-PRF: Semantic Pseudo-Relevance Feedback for Dense Passage and Document Retrieval](https://doi.org/10.1145/3572405) | Wang et al., 2023b · `wang2023b` | Cited |

**Background and boundary cases**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Lir: The first workshop on late interaction and multi vector retrieval@ ecir 2026](https://doi.org/10.1007/978-3-032-21324-2_11) | Clavié et al., 2026 · `clavie2026` | Cited |
| [SPLADE: sparse lexical and expansion model for first stage ranking](https://doi.org/10.1145/3404835.3463098) | Formal et al., 2021a · `formal2021a` | Cited |
| [DPR — Dense passage retrieval for open-domain question answering](https://doi.org/10.18653/V1/2020.EMNLP-MAIN.550) | Karpukhin et al., 2020 · `karpukhin2020` | Cited |
| [Unsupervised dense retrieval with relevance-aware contrastive pre-training](https://aclanthology.org/2023.findings-acl.695/) | Lei et al., 2023 · `lei2023` | Cited |
| [Pretrained Transformers for Text Ranking: BERT and Beyond](https://doi.org/10.2200/S01123ED1V01Y202108HLT053) | Lin et al., 2021 · `lin2021book` | Cited |
| [ME-BERT — Sparse, dense, and attentional representations for text retrieval](https://arxiv.org/abs/2005.00181) | Luan et al., 2020 · `luan2020` | Cited |
| [CEDR: contextualized embeddings for document ranking](https://doi.org/10.1145/3331184.3331317) | MacAvaney et al., 2019 · `macavaney2019` | Cited |
| [Large dual encoders are generalizable retrievers](https://aclanthology.org/2022.emnlp-main.669/) | Ni et al., 2022 · `ni2022` | Cited |
| [Multi-Stage Document Ranking with BERT](https://arxiv.org/abs/1910.14424) | Nogueira et al., 2019 · `nogueira2019multi` | Cited |
| [Okapi at TREC-3](http://trec.nist.gov/pubs/trec3/papers/city.ps.gz) | Robertson et al., 1994 · `robertson1994` | Cited |
| [BEIR: A heterogenous benchmark for zero-shot evaluation of information retrieval models](https://arxiv.org/abs/2104.08663) | Thakur et al., 2021 · `thakur2021` | Cited |
| [Multi-view document representation learning for open-domain dense retrieval](https://aclanthology.org/2022.acl-long.414/) | Zhang et al., 2022 · `zhang2022` | Cited |

**Software and infrastructure**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [PyLate — Pylate: Flexible training and retrieval for late interaction models](https://arxiv.org/abs/2508.03555) | Chaffin and Sourty, 2025 · `chaffin2025` | Cited |

<a id="section-2"></a>

### §2 Defining Late Interaction

No additional explicit citation or identified named-paper discussion in this subsection; see the surrounding subsections.

<a id="section-2.1"></a>

#### §2.1 Formal definition and structural properties

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |

<a id="section-2.2"></a>

#### §2.2 Independent encoding and delayed matching

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Cited |

**Background and boundary cases**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [DPR — Dense passage retrieval for open-domain question answering](https://doi.org/10.18653/V1/2020.EMNLP-MAIN.550) | Karpukhin et al., 2020 · `karpukhin2020` | Cited |
| [CEDR: contextualized embeddings for document ranking](https://doi.org/10.1145/3331184.3331317) | MacAvaney et al., 2019 · `macavaney2019` | Cited |
| [Passage re-ranking with BERT](https://arxiv.org/abs/1901.04085) | Nogueira and Cho, 2019 · `nogueira2019mono` | Cited |
| [ANCE — Approximate nearest neighbor negative contrastive learning for dense text retrieval](https://openreview.net/forum?id=zeFrfgyZln) | Xiong et al., 2021 · `xiong2021` | Cited |

<a id="section-2.3"></a>

#### §2.3 Late interaction retrieval versus multi-vector retrieval

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Cited |
| [ALIGNER — Multi-vector retrieval as sparse alignment](https://arxiv.org/abs/2211.01267) | Qian et al., 2022 · `qian2022` | Cited |
| [PLAID — PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Santhanam et al., 2022a · `santhanam2022a` | Cited |
| [ColBERTv2 — ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Santhanam et al., 2022b · `santhanam2022b` | Cited |

**Background and boundary cases**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Lir: The first workshop on late interaction and multi vector retrieval@ ecir 2026](https://doi.org/10.1007/978-3-032-21324-2_11) | Clavié et al., 2026 · `clavie2026` | Cited |
| [Poly-encoders — Poly-encoders: Architectures and pre-training strategies for fast and accurate multi-sentence scoring](https://openreview.net/forum?id=SkxgnnNFvH) | Humeau et al., 2020 · `humeau2020` | Cited |
| [ME-BERT — Sparse, dense, and attentional representations for text retrieval](https://arxiv.org/abs/2005.00181) | Luan et al., 2020 · `luan2020` | Cited |
| [MVR — Improving document representations by generating pseudo query embeddings for dense retrieval](https://doi.org/10.18653/v1/2021.acl-long.392) | Tang et al., 2021 · `tang2021` | Cited |
| [MLR — Investigating multi-layer representations for dense passage retrieval](https://aclanthology.org/2025.findings-emnlp.1333/) | Xie and Lukasiewicz, 2025 · `xie2025` | Cited |

<a id="section-2.4"></a>

#### §2.4 MaxSim and its retrieval-theoretic interpretation

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [White-box analysis — A White Box Analysis of ColBERT](https://doi.org/10.1007/978-3-030-72240-1_23) | Formal et al., 2021b · `formal2021b` | Cited |
| [TRIAL — TRIAL: Token Relations and Importance Aware Late-Interaction for Accurate Text Retrieval](https://aclanthology.org/2025.emnlp-main.854/) | Kang et al., 2025 · `kang2025` | Cited |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Cited |
| [Token pruning study — A Study on Token Pruning for ColBERT](https://arxiv.org/abs/2112.06540) | Lassance et al., 2021 · `lassance2021` | Cited |
| [Learned token pruning — Learned Token Pruning in Contextualized Late Interaction over BERT (ColBERT)](https://doi.org/10.1145/3477495.3531835) | Lassance et al., 2022 · `lassance2022` | Cited |
| [Matching and pruning analysis — An Analysis on Matching Mechanisms and Token Pruning for Late-Interaction Models](https://doi.org/10.1145/3639818) | Liu et al., 2024 · `liu2024` | Cited |
| [ColBERTv2 — ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Santhanam et al., 2022b · `santhanam2022b` | Cited |
| [Dominance-based pruning — Towards Lossless Token Pruning in Late-Interaction Retrieval Models](https://doi.org/10.1145/3726302.3730100) | Zong and Piwowarski, 2025 · `zong2025` | Cited |

**Background and boundary cases**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Multi-view document representation learning for open-domain dense retrieval](https://aclanthology.org/2022.acl-long.414/) | Zhang et al., 2022 · `zhang2022` | Cited |

<a id="section-2.5"></a>

#### §2.5 Scope, boundaries, and edge cases

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ELK-Multi — Multi-Vector Biomedical Dense Retrieval with Knowledge-Enhanced Entity-Type Clustering](https://doi.org/10.1145/3785368) | Deng et al., 2026 · `deng2026` | Cited |
| [SPLATE — SPLATE: Sparse Late Interaction Retrieval](https://doi.org/10.1145/3626772.3657968) | Formal et al., 2024 · `formal2024` | Cited |
| [COIL — COIL: Revisit Exact Lexical Match in Information Retrieval with Contextualized Inverted List](https://aclanthology.org/2021.naacl-main.241/) | Gao et al., 2021 · `gao2021` | Cited |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Cited |
| [Learned token pruning — Learned Token Pruning in Contextualized Late Interaction over BERT (ColBERT)](https://doi.org/10.1145/3477495.3531835) | Lassance et al., 2022 · `lassance2022` | Cited |
| [XTR — Rethinking the Role of Token Retrieval in Multi-Vector Retrieval](https://papers.nips.cc/paper_files/paper/2023/hash/31d997278ee9069d6721bc194174bb4c-Abstract-Conference.html) | Lee et al., 2023 · `lee2023` | Cited |
| [SLIM — SLIM: Sparsified Late Interaction for Multi-Vector Retrieval with Inverted Indexes](https://doi.org/10.1145/3539618.3591977) | Li et al., 2023a · `li2023a` | Cited |
| [ColBERT-XM — ColBERT-XM: A Modular Multi-Vector Representation Model for Zero-Shot Multilingual Information Retrieval](https://aclanthology.org/2025.coling-main.295/) | Louis et al., 2025 · `louis2025` | Cited |
| [PLAID — PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Santhanam et al., 2022a · `santhanam2022a` | Cited |
| [ColBERTv2 — ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Santhanam et al., 2022b · `santhanam2022b` | Cited |

**Background and boundary cases**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [SPLADE: sparse lexical and expansion model for first stage ranking](https://doi.org/10.1145/3404835.3463098) | Formal et al., 2021a · `formal2021a` | Cited |
| [Contriever — Unsupervised dense information retrieval with contrastive learning](https://openreview.net/forum?id=jKN1pXi7b0) | Izacard et al., 2022 · `izacard2022` | Cited |
| [DPR — Dense passage retrieval for open-domain question answering](https://doi.org/10.18653/V1/2020.EMNLP-MAIN.550) | Karpukhin et al., 2020 · `karpukhin2020` | Cited |
| [A few brief notes on deepimpact, coil, and a conceptual framework for information retrieval techniques](https://arxiv.org/abs/2106.14807) | Lin and Ma, 2021 · `lin2021notes` | Cited |
| [CEDR: contextualized embeddings for document ranking](https://doi.org/10.1145/3331184.3331317) | MacAvaney et al., 2019 · `macavaney2019` | Cited |
| [The expando-mono-duo design pattern for text ranking with pretrained sequence-to-sequence models](https://arxiv.org/abs/2101.05667) | Pradeep et al., 2021 · `pradeep2021` | Cited |
| [Okapi at TREC-3](http://trec.nist.gov/pubs/trec3/papers/city.ps.gz) | Robertson et al., 1994 · `robertson1994` | Cited |
| [ANCE — Approximate nearest neighbor negative contrastive learning for dense text retrieval](https://openreview.net/forum?id=zeFrfgyZln) | Xiong et al., 2021 · `xiong2021` | Cited |

<a id="section-3"></a>

### §3 ColBERT as a Prototype Late-Interaction Pipeline

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |

<a id="section-3.1"></a>

#### §3.1 The modular ColBERT prototype

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Cited |

<a id="section-3.2"></a>

#### §3.2 How later work modifies the prototype

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |

<a id="section-4"></a>

### §4 Scoring and Matching Variants

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |

<a id="section-4.1"></a>

#### §4.1 Learned Token Importance, Relations, and Signed Evidence

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT-AW — ColBERT-AW: Enhancing Late Interaction Retrieval with Attribute-Aware Query Token Weighting](https://doi.org/10.1109/ACCESS.2026.3672116) | An and Lee, 2026 · `an2026` | Cited |
| [token-importance — Incorporating token importance in multi-vector retrieval](https://doi.org/10.1609/aaai.v40i39.40566) | Archish et al., 2026 · `archish2026` | Cited |
| [TRIAL — TRIAL: Token Relations and Importance Aware Late-Interaction for Accurate Text Retrieval](https://aclanthology.org/2025.emnlp-main.854/) | Kang et al., 2025 · `kang2025` | Cited |
| [Signed MaxSim — Quantifying and Expanding the Theoretical Capacity of Late-Interaction Retrieval Models](https://arxiv.org/abs/2607.05803) | Killingback et al., 2026a / Killingback et al., 2026b · `killingback2026a` | Cited |
| [ColBERT-Att — ColBERT-Att: Late-Interaction Meets Attention for Enhanced Retrieval](https://arxiv.org/abs/2603.25248) | Patel and Dutta, 2026 · `patel2026` | Mentioned |

**Background and boundary cases**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Okapi at TREC-3](http://trec.nist.gov/pubs/trec3/papers/city.ps.gz) | Robertson et al., 1994 · `robertson1994` | Cited |
| [A probabilistic model of information retrieval: development and comparative experiments: Part 2](https://www.sciencedirect.com/science/article/abs/pii/S0306457300000169) | Spärck Jones et al., 2000 · `sparckjones2000` | Cited |

<a id="section-4.2"></a>

#### §4.2 Attention-Derived Match Weighting

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |
| [ColBERT-Att — ColBERT-Att: Late-Interaction Meets Attention for Enhanced Retrieval](https://arxiv.org/abs/2603.25248) | Patel and Dutta, 2026 · `patel2026` | Cited |

<a id="section-4.3"></a>

#### §4.3 Hard-Max Pooling and Smoother Alternatives

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Spike Hijacking — Spike Hijacking in Late-Interaction Retrieval](https://arxiv.org/abs/2604.05253) | Suresh et al., 2026 · `suresh2026` | Cited |

<a id="section-4.4"></a>

#### §4.4 Discussion and Takeaways

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [EXCISE — EXCISE: Query-Side Exclusion for Late-Interaction Retrieval](https://arxiv.org/abs/2608.05497) | Ali et al., 2026 · `ali2026` | Cited |
| [ColBERT-AW — ColBERT-AW: Enhancing Late Interaction Retrieval with Attribute-Aware Query Token Weighting](https://doi.org/10.1109/ACCESS.2026.3672116) | An and Lee, 2026 · `an2026` | Cited |
| [token-importance — Incorporating token importance in multi-vector retrieval](https://doi.org/10.1609/aaai.v40i39.40566) | Archish et al., 2026 · `archish2026` | Cited |
| [Late interaction dynamics — Working notes on late interaction dynamics: Analyzing targeted behaviors of late interaction models](https://arxiv.org/abs/2603.26259) | Edy et al., 2026 · `edy2026` | Cited |
| [TRIAL — TRIAL: Token Relations and Importance Aware Late-Interaction for Accurate Text Retrieval](https://aclanthology.org/2025.emnlp-main.854/) | Kang et al., 2025 · `kang2025` | Cited |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Cited |
| [Signed MaxSim — Quantifying and Expanding the Theoretical Capacity of Late-Interaction Retrieval Models](https://arxiv.org/abs/2607.05803) | Killingback et al., 2026a / Killingback et al., 2026b · `killingback2026a` | Cited |
| [ColBERT-Att — ColBERT-Att: Late-Interaction Meets Attention for Enhanced Retrieval](https://arxiv.org/abs/2603.25248) | Patel and Dutta, 2026 · `patel2026` | Cited |
| [Col-Bandit — Col-Bandit: Zero-Shot Query-Time Pruning for Late-Interaction Retrieval](https://arxiv.org/abs/2602.02827) | Pony et al., 2026b · `pony2026b` | Cited |
| [Spike Hijacking — Spike Hijacking in Late-Interaction Retrieval](https://arxiv.org/abs/2604.05253) | Suresh et al., 2026 · `suresh2026` | Cited |

<a id="section-5"></a>

### §5 Lightweight Document Representations

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |

<a id="section-5.1"></a>

#### §5.1 Residual and Code-Based Compression

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |
| [PLAID — PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Santhanam et al., 2022a · `santhanam2022a` | Cited |
| [ColBERTv2 — ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Santhanam et al., 2022b · `santhanam2022b` | Cited |
| [ColBERTSaR — ColBERTSaR: Sparsified ColBERT Index via Product Quantization](https://arxiv.org/abs/2606.05568) | Yang et al., 2026c · `yang2026c` | Cited |
| [Contextual Quantization — Compact Token Representations with Contextual Quantization for Efficient Document Re-ranking](https://aclanthology.org/2022.acl-long.51/) | Yang et al., 2022 · `yang2022` | Cited |

<a id="section-5.2"></a>

#### §5.2 Dimensionality Reduction

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [colberter — Introducing neural bag of whole-words with colberter: Contextualized late interactions using enhanced reduction](https://doi.org/10.1145/3511808.3557367) | Hofstätter et al., 2022 · `hofstatter2022` | Cited |
| [Jina-ColBERT-v2 — Jina-colbert-v2: A general-purpose multilingual late interaction retriever](https://aclanthology.org/2024.mrl-1.11/) | Jha et al., 2024 · `jha2024` | Cited |

<a id="section-5.3"></a>

#### §5.3 Reducing the Number or Granularity of Local Units

No additional explicit citation or identified named-paper discussion in this subsection; see the surrounding subsections.

<a id="section-5.3.1"></a>

#### §5.3.1 Heuristic and Learned Document-Token Pruning

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Static pruning — Static Pruning for Multi-Representation Dense Retrieval](https://doi.org/10.1145/3573128.3604896) | Acquavia et al., 2023 · `acquavia2023` | Cited |
| [LeapMV — Token pruning optimization for efficient multi-vector dense retrieval](https://doi.org/10.1007/978-3-031-88708-6_7) | He et al., 2025 · `he2025` | Cited |
| [Voronoi pruning — A Voronoi Cell Formulation for Principled Token Pruning in Late-Interaction Retrieval Models](https://doi.org/10.1145/3805712.3809726) | Kankanampati et al., 2026 · `kankanampati2026` | Cited |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |
| [Token pruning study — A Study on Token Pruning for ColBERT](https://arxiv.org/abs/2112.06540) | Lassance et al., 2021 · `lassance2021` | Cited |
| [Learned token pruning — Learned Token Pruning in Contextualized Late Interaction over BERT (ColBERT)](https://doi.org/10.1145/3477495.3531835) | Lassance et al., 2022 · `lassance2022` | Cited |
| [Matching and pruning analysis — An Analysis on Matching Mechanisms and Token Pruning for Late-Interaction Models](https://doi.org/10.1145/3639818) | Liu et al., 2024 · `liu2024` | Cited |
| [PLAID — PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Santhanam et al., 2022a · `santhanam2022a` | Mentioned |
| [ColBERTv2 — ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Santhanam et al., 2022b · `santhanam2022b` | Mentioned |
| [Pruning comparison — Comparing Token Pruning Approaches for Multi-Vector Retrieval](https://doi.org/10.1145/3805712.3808564) | Schlatt et al., 2026 · `schlatt2026` | Cited |

<a id="section-5.3.2"></a>

#### §5.3.2 Dominance-Based Near-Lossless Pruning

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |
| [Dominance-based pruning — Towards Lossless Token Pruning in Late-Interaction Retrieval Models](https://doi.org/10.1145/3726302.3730100) | Zong and Piwowarski, 2025 · `zong2025` | Cited |

<a id="section-5.3.3"></a>

#### §5.3.3 Pooling, Span Compression, and Fixed Budgets

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Token pooling — Reducing the Footprint of Multi-Vector Retrieval with Minimal Performance Impact via Token Pooling](https://arxiv.org/abs/2409.14683) | Clavié et al., 2024 · `clavie2024` | Cited |
| [ColPali — ColPali: Efficient Document Retrieval with Vision Language Models](https://openreview.net/forum?id=ogjBpZ8uSi) | Faysse et al., 2025 · `faysse2025` | Mentioned |
| [Compression comparison — A Brief Comparison of Training-Free Multi-Vector Sequence Compression Methods](https://arxiv.org/abs/2603.22434) | Jha et al., 2026b · `jha2026b` | Cited |
| [Learn to Pool — Learn to Pool: Lightweight Fine-Tuning for Flexible Multi-Vector Compression](https://arxiv.org/abs/2607.06036) | Josef, 2026 · `josef2026` | Cited |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |
| [Light-ColPali / Light-ColQwen2 — Towards storage-efficient visual document retrieval: An empirical study on reducing patch-level embeddings](https://aclanthology.org/2025.findings-acl.1003/) | Ma et al., 2025 · `ma2025` | Cited |
| [ConstBERT — Efficient constant-space multi-vector retrieval](https://doi.org/10.1007/978-3-031-88714-7_22) | MacAvaney et al., 2025 · `macavaney2025` | Cited |
| [MarginMerge — Coverage Matters: MarginMerge for Compressing Multi-Vector Visual Document Retrievers](https://arxiv.org/abs/2608.02969) | Mahdizadeh et al., 2026 · `mahdizadeh2026` | Cited |
| [SCV — SCV: Light and Effective Multi-Vector Retrieval with Sequence Compressive Vectors](https://aclanthology.org/2025.coling-industry.63/) | Park et al., 2025 · `park2025` | Cited |
| [Compression across modalities — Multi-Vector Index Compression in Any Modality](https://arxiv.org/abs/2602.21202) | Qin et al., 2026 · `qin2026` | Cited |
| [Prune-then-merge — Sculpting the Vector Space: Towards Efficient Multi-Vector Visual Document Retrieval via Prune-then-Merge Framework](https://aclanthology.org/2026.findings-acl.1247/) | Yan et al., 2026b · `yan2026b` | Cited |

<a id="section-5.4"></a>

#### §5.4 Reported Footprints and Comparison Limits

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [LeapMV — Token pruning optimization for efficient multi-vector dense retrieval](https://doi.org/10.1007/978-3-031-88708-6_7) | He et al., 2025 · `he2025` | Mentioned |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |
| [ConstBERT — Efficient constant-space multi-vector retrieval](https://doi.org/10.1007/978-3-031-88714-7_22) | MacAvaney et al., 2025 · `macavaney2025` | Mentioned |
| [SCV — SCV: Light and Effective Multi-Vector Retrieval with Sequence Compressive Vectors](https://aclanthology.org/2025.coling-industry.63/) | Park et al., 2025 · `park2025` | Mentioned |
| [ColBERTv2 — ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Santhanam et al., 2022b · `santhanam2022b` | Mentioned |

<a id="section-5.5"></a>

#### §5.5 Discussion and Takeaways

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [LeapMV — Token pruning optimization for efficient multi-vector dense retrieval](https://doi.org/10.1007/978-3-031-88708-6_7) | He et al., 2025 · `he2025` | Cited |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |
| [Matching and pruning analysis — An Analysis on Matching Mechanisms and Token Pruning for Late-Interaction Models](https://doi.org/10.1145/3639818) | Liu et al., 2024 · `liu2024` | Cited |
| [ConstBERT — Efficient constant-space multi-vector retrieval](https://doi.org/10.1007/978-3-031-88714-7_22) | MacAvaney et al., 2025 · `macavaney2025` | Cited |
| [SCV — SCV: Light and Effective Multi-Vector Retrieval with Sequence Compressive Vectors](https://aclanthology.org/2025.coling-industry.63/) | Park et al., 2025 · `park2025` | Cited |
| [PLAID — PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Santhanam et al., 2022a · `santhanam2022a` | Mentioned |
| [ColBERTv2 — ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Santhanam et al., 2022b · `santhanam2022b` | Cited |

<a id="section-6"></a>

### §6 Efficient Late-Interaction Retrieval

No additional explicit citation or identified named-paper discussion in this subsection; see the surrounding subsections.

<a id="section-6.1"></a>

#### §6.1 Online Retrieval Costs

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [IGP — Igp: Efficient multi-vector retrieval via proximity graph index](https://doi.org/10.1145/3726302.3730004) | Bian et al., 2025 · `bian2025` | Mentioned |
| [MUVERA — MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings](https://arxiv.org/abs/2405.19504) | Dhulipala et al., 2024 · `dhulipala2024` | Mentioned |
| [LEMUR — LEMUR: Learned Multi-Vector Retrieval](https://arxiv.org/abs/2601.21853) | Jääsaari et al., 2026 · `jaasaari2026` | Mentioned |
| [XTR — Rethinking the Role of Token Retrieval in Multi-Vector Retrieval](https://papers.nips.cc/paper_files/paper/2023/hash/31d997278ee9069d6721bc194174bb4c-Abstract-Conference.html) | Lee et al., 2023 · `lee2023` | Mentioned |
| [TACHIOM — Efficient Multivector Retrieval with Token-Aware Clustering and Hierarchical Indexing](https://arxiv.org/abs/2604.28142) | Martinico et al., 2026 · `martinico2026` | Mentioned |
| [EMVB — Efficient Multi-Vector Dense Retrieval Using Bit Vectors](https://arxiv.org/abs/2404.02805) | Nardini et al., 2024 · `nardini2024` | Mentioned |
| [SCV — SCV: Light and Effective Multi-Vector Retrieval with Sequence Compressive Vectors](https://aclanthology.org/2025.coling-industry.63/) | Park et al., 2025 · `park2025` | Mentioned |
| [Col-Bandit — Col-Bandit: Zero-Shot Query-Time Pruning for Late-Interaction Retrieval](https://arxiv.org/abs/2602.02827) | Pony et al., 2026b · `pony2026b` | Mentioned |
| [PLAID — PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Santhanam et al., 2022a · `santhanam2022a` | Mentioned |
| [WARP — WARP: An Efficient Engine for Multi-Vector Retrieval](https://doi.org/10.1145/3726302.3729904) | Scheerer et al., 2025 · `scheerer2025` | Mentioned |

<a id="section-6.2"></a>

#### §6.2 Multi-Stage Late-Interaction Retrieval

No additional explicit citation or identified named-paper discussion in this subsection; see the surrounding subsections.

<a id="section-6.2.1"></a>

#### §6.2.1 PLAID: Centroid Filtering and Residual Scoring

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [PLAID reproduction — A Reproducibility Study of PLAID](https://doi.org/10.1145/3626772.3657856) | MacAvaney and Tonellotto, 2024 · `macavaney2024` | Cited |
| [PLAID — PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Santhanam et al., 2022a · `santhanam2022a` | Cited |
| [ColBERTv2 — ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Santhanam et al., 2022b · `santhanam2022b` | Mentioned |

<a id="section-6.2.2"></a>

#### §6.2.2 Bit-Vector, Graph, and Coarse-to-Fine Retrieval

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [IGP — Igp: Efficient multi-vector retrieval via proximity graph index](https://doi.org/10.1145/3726302.3730004) | Bian et al., 2025 · `bian2025` | Cited |
| [TACHIOM — Efficient Multivector Retrieval with Token-Aware Clustering and Hierarchical Indexing](https://arxiv.org/abs/2604.28142) | Martinico et al., 2026 · `martinico2026` | Cited |
| [EMVB — Efficient Multi-Vector Dense Retrieval Using Bit Vectors](https://arxiv.org/abs/2404.02805) | Nardini et al., 2024 · `nardini2024` | Cited |
| [SCV — SCV: Light and Effective Multi-Vector Retrieval with Sequence Compressive Vectors](https://aclanthology.org/2025.coling-industry.63/) | Park et al., 2025 · `park2025` | Cited |
| [PLAID — PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Santhanam et al., 2022a · `santhanam2022a` | Mentioned |

<a id="section-6.3"></a>

#### §6.3 Vector-Set Indexes and Single-Vector Candidate Search

No additional explicit citation or identified named-paper discussion in this subsection; see the surrounding subsections.

<a id="section-6.3.1"></a>

#### §6.3.1 DESSERT: Retrieval Tables for Vector Sets

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [DESSERT — Dessert: an efficient algorithm for vector set search with vector set queries](https://arxiv.org/abs/2210.15748) | Engels et al., 2023 · `engels2023` | Cited |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |

<a id="section-6.3.2"></a>

#### §6.3.2 Native Multi-Vector Graph Indexes

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [GEM — GEM: A Native Graph-Based Index for Multi-Vector Retrieval](https://arxiv.org/abs/2603.20336) | Tian et al., 2026 · `tian2026` | Cited |
| [MV-HNSW — Unified and Efficient Approach for Multi-Vector Similarity Search](https://arxiv.org/abs/2604.02815) | Yang et al., 2026a · `yang2026a` | Cited |

<a id="section-6.3.3"></a>

#### §6.3.3 MUVERA and LEMUR: Single-Vector Candidate Search

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [MUVERA — MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings](https://arxiv.org/abs/2405.19504) | Dhulipala et al., 2024 · `dhulipala2024` | Cited |
| [LEMUR — LEMUR: Learned Multi-Vector Retrieval](https://arxiv.org/abs/2601.21853) | Jääsaari et al., 2026 · `jaasaari2026` | Cited |

<a id="section-6.4"></a>

#### §6.4 Retrieval and Scoring Co-Design

No additional explicit citation or identified named-paper discussion in this subsection; see the surrounding subsections.

<a id="section-6.4.1"></a>

#### §6.4.1 XTR: Training for Token Retrieval and Scoring

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [XTR replicability — A Replicability Study of XTR](https://arxiv.org/abs/2605.00646) | Jha et al., 2026a · `jha2026a` | Cited |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |
| [XTR — Rethinking the Role of Token Retrieval in Multi-Vector Retrieval](https://papers.nips.cc/paper_files/paper/2023/hash/31d997278ee9069d6721bc194174bb4c-Abstract-Conference.html) | Lee et al., 2023 · `lee2023` | Cited |

<a id="section-6.4.2"></a>

#### §6.4.2 WARP: Efficient XTR Retrieval

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [XTR — Rethinking the Role of Token Retrieval in Multi-Vector Retrieval](https://papers.nips.cc/paper_files/paper/2023/hash/31d997278ee9069d6721bc194174bb4c-Abstract-Conference.html) | Lee et al., 2023 · `lee2023` | Mentioned |
| [PLAID — PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Santhanam et al., 2022a · `santhanam2022a` | Mentioned |
| [WARP — WARP: An Efficient Engine for Multi-Vector Retrieval](https://doi.org/10.1145/3726302.3729904) | Scheerer et al., 2025 · `scheerer2025` | Cited |

<a id="section-6.5"></a>

#### §6.5 Query-Time Pruning and Adaptive Scoring

No additional explicit citation or identified named-paper discussion in this subsection; see the surrounding subsections.

<a id="section-6.5.1"></a>

#### §6.5.1 Query-Token Pruning

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Matching and pruning analysis — An Analysis on Matching Mechanisms and Token Pruning for Late-Interaction Models](https://doi.org/10.1145/3639818) | Liu et al., 2024 · `liu2024` | Cited |
| [Query embedding pruning — Query Embedding Pruning for Dense Retrieval](https://doi.org/10.1145/3459637.3482162) | Tonellotto and Macdonald, 2021 · `tonellotto2021` | Cited |

<a id="section-6.5.2"></a>

#### §6.5.2 Adaptive Score Evaluation

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Col-Bandit — Col-Bandit: Zero-Shot Query-Time Pruning for Late-Interaction Retrieval](https://arxiv.org/abs/2602.02827) | Pony et al., 2026b · `pony2026b` | Cited |

<a id="section-6.6"></a>

#### §6.6 Deployment Requirements and Evaluation

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [IGP — Igp: Efficient multi-vector retrieval via proximity graph index](https://doi.org/10.1145/3726302.3730004) | Bian et al., 2025 · `bian2025` | Mentioned |
| [MUVERA — MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings](https://arxiv.org/abs/2405.19504) | Dhulipala et al., 2024 · `dhulipala2024` | Mentioned |
| [DESSERT — Dessert: an efficient algorithm for vector set search with vector set queries](https://arxiv.org/abs/2210.15748) | Engels et al., 2023 · `engels2023` | Mentioned |
| [LEMUR — LEMUR: Learned Multi-Vector Retrieval](https://arxiv.org/abs/2601.21853) | Jääsaari et al., 2026 · `jaasaari2026` | Mentioned |
| [XTR — Rethinking the Role of Token Retrieval in Multi-Vector Retrieval](https://papers.nips.cc/paper_files/paper/2023/hash/31d997278ee9069d6721bc194174bb4c-Abstract-Conference.html) | Lee et al., 2023 · `lee2023` | Mentioned |
| [TACHIOM — Efficient Multivector Retrieval with Token-Aware Clustering and Hierarchical Indexing](https://arxiv.org/abs/2604.28142) | Martinico et al., 2026 · `martinico2026` | Mentioned |
| [EMVB — Efficient Multi-Vector Dense Retrieval Using Bit Vectors](https://arxiv.org/abs/2404.02805) | Nardini et al., 2024 · `nardini2024` | Mentioned |
| [SCV — SCV: Light and Effective Multi-Vector Retrieval with Sequence Compressive Vectors](https://aclanthology.org/2025.coling-industry.63/) | Park et al., 2025 · `park2025` | Mentioned |
| [Col-Bandit — Col-Bandit: Zero-Shot Query-Time Pruning for Late-Interaction Retrieval](https://arxiv.org/abs/2602.02827) | Pony et al., 2026b · `pony2026b` | Mentioned |
| [PLAID — PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Santhanam et al., 2022a · `santhanam2022a` | Mentioned |
| [ColBERTv2 — ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Santhanam et al., 2022b · `santhanam2022b` | Mentioned |
| [WARP — WARP: An Efficient Engine for Multi-Vector Retrieval](https://doi.org/10.1145/3726302.3729904) | Scheerer et al., 2025 · `scheerer2025` | Mentioned |
| [GEM — GEM: A Native Graph-Based Index for Multi-Vector Retrieval](https://arxiv.org/abs/2603.20336) | Tian et al., 2026 · `tian2026` | Mentioned |
| [MV-HNSW — Unified and Efficient Approach for Multi-Vector Similarity Search](https://arxiv.org/abs/2604.02815) | Yang et al., 2026a · `yang2026a` | Mentioned |

<a id="section-6.7"></a>

#### §6.7 Discussion and Takeaways

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [MUVERA — MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings](https://arxiv.org/abs/2405.19504) | Dhulipala et al., 2024 · `dhulipala2024` | Mentioned |
| [LEMUR — LEMUR: Learned Multi-Vector Retrieval](https://arxiv.org/abs/2601.21853) | Jääsaari et al., 2026 · `jaasaari2026` | Mentioned |
| [XTR — Rethinking the Role of Token Retrieval in Multi-Vector Retrieval](https://papers.nips.cc/paper_files/paper/2023/hash/31d997278ee9069d6721bc194174bb4c-Abstract-Conference.html) | Lee et al., 2023 · `lee2023` | Mentioned |
| [Col-Bandit — Col-Bandit: Zero-Shot Query-Time Pruning for Late-Interaction Retrieval](https://arxiv.org/abs/2602.02827) | Pony et al., 2026b · `pony2026b` | Mentioned |
| [WARP — WARP: An Efficient Engine for Multi-Vector Retrieval](https://doi.org/10.1145/3726302.3729904) | Scheerer et al., 2025 · `scheerer2025` | Mentioned |

<a id="section-7"></a>

### §7 Sparse and Hybrid Retrieval for Late Interaction

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |

<a id="section-7.1"></a>

#### §7.1 Scope and Boundaries of Sparse Late Interaction

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [SPLATE — SPLATE: Sparse Late Interaction Retrieval](https://doi.org/10.1145/3626772.3657968) | Formal et al., 2024 · `formal2024` | Mentioned |
| [COIL — COIL: Revisit Exact Lexical Match in Information Retrieval with Contextualized Inverted List](https://aclanthology.org/2021.naacl-main.241/) | Gao et al., 2021 · `gao2021` | Cited |
| [Single-stage sparse coding — No More K-Means: Single-Stage Sparse Coding for Efficient Multi-Vector Retrieval](https://arxiv.org/abs/2605.30120) | Guo et al., 2026 · `guo2026` | Cited |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |
| [SLIM — SLIM: Sparsified Late Interaction for Multi-Vector Retrieval with Inverted Indexes](https://doi.org/10.1145/3539618.3591977) | Li et al., 2023a · `li2023a` | Cited |
| [CITADEL — CITADEL: Conditional Token Interaction via Dynamic Lexical Routing for Efficient and Effective Multi-Vector Retrieval](https://aclanthology.org/2023.acl-long.663/) | Li et al., 2023b · `li2023b` | Cited |
| [ALIGNER — Multi-vector retrieval as sparse alignment](https://arxiv.org/abs/2211.01267) | Qian et al., 2022 · `qian2022` | Cited |
| [PLAID — PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Santhanam et al., 2022a · `santhanam2022a` | Mentioned |
| [ColBERTv2 — ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Santhanam et al., 2022b · `santhanam2022b` | Mentioned |
| [ColBERTSaR — ColBERTSaR: Sparsified ColBERT Index via Product Quantization](https://arxiv.org/abs/2606.05568) | Yang et al., 2026c · `yang2026c` | Cited |

**Background and boundary cases**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [SPLADE: sparse lexical and expansion model for first stage ranking](https://doi.org/10.1145/3404835.3463098) | Formal et al., 2021a · `formal2021a` | Cited |

<a id="section-7.2"></a>

#### §7.2 Sparse Candidate Retrieval and Hybrid Scoring

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [SPLATE — SPLATE: Sparse Late Interaction Retrieval](https://doi.org/10.1145/3626772.3657968) | Formal et al., 2024 · `formal2024` | Cited |
| [COIL — COIL: Revisit Exact Lexical Match in Information Retrieval with Contextualized Inverted List](https://aclanthology.org/2021.naacl-main.241/) | Gao et al., 2021 · `gao2021` | Mentioned |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |
| [SLIM — SLIM: Sparsified Late Interaction for Multi-Vector Retrieval with Inverted Indexes](https://doi.org/10.1145/3539618.3591977) | Li et al., 2023a · `li2023a` | Mentioned |
| [CITADEL — CITADEL: Conditional Token Interaction via Dynamic Lexical Routing for Efficient and Effective Multi-Vector Retrieval](https://aclanthology.org/2023.acl-long.663/) | Li et al., 2023b · `li2023b` | Mentioned |
| [ColBERTv2 — ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Santhanam et al., 2022b · `santhanam2022b` | Mentioned |
| [ColBERTSaR — ColBERTSaR: Sparsified ColBERT Index via Product Quantization](https://arxiv.org/abs/2606.05568) | Yang et al., 2026c · `yang2026c` | Mentioned |

**Background and boundary cases**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [M3-Embedding / BGE-M3 — M3-embedding: Multi-linguality, multi-functionality, multi-granularity text embeddings through self-knowledge distillation](https://doi.org/10.18653/V1/2024.FINDINGS-ACL.137) | Chen et al., 2024 · `chen2024` | Cited |

<a id="section-7.3"></a>

#### §7.3 Discussion and Takeaways

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [PLAID — PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Santhanam et al., 2022a · `santhanam2022a` | Mentioned |
| [ColBERTSaR — ColBERTSaR: Sparsified ColBERT Index via Product Quantization](https://arxiv.org/abs/2606.05568) | Yang et al., 2026c · `yang2026c` | Mentioned |

<a id="section-8"></a>

### §8 Query-Side Enhancement with Pseudo-Relevance Feedback

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [PLAID-PRF — PLAID-PRF: Pseudo-Relevance Feedback with Centroid-Like Tokens in PLAID](https://doi.org/10.1145/3805712.3809690) | Wang et al., 2026 · `wang2026` | Mentioned |
| [CWPRF — Effective Contrastive Weighting for Dense Query Expansion](https://aclanthology.org/2023.acl-long.710/) | Wang et al., 2023a · `wang2023a` | Mentioned |
| [ColBERT-PRF — ColBERT-PRF: Semantic Pseudo-Relevance Feedback for Dense Passage and Document Retrieval](https://doi.org/10.1145/3572405) | Wang et al., 2023b · `wang2023b` | Mentioned |

<a id="section-8.1"></a>

#### §8.1 A Framework for Token-Level Semantic Feedback

**Background and boundary cases**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [VectorPRF — Pseudo relevance feedback with deep language models and dense retrievers: Successes and pitfalls](https://arxiv.org/abs/2108.11044) | Li et al., 2021 · `li2021` | Cited |
| [ANCE-PRF — Improving query representations for dense retrieval with pseudo relevance feedback](https://doi.org/10.1145/3459637.3482124) | Yu et al., 2021 · `yu2021` | Cited |

<a id="section-8.2"></a>

#### §8.2 Pseudo-Relevance Feedback for Late Interaction

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [PLAID-PRF — PLAID-PRF: Pseudo-Relevance Feedback with Centroid-Like Tokens in PLAID](https://doi.org/10.1145/3805712.3809690) | Wang et al., 2026 · `wang2026` | Mentioned |
| [CWPRF — Effective Contrastive Weighting for Dense Query Expansion](https://aclanthology.org/2023.acl-long.710/) | Wang et al., 2023a · `wang2023a` | Mentioned |
| [ColBERT-PRF — ColBERT-PRF: Semantic Pseudo-Relevance Feedback for Dense Passage and Document Retrieval](https://doi.org/10.1145/3572405) | Wang et al., 2023b · `wang2023b` | Mentioned |

<a id="section-8.2.1"></a>

#### §8.2.1 Runtime Clustering Feedback

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |
| [Early ColBERT-PRF — Pseudo-Relevance Feedback for Multiple Representation Dense Retrieval](https://doi.org/10.1145/3471158.3472250) | Wang et al., 2021 · `wang2021` | Cited |
| [ColBERT-PRF — ColBERT-PRF: Semantic Pseudo-Relevance Feedback for Dense Passage and Document Retrieval](https://doi.org/10.1145/3572405) | Wang et al., 2023b · `wang2023b` | Cited |

<a id="section-8.2.2"></a>

#### §8.2.2 Learned Feedback Weighting

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [CWPRF — Effective Contrastive Weighting for Dense Query Expansion](https://aclanthology.org/2023.acl-long.710/) | Wang et al., 2023a · `wang2023a` | Cited |
| [ColBERT-PRF — ColBERT-PRF: Semantic Pseudo-Relevance Feedback for Dense Passage and Document Retrieval](https://doi.org/10.1145/3572405) | Wang et al., 2023b · `wang2023b` | Mentioned |

<a id="section-8.2.3"></a>

#### §8.2.3 Index-Aware Feedback Selection

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [PLAID — PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Santhanam et al., 2022a · `santhanam2022a` | Mentioned |
| [ColBERTv2 — ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Santhanam et al., 2022b · `santhanam2022b` | Mentioned |
| [PLAID-PRF — PLAID-PRF: Pseudo-Relevance Feedback with Centroid-Like Tokens in PLAID](https://doi.org/10.1145/3805712.3809690) | Wang et al., 2026 · `wang2026` | Cited |
| [CWPRF — Effective Contrastive Weighting for Dense Query Expansion](https://aclanthology.org/2023.acl-long.710/) | Wang et al., 2023a · `wang2023a` | Cited |
| [ColBERT-PRF — ColBERT-PRF: Semantic Pseudo-Relevance Feedback for Dense Passage and Document Retrieval](https://doi.org/10.1145/3572405) | Wang et al., 2023b · `wang2023b` | Cited |

<a id="section-8.3"></a>

#### §8.3 Discussion and Takeaways

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [LITTA — LITTA: Late-Interaction and Test-Time Alignment for Visually-Grounded Multimodal Retrieval](https://arxiv.org/abs/2603.26683) | Kim, 2026 · `kim2026litta` | Cited |
| [PO / query decomposition — PO: Performance-Oriented Query Decomposer for Multi-Vector Retrieval](https://arxiv.org/abs/2505.19189) | Liu et al., 2025 · `liu2025` | Cited |

<a id="section-9"></a>

### §9 Training and Methodological Infrastructure

No additional explicit citation or identified named-paper discussion in this subsection; see the surrounding subsections.

<a id="section-9.1"></a>

#### §9.1 Training Late-Interaction Models

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |

<a id="section-9.1.1"></a>

#### §9.1.1 Supervised Training and Negative Sampling

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Cited |

<a id="section-9.1.2"></a>

#### §9.1.2 Distillation and Denoised Supervision

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |
| [ColBERTv2 — ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Santhanam et al., 2022b · `santhanam2022b` | Cited |

<a id="section-9.1.3"></a>

#### §9.1.3 Multi-Vector Pre-training and Model Adaptation

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT-Zero — ColBERT-Zero: To Pre-Train or Not to Pre-Train ColBERT Models?](https://arxiv.org/abs/2602.16609) | Chaffin et al., 2026 · `chaffin2026` | Cited |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |
| [XTR — Rethinking the Role of Token Retrieval in Multi-Vector Retrieval](https://papers.nips.cc/paper_files/paper/2023/hash/31d997278ee9069d6721bc194174bb4c-Abstract-Conference.html) | Lee et al., 2023 · `lee2023` | Mentioned |
| [LateOn / mLateOn — DenseOn with the LateOn: Fully Open Dense and Late-Interaction Models for Multilingual, Long-Context, and Code Search](https://arxiv.org/abs/2607.27178) | Sourty et al., 2026 · `sourty2026` | Cited |

<a id="section-9.2"></a>

#### §9.2 Reproducibility and Evaluation Protocols

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Cross-backend reproduction — Reproduction Beyond Benchmarks: ConstBERT and ColBERT-v2 Across Backends and Query Distributions](https://doi.org/10.1145/3805712.3808561) | Ghosh et al., 2026 · `ghosh2026` | Cited |
| [XTR replicability — A Replicability Study of XTR](https://arxiv.org/abs/2605.00646) | Jha et al., 2026a · `jha2026a` | Cited |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |
| [XTR — Rethinking the Role of Token Retrieval in Multi-Vector Retrieval](https://papers.nips.cc/paper_files/paper/2023/hash/31d997278ee9069d6721bc194174bb4c-Abstract-Conference.html) | Lee et al., 2023 · `lee2023` | Mentioned |
| [ConstBERT — Efficient constant-space multi-vector retrieval](https://doi.org/10.1007/978-3-031-88714-7_22) | MacAvaney et al., 2025 · `macavaney2025` | Mentioned |
| [PLAID reproduction — A Reproducibility Study of PLAID](https://doi.org/10.1145/3626772.3657856) | MacAvaney and Tonellotto, 2024 · `macavaney2024` | Cited |
| [PLAID — PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Santhanam et al., 2022a · `santhanam2022a` | Cited |
| [ColBERTv2 — ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Santhanam et al., 2022b · `santhanam2022b` | Mentioned |
| [WARP — WARP: An Efficient Engine for Multi-Vector Retrieval](https://doi.org/10.1145/3726302.3729904) | Scheerer et al., 2025 · `scheerer2025` | Mentioned |
| [Col⋆ — Reproducibility, Replicability, and Insights into Dense Multi-Representation Retrieval Models: from ColBERT to Col⋆](https://doi.org/10.1145/3539618.3591916) | Wang et al., 2023c · `wang2023c` | Cited |

<a id="section-9.3"></a>

#### §9.3 Software and Serving Infrastructure

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |
| [PLAID — PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Santhanam et al., 2022a · `santhanam2022a` | Cited |
| [WARP — WARP: An Efficient Engine for Multi-Vector Retrieval](https://doi.org/10.1145/3726302.3729904) | Scheerer et al., 2025 · `scheerer2025` | Cited |
| [RoutIR — RoutIR: Fast Serving of Retrieval Pipelines for Retrieval-Augmented Generation](https://arxiv.org/abs/2601.10644) | Yang et al., 2026b · `yang2026b` | Cited |

**Software and infrastructure**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Ragatouille: Simple colbert training and retrieval for rag](https://github.com/AnswerDotAI/RAGatouille) | Answer.AI, 2024 · `answerai2024` | Cited |
| [PyLate — Pylate: Flexible training and retrieval for late interaction models](https://arxiv.org/abs/2508.03555) | Chaffin and Sourty, 2025 · `chaffin2025` | Cited |
| [Pyterrier: Declarative experimentation in python from BM25 to dense retrieval](https://doi.org/10.1145/3459637.3482013) | Macdonald et al., 2021 · `macdonald2021` | Cited |
| [qdrant/qdrant: Qdrant vector database and vector search engine](https://github.com/qdrant/qdrant) | Qdrant Team, n.d. · `qdrantteamnd` | Cited |

<a id="section-9.4"></a>

#### §9.4 Diagnostics and Failure Analysis

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [beneath-mask — Beneath the [mask]: An analysis of structural query tokens in colbert](https://doi.org/10.1007/978-3-031-56063-7_35) | Giacalone et al., 2024 · `giacalone2024` | Cited |
| [ColBERTv2 — ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Santhanam et al., 2022b · `santhanam2022b` | Mentioned |
| [Spike Hijacking — Spike Hijacking in Late-Interaction Retrieval](https://arxiv.org/abs/2604.05253) | Suresh et al., 2026 · `suresh2026` | Cited |
| [NevIR — Nevir: Negation in neural information retrieval](https://aclanthology.org/2024.eacl-long.139/) | Weller et al., 2024 · `weller2024` | Cited |

<a id="section-9.5"></a>

#### §9.5 Interpretation of Local Evidence

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Counterfactual explanations — A Counterfactual Explanation Framework for Retrieval Models](https://arxiv.org/abs/2409.00860) | Chandna and Sen, 2024 · `chandna2024` | Cited |
| [White-box analysis — A White Box Analysis of ColBERT](https://doi.org/10.1007/978-3-030-72240-1_23) | Formal et al., 2021b · `formal2021b` | Cited |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |
| [Diagnosable ColBERT — Diagnosable ColBERT: Debugging Late-Interaction Retrieval Models Using a Learned Latent Space as Reference](https://arxiv.org/abs/2604.19566) | Remy, 2026 · `remy2026` | Cited |

<a id="section-9.6"></a>

#### §9.6 Discussion and Takeaways

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [PLAID — PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Santhanam et al., 2022a · `santhanam2022a` | Mentioned |

<a id="section-10"></a>

### §10 Extensions Beyond Standard Ad Hoc Text Retrieval

No additional explicit citation or identified named-paper discussion in this subsection; see the surrounding subsections.

<a id="section-10.1"></a>

#### §10.1 Multilingual and Cross-Lingual Retrieval

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [JaColBERTv2.5 — Jacolbertv2.5: Optimising multi-vector retrievers to create state-of-the-art japanese retrievers with constrained resources](https://www.jstage.jst.go.jp/article/jnlp/32/1/32_176/_article/-char/en/) | Clavié, 2025 · `clavie2025` | Cited |
| [Jina-ColBERT-v2 — Jina-colbert-v2: A general-purpose multilingual late interaction retriever](https://aclanthology.org/2024.mrl-1.11/) | Jha et al., 2024 · `jha2024` | Cited |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |
| [ColBERT-XM — ColBERT-XM: A Modular Multi-Vector Representation Model for Zero-Shot Multilingual Information Retrieval](https://aclanthology.org/2025.coling-main.295/) | Louis et al., 2025 · `louis2025` | Cited |
| [ColBERT-X — Transfer Learning Approaches for Building Cross-Language Dense Retrieval Models](https://doi.org/10.1007/978-3-030-99736-6_26) | Nair et al., 2022 · `nair2022` | Cited |
| [LateOn / mLateOn — DenseOn with the LateOn: Fully Open Dense and Late-Interaction Models for Multilingual, Long-Context, and Code Search](https://arxiv.org/abs/2607.27178) | Sourty et al., 2026 · `sourty2026` | Cited |

<a id="section-10.2"></a>

#### §10.2 Multimodal and Visually Rich Document Retrieval

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Argus-Retriever — Argus-Retriever: Vision-LLM Late-Interaction Retrieval with Region-Aware Query-Conditioned MoE for Visual Document Retrieval](https://arxiv.org/abs/2606.04300) | Abdallah et al., 2026 · `abdallah2026` | Cited |
| [ColPali — ColPali: Efficient Document Retrieval with Vision Language Models](https://openreview.net/forum?id=ogjBpZ8uSi) | Faysse et al., 2025 · `faysse2025` | Cited |
| [Hydra — Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model](https://arxiv.org/abs/2603.28554) | Georgiou, 2026 · `georgiou2026` | Cited |
| [LITTA — LITTA: Late-Interaction and Test-Time Alignment for Visually-Grounded Multimodal Retrieval](https://arxiv.org/abs/2603.26683) | Kim, 2026 · `kim2026litta` | Cited |
| [ColMate — ColMate: Contrastive Late Interaction and Masked Text for Multimodal Document Retrieval](https://aclanthology.org/2025.emnlp-industry.145/) | Masry et al., 2025 · `masry2025` | Cited |
| [Nemotron ColEmbed V2 — Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval](https://arxiv.org/abs/2602.03992) | Moreira et al., 2026 · `moreira2026` | Cited |
| [Video-ColBERT — Video-colbert: Contextualized late interaction for text-to-video retrieval](https://openaccess.thecvf.com/content/CVPR2025/html/Reddy_Video-ColBERT_Contextualized_Late_Interaction_for_Text-to-Video_Retrieval_CVPR_2025_paper.html) | Reddy et al., 2025 · `reddy2025` | Cited |
| [CLaMR — CLaMR: Contextualized Late-Interaction for Multimodal Content Retrieval](https://arxiv.org/abs/2506.06144) | Wan et al., 2025 · `wan2025` | Cited |
| [ColChunk — Visual Late Chunking: An Empirical Study of Contextual Chunking for Efficient Visual Document Retrieval](https://arxiv.org/abs/2604.10167) | Yan et al., 2026a · `yan2026a` | Cited |

**Background and boundary cases**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ViDoRe V3 — ViDoRe V3: A Comprehensive Evaluation of Retrieval Augmented Generation in Complex Real-World Scenarios](https://arxiv.org/abs/2601.08620) | Loison et al., 2026 · `loison2026` | Mentioned |

<a id="section-10.3"></a>

#### §10.3 Specialised Domains and Retrieval Capabilities

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ELK-Multi — Multi-Vector Biomedical Dense Retrieval with Knowledge-Enhanced Entity-Type Clustering](https://doi.org/10.1145/3785368) | Deng et al., 2026 · `deng2026` | Cited |
| [NumColBERT — NumColBERT: Non-Intrusive Numeracy Injection for Late-Interaction Retrieval Models](https://arxiv.org/abs/2605.10109) | Fujimaki and Kato, 2026 · `fujimaki2026` | Cited |
| [ColBERT — ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Khattab and Zaharia, 2020 · `khattab2020` | Mentioned |

<a id="section-10.4"></a>

#### §10.4 Iterative and Multi-Hop Retrieval

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Baleen / FLIPR — Baleen: Robust Multi-Hop Reasoning at Scale via Condensed Retrieval](https://arxiv.org/abs/2101.00436) | Khattab et al., 2021 · `khattab2021` | Cited |

<a id="section-10.5"></a>

#### §10.5 Discussion and Takeaways

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Argus-Retriever — Argus-Retriever: Vision-LLM Late-Interaction Retrieval with Region-Aware Query-Conditioned MoE for Visual Document Retrieval](https://arxiv.org/abs/2606.04300) | Abdallah et al., 2026 · `abdallah2026` | Cited |
| [JaColBERTv2.5 — Jacolbertv2.5: Optimising multi-vector retrievers to create state-of-the-art japanese retrievers with constrained resources](https://www.jstage.jst.go.jp/article/jnlp/32/1/32_176/_article/-char/en/) | Clavié, 2025 · `clavie2025` | Cited |
| [ELK-Multi — Multi-Vector Biomedical Dense Retrieval with Knowledge-Enhanced Entity-Type Clustering](https://doi.org/10.1145/3785368) | Deng et al., 2026 · `deng2026` | Cited |
| [ColPali — ColPali: Efficient Document Retrieval with Vision Language Models](https://openreview.net/forum?id=ogjBpZ8uSi) | Faysse et al., 2025 · `faysse2025` | Cited |
| [NumColBERT — NumColBERT: Non-Intrusive Numeracy Injection for Late-Interaction Retrieval Models](https://arxiv.org/abs/2605.10109) | Fujimaki and Kato, 2026 · `fujimaki2026` | Cited |
| [Hydra — Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model](https://arxiv.org/abs/2603.28554) | Georgiou, 2026 · `georgiou2026` | Cited |
| [Jina-ColBERT-v2 — Jina-colbert-v2: A general-purpose multilingual late interaction retriever](https://aclanthology.org/2024.mrl-1.11/) | Jha et al., 2024 · `jha2024` | Cited |
| [Baleen / FLIPR — Baleen: Robust Multi-Hop Reasoning at Scale via Condensed Retrieval](https://arxiv.org/abs/2101.00436) | Khattab et al., 2021 · `khattab2021` | Cited |
| [LITTA — LITTA: Late-Interaction and Test-Time Alignment for Visually-Grounded Multimodal Retrieval](https://arxiv.org/abs/2603.26683) | Kim, 2026 · `kim2026litta` | Cited |
| [ColBERT-XM — ColBERT-XM: A Modular Multi-Vector Representation Model for Zero-Shot Multilingual Information Retrieval](https://aclanthology.org/2025.coling-main.295/) | Louis et al., 2025 · `louis2025` | Cited |
| [ColMate — ColMate: Contrastive Late Interaction and Masked Text for Multimodal Document Retrieval](https://aclanthology.org/2025.emnlp-industry.145/) | Masry et al., 2025 · `masry2025` | Cited |
| [Nemotron ColEmbed V2 — Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval](https://arxiv.org/abs/2602.03992) | Moreira et al., 2026 · `moreira2026` | Cited |
| [ColBERT-X — Transfer Learning Approaches for Building Cross-Language Dense Retrieval Models](https://doi.org/10.1007/978-3-030-99736-6_26) | Nair et al., 2022 · `nair2022` | Cited |
| [Video-ColBERT — Video-colbert: Contextualized late interaction for text-to-video retrieval](https://openaccess.thecvf.com/content/CVPR2025/html/Reddy_Video-ColBERT_Contextualized_Late_Interaction_for_Text-to-Video_Retrieval_CVPR_2025_paper.html) | Reddy et al., 2025 · `reddy2025` | Cited |
| [LateOn / mLateOn — DenseOn with the LateOn: Fully Open Dense and Late-Interaction Models for Multilingual, Long-Context, and Code Search](https://arxiv.org/abs/2607.27178) | Sourty et al., 2026 · `sourty2026` | Cited |
| [CLaMR — CLaMR: Contextualized Late-Interaction for Multimodal Content Retrieval](https://arxiv.org/abs/2506.06144) | Wan et al., 2025 · `wan2025` | Cited |

**Background and boundary cases**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ViDoRe V3 — ViDoRe V3: A Comprehensive Evaluation of Retrieval Augmented Generation in Complex Real-World Scenarios](https://arxiv.org/abs/2601.08620) | Loison et al., 2026 · `loison2026` | Mentioned |

<a id="section-11"></a>

### §11 Open Challenges and Future Directions

No additional explicit citation or identified named-paper discussion in this subsection; see the surrounding subsections.

<a id="section-11.1"></a>

#### §11.1 Learning the Units of Interaction

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Argus-Retriever — Argus-Retriever: Vision-LLM Late-Interaction Retrieval with Region-Aware Query-Conditioned MoE for Visual Document Retrieval](https://arxiv.org/abs/2606.04300) | Abdallah et al., 2026 · `abdallah2026` | Cited |
| [SaMer — Do All Visual Tokens Matter Equally? Object-Evidence Preserving Token Merging for Vision-Language Retrieval](https://arxiv.org/abs/2607.04605) | Park et al., 2026 · `park2026` | Cited |
| [H+ Embedding — H+ Embedding: Harmonizing Global and Token-Level Retrieval with Context-Dependent Phrases](https://arxiv.org/abs/2608.00065) | Zhang et al., 2026 · `zhang2026` | Cited |

<a id="section-11.2"></a>

#### §11.2 Composable, Updatable, and Hardware-Aware Retrieval Infrastructure

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [MUVERA — MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings](https://arxiv.org/abs/2405.19504) | Dhulipala et al., 2024 · `dhulipala2024` | Cited |
| [SPLATE — SPLATE: Sparse Late Interaction Retrieval](https://doi.org/10.1145/3626772.3657968) | Formal et al., 2024 · `formal2024` | Cited |
| [Single-stage sparse coding — No More K-Means: Single-Stage Sparse Coding for Efficient Multi-Vector Retrieval](https://arxiv.org/abs/2605.30120) | Guo et al., 2026 · `guo2026` | Cited |
| [LEMUR — LEMUR: Learned Multi-Vector Retrieval](https://arxiv.org/abs/2601.21853) | Jääsaari et al., 2026 · `jaasaari2026` | Cited |
| [CITADEL — CITADEL: Conditional Token Interaction via Dynamic Lexical Routing for Efficient and Effective Multi-Vector Retrieval](https://aclanthology.org/2023.acl-long.663/) | Li et al., 2023b · `li2023b` | Cited |
| [Flash-MaxSim — FLASH-MAXSIM: IO-Aware Fused Kernels for Late-Interaction Retrieval](https://arxiv.org/abs/2605.29517) | Pony et al., 2026a · `pony2026a` | Cited |
| [TileMaxSim — TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization](https://arxiv.org/abs/2606.26439) | Sharma, 2026 · `sharma2026` | Cited |
| [GEM — GEM: A Native Graph-Based Index for Multi-Vector Retrieval](https://arxiv.org/abs/2603.20336) | Tian et al., 2026 · `tian2026` | Cited |
| [MV-HNSW — Unified and Efficient Approach for Multi-Vector Similarity Search](https://arxiv.org/abs/2604.02815) | Yang et al., 2026a · `yang2026a` | Cited |

<a id="section-11.3"></a>

#### §11.3 Risk-Aware and Query-Adaptive Late Interaction

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [HEAVEN / ViMDOC — Hybrid-vector retrieval for visually rich documents: Combining single-vector efficiency and multi-vector accuracy](https://aclanthology.org/2026.findings-acl.54/) | Kim et al., 2026 · `kim2026heaven` | Cited |
| [PO / query decomposition — PO: Performance-Oriented Query Decomposer for Multi-Vector Retrieval](https://arxiv.org/abs/2505.19189) | Liu et al., 2025 · `liu2025` | Cited |
| [Col-Bandit — Col-Bandit: Zero-Shot Query-Time Pruning for Late-Interaction Retrieval](https://arxiv.org/abs/2602.02827) | Pony et al., 2026b · `pony2026b` | Cited |
| [WARP — WARP: An Efficient Engine for Multi-Vector Retrieval](https://doi.org/10.1145/3726302.3729904) | Scheerer et al., 2025 · `scheerer2025` | Cited |

<a id="section-11.4"></a>

#### §11.4 Learning and Approximation with Explicit Preservation Targets

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [AGREE — Attention grounded enhancement for visual document retrieval](https://arxiv.org/abs/2511.13415) | Cui et al., 2025 · `cui2025` | Cited |
| [TRIAL — TRIAL: Token Relations and Importance Aware Late-Interaction for Accurate Text Retrieval](https://aclanthology.org/2025.emnlp-main.854/) | Kang et al., 2025 · `kang2025` | Cited |
| [Voronoi pruning — A Voronoi Cell Formulation for Principled Token Pruning in Late-Interaction Retrieval Models](https://doi.org/10.1145/3805712.3809726) | Kankanampati et al., 2026 · `kankanampati2026` | Cited |
| [Signed MaxSim — Quantifying and Expanding the Theoretical Capacity of Late-Interaction Retrieval Models](https://arxiv.org/abs/2607.05803) | Killingback et al., 2026a / Killingback et al., 2026b · `killingback2026a` | Cited |

<a id="section-11.5"></a>

#### §11.5 Stateful Late Interaction for RAG and Agentic Search

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Hydra — Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model](https://arxiv.org/abs/2603.28554) | Georgiou, 2026 · `georgiou2026` | Cited |
| [Baleen / FLIPR — Baleen: Robust Multi-Hop Reasoning at Scale via Condensed Retrieval](https://arxiv.org/abs/2101.00436) | Khattab et al., 2021 · `khattab2021` | Cited |

**Background and boundary cases**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [AgentIR — AgentIR: Reasoning-Aware Retrieval for Deep Research Agents](https://arxiv.org/abs/2603.04384) | Chen et al., 2026a · `chen2026a` | Cited |
| [Agentic-R — Agentic-R: Learning to Retrieve for Agentic Search](https://aclanthology.org/2026.findings-acl.785/) | Liu et al., 2026 · `liu2026` | Cited |

<a id="section-11.6"></a>

#### §11.6 Causal Diagnosis, Robustness, and Control of Local Evidence

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [Counterfactual explanations — A Counterfactual Explanation Framework for Retrieval Models](https://arxiv.org/abs/2409.00860) | Chandna and Sen, 2024 · `chandna2024` | Cited |
| [AGREE — Attention grounded enhancement for visual document retrieval](https://arxiv.org/abs/2511.13415) | Cui et al., 2025 · `cui2025` | Cited |
| [Spike Hijacking — Spike Hijacking in Late-Interaction Retrieval](https://arxiv.org/abs/2604.05253) | Suresh et al., 2026 · `suresh2026` | Cited |

<a id="section-11.7"></a>

#### §11.7 Evaluation under Heterogeneous and Changing Conditions

**Late-interaction methods, systems, analyses, and extensions**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [ColPali — ColPali: Efficient Document Retrieval with Vision Language Models](https://openreview.net/forum?id=ogjBpZ8uSi) | Faysse et al., 2025 · `faysse2025` | Cited |
| [NumColBERT — NumColBERT: Non-Intrusive Numeracy Injection for Late-Interaction Retrieval Models](https://arxiv.org/abs/2605.10109) | Fujimaki and Kato, 2026 · `fujimaki2026` | Cited |
| [HEAVEN / ViMDOC — Hybrid-vector retrieval for visually rich documents: Combining single-vector efficiency and multi-vector accuracy](https://aclanthology.org/2026.findings-acl.54/) | Kim et al., 2026 · `kim2026heaven` | Cited |
| [Light-ColPali / Light-ColQwen2 — Towards storage-efficient visual document retrieval: An empirical study on reducing patch-level embeddings](https://aclanthology.org/2025.findings-acl.1003/) | Ma et al., 2025 · `ma2025` | Cited |

**Background and boundary cases**

| Work / paper | Survey citation | Evidence |
| --- | --- | --- |
| [BrowseComp-Plus — BrowseComp-Plus: A Fair and Disentangled Evaluation Benchmark for Deep Search Agents](https://aclanthology.org/2026.acl-long.1023/) | Chen et al., 2026b · `chen2026b` | Cited |
| [ViDoRe V3 — ViDoRe V3: A Comprehensive Evaluation of Retrieval Augmented Generation in Complex Real-World Scenarios](https://arxiv.org/abs/2601.08620) | Loison et al., 2026 · `loison2026` | Cited |

## Citation

If the survey is useful to your work, please cite the paper. The entry below cites the preprint rather than a journal acceptance. When a version of record becomes available, prefer that version.

```bibtex
@misc{wang2026lateinteractionsurvey,
  title  = {A Survey of Late-Interaction Neural Retrieval:
            Paradigms, Systems, and Research Frontiers},
  author = {Wang, Xiao and Yu, Chuting and Li, Minghan and
            Yang, Binci and Li, Hang and He, Ben},
  year   = {2026},
  howpublished = {SSRN preprint},
  url    = {https://ssrn.com/abstract=7412000},
  note   = {SSRN abstract 7412000}
}
```

Download [survey.bib](survey.bib). GitHub's **Cite this repository** control uses [CITATION.cff](CITATION.cff) with the survey as the preferred citation.

## Updates and Contributions

The reading lists follow the survey's numbered subsections with many-to-many paper placement. Subsequent additions should identify whether they are already discussed in the survey or are post-survey updates. See [CONTRIBUTING.md](CONTRIBUTING.md) and [CHANGELOG.md](CHANGELOG.md).

Please cite individual papers when relying on their methods or findings. Linked papers, models, datasets, and software retain their respective authorship and licenses.
