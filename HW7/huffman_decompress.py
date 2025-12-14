#!/usr/bin/env python3
"""
Huffman Decompress
Read compressed file, rebuild tree, decode text, save orig
"""

import pickle
import sys


"""Convert bytes -> bit string"""
def bytes_to_bits(byte_data):
    return "".join(f"{b:08b}" for b in byte_data)


"""Rm padding bit"""
def remove_padding(bits, pad_len):
    return bits[:-pad_len] if pad_len else bits

"""Reverse code map -> decode"""
def decode_bits(bits, code_map):
    rev_map = {v: k for k, v in code_map.items()}
    out = []
    buf = ""
    for b in bits:
        buf += b
        if buf in rev_map:
            out.append(rev_map[buf])
            buf = ""
    if buf:
        # leftover bits (wont happen for valid file!)
        pass
    return "".join(out)

def main():
    if len(sys.argv) < 2:
        print("Usage: python huffman_decompress.py <compressed_file>")
        sys.exit(1)
    
    in_file = sys.argv[1]
    base = in_file.replace(".huff", "")
    out_file = base + ".decoded.txt"

    # load
    with open(in_file, "rb") as f:
        data = pickle.load(f)
    code_map = data["code_map"]
    pad_len = data["pad_len"]
    byte_data = data["bits"]

    # show input
    print("=== Loaded Code Map ===")
    for ch, code in sorted(code_map.items()):
        print(repr(ch), code)
    print()

    # decode
    bits = bytes_to_bits(byte_data)
    bits = remove_padding(bits, pad_len)
    text = decode_bits(bits, code_map)

    # save
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(text)

    print("=== Reconstructed Text ===")
    print(text)
    print()
    print(f"=== Saved decoded file: {out_file} ===")

if __name__ == "__main__":
    main()