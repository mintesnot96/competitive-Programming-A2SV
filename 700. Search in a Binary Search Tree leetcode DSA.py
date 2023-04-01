# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [root]
        while stack:
            print('stack:  ',stack)
            curr = stack.pop()
            print('\n 1 Pop -----',curr,'\n')
            print('after pop :  ',stack)
            if curr.val == val:
                print('\n    Return  \n')
                return curr
            elif curr.val > val and curr.left:
                stack.append(curr.left)
            elif curr.val < val and curr.right:
                stack.append(curr.right)
        return None
# https://leetcode.com/problems/search-in-a-binary-search-tree/
