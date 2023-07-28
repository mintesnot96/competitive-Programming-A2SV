class Solution:
    def tribonacci(self, n: int) -> int:
        memo=[-1]*(n+1)

        def dp(n):
            if n<=0:
                return 0
            elif n==1 or n==2:
                return 1
            elif memo[n]!=-1:
                return memo[n]
            memo[n]=dp(n-1)+dp(n-2)+dp(n-3)
            return memo[n]
        return dp(n)


# https://leetcode.com/problems/n-th-tribonacci-number/description/
