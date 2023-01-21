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


import unittest


class TestRecursiveTernarySearch(unittest.TestCase):
    def test_recursive_ternary_search(self):
        arr = [1, 2, 3, 4, 5]
        left = 0
        right = len(arr) - 1
        target = 4

        result = recursive_ternary_search(arr, left, right, target)

        self.assertEqual(result, 3)

    def test_recursive_ternary_search_not_found(self):
        arr = [1, 2, 3, 4]
        left = 0
        right = len(arr) - 1
        target = 5

        result = recursive_ternary_search(arr, left, right, target)

        self.assertEqual(result, -1)

    def test_iterative_ternary_search(self):
        arr = [1, 2, 3, 4, 5]
        left = 0
        right = len(arr) - 1
        target = 4

        result = iterative_ternary_search(arr, left, right, target)

        self.assertEqual(result, 3)

    def test_iterative_ternary_search_not_found(self):
        arr = [1, 2, 3]
        left = 0
        right = len(arr) - 1
        target = 4

        result = iterative_ternary_search(arr, left, right, target)

        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
