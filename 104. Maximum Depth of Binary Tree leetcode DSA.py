# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))




        # countl=1
        # countr=1
        # right=root
        # left=root
        # while right.right:
        #     right=right.right
        #     countr+=1
        # while left.left:
        #     left=left.left
        #     countl+=1
        # return max(countr,countl)



# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
