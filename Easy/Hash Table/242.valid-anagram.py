"""
242. Valid Anagram
Difficulty: Easy
https://leetcode.com/problems/valid-anagram/

──────────────────────────────────────────────────

Given two strings s and t, return true if t is an anagram of s, and
false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false



Constraints:

        • 1 <= s.length, t.length <= 5 * 10^4

        • s and t consist of lowercase English letters.



Follow up: What if the inputs contain Unicode characters? How would
you adapt your solution to such a case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        charMapS, charMapT = {}, {}

        for i in range(len(s)):
            charMapS[s[i]] = 1 + charMapS.get(s[i], 0)
            charMapT[t[i]] = 1 + charMapT.get(t[i], 0)

        for c in charMapS:
            if charMapS[c] != charMapT.get(c, 0):
                return False

        return True
