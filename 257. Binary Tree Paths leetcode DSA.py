class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        if not root:
            return result

        stack = [(root, "")]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                result.append(path + str(node.val))
            if node.left:
                stack.append((node.left, path + str(node.val) + "->"))
            if node.right:
                stack.append((node.right, path + str(node.val) + "->"))
        return result
    
# https://leetcode.com/problems/binary-tree-paths/description/
