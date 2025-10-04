"""
Problem
-------
Rolling sum of a list.

Given an integer list `nums`. Solution should return the rolling sum of the nums list.

Example:
Input: nums = [1, 2, 3, 4, 5]
Output: [1,3,6,10,15]

Complexity: O(n) time, O(1) extra space (excluding the output list)
"""

from typing import List


class Solution:
    """Template for rolling sum (sliding-window) problems."""

    def rolling_sum(self, nums: List[int]) -> List[int]:
        """Return list of sums of each contiguous window of size `k`.

        Args:
            nums: list of integers

        Returns:
            A list of integers with rolling sum

        """
        if nums is None:
            return None

        rolling_sum = [nums[0]]

        for i in range(1, len(nums)):
            rolling_sum.append(rolling_sum[i-1] + nums[i])

        return rolling_sum

if __name__ == "__main__":
    example = [1, 2, 3, 4, 5]
    print(Solution().rolling_sum(example))