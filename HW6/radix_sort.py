import sys
import random

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Store count of occurrences, in count[] array
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # let count[i] hold actual position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    #To build output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # cp output array to arr[], now arr hold sorted num, according to current digit
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
   
    if not arr:     # Find max num to know number of digits
        return arr
    max1 = max(arr)

    # counting sort for every digit. 
    # Note: instead of passing digit number, exp is passed. exp is 10^i where i is current digit number
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

""" Aux checker"""
def check_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

""" Display sorting check result """
def run_test(filename):
    print(f"\n{'='*20} Testing with {filename} {'='*20}")
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
            if not content:
                print("File is empty.")
                return
            original_data = list(map(int, content.split()))
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return

    print(f"Input Data Size: {len(original_data)}")
    data_copy = original_data.copy()
    print("\n--- Radix Sort ---")
    sorted_data = radix_sort(data_copy)
    print(f"Sorted Data: {sorted_data}")
    print(f"Is Sorted: {check_sorted(sorted_data)}")

if __name__ == "__main__":
    files = ['HW6/input_small.txt', 'HW6/input_medium.txt', 'HW6/input_large.txt']
    for f in files:
        run_test(f)
