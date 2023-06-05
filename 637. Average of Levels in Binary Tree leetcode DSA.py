# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages = []
        queue = deque([root])

        while queue:
            level_sum = 0
            level_count = 0
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                level_count += 1

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level_average = level_sum / level_count
            averages.append(level_average)

        return averages
