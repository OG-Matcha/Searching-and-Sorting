"""
Exponential Search: is an algorithm, It is used when the element to be searched is not frequently found. 
It starts by comparing x with the value of the element present at the first position, 
if they are not equal then it starts comparing x with the value of the element present at 2^0 th position, then 2^1, 2^2 and so on.
"""

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
    if not arr:
        return -1
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


import unittest


class TestExponentialSearch(unittest.TestCase):
    def test_exponential_search(self):
        arr = [1, 2, 3, 4, 5]
        target = 3
        self.assertEqual(exponential_search(arr, target), 2)

    def test_target_not_in_array(self):
        arr = [1, 2, 3, 4, 5]
        target = 6
        self.assertEqual(exponential_search(arr, target), -1)

    def test_empty_array(self):
        arr = []
        target = 6
        self.assertEqual(exponential_search(arr, target), -1)

    def test_one_element_array(self):
        arr = [3]
        target = 3
        self.assertEqual(exponential_search(arr, target), 0)

    def test_target_at_beginning(self):
        arr = [3, 4, 5, 6]
        target = 3
        self.assertEqual(exponential_search(arr, target), 0)

    def test_target_at_end(self):
        arr = [3, 4, 5, 6]
        target = 6
        self.assertEqual(exponential_search(arr, target), 3)


if __name__ == "__main__":
    unittest.main()
