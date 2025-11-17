# Problem 1. Binary Search Tree

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
python HW5/bst.py
```

## Note:

- Duplicate values get auto ignored.
- Empty tree prints `(empty)`.
- For reproducible run, open `HW5/bst.py`, uncomment `random.seed(42)`.

# Q. Vowel-only Morse Sequences

## Algo Description

1. Read input file: first line is length `n`, second line is a string of `.` and `-`.
2. Use International Morse vowel codes: `A=.-`, `E=.`, `I=..`, `O=---`, `U=..-`.
3. Count the number of ways to split the string into these vowel codes using DP.
4. Print results in exact format:
   - `File Input: vowel_input<k>.txt`
   - `The Number of Vowel combinations is:  <count>`

## To Run Tests

```powershell
python HW5/vowel_morse.py HW5/vowel_input1.txt
python HW5/vowel_morse.py HW5/vowel_input2.txt
python HW5/vowel_morse.py HW5/vowel_input3.txt
python HW5/vowel_morse.py HW5/vowel_input4.txt
```

## Note

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
python HW5/longest_seq.py HW5/longest_seq1.txt
python HW5/longest_seq.py HW5/longest_seq2.txt
python HW5/longest_seq.py HW5/longest_seq3.txt
python HW5/longest_seq.py HW5/longest_seq4.txt
# HW5/longest_seq5.txt 和 HW5/longest_seq6.txt 可能非常大，运行时间较长
```

## Notes

- Algorithm uses dynamic programming with prefix maxima, time `O(n*m)` and space `O(n*m)`.
- Large inputs (e.g., 10k by 10k) can take long. Do not interrupt; consider running smaller files for screenshots.
