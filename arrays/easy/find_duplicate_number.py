#Find Duplicate Number
#Given an array of integers where one or more values repeat, return a list of duplicated values.
#Example:
#Input: [1, 3, 4, 2, 2] → Output: 2

class Solution:
	"""
	Find a duplicated number from an array.

	Common approaches:
	- Use a set to detect the first seen duplicate (O(n) time, O(n) space)
	- If numbers are in range 1..n and there is exactly one duplicate, use Floyd's
	  cycle detection for O(n) time and O(1) space (advanced)
	"""

	def find_duplicate(self, nums):
		"""Return any duplicated value found in nums, or None if no duplicate.

		Hint: the simple approach is to track seen values with a set. For the constrained
		variant (values 1..n with n+1 length) consider cycle detection.
		"""
		if not nums:
			return []

		counts = {}
		duplicates = []

		for num in nums:
			counts[num] = counts.get(num, 0) + 1
			if counts[num] == 2:
				duplicates.append(num)

		return duplicates

if __name__ == "__main__":
	s = Solution()
	sample = [1, 3, 4, 2, 2]
	print(s.find_duplicate(sample))
