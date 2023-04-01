# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
        
            return head
        
        odd_head = odd_tail = ListNode()
        even_head = even_tail = ListNode()
        
        i = 1
        curr = head
        while curr:
            if i % 2 == 1:  # odd index
                odd_tail.next = curr
                odd_tail = odd_tail.next
            else:  # even index
                even_tail.next = curr
                even_tail = even_tail.next
            
            curr = curr.next
            i += 1
        
        odd_tail.next = even_head.next
        even_tail.next = None
        
        return odd_head.next
# https://leetcode.com/problems/odd-even-linked-list/
