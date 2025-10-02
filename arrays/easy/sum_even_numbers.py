"""
Problem
-------
Given an array of integers, return the sum of all even numbers in the array.

Example:
Input: [1, 2, 3, 4, 5, 6]
Output: 12  # (2 + 4 + 6)

Complexity: O(n) time, O(1) extra space
"""

from typing import List


class Solution:
    """Solution skeleton for summing even numbers in a list."""

    def sum_even(self, nums: List[int]) -> int:
        """Return the sum of even numbers in nums.

        Args:
            nums: list of integers

        Returns:
            Sum of integers in nums that are even.
        """
        sum_of_even_numbers = 0

        for num in nums:
            if num % 2 == 0:
                sum_of_even_numbers += num

        return sum_of_even_numbers


if __name__ == "__main__":
    example = [1, 2, 3, 4, 5, 6]
    print("Example input:", example)
    print("Sum of even numbers:", Solution().sum_even(example))
