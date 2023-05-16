"""
Quick Sort is an efficient, recursive divide-and-conquer based sorting algorithm. 
It works by selecting a pivot element from the array and partitioning the other elements into two sub-arrays, 
according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively. 
This process continues until all elements are sorted.
"""

# Quick Sort


import unittest


def quick_sort(arr, left, right):
    if left >= right:
        return

    i = left
    j = right
    pivot = arr[left]

    while i < j:
        while arr[i] <= pivot and i < j:
            i += 1
        while arr[j] > pivot and i <= j:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]

    quick_sort(arr, left, j - 1)
    quick_sort(arr, j + 1, right)


# Best-Case Time complexity = O(nlogn)
# Average-Case Time complexity = O(nlogn)
# Worst-Case Time complexity = O(n^2)
# Space complexity = O(logn)


class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        arr = [3, 4, 5, 2, 1]
        quick_sort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

        arr = [1]
        quick_sort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1])

        arr = []
        quick_sort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [])

        arr = [-2, -4, -3, -1]
        quick_sort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [-4, -3, -2, -1])

        arr = [0]
        quick_sort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [0])


if __name__ == "__main__":
    unittest.main()
