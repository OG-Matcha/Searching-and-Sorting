"""
Heap Sort is an efficient sorting algorithm that uses a binary heap data structure to sort elements in an array. 
It works by first building a heap from the elements of the array, 
then repeatedly removing the largest element from the heap and placing it at the end of the sorted array.
"""

# Heap Sort


def heapify(arr, length, i):
    maxi = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < length and arr[left] > arr[maxi]:
        maxi = left
    if right < length and arr[right] > arr[maxi]:
        maxi = right
    if maxi != i:
        arr[i], arr[maxi] = arr[maxi], arr[i]
        heapify(arr, length, maxi)


def heap_sort(arr):
    length = len(arr)

    for i in range(length // 2 - 1, -1, -1):
        heapify(arr, length, i)

    for i in range(length - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# Best-Case Time complexity = O(nlogn)
# Average-Case Time complexity = O(nlogn)
# Worst-Case Time complexity = O(nlogn)
# Space complexity = O(1)

import unittest


class TestHeapSort(unittest.TestCase):
    def test_heap_sort(self):
        arr = [3, 4, 5, 6, 7, 8]
        heap_sort(arr)
        self.assertEqual(arr, [3, 4, 5, 6, 7, 8])

        arr = [8, 7, 6, 5, 4, 3]
        heap_sort(arr)
        self.assertEqual(arr, [3, 4, 5, 6, 7, 8])

        arr = [1]
        heap_sort(arr)
        self.assertEqual(arr, [1])

        arr = []
        heap_sort(arr)
        self.assertEqual(arr, [])


if __name__ == "__main__":
    unittest.main()
