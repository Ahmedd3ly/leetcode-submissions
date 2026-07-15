"""
104. Maximum Depth of Binary Tree
Difficulty: Easy
https://leetcode.com/problems/maximum-depth-of-binary-tree/

──────────────────────────────────────────────────

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2



Constraints:

        • The number of nodes in the tree is in the range [0, 10^4].

        • -100 <= Node.val <= 100
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        ############### Recursive Depth First Search (DFS) #################
        # if not root:
        #     return 0

        # # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        ############### Iterative Breadth First Search (BFS) ###############
        # deq = deque([root])
        # level = 0

        # while deq:

        #     for _ in range(len(deq)):
        #         node = deq.popleft()

        #         if node.left:
        #             deq.append(node.left)
        #         if node.right:
        #             deq.append(node.right)

        #     level += 1

        # return level

        ############### Iterative Depth First Search (DFS) #################
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return res
