# Software, Models, and Evaluation Resources

[Back to the survey](../README.md)

Software entries are grouped by role. They do not imply interchangeable scoring, checkpoint compatibility, or retrieval results.

## Implementations and serving

| Resource | Role | Connection to the survey |
| --- | --- | --- |
| [ColBERT](https://github.com/stanford-futuredata/ColBERT) | Reference model and retrieval implementation | ColBERT, ColBERTv2, and PLAID |
| [PyLate](https://github.com/lightonai/pylate) | Training, encoding, and retrieval toolkit | Research infrastructure in Section 9 |
| [ColPali](https://github.com/illuin-tech/colpali) | Visual document retrieval code | Multimodal late interaction in Section 10 |
| [ColBERTer](https://github.com/sebastian-hofstaetter/colberter) | Reduced whole-word multi-vector model | Representation reduction in Section 5 |
| [RAGatouille](https://github.com/AnswerDotAI/RAGatouille) | ColBERT-oriented training and RAG integration | Workflow infrastructure in Section 9 |
| [Qdrant](https://github.com/qdrant/qdrant) | Vector database and serving | Multi-vector storage and scoring infrastructure |
| [PyTerrier paper](https://doi.org/10.1145/3459637.3482013) | Declarative IR experimentation | Pipeline composition and evaluation |
| [RoutIR paper](https://arxiv.org/abs/2601.10644) | Retrieval-pipeline serving | Serving costs and deployment |
| [ColBERT-X / PLAID-X](https://github.com/hltcoe/ColBERT-X) | Cross-language implementation | Historical multilingual resource; repository is archived |

See each project's own documentation for installation, model compatibility, and license terms.

## Models

| Model family | Resource | Reading note |
| --- | --- | --- |
| ColBERTv2 | [Reference implementation](https://github.com/stanford-futuredata/ColBERT) | Keep the model checkpoint and retrieval-engine settings explicit. |
| Jina-ColBERT-v2 | [Model page](https://jina.ai/models/jina-colbert-v2/) | Multilingual model with dimensionality choices; record the selected projection. |
| ColPali and related visual retrievers | [ColPali implementation](https://github.com/illuin-tech/colpali) | Record page preprocessing and the number of visual vectors. |
| Nemotron ColEmbed V2 | [Paper](https://arxiv.org/abs/2602.03992) | Distinguish model sizes and benchmark versions. |
| LateOn / mLateOn | [Paper](https://arxiv.org/abs/2607.27178) | Distinguish same-language retrieval, cross-language retrieval, and transfer. |

## Benchmarks and evaluation references

| Resource | What it supports | Main comparability concern |
| --- | --- | --- |
| [BEIR](https://arxiv.org/abs/2104.08663) | Zero-shot retrieval evaluation | Report datasets individually as well as the aggregation rule. |
| [ColPali / ViDoRe](https://openreview.net/forum?id=ogjBpZ8uSi) | Visual document-page retrieval | Page-level relevance differs from text-passage relevance. |
| [ViDoRe V3](https://arxiv.org/abs/2601.08620) | Complex visual-document and RAG evaluation | V1, V2, and V3 are not interchangeable benchmark sets. |
| [Baleen](https://arxiv.org/abs/2101.00436) | Multi-hop retrieval on HotpotQA and HoVer | Evidence coverage across hops differs from single-pass nDCG. |
| [BrowseComp-Plus](https://aclanthology.org/2026.acl-long.1023/) | Deep-search agent evaluation | Separate retrieval access from agent and generator effects. |

For MS MARCO and TREC Deep Learning experiments, identify the exact collection version, query split, relevance judgments, and metric. A score labeled only "MS MARCO" or "TREC DL" is not a complete protocol.
