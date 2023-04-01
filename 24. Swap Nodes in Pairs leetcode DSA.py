# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('-inf'))
        dummy.next = head
        prev = dummy
        curr = head
        while curr and curr.next:
            temp = curr.val
            curr.val = curr.next.val
            curr.next.val = temp
            prev = curr.next
            curr = curr.next.next

        return dummy.next
# https://leetcode.com/problems/swap-nodes-in-pairs/
