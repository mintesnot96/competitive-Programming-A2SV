# https://leetcode.com/problems/get-maximum-in-generated-array/description/
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        memo=[0]*(n+1)
        memo[1]=1

        for i in range(2,n+1):
            if i%2==0:
                memo[i]=memo[i//2]
            elif i%2!=0:
                memo[i]=memo[i//2]+memo[i-i//2]
        print(memo)
        return max(memo)



        # memo=[-1]*(n+1)
        # def dp(n):
        #     print(memo)
        #     if n==0:
        #         return 0
        #     elif n==1:
        #         return 1
        #     elif memo[n] != -1:
        #         return memo[n]
        #     memo[n]=dp(n-1)+dp(n-2) if n%2!=0 else dp(n//2)
        #     return max(memo[:])
        # print(memo)
        # return dp(n)


