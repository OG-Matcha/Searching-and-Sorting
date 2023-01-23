"""
Selection Sort: is an in-place comparison sorting algorithm. 
It works by selecting the smallest element from the unsorted list and placing it at the beginning of the sorted list. 
This process is repeated until all elements are sorted.
"""

# Selection Sort


def selection_sort(arr):
    length = len(arr)

    for i in range(length):
        mini = i

        for j in range(i + 1, length):
            if arr[j] < arr[mini]:
                mini = j

        arr[mini], arr[i] = arr[i], arr[mini]


# Best-Case Time complexity = O(n^2)
# Average-Case Time complexity = O(n^2)
# Worst-Case Time complexity = O(n^2)
# Space complexity = O(1)

import unittest


class SelectionSortTest(unittest.TestCase):
    def test_selection_sort(self):
        arr = [3, 2, 4, 1]
        selection_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4])

        arr = [7, 5, 2, 4, 3, 9]
        selection_sort(arr)
        self.assertEqual(arr, [2, 3, 4, 5, 7, 9])

        arr = [-1]
        selection_sort(arr)
        self.assertEqual(arr, [-1])

        arr = []
        selection_sort(arr)
        self.assertEqual(arr, [])


if __name__ == "__main__":
    unittest.main()
