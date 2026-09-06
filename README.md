# Late-Interaction Neural Retrieval: Survey and Resources

Companion resources for **[A Survey of Late-Interaction Neural Retrieval: Paradigms, Systems, and Research Frontiers](https://ssrn.com/abstract=7412000)**.

**Xiao Wang · Chuting Yu · Minghan Li · Binci Yang · Hang Li · Ben He**

[Read the preprint](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7412000) · [Citation](#citation) · [Software and benchmarks](docs/resources.md) · [Evaluation guide](docs/evaluation.md) · [Contribute](CONTRIBUTING.md)

Late interaction retains independently encoded local representations and performs fine-grained matching at scoring time. This survey organizes the field around the components of the retrieval pipeline, connecting model design to representation storage, candidate generation, final scoring, and deployment.

This initial collection contains **76 distinct linked research entries**, organized by their primary role in the survey. It is a curated starting collection, not the complete bibliography. A paper may affect several pipeline components; its primary placement is a reading aid, not an exclusive classification. Publication labels follow the surveyed reference version and may differ from a later version available at the link. See [coverage and provenance](docs/coverage.md).

## Start Here

- **Understand the architecture:** ColBERT → ColBERTv2 → PLAID; read survey Sections 2–3 first.
- **Reduce index storage:** residual compression, token pruning, and pooling in Section 5.
- **Reduce query latency:** engines, proxies, query pruning, and fused scoring in Section 6.
- **Improve query representations:** ColBERT-PRF → CWPRF → PLAID-PRF in Section 8.
- **Explore visual or iterative retrieval:** ColPali and Baleen in Section 10.
- **Run comparable experiments:** [evaluation and reproducibility guide](docs/evaluation.md).

## Survey Navigation

| Survey section | Topic | Repository entry |
| --- | --- | --- |
| 2 | Definition and boundaries | [Scope](#scope) |
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

<a id="section-3"></a>

### Section 3: ColBERT Prototype

Independent encoders, local representations, and delayed MaxSim provide the reference pipeline.

| Work | Year / venue or version | Paper | Main role |
| --- | --- | --- | --- |
| ColBERT | 2020 · SIGIR | [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://doi.org/10.1145/3397271.3401075) | Independent token encoding and MaxSim establish the prototype pipeline. |

<a id="section-4"></a>

### Section 4: Scoring and Matching

Methods here change how local evidence contributes to relevance. Adaptive execution of an unchanged scorer belongs in Section 6.

| Work | Year / venue or version | Paper | Main role |
| --- | --- | --- | --- |
| TRIAL | 2025 · EMNLP | [TRIAL: Token Relations and Importance Aware Late-Interaction for Accurate Text Retrieval](https://aclanthology.org/2025.emnlp-main.854/) | Adds token importance and relation-aware matching. |
| ColBERT-Att | 2026 · arXiv | [ColBERT-Att: Late-Interaction Meets Attention for Enhanced Retrieval](https://arxiv.org/abs/2603.25248) | Uses attention-derived weights for selected matches. |
| ColBERT-AW | 2026 · IEEE Access | [ColBERT-AW: Enhancing Late Interaction Retrieval with Attribute-Aware Query Token Weighting](https://doi.org/10.1109/ACCESS.2026.3672116) | Weights query-token contributions. |
| EXCISE | 2026 · arXiv | [EXCISE: Query-Side Exclusion for Late-Interaction Retrieval](https://arxiv.org/abs/2608.05497) | Diagnoses exclusion inversion; the remedy adds candidate-stage processing. |
| Signed MaxSim | 2026 · arXiv | [Quantifying and Expanding the Theoretical Capacity of Late-Interaction Retrieval Models](https://arxiv.org/abs/2607.05803) | Studies representational capacity and introduces signed contributions. |
| Spike Hijacking | 2026 · arXiv / LIR Workshop | [Spike Hijacking in Late-Interaction Retrieval](https://arxiv.org/abs/2604.05253) | Examines hard-max concentration and alternative pooling rules. |

<a id="section-5"></a>

### Section 5: Lightweight Document Representations

Offline compression, dimension reduction, pruning, and merging change what is stored before a query arrives. ColBERTv2 also contributes training methods; ColBERTer and SCV also affect retrieval.

| Work | Year / venue or version | Paper | Main role |
| --- | --- | --- | --- |
| Token pruning study | 2021 · arXiv | [A Study on Token Pruning for ColBERT](https://arxiv.org/abs/2112.06540) | Studies offline removal of document-token vectors. |
| ColBERTer | 2022 · CIKM | [Introducing Neural Bag of Whole-Words with ColBERTer](https://doi.org/10.1145/3511808.3557367) | Combines whole-word representations, low-dimensional vectors, and learned pruning. |
| ColBERTv2 | 2022 · NAACL | [ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://aclanthology.org/2022.naacl-main.272/) | Residual compression reduces vector storage; denoised supervision is a separate training contribution. |
| Contextual Quantization | 2022 · ACL | [Compact Token Representations with Contextual Quantization for Efficient Document Re-ranking](https://aclanthology.org/2022.acl-long.51/) | Compresses contextual document-token representations for reranking. |
| Learned token pruning | 2022 · SIGIR | [Learned Token Pruning in Contextualized Late Interaction over BERT (ColBERT)](https://doi.org/10.1145/3477495.3531835) | Learns document-token selection before indexing. |
| Static pruning | 2023 · DocEng | [Static Pruning for Multi-Representation Dense Retrieval](https://doi.org/10.1145/3573128.3604896) | Transfers lexical importance estimates to offline embedding pruning. |
| Token pooling | 2024 · arXiv | [Reducing the Footprint of Multi-Vector Retrieval with Minimal Performance Impact via Token Pooling](https://arxiv.org/abs/2409.14683) | Merges groups of document vectors into pooled representatives. |
| Dominance-based pruning | 2025 · SIGIR | [Towards Lossless Token Pruning in Late-Interaction Retrieval Models](https://doi.org/10.1145/3726302.3730100) | Separates exact dominance conditions from approximate practical pruning. |
| SCV | 2025 · COLING Industry | [SCV: Light and Effective Multi-Vector Retrieval with Sequence Compressive Vectors](https://aclanthology.org/2025.coling-industry.63/) | Constructs span representations; also uses coarse-to-fine retrieval. |
| ColChunk | 2026 · arXiv | [Visual Late Chunking: An Empirical Study of Contextual Chunking for Efficient Visual Document Retrieval](https://arxiv.org/abs/2604.10167) | Combines contextual patch clustering with a spatial prior. |
| Compression across modalities | 2026 · arXiv | [Multi-Vector Index Compression in Any Modality](https://arxiv.org/abs/2602.21202) | Examines compression across different multi-vector inputs. |
| Compression comparison | 2026 · arXiv | [A Brief Comparison of Training-Free Multi-Vector Sequence Compression Methods](https://arxiv.org/abs/2603.22434) | Compares training-free sequence compression methods. |
| Learn to Pool | 2026 · arXiv | [Learn to Pool: Lightweight Fine-Tuning for Flexible Multi-Vector Compression](https://arxiv.org/abs/2607.06036) | Learns pooling for flexible vector budgets. |
| MarginMerge | 2026 · arXiv | [Coverage Matters: MarginMerge for Compressing Multi-Vector Visual Document Retrievers](https://arxiv.org/abs/2608.02969) | Studies evidence coverage when compressing visual multi-vectors. |
| Prune-then-merge | 2026 · ACL Findings | [Sculpting the Vector Space: Towards Efficient Multi-Vector Visual Document Retrieval via Prune-then-Merge Framework](https://aclanthology.org/2026.findings-acl.1247/) | Combines visual-token pruning and merging. |
| SaMer | 2026 · arXiv | [Do All Visual Tokens Matter Equally? Object-Evidence Preserving Token Merging for Vision-Language Retrieval](https://arxiv.org/abs/2607.04605) | Targets preservation of object-level visual evidence during merging. |
| Voronoi pruning | 2026 · SIGIR | [A Voronoi Cell Formulation for Principled Token Pruning in Late-Interaction Retrieval Models](https://doi.org/10.1145/3805712.3809726) | Uses document-vector geometry to reason about retained local evidence. |

<a id="section-6"></a>

### Section 6: Efficient Retrieval and Execution

Candidate search, vector access, approximate scoring, and hardware execution are distinct interventions. Proxy search can recover original scores only within the candidate set when the required vectors are retained.

| Work | Year / venue or version | Paper | Main role |
| --- | --- | --- | --- |
| Query embedding pruning | 2021 · CIKM | [Query Embedding Pruning for Dense Retrieval](https://doi.org/10.1145/3459637.3482162) | Prunes query probes during candidate generation while retaining full-query final scoring. |
| PLAID | 2022 · CIKM | [PLAID: An Efficient Engine for Late Interaction Retrieval](https://doi.org/10.1145/3511808.3557325) | Prunes with centroid-level scores before residual reconstruction and final scoring. |
| XTR | 2023 · NeurIPS | [Rethinking the Role of Token Retrieval in Multi-Vector Retrieval](https://papers.nips.cc/paper_files/paper/2023/hash/31d997278ee9069d6721bc194174bb4c-Abstract-Conference.html) | Co-designs token retrieval, training, and missing-similarity scoring. |
| EMVB | 2024 · arXiv | [Efficient Multi-Vector Dense Retrieval Using Bit Vectors](https://arxiv.org/abs/2404.02805) | Uses bit-vector prefiltering and quantized, SIMD-oriented execution. |
| MUVERA | 2024 · arXiv | [MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings](https://arxiv.org/abs/2405.19504) | Maps vector sets to fixed-dimensional proxies for candidate search. |
| PO / query decomposition | 2025 · ICML | [PO: Performance-Oriented Query Decomposer for Multi-Vector Retrieval](https://arxiv.org/abs/2505.19189) | Optimizes query decomposition for retrieval performance. |
| WARP | 2025 · SIGIR | [WARP: An Efficient Engine for Multi-Vector Retrieval](https://doi.org/10.1145/3726302.3729904) | Accelerates XTR-trained retrieval with imputation and efficient score reduction. |
| Col-Bandit | 2026 · arXiv | [Col-Bandit: Zero-Shot Query-Time Pruning for Late-Interaction Retrieval](https://arxiv.org/abs/2602.02827) | Adaptively allocates MaxSim evaluations during top-k reranking. |
| Flash-MaxSim | 2026 · arXiv | [FLASH-MAXSIM: IO-Aware Fused Kernels for Late-Interaction Retrieval](https://arxiv.org/abs/2605.29517) | Fuses scoring operations to reduce memory traffic. |
| GEM | 2026 · arXiv | [GEM: A Native Graph-Based Index for Multi-Vector Retrieval](https://arxiv.org/abs/2603.20336) | Constructs a native graph over vector sets. |
| LEMUR | 2026 · arXiv | [LEMUR: Learned Multi-Vector Retrieval](https://arxiv.org/abs/2601.21853) | Learns corpus-specific fixed-dimensional reductions. |
| MV-HNSW | 2026 · arXiv | [Unified and Efficient Approach for Multi-Vector Similarity Search](https://arxiv.org/abs/2604.02815) | Adapts hierarchical graph search to multi-vector objects. |
| TileMaxSim | 2026 · arXiv | [TileMaxSim: IO-Aware GPU MaxSim Scoring with Dimension Tiling and Fused Product Quantization](https://arxiv.org/abs/2606.26439) | Uses tiled GPU scoring and fused quantization operations. |
| Token-aware hierarchical indexing | 2026 · arXiv | [Efficient Multivector Retrieval with Token-Aware Clustering and Hierarchical Indexing](https://arxiv.org/abs/2604.28142) | Combines token-aware clustering and hierarchical candidate search. |

<a id="section-7"></a>

### Section 7: Sparse and Hybrid Retrieval

Distinguish sparse local interaction, lexical routing, sparse candidate generation, and score fusion. SPLADE-like pooled sparse retrieval is a comparison class rather than canonical multi-vector late interaction.

| Work | Year / venue or version | Paper | Main role |
| --- | --- | --- | --- |
| COIL | 2021 · NAACL | [COIL: Revisit Exact Lexical Match in Information Retrieval with Contextualized Inverted List](https://aclanthology.org/2021.naacl-main.241/) | Lexically gates contextual token matching; a boundary case in the survey. |
| CITADEL | 2023 · ACL | [CITADEL: Conditional Token Interaction via Dynamic Lexical Routing for Efficient and Effective Multi-Vector Retrieval](https://aclanthology.org/2023.acl-long.663/) | Learns lexical routing for local token interactions. |
| SLIM | 2023 · SIGIR | [SLIM: Sparsified Late Interaction for Multi-Vector Retrieval with Inverted Indexes](https://doi.org/10.1145/3539618.3591977) | Uses sparse local representations and inverted-index-compatible retrieval. |
| SPLATE | 2024 · SIGIR | [SPLATE: Sparse Late Interaction Retrieval](https://doi.org/10.1145/3626772.3657968) | Learns sparse candidate retrieval over frozen ColBERTv2 features, followed by late-interaction reranking. |
| ColBERTSaR | 2026 · arXiv | [ColBERTSaR: Sparsified ColBERT Index via Product Quantization](https://arxiv.org/abs/2606.05568) | Uses residual-free codeword identifiers and inverted lists; also reduces storage. |
| Single-stage sparse coding | 2026 · arXiv | [No More K-Means: Single-Stage Sparse Coding for Efficient Multi-Vector Retrieval](https://arxiv.org/abs/2605.30120) | Uses sparse codes as the local retrieval substrate. |

<a id="section-8"></a>

### Section 8: Query Enhancement and PRF

Feedback expands or weights query-side evidence. Runtime clustering, learned feedback weighting, and index-aware expansion impose different online costs.

| Work | Year / venue or version | Paper | Main role |
| --- | --- | --- | --- |
| Early ColBERT-PRF | 2021 · ICTIR | [Pseudo-Relevance Feedback for Multiple Representation Dense Retrieval](https://doi.org/10.1145/3471158.3472250) | Introduces feedback expansion in the multi-vector representation space. |
| ColBERT-PRF | 2023 · TWeb | [ColBERT-PRF: Semantic Pseudo-Relevance Feedback for Dense Passage and Document Retrieval](https://doi.org/10.1145/3572405) | Clusters feedback embeddings and selects semantic query expansions. |
| CWPRF | 2023 · ACL | [Effective Contrastive Weighting for Dense Query Expansion](https://aclanthology.org/2023.acl-long.710/) | Learns the usefulness of contextual feedback embeddings. |
| PLAID-PRF | 2026 · SIGIR | [PLAID-PRF: Pseudo-Relevance Feedback with Centroid-Like Tokens in PLAID](https://doi.org/10.1145/3805712.3809690) | Reuses index centroids for feedback expansion. |

<a id="section-9"></a>

### Section 9: Training, Evaluation, and Infrastructure

Training, reproducibility, diagnostics, interpretation, and serving support the retrieval pipeline. ColBERTv2 is also a key training reference; multilingual training is cross-referenced in Section 10.

| Work | Year / venue or version | Paper | Main role |
| --- | --- | --- | --- |
| White-box analysis | 2021 · ECIR | [A White Box Analysis of ColBERT](https://doi.org/10.1007/978-3-030-72240-1_23) | Examines lexical and semantic contributions to local matching. |
| Counterfactual explanations | 2024 · arXiv | [A Counterfactual Explanation Framework for Retrieval Models](https://arxiv.org/abs/2409.00860) | Provides a diagnostic perspective on retrieval decisions. |
| Matching and pruning analysis | 2024 · TOIS | [An Analysis on Matching Mechanisms and Token Pruning for Late-Interaction Models](https://doi.org/10.1145/3639818) | Studies document- and query-token pruning with different system effects. |
| PLAID reproduction | 2024 · SIGIR | [A Reproducibility Study of PLAID](https://doi.org/10.1145/3626772.3657856) | Examines implementation and configuration effects on retrieval trade-offs. |
| ColBERT-Zero | 2026 · arXiv | [ColBERT-Zero: To Pre-Train or Not to Pre-Train ColBERT Models?](https://arxiv.org/abs/2602.16609) | Studies pre-training choices for late-interaction models. |
| Cross-backend reproduction | 2026 · SIGIR | [Reproduction Beyond Benchmarks: ConstBERT and ColBERT-v2 Across Backends and Query Distributions](https://doi.org/10.1145/3805712.3808561) | Examines reproducibility across retrieval backends and query distributions. |
| Diagnosable ColBERT | 2026 · arXiv | [Diagnosable ColBERT: Debugging Late-Interaction Retrieval Models Using a Learned Latent Space as Reference](https://arxiv.org/abs/2604.19566) | Uses a learned reference space for diagnostic interpretation. |
| Pruning comparison | 2026 · SIGIR | [Comparing Token Pruning Approaches for Multi-Vector Retrieval](https://doi.org/10.1145/3805712.3808564) | Compares pruning under a common evaluation setting. |
| RoutIR | 2026 · arXiv | [RoutIR: Fast Serving of Retrieval Pipelines for Retrieval-Augmented Generation](https://arxiv.org/abs/2601.10644) | Addresses serving and execution of retrieval pipelines. |
| XTR replicability | 2026 · arXiv | [A Replicability Study of XTR](https://arxiv.org/abs/2605.00646) | Separates token-retrieval behavior from final effectiveness claims. |

<a id="section-10"></a>

### Section 10: Extensions and Applications

Multilingual, visual, domain-specific, and iterative retrieval relax different assumptions. Query-conditioned candidate scorers and neighboring multi-vector designs are labeled explicitly.

| Work | Year / venue or version | Paper | Main role |
| --- | --- | --- | --- |
| Baleen / FLIPR | 2021 · NeurIPS | [Baleen: Robust Multi-Hop Reasoning at Scale via Condensed Retrieval](https://arxiv.org/abs/2101.00436) | Combines focused late interaction with iterative retrieval and fact condensation. |
| ColBERT-X | 2022 · ECIR | [Transfer Learning Approaches for Building Cross-Language Dense Retrieval Models](https://doi.org/10.1007/978-3-030-99736-6_26) | Studies cross-language transfer with multilingual encoders. |
| CLaMR | 2025 · arXiv | [CLaMR: Contextualized Late-Interaction for Multimodal Content Retrieval](https://arxiv.org/abs/2506.06144) | Represents visual, speech, text, and metadata evidence for video retrieval. |
| ColBERT-XM | 2025 · COLING | [ColBERT-XM: A Modular Multi-Vector Representation Model for Zero-Shot Multilingual Information Retrieval](https://aclanthology.org/2025.coling-main.295/) | Uses modular language adaptation for multilingual retrieval. |
| ColMate | 2025 · EMNLP Industry | [ColMate: Contrastive Late Interaction and Masked Text for Multimodal Document Retrieval](https://aclanthology.org/2025.emnlp-industry.145/) | Adds OCR-based pre-training and masked contrastive learning. |
| ColPali | 2025 · ICLR | [ColPali: Efficient Document Retrieval with Vision Language Models](https://openreview.net/forum?id=ogjBpZ8uSi) | Matches query-token embeddings with visual document-page representations. |
| Argus-Retriever | 2026 · arXiv | [Argus-Retriever: Vision-LLM Late-Interaction Retrieval with Region-Aware Query-Conditioned MoE for Visual Document Retrieval](https://arxiv.org/abs/2606.04300) | Refines cached document features conditioned on the query for shortlisted candidates. |
| ELK-Multi | 2026 · TKDD | [Multi-Vector Biomedical Dense Retrieval with Knowledge-Enhanced Entity-Type Clustering](https://doi.org/10.1145/3785368) | A neighboring multi-vector design organized around biomedical entity clusters. |
| Hydra | 2026 · arXiv | [Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model](https://arxiv.org/abs/2603.28554) | Shares a vision-language model between retrieval and generation modes. |
| LateOn / mLateOn | 2026 · arXiv | [DenseOn with the LateOn: Fully Open Dense and Late-Interaction Models for Multilingual, Long-Context, and Code Search](https://arxiv.org/abs/2607.27178) | Studies open training and transfer across languages and retrieval settings. |
| LITTA | 2026 · arXiv | [LITTA: Late-Interaction and Test-Time Alignment for Visually-Grounded Multimodal Retrieval](https://arxiv.org/abs/2603.26683) | Generates query variants and fuses rankings with a fixed page index. |
| Nemotron ColEmbed V2 | 2026 · arXiv | [Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models for Visual Document Retrieval](https://arxiv.org/abs/2602.03992) | Scales visual late-interaction representation learning. |
| NumColBERT | 2026 · arXiv | [NumColBERT: Non-Intrusive Numeracy Injection for Late-Interaction Retrieval Models](https://arxiv.org/abs/2605.10109) | Adds query-side numerical gating while retaining the document index and MaxSim interface. |

<a id="section-11"></a>

### Section 11: Research Frontiers and Evaluation Context

These references motivate future directions. Inclusion of agentic retrieval or a benchmark does not classify it as a canonical late-interaction model.

| Work | Year / venue or version | Paper | Main role |
| --- | --- | --- | --- |
| Agentic-R | 2026 · ACL Findings | [Agentic-R: Learning to Retrieve for Agentic Search](https://aclanthology.org/2026.findings-acl.785/) | Context for agent-retriever learning and downstream evaluation. |
| AgentIR | 2026 · arXiv | [AgentIR: Reasoning-Aware Retrieval for Deep Research Agents](https://arxiv.org/abs/2603.04384) | Context for reasoning-aware retrieval; not automatically a canonical late-interaction model. |
| BrowseComp-Plus | 2026 · ACL | [BrowseComp-Plus: A Fair and Disentangled Evaluation Benchmark for Deep Search Agents](https://aclanthology.org/2026.acl-long.1023/) | Context for evaluating retrieval separately from agent behavior. |
| H+ Embedding | 2026 · arXiv | [H+ Embedding: Harmonizing Global and Token-Level Retrieval with Context-Dependent Phrases](https://arxiv.org/abs/2608.00065) | Motivates learned interaction units beyond fixed token segmentation. |
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

The initial release follows the survey's component-based organization. Subsequent additions should identify whether they are already discussed in the survey or are post-survey updates. See [CONTRIBUTING.md](CONTRIBUTING.md) and [CHANGELOG.md](CHANGELOG.md).

Please cite individual papers when relying on their methods or findings. Linked papers, models, datasets, and software retain their respective authorship and licenses.
