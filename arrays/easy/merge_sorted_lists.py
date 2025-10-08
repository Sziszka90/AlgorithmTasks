"""
Problem
-------
Merge two sorted lists into one sorted list.

Given two sorted lists `a` and `b`, return a new list that contains all the
elements from `a` and `b` in sorted order. This is the classic two-pointer
merge step used in merge sort.

Example:
Input: a = [1, 3, 5], b = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]

Complexity: O(n + m) time, O(n + m) extra space (where n, m are lengths of a, b)
"""

from typing import List


class Solution:
    """Solution skeleton for merging two sorted lists."""

    def merge_sorted(self, a: List[int], b: List[int]) -> List[int]:
        """Merge two sorted lists `a` and `b` and return a new sorted list.

        Args:
            a: first sorted list
            b: second sorted list

        Returns:
            A new list containing all elements from `a` and `b` in sorted order.
        """
        # two-pointer merge
        i, j = 0, 0
        n, m = len(a), len(b)
        res: List[int] = []

        while i < n and j < m:
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1

        if i < n:
            res.extend(a[i:])
        if j < m:
            res.extend(b[j:])

        return res


if __name__ == "__main__":
    a = [1, 3, 5]
    b = [2, 4, 6]
    print("Example input:", a, b)
    print("Expected output: [1, 2, 3, 4, 5, 6]")
    print("This file is a template. Implement Solution.merge_sorted to compute the result.")
