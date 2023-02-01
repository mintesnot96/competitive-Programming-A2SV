class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

            def flip(nums, end):
                start = 0
                while start < end:
                    nums[start], nums[end] = nums[end], nums[start]
                    start += 1
                    end -= 1
                return nums
            ans = []
            range = len(arr)
            sortedArr = sorted(arr)

            while arr != sortedArr:
                indexOfLargest = arr.index(max(arr[:range]))
                flip (arr, indexOfLargest)
                if indexOfLargest != 0:
                    ans.append(indexOfLargest+1)
                flip(arr, range-1)
                ans.append(range)
              
                range -= 1
            return ans
# https://leetcode.com/problems/pancake-sorting/
