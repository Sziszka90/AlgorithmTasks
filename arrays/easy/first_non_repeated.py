"""
Problem
-------
Find First Non-Repeated Number.

Given an array of integers, find the first number that appears exactly once
in the array. Return -1 if no such number exists.

The array may contain duplicate numbers, and you need to find the first
non-repeated number based on the order of first appearance.

Example 1:
Input: nums = [4, 5, 1, 2, 0, 4]
Output: 5
Explanation: 4 appears twice, 5 appears once (first non-repeated), 1, 2, 0 appear once

Example 2:
Input: nums = [1, 2, 1, 2, 3]
Output: 3
Explanation: 1 and 2 appear twice each, 3 appears once

Example 3:
Input: nums = [1, 1, 2, 2]
Output: -1
Explanation: All numbers are repeated

Example 4:
Input: nums = [5]
Output: 5
Explanation: Single element is non-repeated

Constraints:
- 1 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9

Complexity: O(n) time, O(n) extra space (using hash map for counting)
"""

from typing import List


class Solution:
    """Solution for finding the first non-repeated number.
    
    Uses a hash map to count occurrences, then finds the first number
    that appears exactly once.
    """
    
    def first_non_repeated(self, nums: List[int]) -> int:
        """Find the first number that appears exactly once.
        
        Args:
            nums: list of integers (may contain duplicates)
            
        Returns:
            First non-repeated number, or -1 if none exists.
        """
        # Count occurrences of each number
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Find first number with count = 1
        for num in nums:
            if count[num] == 1:
                return num
                
        return -1


if __name__ == "__main__":
    examples = [
        [4, 5, 1, 2, 0, 4],    # expected: 5
        [1, 2, 1, 2, 3],       # expected: 3
        [1, 1, 2, 2],          # expected: -1
        [5],                   # expected: 5
        [1, 2, 3, 4, 5],       # expected: 1
        [2, 2, 1, 1, 3, 3],    # expected: -1
    ]
    
    solution = Solution()
    for nums in examples:
        result = solution.first_non_repeated(nums)
        print(f"nums={nums} -> first non-repeated={result}")