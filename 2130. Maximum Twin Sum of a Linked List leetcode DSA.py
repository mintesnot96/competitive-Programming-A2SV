# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# First solution usnig list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
      maxc=0
      final=head
      array=[]
      while head.next:
        array.append(head.val)
        head=head.next
      array.append(head.val)
      i=0
      j=len(array)-1
      while i<j:
        maxc=max(maxc,array[i]+array[j])
        i+=1
        j-=1
      return maxc


# other alternative using reverse linked list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
      mmax=0
      def reverseList(head: ListNode) -> ListNode:
        prev=None
        while head:
          nextnode=head.next
          head.next=prev
          prev=head
          head=nextnode
        return prev
      s=head
      f=head
      while f:
        s=s.next
        f=f.next.next
      mid=reverseList(s)
      while mid:
        mmax=max(mmax,mid.val+head.val)
        mid=mid.next
        head=head.next
      return mmax
      
