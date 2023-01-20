"""
Interpolation Search: is an algorithm that can be used to search for a particular value in a sorted array, 
it assumes that the values in the array are uniformly distributed. 
It estimates the position of the target value by using a formula based on the array's values at its first and last positions.
"""

# Interpolation Search

"""
 y2 - y1     y key - y1
--------- = ------------   =>  x key = (y key - y1) * (x2 - x1) // (y2 - y1) + x1
 x2 - x1     x key - x1

"""


def interpolation_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (target - arr[left]) * (right - left) // (arr[right] - arr[left]) + left
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Best-Case Time complexity = O(1)
# Average-Case Time complexity = O(log log n)
# Worst-Case Time complexity = O(n)
# Space complexity = O(1)

arr = [1, 4, 6, 9, 12, 15, 16, 25]
target = 16

result = interpolation_search(arr, target)

if result == -1:
    print("Element not found")
else:
    print(f"Element found at index {result}")
