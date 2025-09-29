#Find Maximum Number
#Given an array of integers, return the maximum number.
#Example:
#Input: [3, 7, 1, 9, 2] → Output: 9

class Solution:
	"""
	Find maximum number in a list.

	Complexity: O(n) time, O(1) additional space (one pass keeping the current max)
	"""

	def find_max(self, nums):
		"""Return the maximum value in nums or None if nums is empty.
		   Hint: iterate once and keep track of the current maximum value.
		"""
		if not nums:
			return None
		
		max_number = nums[0]

		for num in nums[1:]:
			if num > max_number:
				max_number = num

		return max_number	

if __name__ == "__main__":
	s = Solution()
	sample = [3, 7, 1, 9, 2]
	print(s.find_max(sample))
