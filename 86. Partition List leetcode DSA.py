# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = before = ListNode(0)
        after_head = after = ListNode(0)
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
                
            head = head.next
            
        after.next = None
        before.next = after_head.next
        return before_head.next
                




# https://leetcode.com/problems/partition-list/
