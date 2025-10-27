"""
Problem
-------
Find First and Last Position of Element in Sorted Array.

Given an array of integers `nums` sorted in non-decreasing order, find the 
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]

Example 2:
Input: nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]

Example 3:
Input: nums = [], target = 0
Output: [-1, -1]

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- nums is a non-decreasing array
- -10^9 <= target <= 10^9

Complexity: O(log n) time, O(1) extra space
"""

from typing import List


class Solution:
    """Solution for finding first and last position of target in sorted array.
    
    This requires implementing binary search variants to find the leftmost
    and rightmost occurrences of the target value.
    """
    
    def search_range(self, nums: List[int], target: int) -> List[int]:
        """Find first and last position of target in sorted array.
        
        Args:
            nums: sorted list of integers (non-decreasing order)
            target: integer to search for
            
        Returns:
            List [first_index, last_index] or [-1, -1] if not found.
        """
        if not nums:
            return [-1, -1]
            
        left_bound = self.find_left_bound(nums, target)
        if left_bound == -1:
            return [-1, -1]
            
        right_bound = self.find_right_bound(nums, target)
        return [left_bound, right_bound]
    
    def find_left_bound(self, nums: List[int], target: int) -> int:
        """Helper: Find leftmost (first) occurrence of target."""
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                result = mid  # Found target, but keep searching left
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return result
    
    def find_right_bound(self, nums: List[int], target: int) -> int:
        """Helper: Find rightmost (last) occurrence of target."""
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                result = mid  # Found target, but keep searching right
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return result


if __name__ == "__main__":
    examples = [
        ([5, 7, 7, 8, 8, 10], 8),     # expected: [3, 4]
        ([5, 7, 7, 8, 8, 10], 6),     # expected: [-1, -1]
        ([], 0),                      # expected: [-1, -1]
        ([1], 1),                     # expected: [0, 0]
        ([2, 2, 2, 2], 2),            # expected: [0, 3]
    ]
    
    solution = Solution()
    for nums, target in examples:
        result = solution.search_range(nums, target)
        print(f"nums={nums}, target={target} -> range={result}")
