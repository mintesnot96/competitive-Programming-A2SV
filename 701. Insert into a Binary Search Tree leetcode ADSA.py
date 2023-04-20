# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if not root:
            return new_node
        curr = root
        while True:
            if val > curr.val:
                if not curr.right:
                    curr.right = new_node
                    break
                curr = curr.right
            else:
                if not curr.left:
                    curr.left = new_node
                    break
                curr = curr.left
        return root
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
