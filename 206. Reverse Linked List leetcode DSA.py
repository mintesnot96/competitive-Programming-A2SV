class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        # 1 2 3 4 5 6
        while head is not None:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev
# Link https://leetcode.com/problems/reverse-linked-list/description/
