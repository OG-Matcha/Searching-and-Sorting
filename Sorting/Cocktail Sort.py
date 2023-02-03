"""
Cocktail sort, also known as bidirectional bubble sort, is an algorithm that sorts a given array in-place. 
It works by repeatedly comparing adjacent elements and swapping them if they are out of order. 
This sorting technique is similar to bubble sort, but it goes both ways, from left to right and from right to left.
"""

# Cocktail Sort


def cocktail_sort(arr):
    length = len(arr)
    swapped = True
    start = 0
    end = length - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1


# Best-Case Time complexity = O(n)
# Average-Case Time complexity = O(n^2)
# Worst-Case Time complexity = O(n^2)
# Space complexity = O(1)


import unittest


class TestCocktailSort(unittest.TestCase):
    def test_cocktail_sort(self):
        arr = [5, 1, 4, 2, 8]
        cocktail_sort(arr)
        self.assertEqual(arr, [1, 2, 4, 5, 8])

        arr = [9, 7, 5, 3]
        cocktail_sort(arr)
        self.assertEqual(arr, [3, 5, 7, 9])

        arr = [1]
        cocktail_sort(arr)
        self.assertEqual(arr, [1])

        arr = []
        cocktail_sort(arr)
        self.assertEqual(arr, [])


if __name__ == "__main__":
    unittest.main()
