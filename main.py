import timeit
import random
import pandas as pd

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Insertion Sort Implementation
def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

# Wrapper for Timsort using built-in sorted()
def timsort(arr):
    return sorted(arr)

# Function to measure execution time
def measure_time(func, arr):
    stmt = lambda: func(arr)
    return timeit.timeit(stmt, number=1)

# Generate datasets
sizes = [100, 1000, 5000]
results = []

for size in sizes:
    data = [random.randint(0, 10000) for _ in range(size)]
    results.append({
        "Size": size,
        "MergeSort": measure_time(merge_sort, data),
        "InsertionSort": measure_time(insertion_sort, data),
        "Timsort": measure_time(timsort, data)
    })

# Create and display DataFrame
df = pd.DataFrame(results)
print("\nРезультати вимірювання часу (в секундах):\n")
print(df)
