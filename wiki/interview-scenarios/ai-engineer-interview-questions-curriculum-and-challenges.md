# AI engineer interview questions curriculum and challenges

## Summary
The [AI-Engineer-Interview-Questions repository](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/tree/main) by Om Bharatiya is a comprehensive preparation suite designed for AI Engineers, Large Language Model (LLM) Engineers, and Applied AI practitioners. It organizes technical depth across 13 modular topics encompassing 596+ questions with worked answers, 10 production system design case studies, and 19 self-contained, from-scratch Python coding challenges.

## Key points
- **Curriculum structure**: Covers 13 dedicated topic tracks spanning classical machine learning foundations, transformer mechanics, prompt/context engineering, RAG, alignment, agentic architectures, and production inference.
- **Runnable coding challenges**: Provides 19 standalone Python challenges using only NumPy and the standard library, each accompanied by reference implementations and test suites.
- **Evaluation and system design**: Incorporates 10 complete system design blueprints (e.g., enterprise RAG, code assistants, text-to-SQL) and interview evaluation rubrics.
- **Pacing frameworks**: Outlines modular preparation timelines ranging from high-signal crash courses ("The AI Engineer 75") to comprehensive 8-week mastery plans.

## Details

### Thirteen core interview topics
Each topic module contains an introductory conceptual primer (`README.md`) paired with a question bank featuring collapsible worked solutions (`questions.md`):

| # | Topic | Questions | Core competencies | Source link |
|---|---|---|---|---|
| 01 | ML & deep learning foundations | 55 | Bias-variance tradeoff, optimization algorithms (Adam/SGD), regularization, loss functions, evaluation metrics | [01-ml-and-dl-foundations](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/tree/main/01-ml-and-dl-foundations/) |
| 02 | LLM & transformer fundamentals | 65 | Multi-head attention, rotary positional embeddings (RoPE), tokenization, scaling laws, Mixture of Experts (MoE), KV cache | [02-llm-fundamentals](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/tree/main/02-llm-fundamentals/) |
| 03 | Prompt engineering & context engineering | 50 | Few-shot prompting, Chain-of-Thought (CoT), constrained structured outputs, prompt caching, context rot and compaction | [03-prompt-engineering-and-context](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/tree/main/03-prompt-engineering-and-context/) |
| 04 | RAG & retrieval | 60 | Chunking strategies, dense/sparse embeddings, hybrid search, Reciprocal Rank Fusion (RRF), cross-encoder rerankers, retrieval evaluation | [04-rag-and-retrieval](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/tree/main/04-rag-and-retrieval/) |
| 05 | Fine-tuning, RLHF & alignment | 56 | Supervised Fine-Tuning (SFT), LoRA/QLoRA, DPO, PPO, GRPO, knowledge distillation, GPU VRAM allocation arithmetic | [05-fine-tuning-and-alignment](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/tree/main/05-fine-tuning-and-alignment/) |
| 06 | Agents, tool use & MCP | 65 | Function calling protocols, Model Context Protocol (MCP), ReAct planning loops, multi-agent coordination, agent sandboxing | [06-agents-and-tool-use](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/tree/main/06-agents-and-tool-use/) |
| 07 | Evals & observability | 55 | LLM-as-a-judge patterns, benchmark limitations (MMLU, GSM8K), RAG triad evals, tracing pipelines, regression testing | [07-evaluation-and-observability](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/tree/main/07-evaluation-and-observability/) |
| 08 | Inference, serving & production LLM systems | 56 | Prefill vs. decode phases, paged KV cache (vLLM), post-training quantization (AWQ/GPTQ), speculative decoding, throughput optimization | [08-inference-and-production](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/tree/main/08-inference-and-production/) |
| 09 | Safety, security & responsible AI | 52 | Indirect prompt injection, jailbreaking, OWASP Top 10 for LLMs, guardrails frameworks, data privacy and governance | [09-safety-security-and-responsible-ai](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/tree/main/09-safety-security-and-responsible-ai/) |
| 10 | Multimodal models | 40 | Vision-Language Models (VLMs), cross-attention conditioning, diffusion models, automatic speech recognition (ASR), voice agents | [10-multimodal](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/tree/main/10-multimodal/) |
| 11 | AI system design | 10 case studies | End-to-end design frameworks, capacity estimation, component architecture, failure modes, cost engineering | [11-ai-system-design](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/tree/main/11-ai-system-design/) |
| 12 | Coding challenges | 19 challenges | Implementation of fundamental algorithms and systems from scratch without external ML frameworks | [12-coding-challenges](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/tree/main/12-coding-challenges/) |
| 13 | Interview process & behavioral | 42 | Loop structures across frontier labs and tech giants, take-home projects, AI project storytelling, failure retrospectives | [13-interview-process-and-behavioral](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/tree/main/13-interview-process-and-behavioral/) |

### Nineteen runnable coding challenges
All challenges are self-contained Python scripts requiring only standard libraries and NumPy, paired with integrated test cases:

| # | Challenge | Difficulty | Key concepts tested | Implementation script |
|---|---|---|---|---|
| 01 | Attention | Medium | Scaled dot-product attention, multi-head projections, causal attention masking | [01_attention.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/01_attention.py) |
| 02 | BPE tokenizer | Medium | Byte-level Byte-Pair Encoding (BPE), vocabulary training, token encoding and decoding | [02_bpe_tokenizer.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/02_bpe_tokenizer.py) |
| 03 | Sampling strategies | Easy | Temperature scaling, top-k filtering, top-p (nucleus) sampling, min-p, repetition penalties | [03_sampling.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/03_sampling.py) |
| 04 | Positional encodings | Medium | Absolute sinusoidal positional encodings, Rotary Position Embedding (RoPE) complex rotation | [04_positional_encodings.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/04_positional_encodings.py) |
| 05 | LayerNorm & Softmax | Easy | Numerically stable softmax/log-softmax, standard LayerNorm, RMSNorm normalization | [05_layernorm_and_softmax.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/05_layernorm_and_softmax.py) |
| 06 | KV cache | Medium | Autoregressive decoding loop performance with and without Key-Value caching | [06_kv_cache.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/06_kv_cache.py) |
| 07 | Mini-GPT forward pass | Hard | End-to-end transformer block forward pass: token/position embeddings, MLP, residual heads | [07_mini_gpt_forward.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/07_mini_gpt_forward.py) |
| 08 | Semantic search / RAG | Medium | Dense vector indexing, cosine similarity retrieval, top-k prompt assembly | [08_semantic_search_rag.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/08_semantic_search_rag.py) |
| 09 | Text chunking | Easy | Fixed-size chunking, sliding-window chunking with overlap, sentence boundaries, recursive chunking | [09_text_chunking.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/09_text_chunking.py) |
| 10 | Agent loop | Medium | Autonomous tool invocation, ReAct thought-action-observation loop with mock LLM calls | [10_agent_loop.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/10_agent_loop.py) |
| 11 | Rate limiter & retry | Medium | Token bucket rate limiting, exponential backoff with full jitter for LLM API clients | [11_rate_limiter_and_retry.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/11_rate_limiter_and_retry.py) |
| 12 | Eval metrics | Medium | Unbiased pass@k estimator, Exact Match (EM), token F1 score, LLM-as-judge scoring harness | [12_eval_metrics.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/12_eval_metrics.py) |
| 13 | Streaming parser | Hard | Server-Sent Events (SSE) streaming protocol parser, incremental JSON tool-call assembly | [13_streaming_parser.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/13_streaming_parser.py) |
| 14 | LoRA adapter | Medium | Low-Rank Adaptation forward pass, weight merging ($W + \frac{\alpha}{r}BA$), multi-adapter batched inference | [14_lora_adapter.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/14_lora_adapter.py) |
| 15 | Beam search | Medium | Autoregressive beam search decoding with cumulative log-probability length normalization | [15_beam_search.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/15_beam_search.py) |
| 16 | Semantic cache | Medium | Two-tier cache (exact match hash + vector similarity threshold), TTL, LRU eviction, tag invalidation | [16_semantic_cache.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/16_semantic_cache.py) |
| 17 | Hybrid search & rerank | Medium | BM25 sparse keyword ranking, dense embeddings, Reciprocal Rank Fusion (RRF), Maximal Marginal Relevance (MMR) | [17_hybrid_search_and_rerank.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/17_hybrid_search_and_rerank.py) |
| 18 | Constrained JSON decoding | Hard | Grammar-guided decoding, token trie validation, schema prefix masking | [18_constrained_json_decoding.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/18_constrained_json_decoding.py) |
| 19 | Speculative decoding | Hard | Fast draft model proposal generation, target model verification, rejection sampling acceptance loop | [19_speculative_decoding.py](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/blob/main/12-coding-challenges/19_speculative_decoding.py) |

### Structured study plans and system design
The resource structures candidate preparation into tiered study roadmaps:
- **The AI Engineer 75**: A curated baseline checklist comprising 64 high-frequency conceptual questions, 4 full system design mocks, and 7 core coding challenges.
- **Pacing paths**: Fast-track crash review (days to 1 week), core topic sprint (2–4 weeks focusing on 13 primers and 19 coding challenges), and comprehensive loop readiness (1–2 months including all 596 questions and full portfolio work).
- **System design templates**: Ten real-world case studies formatted with standardized requirements, capacity estimation, architecture diagrams, evaluation metrics, cost modeling, and failure mitigations.

## Related
- [[AI/ML engineer interview preparation]]
- [[Data science core]]
- [[DSA and core CS]]
- [[Interview scenarios]]
- [[Topics]]

## References
- Source: [ai_engineer_interview_questions_ombharatiya.md](file:///home/soumen/Workspace/AIEngineerInterviewPrep/input/ai_engineer_interview_questions_ombharatiya.md)
- GitHub Repository: [ombharatiya/AI-Engineer-Interview-Questions](https://github.com/ombharatiya/AI-Engineer-Interview-Questions/tree/main)
- Author Profile: [Om Bharatiya](https://github.com/ombharatiya)
