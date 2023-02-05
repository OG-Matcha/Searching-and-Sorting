"""
Double selection sort is a sorting algorithm that works by repeatedly selecting the smallest 
and largest elements from an unsorted list, and then swapping them with the elements at the beginning and end of the list. 
This process is repeated until the list is sorted.
"""

# Double Selection Sort


def double_selection_sort(arr):
    length = len(arr)

    for i in range(length // 2):
        min_idx = i
        max_idx = length - i - 1

        for j in range(i, length - i):
            if arr[j] < arr[min_idx]:
                min_idx = j
            if arr[j] > arr[max_idx]:
                max_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        if i == max_idx:
            max_idx = min_idx

        arr[length - i - 1], arr[max_idx] = arr[max_idx], arr[length - i - 1]


# Best-Case Time complexity = O(n^2)
# Average-Case Time complexity = O(n^2)
# Worst-Case Time complexity = O(n^2)
# Space complexity = O(1)

import unittest


class TestDoubleSelectionSort(unittest.TestCase):
    def test_double_selection_sort(self):
        arr = [5, 3, 4, 1, 2]
        double_selection_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

        arr = [3, 1]
        double_selection_sort(arr)
        self.assertEqual(arr, [1, 3])

        arr = [1]
        double_selection_sort(arr)
        self.assertEqual(arr, [1])

        arr = []
        double_selection_sort(arr)
        self.assertEqual(arr, [])


if __name__ == "__main__":
    unittest.main()
