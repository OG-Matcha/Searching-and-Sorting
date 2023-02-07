"""
Comb Sort is an improvement of the Bubble Sort algorithm. 
It works by comparing elements that are a certain distance apart and then swapping them if they are out of order. 
The distance between elements starts out large and is reduced with each iteration until it reaches 1, 
at which point the list is sorted.
"""

# Comb Sort


def comb_sort(arr):
    length = len(arr)
    gap = length
    swap = True

    while gap != 1 or swap:
        gap = gap * 10 // 13

        if gap < 1:
            gap = 1

        swap = False

        for i in range(length - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swap = True


# Best-Case Time complexity = O(nlogn)
# Average-Case Time complexity = O(n^2/2^p) wherre p is the number of increments
# Worst-Case Time complexity = O(n^2)
# Space complexity = O(1)


import unittest


class TestCombSort(unittest.TestCase):
    def test_comb_sort(self):
        arr = [3, 4, 2, 5, 1]
        comb_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

        arr = [9, 8, 7, 6]
        comb_sort(arr)
        self.assertEqual(arr, [6, 7, 8, 9])

        arr = [1]
        comb_sort(arr)
        self.assertEqual(arr, [1])

        arr = []
        comb_sort(arr)
        self.assertEqual(arr, [])


if __name__ == "__main__":
    unittest.main()
