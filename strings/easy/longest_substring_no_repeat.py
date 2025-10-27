"""
Problem
-------
Longest Substring Without Repeating Characters.

Given a string `s`, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
Explanation: Empty string has no characters.

Example 5:
Input: s = "dvdf"
Output: 3
Explanation: The answer is "vdf", with the length of 3.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces

Complexity: O(n) time, O(min(m, n)) extra space where m is character set size
"""


class Solution:
    """Solution for finding longest substring without repeating characters.
    
    Uses sliding window technique with a hash map to track character positions.
    When we encounter a repeated character, we shrink the window from the left.
    """
    
    def length_of_longest_substring(self, s: str) -> int:
        """Find length of longest substring without repeating characters.
        
        Args:
            s: input string
            
        Returns:
            Length of longest substring without repeating characters.
        """
        if not s:
            return 0
            
        char_index = {}
        max_length = 0
        left = 0
    
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            
            char_index[char] = right
            
            current_length = right - left + 1
            max_length = max(max_length, current_length)
            
        return max_length
    
    def get_longest_substring(self, s: str) -> str:
        """Return the actual longest substring (bonus method).
        
        Args:
            s: input string
            
        Returns:
            The longest substring without repeating characters.
        """
        if not s:
            return ""
            
        char_index = {}
        max_length = 0
        max_start = 0
        left = 0
        
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            
            char_index[char] = right
            current_length = right - left + 1
            
            if current_length > max_length:
                max_length = current_length
                max_start = left
                
        return s[max_start:max_start + max_length]


if __name__ == "__main__":
    examples = [
        "abcabcbb",    # expected: 3 ("abc")
        "bbbbb",       # expected: 1 ("b")  
        "pwwkew",      # expected: 3 ("wke")
        "",            # expected: 0 ("")
        "dvdf",        # expected: 3 ("vdf")
        "abcdef",      # expected: 6 ("abcdef")
        "aab",         # expected: 2 ("ab")
        " ",           # expected: 1 (" ")
    ]
    
    solution = Solution()
    for s in examples:
        length = solution.length_of_longest_substring(s)
        substring = solution.get_longest_substring(s)
        print(f's="{s}" -> length={length}, substring="{substring}"')