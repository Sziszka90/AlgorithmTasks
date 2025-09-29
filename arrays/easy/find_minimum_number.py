#Find Minimum Number
#Given an array of integers, return the minimum number.
#Example:
#Input: [3, 7, 1, 9, 2] → Output: 1

class Solution:
	"""
	Find minimum number in a list.

	Complexity: O(n) time, O(1) additional space (one pass keeping the current min)
	"""

	def find_min(self, nums):
		"""Return the minimum value in nums or None if nums is empty.

		Hint: iterate once and keep track of the current minimum value.
		"""
		if not nums:
			return None
		
		min_number = nums[0]

		for num in nums[1:]:
			if num < min_number:
				min_number = num

		return min_number


if __name__ == "__main__":
	s = Solution()
	sample = [3, 7, 1, 9, 2]
	print(s.find_min(sample))
