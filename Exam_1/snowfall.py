import sys

def algo(file_path):
    """
    Reads snowfall data from a file, determines if any 3 consecutive days 
    produced more than half of the total snowfall, and prints the result.
    """
    try:
        with open(file_path, 'r') as f:
            n_str = f.readline()
            if not n_str:
                print(f"{file_path} solution: NO")
                return
            n = int(n_str.strip())

            cumulative_str = f.readline()
            if not cumulative_str:
                print(f"{file_path} solution: NO")
                return
        
        cumulative_snowfall = [int(item) for item in cumulative_str.strip().replace(' ', ',').split(',')]

        if n < 3:
            print(f"{file_path} solution: NO")
            return

        total_snowfall = cumulative_snowfall[n - 1]

        if total_snowfall == 0:
            print(f"{file_path} solution: NO")
            return

        daily_snowfall = [0] * n
        daily_snowfall[0] = cumulative_snowfall[0]
        for i in range(1, n):
            daily_snowfall[i] = cumulative_snowfall[i] - cumulative_snowfall[i - 1]

        current_3_day_sum = sum(daily_snowfall[0:3])

        if current_3_day_sum * 2 > total_snowfall:
            print(f"{file_path} solution: YES")
            return

        for i in range(3, n):
            current_3_day_sum = current_3_day_sum - daily_snowfall[i - 3] + daily_snowfall[i]
            
            if current_3_day_sum * 2 > total_snowfall:
                print(f"{file_path} solution: YES")
                return
        
        print(f"{file_path} solution: NO")

    except (ValueError, IndexError) as e:
        print(f"Error processing input from {file_path}: {e}")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python snowfall.py <path_to_input_file>")
    else:
        algo(sys.argv[1])

