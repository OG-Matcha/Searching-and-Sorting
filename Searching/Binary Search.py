"""
Binary Search: is a search algorithm that finds the position of a target value within a sorted array. 
It compares the target value to the middle element of the array; 
if they are unequal, the half in which the target cannot lie is eliminated and the search continues on the remaining half until it is successful.
"""

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


# Best-Case Time complexity = O(1)
# Average-Case Time complexity = O(log n)
# Worst-Case Time complexity = O(log n)
# Space complexity = O(log n)


# Iterative Binary Search


def iterative_binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return -1


# Best-Case Time complexity = O(1)
# Average-Case Time complexity = O(log n)
# Worst-Case Time complexity = O(log n)
# Space complexity = O(1)


import unittest


class TestBinarySearch(unittest.TestCase):
    def test_iterative_binary_search(self):
        arr = [1, 2, 3, 4, 5]
        target = 3

        result = iterative_binary_search(arr, target)

        self.assertEqual(result, 2)

    def test_iterative_binary_search_not_found(self):
        arr = [1, 2, 3, 4, 5]
        target = 6

        result = iterative_binary_search(arr, target)

        self.assertEqual(result, -1)

    def test_recursive_binary_search(self):
        arr = [1, 2, 3, 4, 5]
        left = 0
        right = len(arr) - 1
        target = 3

        result = recursive_binary_search(arr, left, right, target)

        self.assertEqual(result, 2)

    def test_recursive_binary_search_not_found(self):
        arr = [1, 2, 3, 4, 5]
        left = 0
        right = len(arr) - 1
        target = 6

        result = recursive_binary_search(arr, left, right, target)

        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
