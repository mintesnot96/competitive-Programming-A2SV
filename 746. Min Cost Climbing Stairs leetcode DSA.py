https://leetcode.com/problems/min-cost-climbing-stairs/description/
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a=0
        for i in range(2,len(cost)):
            
            cost[i]+=min(cost[i-1],cost[i-2])
            if i==len(cost)-1:
                a=i
                break
                
        return min(cost[a],cost[a-1])
