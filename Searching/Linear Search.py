"""
Linear Search: is a simple search algorithm that looks for a specific value in an array 
by examining each element in sequence until a match is found or the end of the array is reached.
"""

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

import unittest


class TestLinearSearch(unittest.TestCase):
    def test_linear_search(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(linear_search(arr, 1), 0)
        self.assertEqual(linear_search(arr, 2), 1)
        self.assertEqual(linear_search(arr, 3), 2)
        self.assertEqual(linear_search(arr, 4), 3)
        self.assertEqual(linear_search(arr, 5), -1)


if __name__ == "__main__":
    unittest.main()
