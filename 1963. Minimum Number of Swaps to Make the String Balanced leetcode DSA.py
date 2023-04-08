class Solution:
    def minSwaps(self, s: str) -> int:
        if not s:
            return 0
          
        count = 0
        for c in s:
            if c == "[":
                count += 1
            elif count > 0:
                count -= 1
                
        return (count + 1) // 2
#       https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/
