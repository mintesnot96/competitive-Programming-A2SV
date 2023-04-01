
from sortedcontainers import SortedList

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted_nums = SortedList(nums1)
        for i, num in enumerate(nums2):
            index = 0 if sorted_nums[-1] <= num else sorted_nums.bisect_right(num)
            nums1[i] = sorted_nums[index]
            del sorted_nums[index]
        return nums1
# https://leetcode.com/problems/advantage-shuffle/
