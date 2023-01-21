"""
Merge Sort: is a divide and conquer algorithm that divides a list into two halves, recursively sorts each half, 
and then merges the two sorted halves back together. 
It is an efficient, general-purpose sorting algorithm which produces a stable sort.
"""

# Merge Sort


def merge(left, right):
    result = []

    while len(left) and len(right):
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result += left if len(left) else right
    return result


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    return merge(merge_sort(left_arr), merge_sort(right_arr))


# Best-Case Time complexity = O(nlogn)
# Average-Case Time complexity = O(nlogn)
# Worst-Case Time complexity = O(nlogn)
# Space complexity = O(n)

import unittest


class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(merge_sort(arr), [1, 2, 3, 4, 5])

        arr = [1]
        self.assertEqual(merge_sort(arr), [1])

        arr = []
        self.assertEqual(merge_sort(arr), [])

        arr = [-4, -5]
        self.assertEqual(merge_sort(arr), [-5, -4])

        arr = [2, 1, 0]
        self.assertEqual(merge_sort(arr), [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
