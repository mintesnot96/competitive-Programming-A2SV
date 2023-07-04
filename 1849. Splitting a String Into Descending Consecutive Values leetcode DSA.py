# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/
class Solution:
    def splitString(self, s: str) -> bool:
        def isValid(s: str, start: int, prev: int, segment: int) -> bool:
            if start == len(s) and segment > 1:
                return True

            curr = 0
            i = start
            while i < len(s):
                curr = curr * 10 + int(s[i])
                if curr > 9999999999:
                    return False
                if (prev == -1 or curr == prev - 1) and isValid(s, i + 1, curr, segment + 1):
                    return True
                i += 1

            return False

        return isValid(s, 0, -1, 0)
