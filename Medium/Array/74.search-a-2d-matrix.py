"""
74. Search a 2D Matrix
Difficulty: Medium
https://leetcode.com/problems/search-a-2d-matrix/

──────────────────────────────────────────────────

You are given an m x n integer matrix matrix with the following two
properties:

        • Each row is sorted in non-decreasing order.

• The first integer of each row is greater than the last integer of
the previous row.

Given an integer target, return true if target is in matrix or false
otherwise.

You must write a solution in O(log(m * n)) time complexity.



Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false



Constraints:

        • m == matrix.length

        • n == matrix[i].length

        • 1 <= m, n <= 100

        • -10^4 <= matrix[i][j], target <= 10^4
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols
        l, r = 0, total - 1

        while l <= r:
            midIndex = (l + r) // 2
            i = midIndex // cols
            j = midIndex % cols
            midNum = matrix[i][j]

            if midNum < target:
                l = midIndex + 1
            elif midNum > target:
                r = midIndex - 1
            else:
                return True

        return False
