"""
Radix sort is an efficient sorting algorithm that sorts elements in a given array by comparing the digits of each element. 
It works by starting with the least significant digit and sorting the elements based on their values. 
It then moves to the next most significant digit and continues sorting until all digits have been compared. 
Radix sort is a stable sorting algorithm, 
meaning that elements with equal values will remain in the same order after being sorted.
"""

# Radix Sort


def radix_sort(arr):
    if not arr:
        return arr

    maxi = max(arr)
    max_len = 1

    while maxi > 9:
        max_len += 1
        maxi /= 10

    for i in range(max_len):
        buckets = [[] for _ in range(10)]
        for j in arr:
            digit = j // 10**i % 10
            buckets[digit].append(j)
        arr = [x for bucket in buckets for x in bucket]
    return arr


# Best-Case Time complexity = O(n * k) where k is the maximum number of digits.
# Average-Case Time complexity = O(n * k)
# Worst-Case Time complexity = O(n * k)
# Space complexity = O(n + k)

import unittest


class TestRadixSort(unittest.TestCase):
    def test_radix_sort(self):
        arr = [170, 45, 75, 90, 802, 24, 2, 66]
        self.assertEqual(radix_sort(arr), [2, 24, 45, 66, 75, 90, 170, 802])

        arr = [3, 5, 2, 8]
        self.assertEqual(radix_sort(arr), [2, 3, 5, 8])

        arr = [7, 4, 9, 0]
        self.assertEqual(radix_sort(arr), [0, 4, 7, 9])

        arr = [1, 6, 3]
        self.assertEqual(radix_sort(arr), [1, 3, 6])

        arr = [54321, 12345]
        self.assertEqual(radix_sort(arr), [12345, 54321])

        arr = [0]
        self.assertEqual(radix_sort(arr), [0])

        arr = []
        self.assertEqual(radix_sort(arr), [])


if __name__ == "__main__":
    unittest.main()
