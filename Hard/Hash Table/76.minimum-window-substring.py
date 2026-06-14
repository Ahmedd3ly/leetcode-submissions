"""
76. Minimum Window Substring
Difficulty: Hard
https://leetcode.com/problems/minimum-window-substring/

──────────────────────────────────────────────────

Given two strings s and t of lengths m and n respectively, return the
minimum window substring of s such that every character in t
(including duplicates) is included in the window. If there is no such
substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B',
and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.



Constraints:

        • m == s.length

        • n == t.length

        • 1 <= m, n <= 10^5

        • s and t consist of uppercase and lowercase English letters.



Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        # Dictionary to keep a count of all the unique characters in t.
        countT = {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        # Dictionary to track characters in the current window
        countWindow = {}

        # 'need' is the number of UNIQUE characters required from t
        have, need = 0, len(countT)

        l = 0
        resLength = float("infinity")
        subl, subr = 0, 0

        for r in range(len(s)):
            char = s[r]
            countWindow[char] = 1 + countWindow.get(char, 0)

            # If the current character is desired and its count matches t's requirement
            if char in countT and countWindow[char] == countT[char]:
                have += 1

            # Shrink the window from the left as long as it remains valid
            while have == need:
                # Update our minimum result if the current window is smaller
                windowSize = (r - l) + 1
                if windowSize < resLength:
                    resLength = windowSize
                    subl, subr = l, r + 1

                # Pop the leftmost character out of the window
                char = s[l]
                countWindow[char] -= 1

                # If removing this character breaks our condition, decrement 'have'
                if char in countT and countWindow[char] < countT[char]:
                    have -= 1

                l += 1  # Shift the left pointer forward

        # Return the substring if a valid window was found, otherwise ""
        return s[subl:subr] if resLength != float("infinity") else ""
