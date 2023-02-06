class Solution(object):
    def rearrangeArray(self, nums):
        # nums = [2,1,5,4,3]
        nums.sort() 
        # nums = [1,2,3,4,5]
        # result = [1,2,3,4,5]
        # result = [1,5]
        # result = [1,5,2,4]
        # result = [1,5,2,4,3]
        result=[] 
        left,right=0,len(nums)-1
        for i in range(len(nums)):
            if len(result)!=len(nums):
                result.append(nums[left])
                left+=1
        
                if left<=right:
                    result.append(nums[right])
                    right-=1
            else:
                break
        return result
