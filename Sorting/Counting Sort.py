"""
Counting Sort is an efficient sorting algorithm that uses a range of values as keys to count the occurrences of each value. 
It then uses this information to sort the elements in linear time. 
Counting Sort is a stable sorting algorithm and is often used as a subroutine in other sorting algorithms.
"""

# Counting Sort


def counting_sort(arr, maxi, mini):
    size = maxi - mini + 1
    length = len(arr)

    count = [0] * size
    output = [0] * length

    for i in arr:
        count[i - mini] += 1

    for i in range(1, size):
        count[i] += count[i - 1]

    i = length - 1
    while i >= 0:
        output[count[arr[i] - mini] - 1] = arr[i]
        count[arr[i] - mini] -= 1
        i -= 1

    for i, v in enumerate(output):
        arr[i] = v


# Best-Case Time complexity = O(n + k) where k is the range of input
# Average-Case Time complexity = O(n + k)
# Worst-Case Time complexity = O(n + k)
# Space complexity = O(n + k)


import unittest


class TestCountingSort(unittest.TestCase):
    def test_counting_sort(self):
        arr = [2, 5, 3, 0, 2, 3, 0, 3]
        maxi = 5
        mini = 0

        counting_sort(arr, maxi, mini)

        self.assertEqual(arr, [0, 0, 2, 2, 3, 3, 3, 5])

        arr = [1, 4, 1, 2, 7, 5, 2]
        maxi = 7
        mini = 1

        counting_sort(arr, maxi, mini)

        self.assertEqual(arr, [1, 1, 2, 2, 4, 5, 7])

    def test_counting_sort_with_negative(self):
        arr = [-5, -44, 5, 12, 11, 6, -6]
        maxi = 12
        mini = -44

        counting_sort(arr, maxi, mini)

        self.assertEqual(arr, [-44, -6, -5, 5, 6, 11, 12])

    def test_counting_sort_empty(self):
        arr = []
        maxi = 0
        mini = 0

        counting_sort(arr, maxi, mini)

        self.assertEqual(arr, [])


if __name__ == "__main__":
    unittest.main()
