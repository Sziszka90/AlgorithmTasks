"""
Problem
-------
Valid Parentheses (check matching and closure).

Given a string `s` containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid.

An input string is valid if:
  1. Open brackets are closed by the same type of brackets.
  2. Open brackets are closed in the correct order.

Example:
Input: s = "()[]{}"
Output: True

Complexity: O(n) time, O(n) extra space (stack)
"""

from typing import List


class Solution:
    """Template for checking if parentheses/brackets are valid."""

    def is_valid_parentheses(self, s: str) -> bool:
        """Return True if `s` contains valid matching and nested brackets.

        Args:
            s: input string containing bracket characters

        Returns:
            True if the string is valid, False otherwise.
        """
        brackets = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []

        for bracket in s:
            if bracket in brackets.values():
                stack.append(bracket)
            elif(stack[-1] == brackets[bracket]):
                stack.pop()
            else:
                return False

        return True

if __name__ == "__main__":
    examples = [
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
    ]
    solution = Solution()
    for s, expected in examples:
        print(f"input={s} expected={expected}")
        print(solution.is_valid_parentheses(s))
