"""
84. Largest Rectangle in Histogram
Difficulty: Hard
https://leetcode.com/problems/largest-rectangle-in-histogram/

──────────────────────────────────────────────────

Given an array of integers heights representing the histogram's bar
height where the width of each bar is 1, return the area of the
largest rectangle in the histogram.



Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area =
10 units.

Example 2:

Input: heights = [2,4]
Output: 4



Constraints:

        • 1 <= heights.length <= 10^5

        • 0 <= heights[i] <= 10^4
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Pairs of [start_index, height]
        maxArea = 0

        for i, h in enumerate(heights):
            startInd = i
            # While the stack is not empty AND the top bar is taller than the current bar
            while stack and h < stack[-1][1]:
                poppedInd, poppedHeight = stack.pop()

                # The width is from the popped bar's start index up to the current index i
                width = i - poppedInd
                maxArea = max(maxArea, width * poppedHeight)

                # The current shorter bar can extend backward to where the popped bar started
                startInd = poppedInd

            stack.append([startInd, h])

            # Cleanup: For any bars left in the stack, they extend all the way to the end of the histogram
        for i, h in stack:
            width = len(heights) - i
            maxArea = max(maxArea, width * h)

        return maxArea
