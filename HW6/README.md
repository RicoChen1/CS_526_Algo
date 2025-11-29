# Sorting & Stable Marriage Algorithms

## Algo Description

### 1. Merge Sort

**Core Idea**: Divide & Conquer. Recursively split array in half until size 1, then merge sorted halves back together.

- **Key Op**: `merge` (combines two sorted lists).

### 2. Quick Sort

**Core Idea**: Divide & Conquer. Pick a 'pivot', partition array (left < pivot, right > pivot), then sort partitions recursively.

- **Key Op**: `partition` (places pivot in correct spot).

### 3. Insertion Sort

**Core Idea**: Build sorted list one item at a time. Take next element and insert into correct spot in already-sorted part.

- **Analogy**: Sorting playing cards in your hand.

### 4. Radix Sort

**Core Idea**: Non-comparative. Sorts integers digit-by-digit (LSD to MSD) using a stable subroutine (like Counting Sort).

- **Best for**: Integers or fixed-len strings.

### 5. Gale-Shapley (Stable Marriage)

**Core Idea**: Finds stable matching between two groups (e.g., Men/Women).

- **Process**: Men propose to best choice. Women accept or swap if new suitor is better. Repeat until all matched.
- **Result**: Stable (no pair prefers each other over current partners).

## Performance Comparison

| Algorithm          | Time (Avg)    | Time (Worst)  | Space       | Stable? |
| ------------------ | ------------- | ------------- | ----------- | ------- |
| **Merge Sort**     | $O(n \log n)$ | $O(n \log n)$ | $O(n)$      | Yes     |
| **Quick Sort**     | $O(n \log n)$ | $O(n^2)$      | $O(\log n)$ | No      |
| **Insertion Sort** | $O(n^2)$      | $O(n^2)$      | $O(1)$      | Yes     |
| **Radix Sort**     | $O(nk)$       | $O(nk)$       | $O(n+k)$    | Yes     |
| **Gale-Shapley**   | $O(n^2)$      | $O(n^2)$      | $O(n^2)$    | N/A     |

_$k$ = num digits, $n$ = num elements._

### When to use which?

- **Insertion Sort**: Small data (<50), nearly sorted data, or $O(1)$ space needed.
- **Merge Sort**: Need stability, guaranteed $O(n \log n)$, or sorting Linked Lists.
- **Quick Sort**: Need speed (cache-friendly), stability not needed.
- **Radix Sort**: Sorting integers/strings, small range ($k$), need speed > $O(n \log n)$.
- **Gale-Shapley**: Need stable matching (e.g. residents -> hospitals).

## Run Tests

Run these commands in terminal:

```powershell
# 1. Gen random inputs
python HW6/generate_inputs.py

# 2. Run Sorting (Merge, Quick, Insertion)
python HW6/sorting.py

# 3. Run Radix Sort
python HW6/radix_sort.py

# 4. Run Gale-Shapley
python HW6/gale_shapley.py
```

## Notes

- Scripts read from `HW6/input_*.txt` or `HW6/marriage_*.txt`.
- Output shows **Sorted Data** / **Matches** + Verification.
- Large inputs (500+) print truncated output or just verification.
