"""
4. Median of Two Sorted Arrays
Difficulty: Hard
https://leetcode.com/problems/median-of-two-sorted-arrays/

──────────────────────────────────────────────────

Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.



Constraints:

        • nums1.length == m

        • nums2.length == n

        • 0 <= m <= 1000

        • 0 <= n <= 1000

        • 1 <= m + n <= 2000

        • -10^6 <= nums1[i], nums2[i] <= 10^6
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = nums1, nums2
        total = len(n1) + len(n2)
        half = total // 2

        if len(n1) > len(n2):
            n1, n2 = nums2, nums1

        l, r = 0, len(n1) - 1

        while True:
            mid1 = (l + r) // 2
            mid2 = half - mid1 - 2

            n1Left = n1[mid1] if mid1 >= 0 else float("-infinity")
            n1Right = n1[mid1 + 1] if (mid1 + 1) < len(n1) else float("infinity")
            n2Left = n2[mid2] if mid2 >= 0 else float("-infinity")
            n2Right = n2[mid2 + 1] if (mid2 + 1) < len(n2) else float("infinity")

            # partition is correct
            if n1Left <= n2Right and n2Left <= n1Right:
                # odd
                if total % 2:
                    return min(n1Right, n2Right)
                # even
                return (max(n1Left, n2Left) + min(n1Right, n2Right)) / 2
            elif n1Left > n2Right:
                r = mid1 - 1

            else:
                l = mid1 + 1
