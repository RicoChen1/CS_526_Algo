import sys

"""
    Simulate spread of virus, on grid map.
"""
def pandemic(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return

    # 1st line is grid size
    try:
        grid_size = int(lines[0].strip())
    except (ValueError, IndexError):
        print("Error: Invalid format for grid size.")
        return

    grid = [[0] * grid_size for _ in range(grid_size)] # Init grid

    # Subsequent lines = firstly infected place (Day 0 case)
    try:
        for line in lines[1:]:
            if not line.strip():
                continue
            parts = line.strip().split()
            row, col = int(parts[0]), int(parts[1])
            if 0 <= row < grid_size and 0 <= col < grid_size:
                grid[row][col] = 1 # 1 for infected
    except (ValueError, IndexError):
        print("Error: Invalid format! Exit")
        return

    while True: # Simulation loop
        newly_infected = []

        for r in range(grid_size):  # Find healthy places that will get infected
            for c in range(grid_size):
                if grid[r][c] == 0: # If location is 0 = healthy
                    infected_neighbors = 0
                    # Check neighbors
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < grid_size and 0 <= nc < grid_size and grid[nr][nc] == 1:
                            infected_neighbors += 1
                    
                    if infected_neighbors >= 2:
                        newly_infected.append((r, c))

        # If no new locations were infected, the spread stopped
        if not newly_infected:
            break

        # Update grid with newly infected locations
        for r, c in newly_infected:
            grid[r][c] = 1

    # Check if there are remaining healthy places
    has_healthy_county = False
    for r in range(grid_size):
        for c in range(grid_size):
            if grid[r][c] == 0:
                has_healthy_county = True
                break
        if has_healthy_county:
            break

    if has_healthy_county:
        print(f"{file_path} solution: There are healthy counties left")
    else:
        print(f"{file_path} solution: There are no healthy counties left")


# AI generated entry point for the script
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pandemic.py <path_to_input_file>")
    else:
        pandemic(sys.argv[1])
