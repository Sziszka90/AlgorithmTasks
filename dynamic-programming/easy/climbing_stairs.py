"""
Problem
-------
Climbing Stairs (easy - dynamic programming).

You are climbing a staircase. It takes n steps to reach the top. Each time you
can either climb 1 or 2 steps. In how many distinct ways can you climb to the
top?

Example:
Input: n = 3
Output: 3  # (1+1+1, 1+2, 2+1)

Complexity: O(n) time, O(1) extra space (iterative DP with two variables)
"""

class Solution:
    """Solution skeleton for the climbing stairs problem."""

    def climb_stairs(self, n: int) -> int:
        """Return number of distinct ways to climb `n` steps using 1 or 2 steps.

        Args:
            n: total number of steps (n >= 0)

        Returns:
            Number of distinct ways to reach the top.

        Notes:
            - This is the Fibonacci sequence shifted: ways(n) = ways(n-1) + ways(n-2)
            - Implement iteratively to achieve O(n) time and O(1) extra space.
        """
        if n < 0:
            raise ValueError("n must be non-negative")
        if n <= 1:
            return 1

        prev, curr = 1, 1
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr
        return curr


if __name__ == "__main__":
    examples = [1, 2, 3, 4, 5]
    for n in examples:
        print(f"n={n} -> ways={Solution().climb_stairs(n)}")

0,1,1
0,1,1,2
0,1,1,2,3
0,1,1,2,3,5
0,1,1,2,3,5,8