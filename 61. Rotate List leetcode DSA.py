# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # [1,2,3,4,5], k = 2
        if head==None or head.next==None:
            return head
        tail=head
        leng=1
        while tail.next:
            tail=tail.next
            leng+=1
        tail.next=head
        t=leng-k%leng
        for _ in range(t):
            tail=tail.next
            # head=head.next
        h=tail.next
        tail.next=None
        return h
# https://leetcode.com/problems/rotate-list/description/
