"""
Problem
-------
Nokia 3210 Keypad - Decode button presses to text.

Old mobile phones like the Nokia 3210 had numeric keypads where you had to press
buttons multiple times to get different letters. This problem simulates decoding
such button presses into text.

Keypad mapping:
- 0: space
- 1: (not used for letters)
- 2: abc
- 3: def
- 4: ghi
- 5: jkl
- 6: mno
- 7: pqrs
- 8: tuv
- 9: wxyz

Rules:
- Press a button multiple times to cycle through its letters
- Use ',' (comma) as a pause separator for double characters from the same button
- Example: "44" = 'h', but "4,4" = 'gg' (two separate 'g' characters)

Constraints:
- Input consists of digits 0-9 and comma separators
- Only lowercase letters and spaces in output

Complexity: O(n) time, O(1) extra space (excluding output string)
"""


class Solution:
    """Solution for decoding Nokia keypad button presses.
    
    Uses a keypad mapping and processes groups of consecutive same digits.
    """
    
    def __init__(self):
        """Initialize keypad mapping with nested dictionaries."""
        # Nested dictionary: button -> {press_count: letter}
        self.keypad = {
            '0': {1: ' '},
            '2': {1: 'a', 2: 'b', 3: 'c'},
            '3': {1: 'd', 2: 'e', 3: 'f'},
            '4': {1: 'g', 2: 'h', 3: 'i'},
            '5': {1: 'j', 2: 'k', 3: 'l'},
            '6': {1: 'm', 2: 'n', 3: 'o'},
            '7': {1: 'p', 2: 'q', 3: 'r', 4: 's'},
            '8': {1: 't', 2: 'u', 3: 'v'},
            '9': {1: 'w', 2: 'x', 3: 'y', 4: 'z'}
        }
    
    def decode_keypad(self, button_presses: str) -> str:
        """Decode Nokia keypad button presses into text.
        
        Args:
            button_presses: string of digits and commas
            
        Returns:
            Decoded text message.
        """
        if not button_presses:
            return ""
        
        result = []
        counter = 0
        prev_char = None
        idx = 0
        
        while idx < len(button_presses) + 1:
            if(idx >= len(button_presses)):
                result.append(self.keypad[prev_char][counter])
                counter = 0
                prev_char = ""
            else:
                if( prev_char is not None and prev_char != button_presses[idx] and prev_char != "," ):
                    result.append(self.keypad[prev_char][counter])
                    counter = 0
                    prev_char = ""
                if(button_presses[idx] != ","):
                    counter += 1
                prev_char = button_presses[idx]
                
            idx += 1
        
        return ''.join(result)


if __name__ == "__main__":
    examples = [
        "4433555,555666096667775553",  # expected: "hello world"
        "222",                         # expected: "c"
        "2,22",                        # expected: "ab"
        "44,444",                      # expected: "hi"
        "7777",                        # expected: "s"
        "0",                           # expected: " "
        "666,6",                       # expected: "om"
    ]
    
    solution = Solution()
    for button_presses in examples:
        result = solution.decode_keypad(button_presses)
        print(f'Input: "{button_presses}"')
        print(f'Output: "{result}"')
        print()