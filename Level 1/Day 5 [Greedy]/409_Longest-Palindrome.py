"""
PROBLEM:
    Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
    Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

EXAMPLE 1:
    Input: s = "abccccdd"
    Output: 7
    Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

EXAMPLE 2:
    Input: s = "a"
    Output: 1
    Explanation: The longest palindrome that can be built is "a", whose length is 1.
 
CONSTRAINTS:
    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        pairs = 0
        unpaired_chars = set()
        
        for char in s:
            if char in unpaired_chars:
                pairs += 1
                unpaired_chars.remove(char)
            else:
                unpaired_chars.add(char)
        
        return pairs * 2 + 1 if unpaired_chars else pairs * 2


if __name__ == "__main__":
    solution = Solution()

    # CASE 1
    print("================================== CASE 1 ==================================")
    s = "abccccdd"
    result = solution.longestPalindrome(s)
    print(f"String                    = {s}")
    print(f"Longest Palindrome Length = {result}")
    print()

    # CASE 2
    print("================================== CASE 2 ==================================")
    s = "a"
    result = solution.longestPalindrome(s)
    print(f"String                    = {s}")
    print(f"Longest Palindrome Length = {result}")
    print()

    # CASE 3
    print("================================== CASE 3 ==================================")
    s = "rttjttthbhfhffnhnghrrtyssss"
    result = solution.longestPalindrome(s)
    print(f"String                    = {s}")
    print(f"Longest Palindrome Length = {result}")
    print()
