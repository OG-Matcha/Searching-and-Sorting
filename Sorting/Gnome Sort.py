"""
Gnome Sort is an in-place sorting algorithm based on the idea of a garden gnome sorting his flower pots. 
It works by comparing elements at adjacent indices and swapping them if they are out of order. 
This process is repeated until the list is sorted.
"""

# Gnome Sort

def gnome_sort(arr):
    pos = 0

    while pos < len(arr):
        if pos == 0 or arr[pos] >= arr[pos - 1]:
            pos += 1
        else:
            arr[pos], arr[pos - 1] = arr[pos - 1], arr[pos]
            pos -= 1

# Best-Case Time complexity = O(n)
# Average-Case Time complexity = O(n^2)
# Worst-Case Time complexity = O(n^2)
# Space complexity = O(1)

import unittest
 
class TestGnomeSort(unittest.TestCase):
    def test_gnome_sort(self):
        arr = [3, 7, 4, 9, 5, 2, 6, 1]
        gnome_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7 ,9])

        arr = [1]
        gnome_sort(arr)
        self.assertEqual(arr,[1])

        arr = [2,-1]
        gnome_sort(arr)
        self.assertEqual(arr,[-1 ,2])

        arr = []
        gnome_sort(arr)
        self.assertEqual(arr, [])
 
if __name__ == '__main__':
    unittest.main()