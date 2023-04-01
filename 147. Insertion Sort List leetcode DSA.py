# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
         # Create a dummy node with value -inf
        dummy = ListNode(float('-inf'))
        dummy.next = head
        
        # Initialize prev and curr pointers
        prev = dummy
        curr = head
        
        while curr:
            # If curr's value is less than prev's value, reset prev to dummy
            if curr.val < prev.val:
                prev = dummy
            
            # Find the correct position to insert curr
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            # If curr is already in the correct position, move on to the next node
            if prev.next != curr:
                temp = curr.next
                curr.next = prev.next
                prev.next = curr
                curr = temp
            else:
                curr = curr.next
        
        # Return the sorted list by returning the next pointer of the dummy node
        return dummy.next
# https://leetcode.com/problems/insertion-sort-list/description/
