class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(k):
            count = {}
            start, end = 0, 0
            res = 0
            while end < len(nums):
                count[nums[end]] = count.get(nums[end], 0) + 1
                while len(count) > k:
                    count[nums[start]] -= 1
                    if count[nums[start]] == 0:
                        del count[nums[start]]
                    start += 1
                res += end - start + 1
                end += 1
            return res
        return atMostK(k) - atMostK(k-1)

# https://leetcode.com/problems/subarrays-with-k-different-integers/description/
