"""
25. Reverse Nodes in k-Group
Difficulty: Hard
https://leetcode.com/problems/reverse-nodes-in-k-group/

──────────────────────────────────────────────────

Given the head of a linked list, reverse the nodes of the list k at a
time, and return the modified list.

k is a positive integer and is less than or equal to the length of
the linked list. If the number of nodes is not a multiple of k then
left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes
themselves may be changed.



Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]



Constraints:

        • The number of nodes in the list is n.

        • 1 <= k <= n <= 5000

        • 0 <= Node.val <= 1000



Follow-up: Can you solve the problem in O(1) extra memory space?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        root = ListNode(0, head)
        groupPrev = root  # Tracks the node right before our current group

        while True:
            # 1. Scout ahead to find the k-th node
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next  # Save the connection to the next group

            # 2. Reverse the current group
            # We initialize 'prev' to groupNext so the new tail automatically
            # hooks up to the rest of the list when we finish flipping.
            prev, curr = groupNext, groupPrev.next

            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            # 3. Stitch the previous group's tail to our new group head
            tail = groupPrev.next  # This was the old head, which is now our new tail (remembers [1], which is our new tail)
            groupPrev.next = kth  # Link previous section to the new head (links dummy(0) to the new head [2])
            groupPrev = tail  # Move groupPrev forward to prepare for the next loop (groupPrev moves to tmp ([1]))

        return root.next

    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
