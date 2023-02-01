class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        result = 0
        length = int(len(piles)/3)
        for i in range(len(piles)-2, length-1, -2):
            result += piles[i]
        return result



# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
