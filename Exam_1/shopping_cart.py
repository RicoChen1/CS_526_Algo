
import sys

def max_items(aisles):
    """
    Calc max number of items that can be collected from aisles, with constraint using sliding window.
    The window track a subarray of items, and 'baskets' dict that store count of item categories in that window.
    """
    max_len = 0  # max items collected so far
    start = 0    # start index of window
    baskets = {} # Basket Dick to store item and counts.

    # 'end' is right edge of window, which will expand to right side.
    for end in range(len(aisles)):
        item = aisles[end]
        baskets[item] = baskets.get(item, 0) + 1

        # When >= 2 categories in baskets, shrink window from the left by 'start'++.
        while len(baskets) > 2:
            left_item = aisles[start]
            baskets[left_item] -= 1
            if baskets[left_item] == 0:
                del baskets[left_item] # rm category if its count==0.
            start += 1

        # Update max length found
        max_len = max(max_len, end - start + 1)

    return max_len

# AI generated main and entry point for the script
def main():
    if len(sys.argv) != 2:
        print("Usage: python shopping_cart.py <input_file>")
        return

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
            aisles = lines[1].strip().split(',')
            result = max_items(aisles)
            print(f"{result} items were selected")
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_file}")
    except IndexError:
        print("Error: Input file is not in the correct format.")


if __name__ == "__main__":
    main()
