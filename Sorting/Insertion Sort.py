"""
Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. 
It iterates through an array and removes one element per iteration, 
finds the location it belongs to in the sorted list, and inserts it there. 
It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
"""

# Insertion Sort


def insertion_sort(arr):
    length = len(arr)

    for i in range(length - 1):
        key = arr[i + 1]
        temp = i

        while temp >= 0 and key < arr[temp]:
            arr[temp + 1] = arr[temp]
            temp -= 1

        arr[temp + 1] = key


# Best-Case Time complexity = O(n)
# Average-Case Time complexity = O(n^2)
# Worst-Case Time complexity = O(n^2)
# Space complexity = O(1)


import unittest


class InsertionSortTest(unittest.TestCase):
    def test_insertion_sort(self):
        arr = [3, 2, 4, 1]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4])

        arr = [1, 2, 3]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3])

        arr = [4]
        insertion_sort(arr)
        self.assertEqual(arr, [4])

        arr = []
        insertion_sort(arr)
        self.assertEqual(arr, [])


if __name__ == "__main__":
    unittest.main()
