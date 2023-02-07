"""
Odd-even sort, also known as brick sort, is a relatively simple sorting algorithm. 
It works by comparing all the elements in the list in pairs and swapping them if they are out of order. 
It then goes through the list again and swaps elements in the opposite order. 
This process is repeated until all elements are in order.
"""

# Odd-Even Sort


def odd_even_sort(arr):
    length = len(arr)
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(0, length - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

        for i in range(1, length - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False


# Best-Case Time complexity = O(n)
# Average-Case Time complexity = O(n^2)
# Worst-Case Time complexity = O(n^2)
# Space complexity = O(1)

import unittest


class TestOddEvenSort(unittest.TestCase):
    def test_odd_even_sort(self):
        arr = [3, 1, 4, 5, 2]
        odd_even_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

        arr = [5, 4, 3, 2]
        odd_even_sort(arr)
        self.assertEqual(arr, [2, 3, 4, 5])

        arr = [1]
        odd_even_sort(arr)
        self.assertEqual(arr, [1])

        arr = []
        odd_even_sort(arr)
        self.assertEqual(arr, [])


if __name__ == "__main__":
    unittest.main()
