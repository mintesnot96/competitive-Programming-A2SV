# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.dfs(root,0)


    def dfs(self,node,n):
        
        if not node.left and not node.right:
            return n*10+node.val
        total=0
        if node.left:
            total += self.dfs(node.left, n*10+node.val)
        if node.right:
            total += self.dfs(node.right,n*10+node.val)
        return total
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
