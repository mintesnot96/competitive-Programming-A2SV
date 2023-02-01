class Solution(object):
    def sortColors(self, nums):  
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j+1] < nums[j]:
                    nums[j+1],nums[j] = nums[j],nums[j+1]
                else:
                    continue
# https://leetcode.com/problems/sort-colors/
