"""
PROBLEM:
    Given two strings s and t, determine if they are isomorphic.
    Two strings s and t are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

EXAMPLE 1:
    Input: s = "egg", t = "add"
    Output: true

EXAMPLE 2:
    Input: s = "foo", t = "bar"
    Output: false

EXAMPLE 3:
    Input: s = "paper", t = "title"
    Output: true

CONSTRAINTS:
    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isomorphic_dictionary = {}
        t_list = list(t)

        for i, letter in enumerate(s):
            if letter not in isomorphic_dictionary.keys():
                if t_list[i] in isomorphic_dictionary.values():
                    return False
                isomorphic_dictionary[letter] = t_list[i]

            if letter in isomorphic_dictionary.keys():
                if t_list[i] != isomorphic_dictionary[letter]:
                    return False
        
        return True


if __name__ == "__main__":
    solution = Solution()

    # CASE 1
    result1 = solution.isIsomorphic(s = "egg", t = "add")
    print(result1)

    # CASE 2
    result2 = solution.isIsomorphic(s = "foo", t = "bar")
    print(result2)

    # CASE 3
    result3 = solution.isIsomorphic(s = "paper", t = "title")
    print(result3)

    # CASE 4
    result4 = solution.isIsomorphic(s = "badc", t = "babc")
    print(result4)