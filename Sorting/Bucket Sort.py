"""
Bucket sort is a sorting algorithm that works by distributing elements into a number of buckets, 
then sorting the elements within each bucket. 
It is an efficient algorithm for sorting small to medium-sized data sets. 
Bucket sort is often used as part of a more complex sorting algorithm, 
or as a way to optimize the performance of other algorithms.
"""

# Bucket Sort


def bucket_sort(arr):
    if not arr:
        return []

    maxi = max(arr)
    size = maxi / len(arr)

    buckets = [[] for _ in range(len(arr))]

    for num in arr:
        j = int(num / size)
        if j != len(arr):
            buckets[j].append(num)
        else:
            buckets[len(arr) - 1].append(num)

    for i in range(len(arr)):
        buckets[i] = sorted(buckets[i])

    sorted_arr = []
    for i in range(len(arr)):
        sorted_arr += buckets[i]

    return sorted_arr


# Best-Case Time complexity = O(n + k) where k is the number of buckets
# Average-Case Time complexity = O(n + k)
# Worst-Case Time complexity = O(n^2)
# Space complexity = O(n + k)

import unittest


class TestBucketSort(unittest.TestCase):
    def test_bucket_sort(self):
        array = [2, 5, 3, 0, 2, 3, 0, 3]
        self.assertEqual(bucket_sort(array), [0, 0, 2, 2, 3, 3, 3, 5])

        array = [3.2, 4.5, 1.9]
        self.assertEqual(bucket_sort(array), [1.9, 3.2, 4.5])

        array = []
        self.assertEqual(bucket_sort(array), [])


if __name__ == "__main__":
    unittest.main()
