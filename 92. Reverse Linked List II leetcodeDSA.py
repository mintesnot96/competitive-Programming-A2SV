class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head is None or left == right:
            return head
        dummy = ListNode(0, head)
        prev = dummy
        for i in range(left - 1):
            prev = prev.next
        curr = prev.next
        for i in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        return dummy.next

#Link https://leetcode.com/problems/palindrome-linked-list/description/
