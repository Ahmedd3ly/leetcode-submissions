"""
42. Trapping Rain Water
Difficulty: Hard
https://leetcode.com/problems/trapping-rain-water/

──────────────────────────────────────────────────

Given n non-negative integers representing an elevation map where the
width of each bar is 1, compute how much water it can trap after
raining.



Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented
by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain
water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9



Constraints:

        • n == height.length

        • 1 <= n <= 2 * 10^4

        • 0 <= height[i] <= 10^5
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        waterlvl = 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                waterlvl += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                waterlvl += maxRight - height[r]

        return waterlvl
