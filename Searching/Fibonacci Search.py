"""
Fibonacci Search: is a search algorithm that uses Fibonacci numbers to search an element in a sorted array. 
The idea is to use two pointers, one with value fibonacci(k-1) and other with fibonacci(k) 
where k is the smallest fibonacci number greater than or equal to the size of the array.
"""

# Fibonacci Search


def fibonacci_search(arr, target):
    fib_prev = 0
    fib_cur = 1
    fib_next = fib_prev + fib_cur

    while fib_next < len(arr):
        fib_prev = fib_cur
        fib_cur = fib_next
        fib_next = fib_cur + fib_prev

    offset = -1

    while fib_next > 1:
        i = min(offset + fib_prev, len(arr) - 1)

        if arr[i] < target:
            fib_next = fib_cur
            fib_cur = fib_prev
            fib_prev = fib_next - fib_cur
            offset = i
        elif arr[i] > target:
            fib_next = fib_prev
            fib_cur = fib_cur - fib_prev
            fib_prev = fib_next - fib_cur
        else:
            return i

    if fib_cur and arr[len(arr) - 1] == target:
        return len(arr) - 1

    return -1


# Best-Case Time complexity = O(1)
# Average-Case Time complexity = O(log n)
# Worst-Case Time complexity = O(log n)
# Space complexity = O(1)

import unittest


class TestFibonacciSearch(unittest.TestCase):
    def test_fibonacci_search(self):
        arr = [1, 2, 3, 4, 5]
        target = 3

        result = fibonacci_search(arr, target)

        self.assertEqual(result, 2)

    def test_fibonacci_search_not_found(self):
        arr = [1, 2, 3, 4, 5]
        target = 6

        result = fibonacci_search(arr, target)

        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
