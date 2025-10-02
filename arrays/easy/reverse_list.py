"""
Problem
-------
Reverse a list of integers in-place and return it.

Example:
Input: [1, 2, 3, 4, 5, 6]
Output: [6, 5, 4, 3, 2, 1]

Complexity: O(n) time, O(1) extra space
"""

from typing import List


class Solution:
    """Solution skeleton for reversing a list in-place."""

    def reverse_in_place(self, nums: List[int]) -> List[int]:
        """Reverse the list in-place and return it.

        Args:
            nums: list of integers to reverse

        Returns:
            The same list object with elements reversed.
        """
        n = len(nums)
        for i in range(n // 2):
            nums[i], nums[-(i + 1)] = nums[-(i + 1)], nums[i]
        return nums


if __name__ == "__main__":
    example = [1, 2, 3, 4, 5, 6]
    print("Example input:", example)
    print("Reversed:", Solution().reverse_in_place(example))
