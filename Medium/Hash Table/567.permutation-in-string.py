"""
567. Permutation in String
Difficulty: Medium
https://leetcode.com/problems/permutation-in-string/

──────────────────────────────────────────────────

Given two strings s1 and s2, return true if s2 contains a permutation
of s1, or false otherwise.

In other words, return true if one of s1's permutations is the
substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false



Constraints:

        • 1 <= s1.length, s2.length <= 10^4

        • s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(n1):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        if s1Count == s2Count:
            return True

        for i in range(n1, n2):
            s2Count[ord(s2[i]) - ord("a")] += 1
            s2Count[ord(s2[i - n1]) - ord("a")] -= 1
            if s1Count == s2Count:
                return True

        return False
