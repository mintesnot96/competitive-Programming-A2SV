class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pair_sums = []
        maxN=0
        n = len(nums) - 1
        for i in range(n + 1):
            temp = nums[i] + nums[n - i]
            maxN=max(maxN,temp)

            # nums = [3,5,4,2,4,6]
            #  2 3 4 4 5 6

            # pair_sums.append(temp)
        # ans = max(pair_sums)
        
        # time   
        # space   
        return maxN


# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
