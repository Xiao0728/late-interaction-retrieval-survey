# Evaluating Late-Interaction Systems

[Back to the survey](../README.md)

This guide operationalizes the survey's distinction between model effectiveness, approximation fidelity, and deployed system cost.

| Dimension | Report | Why it matters |
| --- | --- | --- |
| Model | Checkpoint, tokenizer, query/document length limits, local-unit definition, vector dimension, precision | These determine the available local evidence. |
| Scoring | Exact relevance function, weights, normalization, missing-similarity treatment | "MaxSim" alone can conceal different aggregation or approximation rules. |
| Candidate generation | Backend, index configuration, probe count, thresholds, candidate depth | Final exact scoring cannot recover missing candidates. |
| Stored representation | Vector count, retained ratio, quantization, codebook, residuals | Compression interventions change different axes. |
| Complete footprint | Vector payload, IDs, offsets, codebooks, graphs, proxies, forward vectors, auxiliary sparse indexes | A smaller payload is not necessarily a proportionally smaller system. |
| Effectiveness | Dataset/version, splits, qrels, metrics, per-query results, significance procedure | Enables controlled comparisons and failure analysis. |
| Fidelity | Candidate recall, score error, top-k agreement or ranking overlap with a stated reference | Separates model quality from search approximation. |
| Latency | Query encoding, candidate search, gathering, decoding, scoring, feedback, transfers | Reveals whether work moved elsewhere in the pipeline. |
| Deployment | Hardware, software versions, threads, warm-up, batch size, concurrency, cache state | Determines the meaning and portability of timings. |
| Serving | Throughput, median/tail latency, RAM/VRAM, filtering, updates | Single-query speed does not characterize production behavior. |

## Feedback experiments

Report the first-stage retriever, feedback depth, number of expansion vectors, weighting, selection rule, and second-stage retrieval or reranking depth. Include feedback construction and the second retrieval in end-to-end latency. A no-expansion configuration should provide a meaningful baseline comparison.

## Visual and iterative retrieval

For images, report page preprocessing, image resolution, retained patches, and whether document representations depend on the query. For video, report frame sampling and indexed evidence channels. For iterative retrieval, report hop budgets, query/context growth, evidence accumulation, and end-to-end retrieval cost.

## Comparison rules

- Compare configurations on matched data, checkpoints, candidate budgets, and hardware when attributing a gain to an engine.
- Evaluate representation reduction and retrieval approximation separately before interpreting the combined pipeline.
- Distinguish exact scoring over reconstructed vectors from exact scoring over the original uncompressed vectors.
- Report per-query failures and rare-entity, numerical, exclusion, and compositional cases when those capabilities are claimed.
- Avoid ranking systems from unrelated published timing measurements.
