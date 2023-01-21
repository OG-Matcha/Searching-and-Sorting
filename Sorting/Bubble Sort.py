"""
Bubble Sort: is an algorithm that compares adjacent elements of an array and swaps them if they are in the wrong order. 
This process is repeated until all elements are in the correct order. 
Bubble Sort is a simple sorting algorithm that is relatively inefficient for larger datasets.
"""

# Bubble Sort


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Best-Case Time complexity = O(n) 
# Average-Case Time complexity = O(n^2) 
# Worst-Case Time complexity = O(n^2)
# Space complexity = O(1)


import unittest

class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort(self):
        arr = [3, 2, 4, 1]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4])

        arr = [5, 4, 3, 2]
        bubble_sort(arr)
        self.assertEqual(arr, [2, 3, 4, 5])

        arr = [1]
        bubble_sort(arr)
        self.assertEqual(arr, [1])

        arr = []
        bubble_sort(arr)
        self.assertEqual(arr, [])

        
if __name__ == '__main__': 
    unittest.main()
