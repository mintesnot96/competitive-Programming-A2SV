class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr=[]

        while head:
            arr.append(head.val)
            head=head.next
        
        if arr==arr[::-1]:
            return True
        else:
            return False


# link https://leetcode.com/problems/palindrome-linked-list/submissions/
