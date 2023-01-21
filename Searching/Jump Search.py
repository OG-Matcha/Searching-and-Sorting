"""
Jump Search: It is also a searching algorithm. 
It works by first checking the element at the current index and then jumping a fixed number of steps to check the next element. 
It is faster than a linear search but slower than a binary search.
"""

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


import unittest


class TestJumpSearch(unittest.TestCase):
    def test_jump_search(self):
        arr = [1, 2, 3, 4, 5, 6, 7]

        self.assertEqual(jump_search(arr, 1), 0)
        self.assertEqual(jump_search(arr, 2), 1)
        self.assertEqual(jump_search(arr, 3), 2)
        self.assertEqual(jump_search(arr, 4), 3)
        self.assertEqual(jump_search(arr, 5), 4)
        self.assertEqual(jump_search(arr, 6), 5)
        self.assertEqual(jump_search(arr, 7), 6)

    def test_not_found_in_array(self):
        arr = [1, 2, 3]

        self.assertEqual(jump_search(arr, 4), -1)


if __name__ == "__main__":
    unittest.main()
