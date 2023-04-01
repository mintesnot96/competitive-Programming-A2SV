class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        m = float('-inf')
        for i, a in enumerate(arr):
            m = max(m, a)
            if m == i:
                ans += 1
        return ans
# https://leetcode.com/problems/max-chunks-to-make-sorted/description/
