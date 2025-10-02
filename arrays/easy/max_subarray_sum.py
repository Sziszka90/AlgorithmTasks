#Maximum Subarray Sum
#Given an array of integers, find the contiguous subarray with the largest sum and return that sum.
#Example:
#Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4] → Output: 6 (subarray [4, -1, 2, 1])

class Solution:
	"""
	Find maximum subarray sum (Kadane's algorithm).

	Complexity: O(n) time, O(1) extra space
	"""

	def max_subarray_sum(self, nums):
		"""Return the maximum contiguous subarray sum, or None for empty input.

		Hint: keep a running current_sum and max_sum; reset current_sum when it becomes
		smaller than the current element. See the commented guidance below.
		"""
		if not nums:
			return None
		
		current_sum = nums[0]
		max_sum = current_sum
	
		for num in nums[1:]:
			if (num > (current_sum + num)):
				current_sum = num
			else:
				current_sum += num

			max_sum = max(max_sum, current_sum)

		return max_sum

if __name__ == "__main__":

	s = Solution()
	sample = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	print(s.max_subarray_sum(sample))
