# HW7 Huffman Coding

## Overview
Huffman coding shrinks text by giving short bit-codes to frequent chars and long codes to rare ones.  
Mostly do 3 big steps:

1. **Count** – scan text and count each character.  
2. **Build Tree** – use min-heap to merge two smallest counts again and again until 1 root node remains.  
   - This is greedy: always pick the cheapest pair first.  
   - The tree is binary; left edges will later mean “0”, right edges “1”.  
3. **Code & Compress** – walk the tree to make a table (char → bit-string), turn the whole text into bits, pad to bytes, and save the table plus bits to a file.  

To get the text back we just reverse the table (bit-string → char) and scan the bits left-to-right.

2 Python scripts:
- `huffman_compress.py` – does steps 1-3, prints the tree sideways, saves `.huff`.  
- `huffman_decompress.py` – loads `.huff`, rebuilds the text, saves `.decoded.txt`.  

Both print key info to the terminal for easy screenshots.

## Files for testing
```
sample.txt            # example input
sample.txt.huff       # compressed output
sample.txt.decoded.txt # decoded output

```

## How to Run

Compress:
```powershell
python huffman_compress.py sample.txt
```
Output includes:
- Input text
- Frequency map
- Huffman tree (sideways)
- Code map
- Compression ratio

Decompress:
```powershell
python huffman_decompress.py sample.txt.huff
```
Output includes:
- Loaded code map
- Reconstructed text
- Saved decoded file name

## Notes
1. **Frequency**: `Counter` counts every char in one pass.  
2. **Tree building (greedy recursion)**:  
   - Put each (char, count) into a min-heap.  
   - While heap has >1 item: pop two smallest, merge into new node, push back.  
   - Last item left is the root.  
   - Left child = 0 bit, right child = 1 bit.  
3. **Codes**: recurse from root, collect 0/1 along path to each leaf; store in dict.  
4. **Padding**: bit-string length must be multiple of 8; add 0-7 zeros and remember how many.  
5. **File format**: pickle dict with `code_map`, `pad_len`, `bits` so decoder has everything.

## Screenshots
See attached jpg in `screenshots/` folder.