# Fibonacci Search


def fibonacci_search(arr, target):
    fib_prev = 0
    fib_cur = 1
    fib_next = fib_prev + fib_cur

    while fib_next < len(arr):
        fib_prev = fib_cur
        fib_cur = fib_next
        fib_next = fib_cur + fib_prev

    offset = 0

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


arr = [1, 4, 6, 9, 12, 15, 16, 25]
target = 16

result = fibonacci_search(arr, target)

if result == -1:
    print("Element not found")
else:
    print(f"Element found at index {result}")
