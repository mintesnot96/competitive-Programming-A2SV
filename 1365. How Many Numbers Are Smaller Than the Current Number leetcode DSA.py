class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Create a count array to store the frequency of each element
        count = [0] * 101
        for num in nums:
            count[num] += 1
        
        # Use the count array to determine the position of each element in the sorted output
        for i in range(1, 101):
            count[i] += count[i-1]
        
        # Create an empty list to store the results
        result = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            result[count[nums[i]]-1] = nums[i]
            count[nums[i]] -= 1
        return [count[nums[i]] for i in range(len(nums))]


#         #  using dictionary
#         dict = {}
#         result =[None]*len(nums)
#         for i,  num in enumerate(nums):
#             if num not in dict:
#                 lis=[]
#                 dict[num]=lis
#             dict[num].append(i)
#         # 8 0
#         nums.sort()
# # nums = [8,1,2,2,3] 1 2 2 3 8
#         for j, num in enumerate(nums):
#             if j>0 and nums[j-1] ==num:
#                 continue
#             for i in dict[num]:
#                 result[i]=j
#         return result
            


        # for num in nums:
        #     if num in dict:
        #         dict[num]+=1
        #     else:
        #         dict[num]=1
        # count={}
        # for num in sorted(dict):
        #     count[num]=sum(dict[i] for i in dict if i< num)
        # result=[]
        # for num in nums:
        #     result.append(count[num])
        # return result


        # result = []
        # for i in nums:
        #     count = 0
        #     for j in nums:
        #         if j < i:
        #             count+=1
        #     result.append(count)
        # return result




# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
