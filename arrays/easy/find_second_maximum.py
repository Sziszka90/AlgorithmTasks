#Find Second Maximum Number
#Given an array of integers, return the second largest distinct number.
#If the second maximum does not exist (all elements equal or single element), return None.
#Example:
#Input: [3, 7, 1, 9, 2] → Output: 7

class Solution:
	"""
	Find the second maximum (distinct) number in a list.

	Complexity: O(n) time, O(1) extra space (single pass tracking top two values)
	"""

	def find_second_max(self, nums):
		"""Return the second largest distinct value in nums, or None if not present.

		Hint: keep two variables (first, second) while iterating once through the list.
		Edge cases: duplicates, negative numbers, single-element lists.
		"""
		if not nums or len(nums) < 2:
			return None

		first = second = None

		for num in nums:
			if (first is None or num > first):
				second = first
				first = num

			elif (num < first and (second is  None or num > second)):
				second = num
		return second

if __name__ == "__main__":
	s = Solution()
	sample = [3, 7, 1, 9, 2]
	print(s.find_second_max(sample))
