"""
Problem
-------
Check if a string is a palindrome (alphanumeric, case-insensitive).

Given a string `s`, determine whether it reads the same forward and backward
when considering only alphanumeric characters and ignoring case.

Example:
Input: "A man, a plan, a canal: Panama"
Output: True

Complexity: O(n) time, O(n) extra space (filtered string)
"""


class Solution:
    """Solution for checking whether a string is a palindrome (alnum, case-insensitive)."""

    def is_palindrome(self, s: str) -> bool:
        """Return True if `s` is a palindrome when considering only alphanumerics.

        Args:
            s: input string

        Returns:
            True if `s` (filtered and lowercased) equals its reverse.
        """
        if s is None:
            return False

        filtered = "".join(ch.lower() for ch in s if ch.isalnum())
        return filtered == filtered[::-1]


if __name__ == "__main__":
    examples = [
        "A man, a plan, a canal: Panama",  # True
        "race a car",                      # False
        "",                                # True (empty string)
    ]
    sol = Solution()
    for s in examples:
        print(f"input={s!r} -> is_palindrome={sol.is_palindrome(s)}")
