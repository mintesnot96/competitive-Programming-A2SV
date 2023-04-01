# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headAtemp, headBtemp=headA,headB
        al=0
        bl=0

        while headAtemp:
            al =al+1
            headAtemp=headAtemp.next
        while headBtemp:
            bl =bl+1
            headBtemp=headBtemp.next
        headAtemp=headA
        headBtemp=headB
        # print(al,bl)
        if al>bl:
            for j in range(al-bl):
                headAtemp=headAtemp.next
        else:
            for j in range(bl-al):
                headBtemp=headBtemp.next
        # print(headAtemp,headBtemp)
        while headAtemp:
            if headAtemp==headBtemp:
                return headAtemp
            headBtemp=headBtemp.next
            headAtemp=headAtemp.next
        
        return None

        
        

# https://leetcode.com/problems/intersection-of-two-linked-lists/
