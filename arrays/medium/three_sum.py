"""
Problem
-------
Three Sum - Find all unique triplets that sum to zero.

Given an integer array `nums`, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
The distinct triplets are [-1, 0, 1] and [-1, -1, 2].

Example 2:
Input: nums = [0, 1, 1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0, 0, 0]
Output: [[0, 0, 0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

Complexity: O(n²) time, O(1) extra space (not counting output array)
"""

from typing import List


class Solution:
    """Solution for Three Sum problem.
    
    Uses sorting + two pointers approach to find all unique triplets.
    The key insight is to fix one number and use two pointers to find
    the other two numbers that complete the triplet.
    """
    
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """Find all unique triplets that sum to zero.
        
        Args:
            nums: list of integers
            
        Returns:
            List of triplets [a, b, c] where a + b + c = 0.
        """
        nums.sort()  # Sort array first
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
                elif current_sum < 0:
                    left += 1  # Need larger sum
                else:
                    right -= 1  # Need smaller sum
                    
        return result


if __name__ == "__main__":
    examples = [
        [-1, 0, 1, 2, -1, -4],    # expected: [[-1, -1, 2], [-1, 0, 1]]
        [0, 1, 1],                # expected: []
        [0, 0, 0],                # expected: [[0, 0, 0]]
        [-2, 0, 1, 1, 2],         # expected: [[-2, 0, 2], [-2, 1, 1]]
        [1, 2, -2, -1],           # expected: []
    ]
    
    solution = Solution()
    for nums in examples:
        result = solution.three_sum(nums)
        print(f"nums={nums}")
        print(f"triplets={result}")
        # Verify each triplet sums to 0
        for triplet in result:
            print(f"  {triplet[0]} + {triplet[1]} + {triplet[2]} = {sum(triplet)}")
        print()