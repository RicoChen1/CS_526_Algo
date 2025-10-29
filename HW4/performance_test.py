#!/usr/bin/env python3
"""
Performance test for right triangles counting algorithm.
Tests the algorithm with various data sizes to ensure it meets the 30-second requirement.
"""

import time
import random
from rightTriangles import count_right_triangles


def generate_test_points(n, max_coord=1000):
    """
    Generate n random points for testing.
    
    Args:
        n: Number of points to generate
        max_coord: Maximum coordinate value
        
    Returns:
        list: List of (x, y) tuples
    """
    points = set()
    while len(points) < n:
        x = random.randint(-max_coord, max_coord)
        y = random.randint(-max_coord, max_coord)
        points.add((x, y))
    
    return list(points)


def performance_test():
    """
    Run performance tests with different data sizes.
    """
    test_sizes = [100, 500, 1000, 2000, 3000]
    
    print("Right Triangles Algorithm Performance Test")
    print("=" * 50)
    print(f"{'Size':<8} {'Time(s)':<10} {'Result':<10} {'Status'}")
    print("-" * 50)
    
    for n in test_sizes:
        # Generate test data
        points = generate_test_points(n)
        
        # Measure execution time
        start_time = time.time()
        result = count_right_triangles(points)
        end_time = time.time()
        
        execution_time = end_time - start_time
        status = "✓ PASS" if execution_time < 30 else "✗ FAIL"
        
        print(f"{n:<8} {execution_time:<10.3f} {result:<10} {status}")
        
        # If it takes too long, warn and break
        if execution_time > 30:
            print(f"\nWARNING: Algorithm exceeded 30 seconds for n={n}")
            break
    
    print("-" * 50)
    print("Performance test completed.")


def stress_test():
    """
    Run a stress test with maximum reasonable size.
    """
    print("\nStress Test (Large Dataset)")
    print("=" * 30)
    
    # Test with a large dataset
    n = 5000
    print(f"Generating {n} random points...")
    points = generate_test_points(n, max_coord=10000)
    
    print(f"Running algorithm on {n} points...")
    start_time = time.time()
    result = count_right_triangles(points)
    end_time = time.time()
    
    execution_time = end_time - start_time
    status = "✓ PASS" if execution_time < 30 else "✗ FAIL"
    
    print(f"Result: {result} right triangles")
    print(f"Time: {execution_time:.3f} seconds")
    print(f"Status: {status}")


if __name__ == "__main__":
    # Set random seed for reproducible results
    random.seed(42)
    
    # Run performance tests
    performance_test()
    
    # Run stress test
    stress_test()