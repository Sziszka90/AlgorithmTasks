# Fibonacci Number
# Return the n-th Fibonacci number (0-indexed: fib(0)=0, fib(1)=1).
# Example:
# Input: 6 -> Output: 8 (sequence: 0,1,1,2,3,5,8)


class Solution:
    """
    Compute Fibonacci numbers.

    Notes on complexity:
    - Naive recursive: O(2^n) time, O(n) recursion depth
    - Iterative DP: O(n) time, O(1) extra space (recommended for easy tasks)
    - Matrix exponentiation / fast doubling: O(log n) time (advanced)
    """

    def fib(self, n: int) -> int:
        """Return the n-th Fibonacci number (n >= 0).

        Uses an iterative O(n) time, O(1) space approach.
        """

        if n == 0:
            return None

        list = [0,1]

        if n == 1:
            return [0]

        if n == 2:
            return list

        for i in range(3, n):
            list.append(list[-2] + list[-1])

        return list


if __name__ == "__main__":
    s = Solution()
    n = 6
    print(f"fib({n}) ->", end=" ")
    print(s.fib(n))

    n = 0
    print(f"fib({n}) ->", end=" ")
    print(s.fib(n))

    n = 1
    print(f"fib({n}) ->", end=" ")
    print(s.fib(n))

    n = 2
    print(f"fib({n}) ->", end=" ")
    print(s.fib(n))

    n = 10
    print(f"fib({n}) ->", end=" ")
    print(s.fib(n))
