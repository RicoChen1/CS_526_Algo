import sys
sys.setrecursionlimit(20000) # Increase recursion max depth limit by python

def solve():
    # Input format (from stdin):
    # - First line: num of rows, m
    # - Second line: num of columns, n
    # - Next m lines: each contains n altitude integers
    # Read all input from stdin -> list of tokens
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        rows = int(next(iterator))
        cols = int(next(iterator))
    except StopIteration:
        return

    """
        Build altitude matrix. M[r][c] holds altitude at row r, col c.
    """
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(int(next(iterator)))
        matrix.append(row)

    # Memoization table: store max path length, start from each cell
    memo = [[-1 for _ in range(cols)] for _ in range(rows)] # -1 == not computed yet!

    directions = [ # 8 directions: horizontal, vertical, diagonal
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    def dfs(r, c):
        # DFS returns longest strictly-decreasing path length
        # Start from cell (r, c), measure in num of cells in path.
        # Use memo[r][c] to avoid recompute same state.
        if memo[r][c] != -1: # If already computed, return stored value
            return memo[r][c]

        max_len = 1  # Min path length == 1, this cell itself

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Boundary check
            if 0 <= nr < rows and 0 <= nc < cols:
                # Strictly decreasing condition
                if matrix[nr][nc] < matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))

        # Store result for (r, c), future calls could O(1)
        memo[r][c] = max_len
        return max_len

    # Iterate all cells, to find global max
    global_max = 0
    for r in range(rows):
        for c in range(cols):
            # Try starting a path at every cell; take the maximum
            global_max = max(global_max, dfs(r, c))

    # Expected output measures "number of moves" rather than "number of cells".
    # Note that each path of k cells has k-1 moves.
    # Convert cell-count to move-count for final printing.
    print(max(0, global_max - 1))

if __name__ == "__main__":
    solve()
