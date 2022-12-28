"""
PROBLEM:
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

EXAMPLE 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

EXAMPLE 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false
 
CONSTRAINTS:
    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while (j < len(t)) and (i < len(s)):
            if s[i] == t[j]:
                i = i + 1
            j = j + 1
        
        if i == len(s):
            return True
        
        return False


if __name__ == "__main__":
    solution = Solution()

    # CASE 1
    result1 = solution.isSubsequence(s = "abc", t = "ahbgdc")
    print(result1)

    # CASE 2
    result2 = solution.isSubsequence(s = "axc", t = "ahbgdc")
    print(result2)

    # CASE 3
    result3 = solution.isSubsequence(s = "aec", t = "ahbgdc")
    print(result3)