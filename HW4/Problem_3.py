import sys
from collections import defaultdict
from math import gcd


def count_right_triangles(points):
    """
    Count the number of right triangles that can be formed by the given points.
    
    Algorithm: Fix each point as the right angle vertex and count perpendicular vectors.
    
    Args:
        points: List of (x, y) tuples representing 2D points
        
    Returns:
        int: Number of right triangles
    """
    n = len(points)
    if n < 3:
        return 0
    
    total_count = 0
    
    # For each point as potential right angle vertex
    for i in range(n):
        px, py = points[i]
        
        # Dictionary to store direction vectors and their counts
        direction_count = defaultdict(int)
        
        # Calculate direction vectors from current point to all other points
        for j in range(n):
            if i == j:
                continue
                
            qx, qy = points[j]
            dx = qx - px
            dy = qy - py
            
            # Normalize the direction vector to avoid precision issues
            direction = normalize_vector(dx, dy)
            direction_count[direction] += 1
        
        # Count right triangles with current point as right angle vertex
        for direction, count in direction_count.items():
            # Find perpendicular direction
            dx, dy = direction
            perpendicular = (-dy, dx)  # Rotate 90 degrees counterclockwise
            
            if perpendicular in direction_count:
                # Each pair of perpendicular directions forms right triangles
                total_count += count * direction_count[perpendicular]
    
    return total_count


def normalize_vector(dx, dy):
    """
    Normalize a direction vector to its canonical form.
    
    This ensures that equivalent directions are represented identically,
    avoiding floating point precision issues.
    
    Args:
        dx, dy: Components of the direction vector
        
    Returns:
        tuple: Normalized direction vector (dx, dy)
    """
    if dx == 0 and dy == 0:
        return (0, 0)
    
    # Calculate GCD to reduce to simplest form
    g = gcd(abs(dx), abs(dy))
    dx //= g
    dy //= g
    
    # Ensure canonical representation (positive x, or zero x with positive y)
    if dx < 0 or (dx == 0 and dy < 0):
        dx = -dx
        dy = -dy
    
    return (dx, dy)


def read_input():
    """
    Read input from stdin according to the specified format.
    
    Returns:
        list: List of (x, y) tuples representing points
    """
    try:
        n = int(input().strip())
        points = []
        
        for _ in range(n):
            line = input().strip()
            x, y = map(int, line.split())
            points.append((x, y))
        
        return points
    
    except (ValueError, EOFError) as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """
    Main function to solve the right triangles counting problem.
    """
    # Read input points
    points = read_input()
    
    # Count right triangles
    result = count_right_triangles(points)
    
    # Output result in required format
    print(f"The number of right triangles is: {result}")


if __name__ == "__main__":
    main()