# Linear Search


def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i
    else:
        return -1


# Best-Case Time complexity = O(1)
# Average-Case Time complexity = O(n)
# Worst-Case Time complexity = O(n)
# Space complexity = O(1)

arr = [1, 4, 6, 9, 12, 15, 16, 25]
target = 16

result = linear_search(arr, target)

if result == -1:
    print("Element not found")
else:
    print(f"Element found at index {result}")
