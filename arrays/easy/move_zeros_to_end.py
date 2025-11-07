#Move Zeros to the End
#Given an array of integers, move all zeros to the end while maintaining the relative order
#of the non-zero elements.
#Example:
#Input: [0, 1, 0, 3, 12] → Output: [1, 3, 12, 0, 0]

class Solution:
	"""
	Move zeros to the end of the array.

	Complexity target: O(n) time, O(1) extra space (in-place two-pointer)
	"""

	def move_zeros(self, nums):
		"""Modify nums in-place to move zeros to the end and return nums.

		Hint: use a write index to place non-zero elements and then fill the remainder with zeros.
		"""
		if nums is None:
			return None

		last_non_zero_found_at = 0
		for i in range(len(nums)):
			if nums[i] != 0:
				nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
				last_non_zero_found_at += 1

		return nums

if __name__ == "__main__":
	s = Solution()
	sample = [1, 0, 0, 0, 3, 12]
	print(s.move_zeros(sample))
