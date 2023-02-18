class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        se=1
        plh=0
        # [0,0,1,1,1,2,2,3,3,4]
        while len(nums)>se:
            if nums[plh]!=nums[se]:
                nums[plh+1]=nums[se]
                plh+=1
                # se+=1
            se+=1

        return plh+1

