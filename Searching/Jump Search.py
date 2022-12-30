# Jump Search

import math


def jump_search(arr, target):

    start = 0
    step = int(math.sqrt(len(arr)))

    while arr[min(start, len(arr) - 1)] < target:
        start += step
        if start > len(arr):
            return -1

    for i in range(min(start, len(arr) - 1), -1, -1):
        if arr[i] == target:
            return i

    return -1


# Best-Case Time complexity = O(1)
# Average-Case Time complexity = O(√n)
# Worst-Case Time complexity = O(√n)
# Space complexity = O(1)


arr = [1, 4, 6, 9, 12, 15, 16, 25]
target = 16

result = jump_search(arr, target)

if result == -1:
    print("Element not found")
else:
    print(f"Element found at index {result}")
