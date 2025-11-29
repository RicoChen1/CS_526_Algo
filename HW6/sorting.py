import sys
import random

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that >= key, to 1 position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        # Find mid
        mid = len(arr) // 2
        # Divide elements
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L) # Sort first half
        merge_sort(R) # Sort second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if elements left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


# For Quick Sort
def partition(arr, low, high):
    i = (low - 1)         # smaller element index
    pivot = arr[high]     # Work as comparison reference

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition, and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

""" Aux checker"""
def check_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

""" Display sorting check result """"
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

    # Testing  Insertion Sort
    data_copy = original_data.copy()
    print("\n--- Insertion Sort ---")
    sorted_data = insertion_sort(data_copy)
    print(f"Sorted Data: {sorted_data}")
    print(f"Is Sorted: {check_sorted(sorted_data)}")

    # Test Merge Sort
    data_copy = original_data.copy()
    print("\n--- Merge Sort ---")
    sorted_data = merge_sort(data_copy)
    print(f"Sorted Data: {sorted_data}")
    print(f"Is Sorted: {check_sorted(sorted_data)}")

    # Test Quick Sort
    data_copy = original_data.copy()
    print("\n--- Quick Sort ---")
    sorted_data = quick_sort(data_copy, 0, len(data_copy) - 1)
    print(f"Sorted Data: {sorted_data}")
    print(f"Is Sorted: {check_sorted(sorted_data)}")

if __name__ == "__main__":
    files = ['HW6/input_small.txt', 'HW6/input_medium.txt', 'HW6/input_large.txt']
    for f in files:
        run_test(f)
