# Q1 Flood

## Key Ideas
- Greedy Algo: Always fix the largest current crack first. This reduces the biggest source of leakage ASAP.
- Priority queue, in form of max-heap: Quickly find and rm the largest crack in each time unit.
- Lazy growth (delta): All unfixed cracks grow by +1 each time t+1. Instead of adding +1 to each crack every time, we maintain a single global var `delta` to do this growth. This prevent from touching all the elements in every round.


## Why Greedy?
- Bigger cracks leak more water per time.
- Delay fix a big crack costs more leakage both now and in future rounds (as everything grows up).


## Note: Why Not “Array + Scan Everyone”
- As `O(n^2)`, it's too slow for large inputs.

## Instead, Use Max-Heap (Priority Q)
- A PQ gives fast ops:
  - Insert a single crack (should be `O(log n)`).
  - Rm the largest crack (should be`O(log n)`).
- Which is greedy.
- Notice that Python’s `heapq` the priority queue is implemented by binary heap, a binary tree structure stored in an array layout. It's not a simple linear queue; it is a tree-shaped data structure optimized for fast min/max retrieval.
- We use a “max-heap” behavior by pushing negative values into heapq.


## How the Lazy Growth Works
- All unfixed cracks grow together by +1, at end of each round.
- Maintain global `delta` (the number of growth steps applied).
- Each crack is stored as `stored = actual_size - delta`.
- When need the current size, recover it as `stored + delta`.
- Such avoid repeatedly adding +1 to every item in data struct.

## Files
- `Exam_2/flood_solver.py`
- `Exam_2/test_flood.py`
- Sample inputs:
  - `Exam_2/flood_1.txt`
  - `Exam_2/flood_2.txt`

## How to Run
```powershell
# Run solver on one file
python Exam_2/flood_solver.py Exam_2/flood_1.txt
python Exam_2/flood_solver.py Exam_2/flood_2.txt

# Run both tests automatically
python Exam_2/test_flood.py
```

## Expected Behavior on Samples. Format Shortened
- `flood_1.txt`: Safe
- `flood_2.txt`: Evacuate at time 1
- `flood_3.txt`: Safe
- `flood_4.txt`: Evacuate at time 7
- `flood_5.txt`: Safe
- `flood_6.txt`: Evacuate at time 439
- `flood_7.txt`: Safe
- `flood_8.txt`: Evacuate at time 293654
- `flood_9.txt`: Safe
- `flood_10.txt`: Safe
- `flood_11.txt`: Safe
- `flood_12.txt`: Evacuate at time 3

## Output Format
- If flooding occurs, print three lines:
  - `FLOOD`
  - `<time_unit_of_flooding>`
  - `<floodwater_units_at_that_time>`
- If flooding does not occur, print two lines:
  - `SAFE`
  - `<maximum_floodwater_ever_reached>`

---

# Q2 SKI

## Program Description
- Reads a mountain as matrix of altitude values `m x n`.
- Finds longest path, where each next cell has strictly lower altitude.
- Each cell can move to any of 8 neighbors/direction: horizontal, vertical, diagonal.
- Print  path length measured in num of moves (edges).

## Key Ideas
- Strictly decrease move form a DAG (no cycles), so longest path well-defined.
- Use DFS + memo:
  - `dp[r][c]` stores longest path length (cells) starting @ cell `(r, c)`.
  - For each cell, try all 8 direction that has lower altitude, then take the best.
  - Memoization ensures each cell only get computed once.
- Then convert to moves count: moves = cells - 1.

## Time Complexity
- `O(m * n)`

## Files
- `ski.py` — solver script (reads stdin and print longest moves).
- Inputs:
  - `Exam_2/ski_input1.txt`
  - `Exam_2/ski_input2.txt`
  - `Exam_2/ski_input3.txt`

## How to Run
```powershell
Get-Content .\Exam_2\ski_input1.txt | python .\ski.py
Get-Content .\Exam_2\ski_input2.txt | python .\ski.py
Get-Content .\Exam_2\ski_input3.txt | python .\ski.py
```
