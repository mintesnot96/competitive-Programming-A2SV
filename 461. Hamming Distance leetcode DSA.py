class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result=bin(x^y)[2:]
        binary_number = result.lstrip("0")
        binary_number = binary_number.rstrip("0")
        count=0
        for digit in binary_number:
            if digit == "1":
                count += 1
        return count

# https://leetcode.com/problems/hamming-distance/description/
