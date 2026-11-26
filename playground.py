
# load training txt
with open("data/train.txt", encoding="utf-8") as f:
    text = f.read()
print(len(text))

# find every special character
chars = sorted(set(text))
vocab_size = len(chars)
print(vocab_size)
print("".join(chars))

# lookup tables, character <-> number
string_to_int = {ch: i for i, ch in enumerate(chars)}
int_to_string = {i: ch for i, ch in enumerate(chars)}
print(string_to_int["a"])
print(int_to_string[string_to_int["a"]])

# encode and decode
def encode(s):
    return [string_to_int[c] for c in s]

def decode(ids):
    return "".join(int_to_string[i] for i in ids)

encoded_hello = encode("hello")
print(encoded_hello)
print(decode(encoded_hello))

# convert whole dataset to numbers
import torch
data = torch.tensor(encode(text), dtype=torch.long)
print(data.shape)
print(data[:100])