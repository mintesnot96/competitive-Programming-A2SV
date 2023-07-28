class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo = [-1] * (n + 1)
        def tri(n: int) -> int:
            if n <= 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            elif memo[n] != -1:
                return memo[n]

            memo[n] = tri(n - 1) + tri(n - 2) + tri(n - 3)
            return memo[n]

        return tri(n)
# https://leetcode.com/problems/n-th-tribonacci-number/description/
