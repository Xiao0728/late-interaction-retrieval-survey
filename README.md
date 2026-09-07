# Late-Interaction Neural Retrieval: Survey and Resources

Companion resources for **[A Survey of Late-Interaction Neural Retrieval: Paradigms, Systems, and Research Frontiers](https://ssrn.com/abstract=7412000)**.

**Xiao Wang · Chuting Yu · Minghan Li · Binci Yang · Hang Li · Ben He**

[Read the preprint](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7412000) · [Citation](#citation) · [Software and benchmarks](docs/resources.md) · [Evaluation guide](docs/evaluation.md) · [Contribute](CONTRIBUTING.md)

Late interaction retains independently encoded local representations and performs fine-grained matching at scoring time. This survey organizes the field around the components of the retrieval pipeline, connecting model design to representation storage, candidate generation, final scoring, and deployment.

The collection contains **120 distinct bibliography records** from the August 2026 survey snapshot, including background work and software. Papers are grouped by survey chapter; a work may appear in multiple relevant chapters. Background and boundary cases are collected at the end. See [coverage and provenance](docs/coverage.md).

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

Download [references.bib](references.bib) for the literature, or [survey.bib](survey.bib) to cite the survey.

<a id="section-3"></a>

### Section 3: ColBERT as a Prototype Late-Interaction Pipeline

| Work | Year / venue or version | Paper | Main contribution / relevance |
| --- | --- | --- | --- |
| ColBERT | 2020 · SIGIR | [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Independent token encoding and MaxSim establish the prototype pipeline. |

<a id="section-4"></a>

### Section 4: Scoring and Matching Variants

| Work | Year / venue or version | Paper | Main contribution / relevance |
| --- | --- | --- | --- |
| ColBERT | 2020 · SIGIR | [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Independent token encoding and MaxSim establish the prototype pipeline. |
| TRIAL | 2025 · EMNLP | [TRIAL: Token Relations and Importance Aware Late-Interaction for Accurate Text Retrieval](https://aclanthology.org/2025.emnlp-main.854/) | Adds token importance and relation-aware matching. |
| Col-Bandit | 2026 · arXiv | [Col-Bandit: Zero-Shot Query-Time Pruning for Late-Interaction Retrieval](https://arxiv.org/abs/2602.02827) | Adaptively allocates MaxSim evaluations during top-k reranking. |
| ColBERT-Att | 2026 · arXiv | [ColBERT-Att: Late-Interaction Meets Attention for Enhanced Retrieval](https://arxiv.org/abs/2603.25248) | Uses attention-derived weights for selected matches. |
| ColBERT-AW | 2026 · IEEE Access | [ColBERT-AW: Enhancing Late Interaction Retrieval with Attribute-Aware Query Token Weighting](https://doi.org/10.1109/ACCESS.2026.3672116) | Weights query-token contributions. |
| EXCISE | 2026 · arXiv | [EXCISE: Query-Side Exclusion for Late-Interaction Retrieval](https://arxiv.org/abs/2608.05497) | Diagnoses exclusion inversion; the remedy adds candidate-stage processing. |
| Late interaction dynamics | 2026 · LIR Workshop | [Working notes on late interaction dynamics: Analyzing targeted behaviors of late interaction models](https://arxiv.org/abs/2603.26259) | Analyzes length bias and similarities beyond the strongest token match. |
| Signed MaxSim | 2026 · arXiv | [Quantifying and Expanding the Theoretical Capacity of Late-Interaction Retrieval Models](https://arxiv.org/abs/2607.05803) | Studies representational capacity and introduces signed contributions. |
| Spike Hijacking | 2026 · arXiv / LIR Workshop | [Spike Hijacking in Late-Interaction Retrieval](https://arxiv.org/abs/2604.05253) | Examines hard-max concentration and alternative pooling rules. |
| Token importance | 2026 · AAAI | [Incorporating token importance in multi-vector retrieval](https://doi.org/10.1609/aaai.v40i39.40566) | Incorporates token importance into multi-vector retrieval. |

<a id="section-5"></a>

### Section 5: Lightweight Document Representations

| Work | Year / venue or version | Paper | Main contribution / relevance |
| --- | --- | --- | --- |
| ColBERT | 2020 · SIGIR | [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Independent token encoding and MaxSim establish the prototype pipeline. |
| Token pruning study | 2021 · arXiv | [A Study on Token Pruning for ColBERT](https://arxiv.org/abs/2112.06540) | Studies offline removal of document-token vectors. |
| ColBERTer | 2022 · CIKM | [Introducing neural bag of whole-words with colberter: Contextualized late interactions using enhanced reduction](https://doi.org/10.1145/3511808.3557367) | Combines whole-word representations, dimensionality reduction, and learned pruning. |
| ColBERTv2 | 2022 · NAACL | [ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Residual compression reduces vector storage; denoised supervision is a separate training contribution. |
| Contextual Quantization | 2022 · ACL | [Compact Token Representations with Contextual Quantization for Efficient Document Re-ranking](https://aclanthology.org/2022.acl-long.51/) | Compresses contextual document-token representations for reranking. |
| Learned token pruning | 2022 · SIGIR | [Learned Token Pruning in Contextualized Late Interaction over BERT (ColBERT)](https://doi.org/10.1145/3477495.3531835) | Learns document-token selection before indexing. |
| PLAID | 2022 · CIKM | [PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Prunes with centroid-level scores before residual reconstruction and final scoring. |
| Static pruning | 2023 · DocEng | [Static Pruning for Multi-Representation Dense Retrieval](https://doi.org/10.1145/3573128.3604896) | Transfers lexical importance estimates to offline embedding pruning. |
| Jina-ColBERT-v2 | 2024 · MRL Workshop | [Jina-colbert-v2: A general-purpose multilingual late interaction retriever](https://aclanthology.org/2024.mrl-1.11/) | Supports multilingual late interaction and reduced embedding dimensionality. |
| Matching and pruning analysis | 2024 · TOIS | [An Analysis on Matching Mechanisms and Token Pruning for Late-Interaction Models](https://doi.org/10.1145/3639818) | Studies document- and query-token pruning with different system effects. |
| Token pooling | 2024 · arXiv | [Reducing the Footprint of Multi-Vector Retrieval with Minimal Performance Impact via Token Pooling](https://arxiv.org/abs/2409.14683) | Merges groups of document vectors into pooled representatives. |
| ColPali | 2025 · ICLR | [ColPali: Efficient Document Retrieval with Vision Language Models](https://openreview.net/forum?id=ogjBpZ8uSi) | Matches query-token embeddings with visual document-page representations. |
| ConstBERT | 2025 · ECIR | [Efficient constant-space multi-vector retrieval](https://doi.org/10.1007/978-3-031-88714-7_22) | Uses a fixed vector budget for constant-space document representations. |
| Dominance-based pruning | 2025 · SIGIR | [Towards Lossless Token Pruning in Late-Interaction Retrieval Models](https://doi.org/10.1145/3726302.3730100) | Separates exact dominance conditions from approximate practical pruning. |
| LeapMV | 2025 · ECIR | [Token pruning optimization for efficient multi-vector dense retrieval](https://doi.org/10.1007/978-3-031-88708-6_7) | Optimizes token pruning for efficient multi-vector dense retrieval. |
| Light-ColPali / Light-ColQwen2 | 2025 · ACL Findings | [Towards storage-efficient visual document retrieval: An empirical study on reducing patch-level embeddings](https://aclanthology.org/2025.findings-acl.1003/) | Studies storage reduction through fewer patch-level embeddings. |
| SCV | 2025 · COLING Industry | [SCV: Light and Effective Multi-Vector Retrieval with Sequence Compressive Vectors](https://aclanthology.org/2025.coling-industry.63/) | Constructs span representations; also uses coarse-to-fine retrieval. |
| ColBERTSaR | 2026 · arXiv | [ColBERTSaR: Sparsified ColBERT Index via Product Quantization](https://arxiv.org/abs/2606.05568) | Uses residual-free codeword identifiers and inverted lists; also reduces storage. |
| Compression across modalities | 2026 · arXiv | [Multi-Vector Index Compression in Any Modality](https://arxiv.org/abs/2602.21202) | Examines compression across different multi-vector inputs. |
| Compression comparison | 2026 · arXiv | [A Brief Comparison of Training-Free Multi-Vector Sequence Compression Methods](https://arxiv.org/abs/2603.22434) | Compares training-free sequence compression methods. |
| Learn to Pool | 2026 · arXiv | [Learn to Pool: Lightweight Fine-Tuning for Flexible Multi-Vector Compression](https://arxiv.org/abs/2607.06036) | Learns pooling for flexible vector budgets. |
| MarginMerge | 2026 · arXiv | [Coverage Matters: MarginMerge for Compressing Multi-Vector Visual Document Retrievers](https://arxiv.org/abs/2608.02969) | Studies evidence coverage when compressing visual multi-vectors. |
| Prune-then-merge | 2026 · ACL Findings | [Sculpting the Vector Space: Towards Efficient Multi-Vector Visual Document Retrieval via Prune-then-Merge Framework](https://aclanthology.org/2026.findings-acl.1247/) | Combines visual-token pruning and merging. |
| Pruning comparison | 2026 · SIGIR | [Comparing Token Pruning Approaches for Multi-Vector Retrieval](https://doi.org/10.1145/3805712.3808564) | Compares pruning under a common evaluation setting. |
| Voronoi pruning | 2026 · SIGIR | [A Voronoi Cell Formulation for Principled Token Pruning in Late-Interaction Retrieval Models](https://doi.org/10.1145/3805712.3809726) | Uses document-vector geometry to reason about retained local evidence. |

<a id="section-6"></a>

### Section 6: Efficient Late-Interaction Retrieval

| Work | Year / venue or version | Paper | Main contribution / relevance |
| --- | --- | --- | --- |
| ColBERT | 2020 · SIGIR | [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Independent token encoding and MaxSim establish the prototype pipeline. |
| Query embedding pruning | 2021 · CIKM | [Query Embedding Pruning for Dense Retrieval](https://doi.org/10.1145/3459637.3482162) | Prunes query probes during candidate generation while retaining full-query final scoring. |
| ColBERTv2 | 2022 · NAACL | [ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Residual compression reduces vector storage; denoised supervision is a separate training contribution. |
| PLAID | 2022 · CIKM | [PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Prunes with centroid-level scores before residual reconstruction and final scoring. |
| DESSERT | 2023 · NeurIPS | [Dessert: an efficient algorithm for vector set search with vector set queries](https://arxiv.org/abs/2210.15748) | Uses retrieval tables for vector-set search. |
| XTR | 2023 · NeurIPS | [Rethinking the Role of Token Retrieval in Multi-Vector Retrieval](https://papers.nips.cc/paper_files/paper/2023/hash/31d997278ee9069d6721bc194174bb4c-Abstract-Conference.html) | Co-designs token retrieval, training, and missing-similarity scoring. |
| EMVB | 2024 · arXiv | [Efficient Multi-Vector Dense Retrieval Using Bit Vectors](https://arxiv.org/abs/2404.02805) | Uses bit-vector prefiltering and quantized, SIMD-oriented execution. |
| Matching and pruning analysis | 2024 · TOIS | [An Analysis on Matching Mechanisms and Token Pruning for Late-Interaction Models](https://doi.org/10.1145/3639818) | Studies document- and query-token pruning with different system effects. |
| MUVERA | 2024 · arXiv | [MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings](https://arxiv.org/abs/2405.19504) | Maps vector sets to fixed-dimensional proxies for candidate search. |
| PLAID reproduction | 2024 · SIGIR | [A Reproducibility Study of PLAID](https://doi.org/10.1145/3626772.3657856) | Examines implementation and configuration effects on retrieval trade-offs. |
| IGP | 2025 · SIGIR | [Igp: Efficient multi-vector retrieval via proximity graph index](https://doi.org/10.1145/3726302.3730004) | Uses a proximity graph for efficient multi-vector retrieval. |
| SCV | 2025 · COLING Industry | [SCV: Light and Effective Multi-Vector Retrieval with Sequence Compressive Vectors](https://aclanthology.org/2025.coling-industry.63/) | Constructs span representations; also uses coarse-to-fine retrieval. |
| WARP | 2025 · SIGIR | [WARP: An Efficient Engine for Multi-Vector Retrieval](https://doi.org/10.1145/3726302.3729904) | Accelerates XTR-trained retrieval with imputation and efficient score reduction. |
| Col-Bandit | 2026 · arXiv | [Col-Bandit: Zero-Shot Query-Time Pruning for Late-Interaction Retrieval](https://arxiv.org/abs/2602.02827) | Adaptively allocates MaxSim evaluations during top-k reranking. |
| GEM | 2026 · arXiv | [GEM: A Native Graph-Based Index for Multi-Vector Retrieval](https://arxiv.org/abs/2603.20336) | Constructs a native graph over vector sets. |
| LEMUR | 2026 · arXiv | [LEMUR: Learned Multi-Vector Retrieval](https://arxiv.org/abs/2601.21853) | Learns corpus-specific fixed-dimensional reductions. |
| MV-HNSW | 2026 · arXiv | [Unified and Efficient Approach for Multi-Vector Similarity Search](https://arxiv.org/abs/2604.02815) | Adapts hierarchical graph search to multi-vector objects. |
| TACHIOM | 2026 · arXiv | [Efficient Multivector Retrieval with Token-Aware Clustering and Hierarchical Indexing](https://arxiv.org/abs/2604.28142) | Combines token-aware clustering and hierarchical candidate search. |
| XTR replicability | 2026 · arXiv | [A Replicability Study of XTR](https://arxiv.org/abs/2605.00646) | Separates token-retrieval behavior from final effectiveness claims. |

<a id="section-7"></a>

### Section 7: Sparse and Hybrid Retrieval for Late Interaction

| Work | Year / venue or version | Paper | Main contribution / relevance |
| --- | --- | --- | --- |
| ColBERT | 2020 · SIGIR | [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Independent token encoding and MaxSim establish the prototype pipeline. |
| COIL | 2021 · NAACL | [COIL: Revisit Exact Lexical Match in Information Retrieval with Contextualized Inverted List](https://aclanthology.org/2021.naacl-main.241/) | Lexically gates contextual token matching; a boundary case in the survey. |
| ALIGNER | 2022 · arXiv | [Multi-vector retrieval as sparse alignment](https://arxiv.org/abs/2211.01267) | Formulates multi-vector retrieval as sparse alignment. |
| ColBERTv2 | 2022 · NAACL | [ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Residual compression reduces vector storage; denoised supervision is a separate training contribution. |
| PLAID | 2022 · CIKM | [PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Prunes with centroid-level scores before residual reconstruction and final scoring. |
| CITADEL | 2023 · ACL | [CITADEL: Conditional Token Interaction via Dynamic Lexical Routing for Efficient and Effective Multi-Vector Retrieval](https://aclanthology.org/2023.acl-long.663/) | Learns lexical routing for local token interactions. |
| SLIM | 2023 · SIGIR | [SLIM: Sparsified Late Interaction for Multi-Vector Retrieval with Inverted Indexes](https://doi.org/10.1145/3539618.3591977) | Uses sparse local representations and inverted-index-compatible retrieval. |
| SPLATE | 2024 · SIGIR | [SPLATE: Sparse Late Interaction Retrieval](https://doi.org/10.1145/3626772.3657968) | Learns sparse candidate retrieval over frozen ColBERTv2 features, followed by late-interaction reranking. |
| ColBERTSaR | 2026 · arXiv | [ColBERTSaR: Sparsified ColBERT Index via Product Quantization](https://arxiv.org/abs/2606.05568) | Uses residual-free codeword identifiers and inverted lists; also reduces storage. |
| Single-stage sparse coding | 2026 · arXiv | [No More K-Means: Single-Stage Sparse Coding for Efficient Multi-Vector Retrieval](https://arxiv.org/abs/2605.30120) | Uses sparse codes as the local retrieval substrate. |

<a id="section-8"></a>

### Section 8: Query-Side Enhancement with Pseudo-Relevance Feedback

| Work | Year / venue or version | Paper | Main contribution / relevance |
| --- | --- | --- | --- |
| ColBERT | 2020 · SIGIR | [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Independent token encoding and MaxSim establish the prototype pipeline. |
| Early ColBERT-PRF | 2021 · ICTIR | [Pseudo-Relevance Feedback for Multiple Representation Dense Retrieval](https://doi.org/10.1145/3471158.3472250) | Introduces feedback expansion in the multi-vector representation space. |
| ColBERTv2 | 2022 · NAACL | [ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Residual compression reduces vector storage; denoised supervision is a separate training contribution. |
| PLAID | 2022 · CIKM | [PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Prunes with centroid-level scores before residual reconstruction and final scoring. |
| ColBERT-PRF | 2023 · TWeb | [ColBERT-PRF: Semantic Pseudo-Relevance Feedback for Dense Passage and Document Retrieval](https://doi.org/10.1145/3572405) | Clusters feedback embeddings and selects semantic query expansions. |
| CWPRF | 2023 · ACL | [Effective Contrastive Weighting for Dense Query Expansion](https://aclanthology.org/2023.acl-long.710/) | Learns the usefulness of contextual feedback embeddings. |
| PO / query decomposition | 2025 · ICML | [PO: Performance-Oriented Query Decomposer for Multi-Vector Retrieval](https://arxiv.org/abs/2505.19189) | Optimizes query decomposition for retrieval performance. |
| LITTA | 2026 · arXiv | [LITTA: Late-Interaction and Test-Time Alignment for Visually-Grounded Multimodal Retrieval](https://arxiv.org/abs/2603.26683) | Generates query variants and fuses rankings with a fixed page index. |
| PLAID-PRF | 2026 · SIGIR | [PLAID-PRF: Pseudo-Relevance Feedback with Centroid-Like Tokens in PLAID](https://doi.org/10.1145/3805712.3809690) | Reuses index centroids for feedback expansion. |

<a id="section-9"></a>

### Section 9: Training and Methodological Infrastructure

| Work | Year / venue or version | Paper | Main contribution / relevance |
| --- | --- | --- | --- |
| Qdrant | n.d. · Software | [qdrant/qdrant: Qdrant vector database and vector search engine](https://github.com/qdrant/qdrant) | Provides vector database infrastructure with multi-vector search support. |
| ColBERT | 2020 · SIGIR | [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Independent token encoding and MaxSim establish the prototype pipeline. |
| PyTerrier | 2021 · CIKM | [Pyterrier: Declarative experimentation in python from BM25 to dense retrieval](https://doi.org/10.1145/3459637.3482013) | Supports declarative retrieval experiments and pipeline evaluation. |
| White-box analysis | 2021 · ECIR | [A White Box Analysis of ColBERT](https://doi.org/10.1007/978-3-030-72240-1_23) | Examines lexical and semantic contributions to local matching. |
| ColBERTv2 | 2022 · NAACL | [ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Residual compression reduces vector storage; denoised supervision is a separate training contribution. |
| PLAID | 2022 · CIKM | [PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Prunes with centroid-level scores before residual reconstruction and final scoring. |
| Col⋆ | 2023 · SIGIR | [Reproducibility, Replicability, and Insights into Dense Multi-Representation Retrieval Models: from ColBERT to Col⋆](https://doi.org/10.1145/3539618.3591916) | Studies reproducibility and replicability of dense multi-representation retrieval. |
| XTR | 2023 · NeurIPS | [Rethinking the Role of Token Retrieval in Multi-Vector Retrieval](https://papers.nips.cc/paper_files/paper/2023/hash/31d997278ee9069d6721bc194174bb4c-Abstract-Conference.html) | Co-designs token retrieval, training, and missing-similarity scoring. |
| Beneath [MASK] | 2024 · ECIR | [Beneath the [mask]: An analysis of structural query tokens in colbert](https://doi.org/10.1007/978-3-031-56063-7_35) | Analyzes the role of structural query tokens in ColBERT. |
| Counterfactual explanations | 2024 · arXiv | [A Counterfactual Explanation Framework for Retrieval Models](https://arxiv.org/abs/2409.00860) | Provides a diagnostic perspective on retrieval decisions. |
| NevIR | 2024 · EACL | [Nevir: Negation in neural information retrieval](https://aclanthology.org/2024.eacl-long.139/) | Evaluates sensitivity to negation in neural retrieval. |
| PLAID reproduction | 2024 · SIGIR | [A Reproducibility Study of PLAID](https://doi.org/10.1145/3626772.3657856) | Examines implementation and configuration effects on retrieval trade-offs. |
| RAGatouille | 2024 · Software | [Ragatouille: Simple colbert training and retrieval for rag](https://github.com/AnswerDotAI/RAGatouille) | Provides accessible ColBERT training and retrieval tooling. |
| ConstBERT | 2025 · ECIR | [Efficient constant-space multi-vector retrieval](https://doi.org/10.1007/978-3-031-88714-7_22) | Uses a fixed vector budget for constant-space document representations. |
| PyLate | 2025 · CIKM | [Pylate: Flexible training and retrieval for late interaction models](https://arxiv.org/abs/2508.03555) | Supports flexible training and retrieval for late-interaction models. |
| WARP | 2025 · SIGIR | [WARP: An Efficient Engine for Multi-Vector Retrieval](https://doi.org/10.1145/3726302.3729904) | Accelerates XTR-trained retrieval with imputation and efficient score reduction. |
| ColBERT-Zero | 2026 · arXiv | [ColBERT-Zero: To Pre-Train or Not to Pre-Train ColBERT Models?](https://arxiv.org/abs/2602.16609) | Studies pre-training choices for late-interaction models. |
| Cross-backend reproduction | 2026 · SIGIR | [Reproduction Beyond Benchmarks: ConstBERT and ColBERT-v2 Across Backends and Query Distributions](https://doi.org/10.1145/3805712.3808561) | Examines reproducibility across retrieval backends and query distributions. |
| Diagnosable ColBERT | 2026 · arXiv | [Diagnosable ColBERT: Debugging Late-Interaction Retrieval Models Using a Learned Latent Space as Reference](https://arxiv.org/abs/2604.19566) | Uses a learned reference space for diagnostic interpretation. |
| LateOn / mLateOn | 2026 · arXiv | [DenseOn with the LateOn: Fully Open Dense and Late-Interaction Models for Multilingual, Long-Context, and Code Search](https://arxiv.org/abs/2607.27178) | Studies open training and transfer across languages and retrieval settings. |
| RoutIR | 2026 · arXiv | [RoutIR: Fast Serving of Retrieval Pipelines for Retrieval-Augmented Generation](https://arxiv.org/abs/2601.10644) | Addresses serving and execution of retrieval pipelines. |
| Spike Hijacking | 2026 · arXiv / LIR Workshop | [Spike Hijacking in Late-Interaction Retrieval](https://arxiv.org/abs/2604.05253) | Examines hard-max concentration and alternative pooling rules. |
| XTR replicability | 2026 · arXiv | [A Replicability Study of XTR](https://arxiv.org/abs/2605.00646) | Separates token-retrieval behavior from final effectiveness claims. |

<a id="section-10"></a>

### Section 10: Extensions Beyond Standard Ad Hoc Text Retrieval

| Work | Year / venue or version | Paper | Main contribution / relevance |
| --- | --- | --- | --- |
| ColBERT | 2020 · SIGIR | [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Independent token encoding and MaxSim establish the prototype pipeline. |
| Baleen / FLIPR | 2021 · NeurIPS | [Baleen: Robust Multi-Hop Reasoning at Scale via Condensed Retrieval](https://arxiv.org/abs/2101.00436) | Combines focused late interaction with iterative retrieval and fact condensation. |
| ColBERT-X | 2022 · ECIR | [Transfer Learning Approaches for Building Cross-Language Dense Retrieval Models](https://doi.org/10.1007/978-3-030-99736-6_26) | Studies cross-language transfer with multilingual encoders. |
| Jina-ColBERT-v2 | 2024 · MRL Workshop | [Jina-colbert-v2: A general-purpose multilingual late interaction retriever](https://aclanthology.org/2024.mrl-1.11/) | Supports multilingual late interaction and reduced embedding dimensionality. |
| CLaMR | 2025 · arXiv | [CLaMR: Contextualized Late-Interaction for Multimodal Content Retrieval](https://arxiv.org/abs/2506.06144) | Represents visual, speech, text, and metadata evidence for video retrieval. |
| ColBERT-XM | 2025 · COLING | [ColBERT-XM: A Modular Multi-Vector Representation Model for Zero-Shot Multilingual Information Retrieval](https://aclanthology.org/2025.coling-main.295/) | Uses modular language adaptation for multilingual retrieval. |
| ColMate | 2025 · EMNLP Industry | [ColMate: Contrastive Late Interaction and Masked Text for Multimodal Document Retrieval](https://aclanthology.org/2025.emnlp-industry.145/) | Adds OCR-based pre-training and masked contrastive learning. |
| ColPali | 2025 · ICLR | [ColPali: Efficient Document Retrieval with Vision Language Models](https://openreview.net/forum?id=ogjBpZ8uSi) | Matches query-token embeddings with visual document-page representations. |
| JaColBERTv2.5 | 2025 · Journal of Natural Language Processing | [Jacolbertv2.5: Optimising multi-vector retrievers to create state-of-the-art japanese retrievers with constrained resources](https://www.jstage.jst.go.jp/article/jnlp/32/1/32_176/_article/-char/en/) | Studies training and inference improvements for Japanese multi-vector retrieval. |
| Video-ColBERT | 2025 · CVPR | [Video-colbert: Contextualized late interaction for text-to-video retrieval](https://openaccess.thecvf.com/content/CVPR2025/html/Reddy_Video-ColBERT_Contextualized_Late_Interaction_for_Text-to-Video_Retrieval_CVPR_2025_paper.html) | Extends contextualized late interaction to text-to-video retrieval. |
| Argus-Retriever | 2026 · arXiv | [Argus-Retriever: Vision-LLM Late-Interaction Retrieval with Region-Aware Query-Conditioned MoE for Visual Document Retrieval](https://arxiv.org/abs/2606.04300) | Refines cached document features conditioned on the query for shortlisted candidates. |
| ColChunk | 2026 · arXiv | [Visual Late Chunking: An Empirical Study of Contextual Chunking for Efficient Visual Document Retrieval](https://arxiv.org/abs/2604.10167) | Combines contextual patch clustering with a spatial prior. |
| ELK-Multi | 2026 · TKDD | [Multi-Vector Biomedical Dense Retrieval with Knowledge-Enhanced Entity-Type Clustering](https://doi.org/10.1145/3785368) | A neighboring multi-vector design organized around biomedical entity clusters. |
| Hydra | 2026 · arXiv | [Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model](https://arxiv.org/abs/2603.28554) | Shares a vision-language model between retrieval and generation modes. |
| LateOn / mLateOn | 2026 · arXiv | [DenseOn with the LateOn: Fully Open Dense and Late-Interaction Models for Multilingual, Long-Context, and Code Search](https://arxiv.org/abs/2607.27178) | Studies open training and transfer across languages and retrieval settings. |
| LITTA | 2026 · arXiv | [LITTA: Late-Interaction and Test-Time Alignment for Visually-Grounded Multimodal Retrieval](https://arxiv.org/abs/2603.26683) | Generates query variants and fuses rankings with a fixed page index. |
| Nemotron ColEmbed V2 | 2026 · arXiv | [Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval](https://arxiv.org/abs/2602.03992) | Scales visual late-interaction representation learning. |
| NumColBERT | 2026 · arXiv | [NumColBERT: Non-Intrusive Numeracy Injection for Late-Interaction Retrieval Models](https://arxiv.org/abs/2605.10109) | Adds query-side numerical gating while retaining the document index and MaxSim interface. |

<a id="section-11"></a>

### Section 11: Open Challenges and Future Directions

| Work | Year / venue or version | Paper | Main contribution / relevance |
| --- | --- | --- | --- |
| Baleen / FLIPR | 2021 · NeurIPS | [Baleen: Robust Multi-Hop Reasoning at Scale via Condensed Retrieval](https://arxiv.org/abs/2101.00436) | Combines focused late interaction with iterative retrieval and fact condensation. |
| CITADEL | 2023 · ACL | [CITADEL: Conditional Token Interaction via Dynamic Lexical Routing for Efficient and Effective Multi-Vector Retrieval](https://aclanthology.org/2023.acl-long.663/) | Learns lexical routing for local token interactions. |
| Counterfactual explanations | 2024 · arXiv | [A Counterfactual Explanation Framework for Retrieval Models](https://arxiv.org/abs/2409.00860) | Provides a diagnostic perspective on retrieval decisions. |
| MUVERA | 2024 · arXiv | [MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings](https://arxiv.org/abs/2405.19504) | Maps vector sets to fixed-dimensional proxies for candidate search. |
| SPLATE | 2024 · SIGIR | [SPLATE: Sparse Late Interaction Retrieval](https://doi.org/10.1145/3626772.3657968) | Learns sparse candidate retrieval over frozen ColBERTv2 features, followed by late-interaction reranking. |
| AGREE | 2025 · arXiv | [Attention grounded enhancement for visual document retrieval](https://arxiv.org/abs/2511.13415) | Uses attention-derived region signals for visual retrieval supervision. |
| ColPali | 2025 · ICLR | [ColPali: Efficient Document Retrieval with Vision Language Models](https://openreview.net/forum?id=ogjBpZ8uSi) | Matches query-token embeddings with visual document-page representations. |
| Light-ColPali / Light-ColQwen2 | 2025 · ACL Findings | [Towards storage-efficient visual document retrieval: An empirical study on reducing patch-level embeddings](https://aclanthology.org/2025.findings-acl.1003/) | Studies storage reduction through fewer patch-level embeddings. |
| PO / query decomposition | 2025 · ICML | [PO: Performance-Oriented Query Decomposer for Multi-Vector Retrieval](https://arxiv.org/abs/2505.19189) | Optimizes query decomposition for retrieval performance. |
| TRIAL | 2025 · EMNLP | [TRIAL: Token Relations and Importance Aware Late-Interaction for Accurate Text Retrieval](https://aclanthology.org/2025.emnlp-main.854/) | Adds token importance and relation-aware matching. |
| WARP | 2025 · SIGIR | [WARP: An Efficient Engine for Multi-Vector Retrieval](https://doi.org/10.1145/3726302.3729904) | Accelerates XTR-trained retrieval with imputation and efficient score reduction. |
| Argus-Retriever | 2026 · arXiv | [Argus-Retriever: Vision-LLM Late-Interaction Retrieval with Region-Aware Query-Conditioned MoE for Visual Document Retrieval](https://arxiv.org/abs/2606.04300) | Refines cached document features conditioned on the query for shortlisted candidates. |
| Col-Bandit | 2026 · arXiv | [Col-Bandit: Zero-Shot Query-Time Pruning for Late-Interaction Retrieval](https://arxiv.org/abs/2602.02827) | Adaptively allocates MaxSim evaluations during top-k reranking. |
| Flash-MaxSim | 2026 · arXiv | [FLASH-MAXSIM: IO-Aware Fused Kernels for Late-Interaction Retrieval](https://arxiv.org/abs/2605.29517) | Fuses scoring operations to reduce memory traffic. |
| GEM | 2026 · arXiv | [GEM: A Native Graph-Based Index for Multi-Vector Retrieval](https://arxiv.org/abs/2603.20336) | Constructs a native graph over vector sets. |
| H+ Embedding | 2026 · arXiv | [H+ Embedding: Harmonizing Global and Token-Level Retrieval with Context-Dependent Phrases](https://arxiv.org/abs/2608.00065) | Motivates learned interaction units beyond fixed token segmentation. |
| HEAVEN / ViMDOC | 2026 · ACL Findings | [Hybrid-vector retrieval for visually rich documents: Combining single-vector efficiency and multi-vector accuracy](https://aclanthology.org/2026.findings-acl.54/) | Combines single-vector efficiency with multi-vector matching for visually rich documents. |
| Hydra | 2026 · arXiv | [Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model](https://arxiv.org/abs/2603.28554) | Shares a vision-language model between retrieval and generation modes. |
| LEMUR | 2026 · arXiv | [LEMUR: Learned Multi-Vector Retrieval](https://arxiv.org/abs/2601.21853) | Learns corpus-specific fixed-dimensional reductions. |
| MV-HNSW | 2026 · arXiv | [Unified and Efficient Approach for Multi-Vector Similarity Search](https://arxiv.org/abs/2604.02815) | Adapts hierarchical graph search to multi-vector objects. |
| NumColBERT | 2026 · arXiv | [NumColBERT: Non-Intrusive Numeracy Injection for Late-Interaction Retrieval Models](https://arxiv.org/abs/2605.10109) | Adds query-side numerical gating while retaining the document index and MaxSim interface. |
| SaMer | 2026 · arXiv | [Do All Visual Tokens Matter Equally? Object-Evidence Preserving Token Merging for Vision-Language Retrieval](https://arxiv.org/abs/2607.04605) | Targets preservation of object-level visual evidence during merging. |
| Signed MaxSim | 2026 · arXiv | [Quantifying and Expanding the Theoretical Capacity of Late-Interaction Retrieval Models](https://arxiv.org/abs/2607.05803) | Studies representational capacity and introduces signed contributions. |
| Single-stage sparse coding | 2026 · arXiv | [No More K-Means: Single-Stage Sparse Coding for Efficient Multi-Vector Retrieval](https://arxiv.org/abs/2605.30120) | Uses sparse codes as the local retrieval substrate. |
| Spike Hijacking | 2026 · arXiv / LIR Workshop | [Spike Hijacking in Late-Interaction Retrieval](https://arxiv.org/abs/2604.05253) | Examines hard-max concentration and alternative pooling rules. |
| TileMaxSim | 2026 · arXiv | [TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization](https://arxiv.org/abs/2606.26439) | Uses tiled GPU scoring and fused quantization operations. |
| Voronoi pruning | 2026 · SIGIR | [A Voronoi Cell Formulation for Principled Token Pruning in Late-Interaction Retrieval Models](https://doi.org/10.1145/3805712.3809726) | Uses document-vector geometry to reason about retained local evidence. |

<a id="background-and-boundary-cases"></a>

### Background and Boundary Cases

These works provide background, wider multi-vector designs, comparison methods, and evaluation context. Poly-encoders, ME-BERT, MVR, and MLR illustrate the wider multi-vector family; DPR, ANCE, and Contriever are single-vector baselines. COIL and XTR remain in their substantive chapters because the survey discusses their modified forms of late interaction in detail.

| Work | Year / venue or version | Paper | Main contribution / relevance |
| --- | --- | --- | --- |
| Okapi / BM25 | 1994 · TREC | [Okapi at TREC-3](http://trec.nist.gov/pubs/trec3/papers/city.ps.gz) | Provides the classical lexical retrieval baseline. |
| Probabilistic retrieval model | 2000 · Information Processing & Management | [A probabilistic model of information retrieval: development and comparative experiments: Part 2](https://www.sciencedirect.com/science/article/abs/pii/S0306457300000169) | Provides the probabilistic lexical retrieval foundations. |
| CEDR | 2019 · SIGIR | [CEDR: contextualized embeddings for document ranking](https://doi.org/10.1145/3331184.3331317) | Provides a contextualized joint-encoding ranking comparison. |
| Multi-stage BERT ranking | 2019 · arXiv | [Multi-Stage Document Ranking with BERT](https://arxiv.org/abs/1910.14424) | Provides background on multi-stage neural ranking pipelines. |
| BERT passage reranking | 2019 · arXiv | [Passage re-ranking with BERT](https://arxiv.org/abs/1901.04085) | Provides a cross-encoder passage reranking comparison. |
| DPR | 2020 · EMNLP | [Dense passage retrieval for open-domain question answering](https://doi.org/10.18653/V1/2020.EMNLP-MAIN.550) | Provides a supervised single-vector dense passage retrieval baseline. |
| ME-BERT | 2020 · arXiv | [Sparse, dense, and attentional representations for text retrieval](https://arxiv.org/abs/2005.00181) | Uses a fixed number of document vectors as a wider multi-vector design. |
| Poly-encoders | 2020 · ICLR | [Poly-encoders: Architectures and pre-training strategies for fast and accurate multi-sentence scoring](https://openreview.net/forum?id=SkxgnnNFvH) | Uses learned attention codes as a boundary example of multi-vector representation. |
| DeepImpact / COIL conceptual notes | 2021 · arXiv | [A few brief notes on deepimpact, coil, and a conceptual framework for information retrieval techniques](https://arxiv.org/abs/2106.14807) | Clarifies relationships between contextualized lexical and other retrieval approaches. |
| ANCE | 2021 · ICLR | [Approximate nearest neighbor negative contrastive learning for dense text retrieval](https://openreview.net/forum?id=zeFrfgyZln) | Provides a single-vector baseline trained with approximate-neighbor hard negatives. |
| ANCE-PRF | 2021 · CIKM | [Improving query representations for dense retrieval with pseudo relevance feedback](https://doi.org/10.1145/3459637.3482124) | Studies pseudo-relevance feedback for single-vector dense retrieval. |
| BEIR | 2021 · arXiv | [BEIR: A heterogenous benchmark for zero-shot evaluation of information retrieval models](https://arxiv.org/abs/2104.08663) | Provides heterogeneous datasets for zero-shot retrieval evaluation. |
| MVR | 2021 · ACL | [Improving document representations by generating pseudo query embeddings for dense retrieval](https://doi.org/10.18653/v1/2021.acl-long.392) | Generates multiple pseudo-query embeddings to represent document relevance views. |
| Pretrained Transformers for Text Ranking | 2021 · Book | [Pretrained Transformers for Text Ranking: BERT and Beyond](https://doi.org/10.2200/S01123ED1V01Y202108HLT053) | Provides background on transformer-based ranking architectures. |
| SPLADE | 2021 · SIGIR | [SPLADE: sparse lexical and expansion model for first stage ranking](https://doi.org/10.1145/3404835.3463098) | Supplies a learned sparse lexical retrieval comparison. |
| Expando–Mono–Duo | 2021 · arXiv | [The expando-mono-duo design pattern for text ranking with pretrained sequence-to-sequence models](https://arxiv.org/abs/2101.05667) | Describes expansion and sequence-to-sequence reranking pipelines. |
| VectorPRF | 2021 · arXiv | [Pseudo relevance feedback with deep language models and dense retrievers: Successes and pitfalls](https://arxiv.org/abs/2108.11044) | Studies the benefits and pitfalls of feedback for dense retrievers. |
| Contriever | 2022 · TMLR | [Unsupervised dense information retrieval with contrastive learning](https://openreview.net/forum?id=jKN1pXi7b0) | Provides an unsupervised single-vector dense retrieval baseline. |
| Large dual encoders | 2022 · EMNLP | [Large dual encoders are generalizable retrievers](https://aclanthology.org/2022.emnlp-main.669/) | Studies generalization of single-vector dual-encoder retrieval. |
| Multi-view document representation | 2022 · ACL | [Multi-view document representation learning for open-domain dense retrieval](https://aclanthology.org/2022.acl-long.414/) | Learns multiple document views for open-domain dense retrieval. |
| MLR | 2023 · EMNLP Findings | [Investigating multi-layer representations for dense passage retrieval](https://aclanthology.org/2025.findings-emnlp.1333/) | Constructs document representations from multiple encoder layers. |
| Relevance-aware contrastive pre-training | 2023 · ACL Findings | [Unsupervised dense retrieval with relevance-aware contrastive pre-training](https://aclanthology.org/2023.findings-acl.695/) | Provides background on unsupervised dense retriever pre-training. |
| M3-Embedding / BGE-M3 | 2024 · ACL Findings | [M3-embedding: Multi-linguality, multi-functionality, multi-granularity text embeddings through self-knowledge distillation](https://doi.org/10.18653/V1/2024.FINDINGS-ACL.137) | Combines multilingual, dense, sparse, and multi-vector retrieval capabilities. |
| Agentic-R | 2026 · ACL Findings | [Agentic-R: Learning to Retrieve for Agentic Search](https://aclanthology.org/2026.findings-acl.785/) | Context for agent-retriever learning and downstream evaluation. |
| AgentIR | 2026 · arXiv | [AgentIR: Reasoning-Aware Retrieval for Deep Research Agents](https://arxiv.org/abs/2603.04384) | Context for reasoning-aware retrieval; not automatically a canonical late-interaction model. |
| BrowseComp-Plus | 2026 · ACL | [BrowseComp-Plus: A Fair and Disentangled Evaluation Benchmark for Deep Search Agents](https://aclanthology.org/2026.acl-long.1023/) | Context for evaluating retrieval separately from agent behavior. |
| LIR Workshop | 2026 · ECIR | [Lir: The first workshop on late interaction and multi vector retrieval@ ecir 2026](https://doi.org/10.1007/978-3-032-21324-2_11) | Provides context for the late-interaction and multi-vector retrieval research community. |
| ViDoRe V3 | 2026 · arXiv | [ViDoRe V3: A Comprehensive Evaluation of Retrieval Augmented Generation in Complex Real-World Scenarios](https://arxiv.org/abs/2601.08620) | Motivates realistic visual-document evaluation. |

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

The reading lists follow the survey's chapters, with background and boundary cases collected separately. Subsequent additions should identify whether they are already discussed in the survey or are post-survey updates. See [CONTRIBUTING.md](CONTRIBUTING.md) and [CHANGELOG.md](CHANGELOG.md).

Please cite individual papers when relying on their methods or findings. Linked papers, models, datasets, and software retain their respective authorship and licenses.
