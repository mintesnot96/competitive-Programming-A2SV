class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0
        l = -1
        r = -1
        for i, a in enumerate(nums):
            if a > right:
                l = i
                r = i
            elif a >= left:
                r = i
                ans += r - l
            else:
                ans += r - l
        return ans
      
# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/
