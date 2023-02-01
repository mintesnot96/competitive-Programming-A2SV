class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # [1,3,2,4], k = 5
        count=0
        start=0
        end=len(nums)-1
        nums.sort()
        # [1,2,3,4], k = 5
        while start<end:
            if nums[start]+nums[end]<k:
                start+=1
            elif nums[start]+nums[end]>k:
                end-=1
            else:
                start+=1
                end-=1
                count+=1
        return count

        # time nlogn
        # space constant



# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/
