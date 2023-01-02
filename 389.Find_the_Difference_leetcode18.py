class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
            if len(t) < len(s):
                return None
            for ti in t:
                if ti not in s:
                    return ti
                else:
                    s=s.replace(ti, '', 1)
              
# question link
# https://leetcode.com/problems/find-the-difference/submissions/
