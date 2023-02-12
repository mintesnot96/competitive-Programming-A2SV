class Solution:
    def maxArea(self, H: List[int]) -> int:
        # [1,8,6,2,5,4,8,3,7]
        maxA=0
        i=0
        j = len(H)-1
        while (i < j):
            if H[i] <= H[j]:
                area = H[i] * (j - i)
                i += 1
            else:
                area = H[j] * (j - i)
                j -= 1
            if area > maxA:
                maxA = area
        return maxA


# https://leetcode.com/problems/container-with-most-water/
