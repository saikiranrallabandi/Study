# Pretraining Data Curation Playbook
## Complete Reference Guide — Based on FineWeb (HuggingFace)

---

## Note-Taking Framework (Use This For Any Paper/Article)

Every section you study should go through these 6 steps:

1. **Translate** — Rephrase in plain English. Strip jargon. If you can say it differently, you understood it. If you can't, you didn't.
2. **Filter** — Split into three buckets: must remember (concepts, insights, formulas), nice to know (specific numbers, names), and skip (implementation details, tool names, citations).
3. **Connect** — Link to something you already know. Connections turn isolated facts into a web that's harder to forget.
4. **Visualize** — What doodle would make this click? If you can't draw it, you probably don't understand it well enough.
5. **Interview Flip** — If an interviewer asked about this, what's the one sentence that sounds smart? Extract the "so what."
6. **Anti-note** — What should you NOT write? If everything goes in your notes, nothing stands out.

**The rule:** If your notes look exactly like the source, you wasted your time. Good notes are shorter, simpler, and in your voice.

---

## 1. Where Does Training Data Come From?

Two options:
- **Crawl it yourself** — OpenAI, Anthropic do this with their own crawlers
- **Use public crawl data** — CommonCrawl (non-profit, crawling since 2007)

CommonCrawl key numbers:
- One crawl (April 2024) = 2.7 billion web pages = 386 TiB of HTML
- 96 crawls released since 2013
- New crawl every 1–2 months

FineWeb used CommonCrawl as its starting point, following the same approach as many LLM training teams.

**Takeaway:** LLMs aren't trained on curated data — they start with massive, messy web crawls. The real work is in cleaning it up.

---

## 2. What Is "High Quality" Data?

"High quality" is not well defined in pretraining. Even humans can't always agree. Quality depends on what you're training the model for, not on the text itself.

### Three Methods to Judge Data Quality

| Method | How It Works | Speed | Cost | Reliability |
|---|---|---|---|---|
| **Perplexity (Wikipedia)** | Train model on Wikipedia (clean reference), score new data. Low perplexity = clean-ish. | Fast | Cheap | Low |
| **Small model + eval tasks** | Train small models on data subsets, evaluate on diverse benchmarks. | Medium | Medium | Medium |
| **Human evaluation** | Train models, have humans rank outputs (e.g., LMSYS Chatbot Arena). | Slow | Expensive | High |

**Perplexity method flaw:** Biases toward formal/encyclopedic text, filters out useful informal content (code, tutorials, conversations).

**Small model method warning:** Don't overfit to one benchmark — pick diverse evals or you risk hurting generality.

**Human eval problem:** Requires instruction finetuning first (pretrained models can't chat), which adds noise to the comparison.

**Takeaway:** There's no perfect way to evaluate data quality — each method trades off cost vs reliability. The mature answer acknowledges this and explains the tradeoffs.

---

## 3. Ablation Methodology

**Ablation = remove one step and compare results.** Change only ONE thing, keep everything else identical, measure the difference. Same logic as a controlled experiment.

How FineWeb did it:
- Train two identical models (same size, same architecture, same number of tokens, one epoch)
- Only difference = the training data
- One model has the cleaning step, one doesn't
- Compare eval scores on same benchmark tasks

If scores improve → the cleaning step helped. If not → drop it.

### Ablation Model Setup
- 1.82B parameters, Llama architecture, GPT2 tokenizer
- Trained on ~28B tokens (Chinchilla optimal for this model size)
- Confirmed results with longer 350B token runs

**Chinchilla Optimal:** From DeepMind's Chinchilla paper (2022) — for a given compute budget, there's an ideal ratio of model size to training tokens. Roughly: tokens ≈ 20× parameters. Before Chinchilla, teams were training huge models on too little data. After Chinchilla, the field shifted toward more data + appropriately sized models.

### How to Pick Good Eval Benchmarks (3 Criteria)
1. **Low variance** — Results shouldn't change much if you resample the data (stable signal)
2. **Monotonically increasing** — Score should go up as training progresses. If it goes down, benchmark is unreliable at small scale
3. **Above random** — Small models won't score high, but scores must be meaningfully above random chance

**Benchmarks used:** CommonSense QA, HellaSwag, OpenBook QA, PIQA, SIQA, WinoGrande, ARC, MMLU

**Know by name for interviews:** MMLU (57 subjects, knowledge test) and HellaSwag (commonsense sentence completion).

---

## 4. Text Extraction

CommonCrawl has two formats:
- **WARC** = raw HTML + metadata (the full thing)
- **WET** = text already extracted by CommonCrawl (lower quality)

Most datasets use WET (easier). FineWeb used WARC + trafilatura library for better text extraction.

### Experiment Results
- WET = 254B tokens (bigger but worse — extra tokens were boilerplate: menus, footers, nav bars)
- WARC + trafilatura = 200B tokens (smaller but better)

**Takeaway:** More data ≠ better data. Starting from raw HTML gives you more control over quality. Your text extraction method matters because pipeline decisions early on cascade through everything downstream.

---

## 5. Base Filtering

Three-step filtering (following RefinedWeb):
1. **URL blocklist** → remove adult content
2. **Language filter** → fastText classifier, keep English only (score ≥ 0.65)
3. **Quality + repetition filters** → from MassiveText (removes gibberish, repeated text)

Raw CommonCrawl → after base filtering = ~36 trillion tokens

The 0.65 language threshold is lenient on purpose — too strict and you lose valid English text with foreign words mixed in (code, technical terms, names).

**Takeaway:** Every major LLM dataset follows roughly this same pipeline: remove harmful → filter language → remove low quality/repetitive. The specifics differ but the structure is universal.

---

## 6. Deduplication

### Why Deduplicate?
- The web has mirrors, aggregators, templated pages, repeated content
- Crawler itself can introduce duplicates (different links → same page)
- Removing duplicates improves model performance, reduces memorization (→ better generalization), and increases training efficiency (same compute, more diverse data)

### Two Approaches
- **Exact dedup** → checks for identical matches
- **Fuzzy dedup** → uses similarity metric (not perfectly identical but close enough)
- Can operate at different levels: line, paragraph, or full document

### MinHash (What FineWeb Used)
- Break each document into **5-grams** (sliding window of 5 words)
- Compute **112 hash functions** per document
- Split into **14 buckets × 8 hashes** each
- If two docs share all 8 hashes in ANY bucket → considered duplicate
- Target: documents ≥ 75% similar

**Match probability formula:** P = 1 − (1 − s⁸)¹⁴
- 70% similar → 56% chance caught
- 75% similar → 77% chance caught
- 80% similar → 92% chance caught
- 85% similar → 98.8% chance caught

---

## 7. The Deduplication Trap — More Dedup Is NOT Always Better

### What They Tried (Cross-Dump Dedup)
- Dedup ALL 90+ dumps together chronologically (newest first)
- Each dump deduped against itself + all previously processed dumps
- Oldest dumps lost >90% of their data
- Result: 36T tokens → 4T tokens

**Surprise:** Model trained on aggressively deduped data showed almost no improvement over non-deduped data. Scored BELOW RefinedWeb.

### Why It Failed — The Deep Dive
Experiment on dump 2013-48:
- Before dedup: ~490B tokens
- After cross-dump dedup: ~31B tokens (94% removed)
- They trained on the 31B kept data vs the removed data (individually deduped to 171B)
- **Result: The kept data was WORSE than the removed data**
- Kept data was full of ads, keyword spam, bad formatting

### The Key Insight: Uniqueness ≠ Quality
- Good content gets duplicated across the web (popular articles, Wikipedia mirrors, quality sites)
- Garbage is often unique (random spam, keyword stuffing)
- Cross-dump dedup biased toward keeping unique-but-garbage content and removing common-but-good content

### The Fix: Individual Dump Dedup
- Dedup each dump independently (not against other dumps)
- Result: 20T tokens (vs 4T from aggressive dedup)
- Performance: matched RefinedWeb

### Their Hypothesis
- Dedup helps most by removing massive clusters (100K+ duplicate docs, present in every dump)
- Small clusters (<~100 duplicates) → removing these actually hurts
- At full scale (90+ dumps), the upsampling of low-quality unique data outweighs the dedup benefit

### Why Dedup Effects Are Hard to Measure at Small Scale
At 28B token ablations, the sample is too small to encounter enough duplicates for dedup to matter. You need 350B+ tokens to see the real impact. Ablation results at small scale don't always transfer to large scale.

---

## 8. Learning From C4's Filters

C4 (2019, ~175B tokens) is still competitive despite its age because of aggressive filtering. Used in Llama1.

### C4's Filters
- Drop lines: no ending punctuation, javascript mentions, cookie notices
- Drop docs: wrong length, "lorem ipsum", curly brackets
- Line-level dedup
- Word blocklist

### Key Finding
- **Terminal punctuation filter** = biggest individual boost BUT removes 30% of data (too destructive)
- **All other filters combined** = better performance while removing only ~7%
- **Decision:** Use all C4 filters EXCEPT terminal punctuation

**Takeaway:** The most aggressive filter isn't always the best. C4's success from 2019 proves filtering quality matters more than data freshness.

---

## 9. Systematic Filter Development

### 4-Step Process
1. Compute 50+ metrics on high-quality vs low-quality data
2. Find metrics with biggest distribution gap (**Wasserstein distance**)
3. Pick threshold from histogram inspection to make bad data resemble good data
4. Validate with ablation runs

### 3 Winning Filters (Out of 17 Candidates)
1. **Lines ending with punctuation ≤ 0.12** → remove (10% removed) — smarter version of C4's 30% terminal punct filter
2. **Duplicate line characters ≥ 0.1** → remove (12.5% removed)
3. **Short lines (<30 chars) ≥ 0.67** → remove (3.7% removed)

All three combined: ~22% removed → **surpassed C4 performance** with much more data.

**Takeaway:** Compare metric distributions between clean and dirty data, find biggest gaps, set thresholds there. This is a reusable framework for any data quality problem, not just LLMs.

---

## 10. Final FineWeb Pipeline

The complete pipeline, in order, each step providing a performance boost:

1. **Text extraction** — WARC + trafilatura (not WET)
2. **Base filtering** — URL blocklist, language filter, quality/repetition filters
3. **Independent MinHash dedup** per dump (not cross-dump)
4. **C4 filters** — all except terminal punctuation
5. **Custom filters** — punctuation ratio, duplicate lines, short lines

**Result: 15T tokens → best performing open web dataset**

### Dataset Landscape (Know These Names)
| Dataset | Tokens | Notes |
|---|---|---|
| FineWeb | 15T | Best open dataset |
| RedPajama2 | 20T | Bigger but lower quality |
| Dolma v1.6 | 3T | Allen AI |
| SlimPajama | 627B | Cerebras |
| RefinedWeb | 500B | Falcon team |
| The Pile | 340B | EleutherAI |
| C4 | 172B | Small but punches above its weight |

---

## 11. FineWeb-Edu — The Educational Quality Layer

FineWeb-Edu = FineWeb + educational quality filtering → best overall open dataset.

### How They Built It (3 Steps)
1. **LLM-as-annotator:** Used Llama-3-70B to score 500K FineWeb samples on educational quality (0–5 scale, focused on grade/middle-school level knowledge)
2. **Train cheap classifier:** Snowflake-arctic-embed + regression head, trained on 450K annotations → F1 = 82% at threshold 3
3. **Filter at scale:** Run classifier on all 15T tokens → keep only score ≥ 3

**Result:** 92% of data removed → 1.3T tokens remain → outperforms everything.

### Why This Approach Works
Using an LLM to judge quality directly on 15T tokens would be impossibly expensive. Instead:
- LLM annotates a small sample (500K) — expensive but feasible
- Train a tiny classifier on those annotations — cheap
- Run classifier on everything — fast and cheap

This pattern is called **LLM distillation for data curation**. Llama 3 and Phi-3 both used it. This is the state-of-the-art answer for "how would you improve data quality?"

### Threshold Tradeoffs
- Higher threshold (4-5) → better on knowledge benchmarks (MMLU, ARC) but worse on HellaSwag/PIQA
- **Threshold 3 = best balance**
- Also released threshold 2 version: 5.4T tokens (more data, slightly lower quality)

**Ultimate proof of the article's theme:** They removed 92% of data and performance went UP. Quality >>> Quantity.

---

## 12. CommonCrawl Over Time — Synthetic Data

Not all crawls are equal — some dumps perform much better than others. No conclusive explanation found.

### Synthetic Data Contamination
- **Proxy detection:** Frequency of ChatGPT-isms ("delve", "rich tapestry", "it's important to note", "certainly!", "dive into")
- Flat until 2023-14 → steep increase after (ChatGPT released late 2022)
- At small training scale: synthetic data doesn't seem to hurt (might even help)
- At large scale: unknown — open question

### Model Collapse Concern
As LLM-generated content floods the web, future pretraining data will increasingly contain synthetic text. Whether this creates a quality feedback loop (model trained on its own outputs degrades future models) or is actually beneficial is still unknown. This is an active area of research.

---

## Recurring Themes (The Principles Behind Everything)

1. **Quality >>> Quantity** — More data can hurt. 92% removal improved performance.
2. **Uniqueness ≠ Quality** — Good content is duplicated because it's good. Garbage is often unique.
3. **Surgical filtering > Aggressive filtering** — C4's 30% removal was beaten by smarter 10% removal.
4. **Validate every step** — Every pipeline decision was ablation-tested. Don't assume something helps.
5. **Small-scale results don't always transfer** — Dedup effects invisible at 28B tokens, only visible at 350B+.
6. **Data engineering is about balance** — Dedup, filtering, and threshold selection all have diminishing returns and side effects.
7. **LLM distillation for data curation** — Use expensive LLM on small sample → train cheap classifier → run at scale. State of the art.
