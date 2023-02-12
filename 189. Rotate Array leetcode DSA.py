class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        print (k)
        nums[:] = nums[n-k:] + nums[:n-k]
 




# https://leetcode.com/problems/rotate-array/
