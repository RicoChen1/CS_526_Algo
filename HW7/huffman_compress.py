#!/usr/bin/env python3
"""
Huffman Compress
Build frequency map, build tree, encode text, save compressed file
"""

import heapq
import os
import pickle
from collections import Counter, namedtuple

class Node:
    __slots__ = ["char", "freq", "left", "right"]
    def __init__(self, char, freq, left=None, right=None):
        self.char, self.freq, self.left, self.right = char, freq, left, right
    def __lt__(self, other):
        return self.freq < other.freq

"""Count each character"""
def build_frequency_map(text):

    return Counter(text)

"""Build Huffman tree by min-heap"""
def build_huffman_tree(freq_map):

    heap = [Node(ch, f, None, None) for ch, f in freq_map.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)
    
    return heap[0] if heap else None
 
"""Map each character to bit string"""
def build_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}
    if node.char is not None:
        code_map[node.char] = prefix or "0"  # handle single char case
    else:
        build_codes(node.left, prefix + "0", code_map)
        build_codes(node.right, prefix + "1", code_map)
    return code_map

"""Convert text to bit string"""
def encode_text(text, code_map):
    return "".join(code_map[ch] for ch in text)

"""Add padding: length % 8 = 0"""
def pad_bits(bits):
    
    pad_len = (8 - len(bits) % 8) % 8
    padded = bits + "0" * pad_len
    return padded, pad_len

"""Convert bit string -> bytes"""
def bits_to_bytes(bits):
    return bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))

"""Save code map, bits, pad length to file"""
def save_compressed(code_map, padded_bits, pad_len, out_path):
    data = {
        "code_map": code_map,
        "pad_len": pad_len,
        "bits": padded_bits
    }
    with open(out_path, "wb") as f:
        pickle.dump(data, f)

"""Print tree sideways"""
def print_tree(node, prefix="", is_last=True):
    
    if node:
        connector = "└── " if is_last else "├── "
        if node.char is not None:
            print(prefix + connector + repr(node.char) + f"  freq={node.freq}")
        else:
            print(prefix + connector + f"* freq={node.freq}")
            next_prefix = prefix + ("    " if is_last else "│   ")
            kids = [node.left, node.right]
            for i, kid in enumerate(kids):
                print_tree(kid, next_prefix, i == len(kids) - 1)

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python huffman_compress.py <input_file>")
        sys.exit(1)
    
    in_file = sys.argv[1]
    out_file = in_file + ".huff"

    # read input
    with open(in_file, "r", encoding="utf-8") as f:
        text = f.read()

    # build frequency map
    freq_map = build_frequency_map(text)
    print("=== Input Text ===")
    print(text)
    print()

    print("=== Frequency Map ===")
    for ch, f in sorted(freq_map.items()):
        print(repr(ch), f)
    print()

    # build tree and code
    root = build_huffman_tree(freq_map)
    code_map = build_codes(root)

    print("=== Huffman Tree ===")
    print_tree(root)
    print()

    print("=== Code Map ===")
    for ch, code in sorted(code_map.items()):
        print(repr(ch), code)
    print()

    # encode
    bits = encode_text(text, code_map)
    padded_bits, pad_len = pad_bits(bits)
    byte_data = bits_to_bytes(padded_bits)

    # save
    save_compressed(code_map, byte_data, pad_len, out_file)
    print(f"=== Saved compressed file: {out_file} ===")
    print(f"Original bytes: {len(text.encode('utf-8'))}")
    print(f"Compressed bytes: {os.path.getsize(out_file)}")
    print(f"Compression ratio: {os.path.getsize(out_file)/len(text.encode('utf-8')):.2f}")

if __name__ == "__main__":
    main()