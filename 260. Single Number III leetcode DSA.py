# https://leetcode.com/problems/single-number-iii/
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorAll = 0
        for num in nums:
            xorAll ^= num

        rightmostSetBit = xorAll & -xorAll

        num1, num2 = 0, 0
        for num in nums:
            if num & rightmostSetBit:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]
