"""
Problem 2: Shortest Num of Elements
Find min num of elements from array, whose sum >= target T.
Algorithm: Greedy
"""

"""
    Greedy algorithm 
    Args:
        arr: input array
        target: target value T
    
    Returns:
        minimum number of elements
"""
def solve_smallest_number(arr, target):

    sorted_arr = sorted(arr, reverse=True)  ## Descending order!
    
    # Greedy selection aux
    current_sum = 0
    count = 0
    
    for num in sorted_arr:  # Start from largest elements, from sorted ↓ array
        current_sum += num
        count += 1
        
        # Check if target is reached
        if current_sum > target:
            return count
    
    return count

def main():  ## Also handle input/output

    try: ## Parse input
        # Read input
        n = int(input().strip())
        target = int(input().strip())
        arr = list(map(int, input().strip().split()))
        
        # Verify input
        if len(arr) != n:
            print("Error: Array length mismatch")
            return
        
        result = solve_smallest_number(arr, target)
        
        # Format output
        arr_str = ','.join(map(str, arr))
        print(f"Input: {arr_str} Target: {target} Answer: {result}")
    
    ## Input error handle
    except ValueError as e: 
        print(f"Input error: {e}")
    except Exception as e:
        print(f"Execute error: {e}")

if __name__ == "__main__":
    main()