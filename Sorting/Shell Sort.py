"""
Shell Sort is an in-place comparison sorting algorithm that sorts elements by comparing elements that are far apart. 
It works by first comparing elements that are a certain number of positions away from each other, 
then reducing the gap between elements until all elements are compared. 
"""

# Shell Sort


def shell_sort(arr):
    length = len(arr)
    step = length // 2

    while step > 0:
        for i in range(step, length):
            temp = arr[i]
            j = i

            while j >= step and arr[j - step] > temp:
                arr[j] = arr[j - step]
                j -= step

            arr[j] = temp

        step //= 2


# Best-Case Time complexity = O(nlogn)
# Average-Case Time complexity = O(nlogn) O(n^1.25)
# Worst-Case Time complexity = O(n^2)
# Space complexity = O(logn)

import unittest


class TestShellSort(unittest.TestCase):
    def test_shell_sort(self):
        arr = [5, 4, 3, 2, 1]
        shell_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

        arr = [3, 4, 1]
        shell_sort(arr)
        self.assertEqual(arr, [1, 3, 4])

        arr = [3]
        shell_sort(arr)
        self.assertEqual(arr, [3])

        arr = []
        shell_sort(arr)
        self.assertEqual(arr, [])


if __name__ == "__main__":
    unittest.main()
