# Recursive Binary Search


def recursive_binary_search(arr, left, right, target):
    if left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            return recursive_binary_search(arr, mid + 1, right, target)
        elif arr[mid] > target:
            return recursive_binary_search(arr, left, mid - 1, target)
        else:
            return mid
    else:
        return -1


arr = [1, 4, 6, 9, 12, 15, 16, 25]
target = 16

left = 0
right = len(arr) - 1

result = recursive_binary_search(arr, left, right, target)

if result == -1:
    print("Element not found")
else:
    print(f"Element found at index {result}")

# Time complexity = O(log n)
# Space complexity = O(log n)


# Iterative Binary Search


def iterative_binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return -1


arr = [1, 4, 6, 9, 12, 15, 16, 25]
target = 24

left = 0
right = len(arr) - 1

result = iterative_binary_search(arr, target)

if result == -1:
    print("Element not found")
else:
    print(f"Element found at index {result}")

# Time complexity = O(log n)
# Space complexity = O(1)
