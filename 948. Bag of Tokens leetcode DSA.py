# https://leetcode.com/problems/bag-of-tokens/
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
            n = len(tokens)
            tokens.sort()
            l, r = 0, n-1
            p, s = power, 0
            while l <= r:
                if p >= tokens[l]:
                    s += 1
                    p -= tokens[l]
                    l += 1
                elif s > 0 and r > l:
                    p += tokens[r]
                    s -= 1
                    r -= 1
                else:
                    break
            return s
