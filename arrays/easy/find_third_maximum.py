#Find Third Maximum Distinct Number
#Given an array of integers, return the third largest distinct number.
#If the third maximum does not exist (fewer than three distinct values), return None.
#Example:
#Input: [3, 7, 1, 9, 2] → Output: 3

class Solution:
	"""
	Find the third maximum distinct number in a list.

	Complexity target: O(n) time, O(1) extra space (single pass tracking top three distinct values)
	"""

	def find_third_max(self, nums):
		"""Return the third largest distinct value in nums, or None if not present.

		Hint: maintain three variables (first, second, third) storing distinct values while
		iterating the list once. Alternatively, for simplicity use `sorted(set(nums))` and
		index from the end (this is O(n log n) due to sorting).
		"""
		if not nums:
			return None

		first = None
		second = None
		third = None

		for num in nums:
			if first is None or num > first:
				third = second
				second = first
				first = num
			elif num != first and (second is None or num > second):
				third = second
				second = num
			elif num != first and num != second and (third is None or num > third):
				third = num

		return third

if __name__ == "__main__":
	s = Solution()
	sample = [3, 7, 1, 9, 2]
	print(s.find_third_max(sample))
