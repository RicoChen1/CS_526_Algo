
# Q1. Snowfall 

## Algo Description

1.  Reads number of days (n), and a list of cumulative snowfall totals from an input file, specified as cmd arg.
2.  Calculates daily snowfall amounts from cumulative totals.
3.  Calculates total snowfall over entire period.
4.  Uses sliding window, size = 3, iterate through daily snowfall amounts.
5.  For each 3-day size window, it calculates sum of snowfall.
6.  It checks if this 3-day sum is more than half of the total snowfall.
7.  If such a 3-day period is found, print `<input_file> solution: YES`; otherwise, `<input_file> solution: NO`.

## To Run Tests

```powershell
python snowfall.py snowfall_input1.txt
```
</br>

# Q2. Pandemic 

## Algo Description

1.  Reads grid size and a list of initially infected county coordinates from an input file specified as a command-line argument.
2.  Initializes a 2D grid representing state, note `1` means infected places and `0` for healthy.
3.  Enters a simulation loop that continues as long as new infections occur in a cycle (day).
4.  In each cycle, it identifies all healthy counties that have at least two infected neighbors (up, down, left, or right).
5.  These newly infected counties are recorded in a temporary list to ensure that all calculations for current Day_x are based on the state at the beginning of that day.
6.  After checking all counties, grid is updated with newly infected counties.
7.  The simulation stops when a full day passes with no new infections.
8.  Finally, it checks grid for any remaining healthy counties and prints `<input_file> solution: There are healthy counties left` or `<input_file> solution: There are no healthy counties left`.

## to Run Test

```powershell
python pandemic.py pandemic_input1.txt
```
</br>

# Q3. Shopping Cart

## Algo Description

The core is sliding window method. The "window" is a sub-array that slides over input main array. Here sub window represents the sequence of items being collected.

1.  **Init Field**:
    *   `max_len`: Store max number of items collected so far. (Init = 0)
    *   `start`: Left ptr of sliding window. Init = 0
    *   `baskets`: A dict (or hash map) to track of item categories current in "basket", also tracking their counts.

2.  **Iteration**:
    *   Iterate through  `aisles` array left to right, using `end` ptr, that represents most right side of window.
    *   For each `item` @ `aisles[end]`, add it on `baskets`.

3.  **Window Adjust**:
    *   After add an item, check if number of unique item categories in `baskets` has exceeded 2 `len(baskets) > 2`.
    *   If `len(baskets) > 2`, it means we have picked up a third category of item, which is not allowed. To fix this, shrink window from left side. Also, move `start` ptr to right.
    *   Decrement count of item @ `aisles[start]`. If its count == 0, completely remove that item category in `baskets`.
    *   Continue shrink the window until back to having at most 2 categories in `baskets`.

4.  **Update Maximum**:
    *   After a possible window expansion, update window size (`end - start + 1`) at each step of `end` ptr.
    *   Update `max_len` with window current size if larger than previous `max_len`.

5.  **Result**:
    *   After the loop finishes, `max_len` will hold the length of the longest subarray (contiguous sequence of aisles) that contains at most two distinct item categories. This is the maximum number of items we could have collected.

## To Run Tests

```powershell
python shopping_cart.py <input_file>
```
<br>

# Q4. Symbol Puzzle Game

## Algo Description

The algo validates puzzle board by checking for uniqueness of symbols in each row, column, and each sub-grid.

1.  **Initialization**:
    *   Board size n, set of allowed symbols got read from file.
    *   Size of sub-boards calc as sqrt of n.

2.  **Row & Column Verification**:
    *   IIterates through each row and column, simultaneously.
    *   Use set `row_symbols` and set `col_symbols`, tracking symbols encountered in current row & column.
    *   If a symbol found that already in corresponding set (and is not a '.'), then find a duplicate! So this board is invalid.

3.  **Sub-board**:
    *   Iterates through board by `sub_board_size`, visit top-left corner of each sub-board.
    *   For each sub-board, new set `sub_board_symbols` create.
    *   Walk through each cell inside sub-board.
    *   If a symbol found that already in `sub_board_symbols` set (and is not a '.'), then board invalid!


## To Run Tests

```powershell
python symbol_puzzle_game.py <input_file>
```
