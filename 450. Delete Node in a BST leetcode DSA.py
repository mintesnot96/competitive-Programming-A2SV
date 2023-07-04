# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

      if root is None:
        return None
    
      if key < root.val:
          root.left = self.deleteNode(root.left, key)
      elif key > root.val:
          root.right = self.deleteNode(root.right, key)
      else:
          if root.left is None and root.right is None:  # Case 1: Leaf node
              return None
          elif root.left is None:  # Case 2: Node with only right child
              return root.right
          elif root.right is None:  # Case 2: Node with only left child
              return root.left
          else:  # Case 3: Node with both left and right children
              successor = self.findSuccessor(root.right)
              root.val = successor.val
              root.right = self.deleteNode(root.right, successor.val)
      
      return root
    def findSuccessor(self,node):
        while node.left:
            node = node.left
        return node


# https://leetcode.com/problems/delete-node-in-a-bst/
