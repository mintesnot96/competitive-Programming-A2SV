class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        def isArithmetic(arr):
            d = arr[1] - arr[0]
            for i in range(1, len(arr)):
                if arr[i] - arr[i-1] != d:
                    return False
            return True
        # mnlnog(n)
        result = []
        for i in range(len(l)):
            subarray = nums[l[i]:r[i]+1]
            subarray.sort() #n
            result.append(isArithmetic(subarray))
        return result
