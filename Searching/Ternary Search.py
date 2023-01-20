"""
Ternary Search: is a search algorithm that divides an array into three parts and then checks if the target value is in the left, middle, or right part. 
If the target value is found in the middle part, the search is successful. 
If the target value is in the left or right part, the search continues in that part until the target value is found or the end of the array is reached.
"""

# Ternary Search


def recursive_ternary_search(arr, left, right, target):
    if right > left:
        midl = left + (right - left) // 3
        midr = right - (right - left) // 3

        if arr[midl] == target:
            return midl
        if arr[midr] == target:
            return midr

        if arr[midl] > target:
            return recursive_ternary_search(arr, left, midl - 1, target)
        elif arr[midr] < target:
            return recursive_ternary_search(arr, midr + 1, right, target)
        else:
            return recursive_ternary_search(arr, midl + 1, midr - 1, target)

    return -1


# Best-Case Time complexity = O(1)
# Average-Case Time complexity = O(log n (base 3))
# Worst-Case Time complexity = O(log n (base 3))
# Space complexity = O(log n (base 3))


# Iterative Ternary Search


def iterative_ternary_search(arr, left, right, target):
    while right > left:
        midl = left + (right - left) // 3
        midr = right - (right - left) // 3

        if arr[midl] == target:
            return midl
        if arr[midr] == target:
            return midr

        if arr[midl] > target:
            right = midl - 1
        elif arr[midr] < target:
            left = midr + 1
        else:
            left = midl + 1
            right = midr - 1

    return -1


# Best-Case Time complexity = O(1)
# Average-Case Time complexity = O(log n (base 3))
# Worst-Case Time complexity = O(log n (base 3))
# Space complexity = O(1)


arr = [1, 4, 6, 9, 12, 15, 16, 25]
target = 16

left = 0
right = len(arr) - 1

result = recursive_ternary_search(arr, left, right, target)

if result == -1:
    print("Element not found")
else:
    print(f"Element found at index {result}")

result = iterative_ternary_search(arr, left, right, target)

if result == -1:
    print("Element not found")
else:
    print(f"Element found at index {result}")
