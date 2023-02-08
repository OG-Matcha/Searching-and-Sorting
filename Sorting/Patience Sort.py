"""
Patience sorting is a sorting algorithm that is based on the concept of a card game. 
It works by repeatedly comparing piles of cards and merging them together in the correct order. 
The algorithm is useful for sorting large datasets, as it can be done in linear time.
"""

# Patience Sort

from bisect import bisect_left


def patience_sort(arr):
    piles = []

    for val in arr:

        i = bisect_left(piles, [val])

        if i == len(piles):
            piles.append([val])
        else:
            piles[i].append(val)

    res = []
    for pile in piles:
        res.extend(reversed(pile))

    return res


# Best-Case Time complexity = O(n)
# Average-Case Time complexity = O(nlogn)
# Worst-Case Time complexity = O(nlogn)
# Space complexity = O(n)


import unittest


class TestPatienceSort(unittest.TestCase):
    def test_patience_sort(self):
        arr = [4, 6, 8, 5, 7, 3, 9]
        expected = [3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(patience_sort(arr), expected)

    def test_patience_sort_empty(self):
        arr = []
        expected = []
        self.assertEqual(patience_sort(arr), expected)

    def test_patience_sort_one(self):
        arr = [1]
        expected = [1]
        self.assertEqual(patience_sort(arr), expected)

    def test_patience_sort_same(self):
        arr = [5, 5]
        expected = [5, 5]
        self.assertEqual(patience_sort(arr), expected)

    def test_patience_sort_reverse(self):
        arr = [9, 8, 7, 6, 5, 4, 3]
        expected = [3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(patience_sort(arr), expected)


if __name__ == "__main__":
    unittest.main()
