# Exponential Search


def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= target:
        i <<= 1
    return binary_search(arr, i >> 1, min(i, len(arr) - 1), target)


# Best-Case Time complexity = O(1)
# Average-Case Time complexity = O(log n)
# Worst-Case Time complexity = O(log n)
# Space complexity = O(1)


arr = [1, 4, 6, 9, 12, 15, 16, 25]
target = 16

result = exponential_search(arr, target)

if result == -1:
    print("Element not found")
else:
    print(f"Element found at index {result}")
