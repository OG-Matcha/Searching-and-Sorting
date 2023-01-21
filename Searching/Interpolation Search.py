"""
Interpolation Search: is an algorithm that can be used to search for a particular value in a sorted array, 
it assumes that the values in the array are uniformly distributed. 
It estimates the position of the target value by using a formula based on the array's values at its first and last positions.
"""

# Interpolation Search

"""
 y2 - y1     y key - y1
--------- = ------------   =>  x key = (y key - y1) * (x2 - x1) // (y2 - y1) + x1
 x2 - x1     x key - x1

"""


def interpolation_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right and arr[left] <= target <= arr[right]:
        if arr[left] == target:
            return left

        mid = (target - arr[left]) * (right - left) // (arr[right] - arr[left]) + left

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# Best-Case Time complexity = O(1)
# Average-Case Time complexity = O(log log n)
# Worst-Case Time complexity = O(n)
# Space complexity = O(1)


import unittest


class TestInterpolationSearch(unittest.TestCase):
    def test_interpolation_search_found(self):
        arr = [1, 2, 3, 4, 5]
        target = 3
        result = interpolation_search(arr, target)
        self.assertEqual(result, 2)

    def test_interpolation_search_not_found(self):
        arr = [1, 2, 3, 4, 5]
        target = 6
        result = interpolation_search(arr, target)
        self.assertEqual(result, -1)

    def test_interpolation_search_empty_array(self):
        arr = []
        target = 6
        result = interpolation_search(arr, target)
        self.assertEqual(result, -1)

    def test_interpolation_search_single_element(self):
        arr = [3]  # single element array
        target = 3  # element in array
        result = interpolation_search(arr, target)  # search for element
        self.assertEqual(result, 0)  # should return index 0


if __name__ == "__main__":
    unittest.main()
