# llm.c Deep Study Plan
## Saikiran — Post-Training Research Engineer Prep
## Started: Nov 5, 2026

### Learning Path Context
3B1B theory (done) → nanoGPT Python (done) → **llm.c C/CUDA (current)** → nanochat (next)

### Repository: github.com/karpathy/llm.c
- **Purpose:** GPT-2 training in pure C/CUDA, no PyTorch
- **Star file:** train_gpt2.c (~1000 lines, 50KB) — entire GPT-2 in one C file
- **What's new vs nanoGPT:** manual memory (malloc/free), pointer arithmetic for tensors, hand-written forward AND backward passes, no autograd

---

## Session Plan (10 Sessions)

### Session 1: Reconnaissance [DONE - Nov 5]
- Read README, map file structure, plan sessions
- Created this study plan

### Session 2: C Foundations — Structs + Memory Layout
**File:** train_gpt2.c (top ~150 lines)
- #include headers, GPT2Config struct
- ParameterTensors / ActivationTensors structs
- malloc_and_point() — contiguous memory allocation
- **Key concept:** All 124M parameters in ONE malloc block, pointers index into it

### Session 3: Forward Pass — Layers Part 1
**File:** train_gpt2.c (layer functions)
- encoder_forward() — token + position embeddings
- layernorm_forward() — mean, variance, normalize (the math!)
- matmul_forward() — triple nested loop (i,j,k)
- **Connection to nanoGPT:** same math, but you see every multiply

### Session 4: Forward Pass — Layers Part 2
**File:** train_gpt2.c (more layer functions)
- attention_forward() — Q*K^T/sqrt(d), softmax, V multiply
- gelu_forward() — activation function in raw C
- residual_forward() — x = x + f(x) in a loop
- softmax_forward() — numerical stability (subtract max)
- crossentropy_forward() — -log(prob) loss

### Session 5: gpt2_forward() — Full Forward Assembly
**File:** train_gpt2.c (gpt2_forward function)
- How individual layers chain together
- Activation memory: pre-allocated, indexed by layer
- The full data flow: tokens → embeddings → N layers → logits → loss

### Session 6: Backward Pass — Manual Gradients
**File:** train_gpt2.c (all *_backward functions)
- **THE biggest learning:** chain rule without autograd
- crossentropy_softmax_backward (fused)
- matmul_backward, layernorm_backward, attention_backward
- encoder_backward
- gpt2_backward() — reverse order through layers

### Session 7: Training Loop — main()
**File:** train_gpt2.c (main function + helpers)
- gpt2_build_from_checkpoint() — loading binary weights
- gpt2_update() — AdamW in C (m, v buffers)
- DataLoader (reading .bin token files)
- Tokenizer (BPE decoding for samples)
- The full training loop: forward → backward → update → repeat
- malloc/free lifecycle

### Session 8: llmc/ Library Headers
**Files:** llmc/tokenizer.h, llmc/dataloader.h, llmc/utils.h, llmc/schedulers.h, llmc/sampler.h
- Supporting infrastructure
- How C header files work (#ifndef guards, inline functions)
- Binary file format for tokens (.bin)
- LR scheduling in C (cosine, linear warmup)

### Session 9: LayerNorm Tutorial
**Files:** doc/layernorm/layernorm.md, layernorm.c, layernorm.py
- Karpathy's step-by-step Python → C tutorial
- Forward pass: compute mean, variance, normalize, scale+shift
- Backward pass: derive gradients by hand
- **Methodology:** how to translate ANY PyTorch layer to C

### Session 10: CUDA Introduction (Overview)
**Files:** train_gpt2.cu (overview), dev/cuda/ (selected kernels)
- How the same algorithm maps to GPU threads
- Thread blocks, shared memory, coalesced access
- cuBLAS for matmul, Flash Attention via cuDNN
- NCCL for multi-GPU (replaces PyTorch DDP)

---

## Files We'll Study (in order)
| File | Size | Session | Why |
|------|------|---------|-----|
| train_gpt2.c | 50KB | S2-S7 | THE star file — entire GPT-2 in C |
| llmc/utils.h | 8KB | S8 | File I/O safety wrappers |
| llmc/tokenizer.h | 3KB | S8 | BPE tokenizer in C |
| llmc/dataloader.h | 24KB | S8 | Batch loading from .bin files |
| llmc/schedulers.h | 4KB | S8 | LR schedules |
| llmc/sampler.h | 1KB | S8 | Top-k sampling |
| doc/layernorm/ | 26KB | S9 | Tutorial: Python → C translation |
| train_gpt2.cu | 104KB | S10 | CUDA GPU version (overview) |
| dev/cuda/*.cu | varies | S10 | Educational kernel implementations |

## Files We'll Skip (and why)
| File | Why Skip |
|------|----------|
| train_gpt2.py | Already know this from nanoGPT |
| train_llama3.py | Llama variant, not needed now |
| test_gpt2.c/cu | Testing infrastructure, not core learning |
| profile_gpt2.cu | Profiling tools |
| dev/data/*.py | Python data prep (similar to nanoGPT prepare.py) |
| scripts/*.sh | Just shell scripts with hyperparameters |
| train_gpt2_fp32.cu | Simpler CUDA version, covered by S10 overview |
| llmc/zero.cuh | ZeRO sharding — advanced, skip for now |
| llmc/cudnn_att.* | cuDNN attention — advanced, skip for now |

## LeetCode Pattern File
- Will create: llm.c/lesson_for_leetcode (C coding patterns)
- Focus on: pointer arithmetic, struct packing, malloc patterns, loop optimization, bitwise ops

## PDF Notes
- Will create after completing sessions for train_gpt2.c (Sessions 2-7)
- Same style as nanoGPT PDFs (reportlab, color-coded, interview flashcards)
