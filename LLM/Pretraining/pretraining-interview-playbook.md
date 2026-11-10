# Pretraining Data — Interview Playbook
## What to Say, When to Say It, and How to Stand Out

---

## How to Use This Playbook

Each section has:
- **If they ask...** — The interview question or topic
- **Your answer** — What to say (concise, confident, structured)
- **Stand-out move** — The extra insight that separates you from other candidates
- **Connect to** — Links to other concepts you've studied (neural nets, backprop, memorization paper, loss surfaces)

---

## Q1: "Where does pretraining data come from?"

**Your answer:**
"There are two main approaches — crawl the web yourself, like OpenAI and Anthropic do, or use a public repository like CommonCrawl. CommonCrawl has been crawling since 2007 and releases a new crawl every one to two months, each containing around 2–3 billion web pages and hundreds of terabytes of HTML. Most open LLM training efforts, including FineWeb, RefinedWeb, and Dolma, start from CommonCrawl and then apply extensive filtering and deduplication."

**Stand-out move:** Mention specific scale — "A single CommonCrawl dump from April 2024 contains 2.7 billion web pages totaling 386 terabytes of uncompressed HTML."

---

## Q2: "How do you define 'high quality' training data?"

**Your answer:**
"That's actually one of the hardest questions in pretraining — there's no universal definition. Quality depends on the downstream task. There are three main approaches to measure it, each with tradeoffs."

Then describe the three methods:
1. **Perplexity against a reference corpus** (usually Wikipedia) — fast and cheap but unreliable. Biases toward formal text and filters out useful informal content.
2. **Train small models and evaluate on diverse benchmarks** — more reliable but slower. Critical to use diverse evals and avoid overfitting to any single benchmark.
3. **Human evaluation** (like LMSYS Chatbot Arena) — most reliable but too expensive and slow for data ablations. Also requires instruction finetuning first.

**Stand-out move:** "The FineWeb team found that the state-of-the-art approach is using an LLM to annotate a small sample for educational quality, then training a cheap classifier on those annotations to filter at scale. This is what Llama 3 and Phi-3 both used — LLM distillation for data curation."

---

## Q3: "Walk me through a pretraining data pipeline."

**Your answer (use this exact structure):**

"The pipeline has five main stages:

First, **text extraction** — starting from raw HTML (WARC format) rather than pre-extracted text gives better results. The FineWeb team showed that using the trafilatura library on raw HTML produced 25% less data than the default extraction but significantly better model performance, because the extra tokens were just page boilerplate.

Second, **base filtering** — remove adult content via URL blocklists, filter to English-only using a language classifier, and apply quality and repetition filters. This took CommonCrawl from raw data down to about 36 trillion tokens.

Third, **deduplication** — using MinHash for fuzzy deduplication within each dump independently. The key finding was that deduplicating across all dumps actually hurt performance because good content tends to be duplicated across the web while garbage is often unique. Individual dump dedup brought it to 20 trillion tokens.

Fourth, **heuristic filters** — comparing metric distributions between clean and dirty data, finding the biggest gaps using Wasserstein distance, and setting thresholds. Three filters removed about 22% of tokens and surpassed C4's performance.

Fifth, **educational quality filtering** — using an LLM to score a sample, training a classifier, filtering at scale. This removed 92% of data, leaving 1.3 trillion tokens that outperformed every other open dataset."

**Stand-out move:** End with: "The recurring lesson across every step was that quality matters far more than quantity. They removed 92% of their data in the final step and performance went up."

---

## Q4: "Tell me about deduplication. Why is it important?"

**Your answer:**
"Deduplication removes redundant content from the dataset. The web has mirrors, aggregators, templated pages, and crawler artifacts that create massive duplication. Removing duplicates improves model performance, reduces memorization which helps generalization, and increases training efficiency — same compute budget, but the model sees more diverse data."

Then mention the two types:
- **Exact dedup** — identical document/line matching
- **Fuzzy dedup** — similarity-based, typically using MinHash. You hash n-grams of documents into buckets. If two documents collide in any bucket, they're likely duplicates. You can tune precision vs compute by adjusting bucket count and size.

**Stand-out move:** "One counterintuitive finding from FineWeb is that aggressive deduplication can backfire. When they deduped across all 90+ CommonCrawl dumps, the oldest dumps lost over 90% of their data, and the remaining data was actually worse quality than what was removed. High-quality content tends to be replicated across the web, while low-quality spam is often unique. So deduping too aggressively removes the good stuff and keeps the junk. They switched to individual dump deduplication, which fixed the problem."

**Connect to:** The memorization paper (Arpit et al.) — "Duplicated data encourages memorization over learning, which degrades generalization."

---

## Q5: "How would you evaluate whether a data filtering step actually helps?"

**Your answer:**
"The gold standard is ablation testing. Train two identical models — same architecture, same size, same number of tokens, one epoch — with the only difference being whether the filtering step was applied. Then compare on a diverse set of evaluation benchmarks."

Then add the nuances:
- "Benchmarks need to be carefully chosen — they should have low variance across runs, monotonically increase during training, and score above random baseline at small model scale."
- "Small-scale ablations don't always transfer. The FineWeb team found that deduplication effects were invisible at 28 billion tokens but clearly visible at 350 billion. So you need to validate important findings with longer runs."

**Stand-out move:** Mention the systematic filter development framework: "You can systematically develop heuristic filters by computing 50+ metrics on both clean and dirty data, finding the metrics with the largest Wasserstein distance between distributions, setting thresholds from histogram inspection, and validating with ablations. This is a reusable framework for any data quality problem."

---

## Q6: "What is FineWeb-Edu and why does it matter?"

**Your answer:**
"FineWeb-Edu is a filtered version of FineWeb that uses an educational quality classifier. The approach was: use Llama-3-70B to score 500,000 samples on educational quality from 0 to 5, train a small embedding model with a regression head on those annotations, then run the classifier on all 15 trillion tokens of FineWeb. With a threshold of 3, 92% of data was removed, leaving 1.3 trillion tokens."

"The result outperformed every other open web dataset, and achieved the same MMLU performance as C4 and Dolma with 10x fewer tokens."

**Stand-out move:** "The pattern — use an expensive LLM to annotate a small sample, distill that judgment into a cheap classifier, run at scale — is called LLM distillation for data curation. It's the current state of the art. Both Llama 3 and Phi-3 used this approach, but their classifiers aren't public. FineWeb-Edu is the first open reproduction."

---

## Q7: "What about synthetic data in pretraining?"

**Your answer:**
"As LLMs have become more popular, the web increasingly contains LLM-generated content. The FineWeb team tracked this by measuring frequency of ChatGPT-isms like 'delve', 'rich tapestry', and 'it's important to note' across CommonCrawl dumps. The frequency was flat until mid-2023, then spiked steeply after ChatGPT's release."

"At small training scales, this synthetic data doesn't seem to hurt and might even help. But the long-term effect at large scale is an open question — there's a concern called model collapse, where training on AI-generated data could degrade future models."

**Stand-out move:** Frame it as a frontier problem: "This is one of the most important open questions in the field — as the web fills with AI content, how do we ensure future training data quality? No one has a definitive answer yet."

---

## Q8: "What datasets should I know about?"

| Dataset | Size | Key Thing to Know |
|---|---|---|
| **FineWeb** | 15T tokens | Best open web dataset, ablation-validated pipeline |
| **FineWeb-Edu** | 1.3T tokens | FineWeb filtered for educational quality, outperforms everything |
| **C4** | 172B tokens | Old (2019) but still competitive — proves filtering > recency |
| **RefinedWeb** | 500B tokens | Falcon team, introduced MinHash dedup at scale |
| **The Pile** | 340B tokens | EleutherAI, curated mix of diverse sources |
| **RedPajama2** | 20T tokens | Large but less filtered |
| **Dolma** | 3T tokens | Allen AI, used in OLMo |
| **SlimPajama** | 627B tokens | Cerebras, deduplicated RedPajama |

---

## Q9: "What's the Chinchilla scaling law?"

**Your answer:**
"The Chinchilla paper from DeepMind in 2022 found that for a given compute budget, there's an optimal ratio of model size to training tokens — roughly 20 tokens per parameter. Before Chinchilla, teams were training huge models on too little data, like GPT-3. After Chinchilla, the field shifted toward scaling data proportionally with model size, which is why models like Llama can be competitive with much larger models."

**Connect to:** This is why FineWeb's ablation models used 28B tokens for 1.82B parameters — that's approximately Chinchilla optimal.

---

## Q10: "What's the most important lesson from pretraining data research?"

**Your answer (memorize this):**
"Quality matters far more than quantity. The FineWeb team repeatedly showed this — better text extraction gave 25% less data but better results; individual dedup gave 5x more data than aggressive dedup and performed better because aggressive dedup kept unique garbage and removed common good content; educational filtering removed 92% of data and performance went up. The entire field is moving from 'collect everything' to 'curate carefully.'"

---

## Key Principles (Quick Reference)

1. **Quality >>> Quantity** — More data can hurt. 92% removal improved performance.
2. **Uniqueness ≠ Quality** — Good content is duplicated because it's good. Garbage is often unique.
3. **Surgical filtering > Aggressive filtering** — Smart 10% removal beat blunt 30% removal.
4. **Validate every step** — Ablation test each pipeline decision. Don't assume something helps.
5. **Small-scale ≠ Large-scale** — Results at 28B tokens don't always hold at 350B+.
6. **LLM distillation for data curation** — Expensive LLM annotates small sample → cheap classifier runs at scale. State of the art.
7. **Data engineering is about balance** — Every technique has diminishing returns and side effects.

---

## Connections to Your Previous Study Topics

| This Article | Connects To | How |
|---|---|---|
| Dedup reduces memorization | Arpit et al. memorization paper | Duplicated data encourages memorization over learning |
| Training on data, evaluating loss | Backpropagation & gradient descent | Same optimization loop, just at data-pipeline scale |
| Model performance on loss surface | Choromanska et al. loss surfaces | Data quality affects which minima the model finds |
| Small models for ablation | Nielsen's network.py | Same concept — small networks to test ideas cheaply |
| Chinchilla scaling | 3Blue1Brown neural networks | Parameters × data = compute budget tradeoff |
| LLM-as-judge for data quality | Attention mechanism (3B1B) | The classifier uses embeddings — same vector space concepts |
| Benchmark evaluation | Cost function from backprop | Benchmarks are just another way to measure "how wrong is the model" |
