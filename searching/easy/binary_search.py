"""
Problem
-------
Binary Search - Find target element in sorted array.

Given a sorted array of integers `nums` and a target value, return the index
of the target if it exists in the array, otherwise return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All integers in nums are unique
- nums is sorted in ascending order

Complexity: O(log n) time, O(1) extra space
"""

from typing import List


class Solution:
    """Solution for binary search in sorted array.
    
    Template intentionally leaves the method unimplemented so you can 
    practice the classic binary search algorithm yourself.
    """
    
    def search(self, nums: List[int], target: int) -> int:
        """Return index of target in sorted array, or -1 if not found.
        
        Args:
            nums: sorted list of integers (ascending order)
            target: integer to search for
            
        Returns:
            Index of target if found, otherwise -1.
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1


if __name__ == "__main__":
    examples = [
        ([-1, 0, 3, 5, 9, 12], 9),   # expected: 4
        ([-1, 0, 3, 5, 9, 12], 2),   # expected: -1
        ([5], 5),                    # expected: 0
        ([1, 3, 5, 7, 9], 7),        # expected: 3
        ([1, 2, 3, 4, 5], 10),       # expected: -1
    ]
    
    solution = Solution()
    for nums, target in examples:
        result = solution.search(nums, target)
        print(f"nums={nums}, target={target} -> index={result}")