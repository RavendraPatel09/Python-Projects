import random
import time

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def time_search(func, arr, target):
    start = time.perf_counter()
    result = func(arr, target)
    elapsed = time.perf_counter() - start
    return result, elapsed

def main():
    size = int(input("Array size: "))
    arr = sorted(random.sample(range(size * 10), size))
    target = random.choice(arr)
    lin_result, lin_time = time_search(linear_search, arr, target)
    bin_result, bin_time = time_search(binary_search, arr, target)
    print(f"Searching for {target} in array of size {size}")
    print(f"Linear search: index {lin_result}, time {lin_time:.8f}s")
    print(f"Binary search: index {bin_result}, time {bin_time:.8f}s")

if __name__ == "__main__":
    main()
