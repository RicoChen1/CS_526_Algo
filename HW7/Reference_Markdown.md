# HW5 File Structure
- Including problem description pdf, 3 problem solution python, testing txt document, a README.md, and a md file This is a partial record of my conversation with the AI, presented as a record of my AI usage (in Chinese).


# Q1. Binary Search Tree

## Algo Description

1. Generate a unique random input set. Size 5~50. Values 1~1000.
2. Build BST by inserting values.
3. Print input set and the initial tree.
4. Do some add op with values not in tree. Print after each.
5. Do some delete op with values in tree. Print after each.
6. Pick one present value and one absent value. Run `find_node` and print `FOUND/NOT FOUND`.
7. Tree printing is sideways: right -> root -> left.

## ADT Fn

- Node: fields `value`, `left`, `right`.
- BST: `add_node(value)`, `delete_node(value)`, `find_node(value)`, `print_tree()`.

## Run Tests

```powershell
python HW5/bst_YChen_HW5.py // No input required
```

## Note:

- Duplicate values get auto ignored.
- Empty tree prints `(empty)`.
- For reproducible run, uncomment `bst.py`file `random.seed(42)`.

# Q2. Vowel-only Morse Sequence

## Algo Description

1. Read input file: first line is length `n`, second line is a string of `.` and `-`.
2. Morse Note: `A=.-`, `E=.`, `I=..`, `O=---`, `U=..-`.
3. Count number of ways to split string into these vowel codes using DP.
4. Print results in exact format:
   - `File Input: vowel_input<k>.txt`
   - `The Number of Vowel combinations is:  <count>`

## To Run Tests

```powershell
python HW5/vowel_morse_YChen_HW5.py HW5/vowel_inputX.txt
```

## Note:

- If the first line length differs from actual string length, program uses the string as-is.
- DP runs in `O(n * 5)` since 5 vowel codes are checked.

# Q. Alternating Increasing Sequence (A/B)

## Algo Description

1. Read a file with 4 lines: |A|, |B|, A values, B values.
2. Find the longest sequence of strictly increasing numbers that alternates sources A and B.
3. The subsequence must keep the relative order inside A and inside B.
4. Output:
   - `File Input: longest_seq<k>.txt`
   - `Longest Sequence: <numbers space-separated>`

## To Run Tests

```powershell
python HW5/longest_seq_YChen_HW5.py HW5/longest_seq1.txt
python HW5/longest_seq_YChen_HW5.py HW5/longest_seq2.txt
python HW5/longest_seq_YChen_HW5.py HW5/longest_seq3.txt
python HW5/longest_seq_YChen_HW5.py HW5/longest_seq4.txt
# 5 and 6 suffer from long running time. I'm not sure if the program has entered an infinite loop/halting.
# Well it's actually I set my computer to quite mode that's why it's running so slow.
# Now it's solved
```

## Notes

- Large inputs (e.g., 10k by 10k) can take forever.