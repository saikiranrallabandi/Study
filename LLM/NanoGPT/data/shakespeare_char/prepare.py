import os
import requests
import numpy as np
import pickle

input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
print(input_file_path)
if not os.path.exists(input_file_path):
    data_url = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'
    with open(input_file_path, 'w') as f:
        f.write(requests.get(data_url).text)
with open(input_file_path, 'r') as f:
    data = f.read()
print(f"length of dataset in charcaters: {len(data):,}")

# get all the unique characters that occur in this text
chars = sorted(list(set(data)))
vocab_size = len(chars)
print("all the unique characters:", "".join(chars))
print(f"vocab size: {vocab_size:,}")


# create a mapping from characters to integers
stoi = { ch:i for i,ch in enumerate(chars)}
itos = { i:ch for i,ch in enumerate(chars) }
def encode(s):
    return [stoi[c] for c in s] # encoder: take a string, output a list of integers
def decode(l):
    return ''.join([itos[i] for i in l])

# create the train and test splits
n = len(data)
train_data = data[:int(n*0.9)]
val_data = data[int(n*0.9):]

# encode both to integers
train_ids = encode(train_data)
val_ids = encode(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
"""
You have a list of integers like [18, 47, 56, 57, 58, 1, 15, ...] — your encoded Shakespeare. But a Python list is slow and fat — each integer is a full Python object with overhead.

np.array(train_ids, dtype=np.uint16) does two things:

np.array() — converts your Python list into a numpy array (a tight, C-style block of memory, no per-element overhead)
dtype=np.uint16 — each number uses exactly 2 bytes (16 bits), which can store values 0 to 65,535

Why uint16? Your vocab size is 65. So you need a type that can hold values 0-64. uint8 (1 byte, 0-255) would actually work too, but uint16 is safer if you later switch to BPE with ~50k tokens. int32 (4 bytes) would waste double the disk space for no reason.

After this, when you call train_ids.tofile('train.bin'), it writes the raw bytes to disk — no headers, no formatting, just numbers packed tightly. The training loop will later read this file with np.memmap and grab random chunks directly from disk without loading everything into RAM.
"""
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))

# save the meta information as well, to help us encode/decode later

meta = {
    'vocab_size' : vocab_size,
    'itos': itos,
    'stoi': stoi,
}

with open(os.path.join(os.path.dirname(__file__), 'meta.pkl'), 'wb') as f:
    pickle.dump(meta, f)
"""
length of dataset in charcaters: 1,115,394
all the unique characters:
 !$&',-.3:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
vocab size: 65
train has 1,003,854 tokens
val has 1,003,854 tokens

"""