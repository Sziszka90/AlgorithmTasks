"""
Problem
-------
Two Sum - Find two numbers that add up to target.

Given an array of integers `nums` and an integer `target`, return indices of
the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 2 + 7 == 9

Example 2:
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: Because nums[1] + nums[2] == 2 + 4 == 6

Example 3:
Input: nums = [3, 3], target = 6
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 3 + 3 == 6

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists

Complexity: O(n) time, O(n) extra space (using hash map)
"""

from typing import List


class Solution:
    """Solution for Two Sum problem.
    
    Uses a hash map to store numbers we've seen and their indices,
    allowing us to find the complement in O(1) time.
    """
    
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """Find indices of two numbers that add up to target.
        
        Args:
            nums: list of integers
            target: target sum
            
        Returns:
            List of two indices [i, j] where nums[i] + nums[j] == target.
        """
        # Hash map to store {number: index}
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists in our seen numbers
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number and its index
            seen[num] = i
        
        # Should never reach here given problem constraints
        return []


if __name__ == "__main__":
    examples = [
        ([2, 7, 11, 15], 9),    # expected: [0, 1]
        ([3, 2, 4], 6),         # expected: [1, 2]
        ([3, 3], 6),            # expected: [0, 1]
        ([1, 5, 3, 7], 8),      # expected: [1, 3] (5 + 3 = 8)
        ([-1, 2, 1, -4], 0),    # expected: [0, 2] (-1 + 1 = 0)
    ]
    
    solution = Solution()
    for nums, target in examples:
        result = solution.two_sum(nums, target)
        print(f"nums={nums}, target={target} -> indices={result}")
        if result:
            print(f"  Verification: {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}")
        print()