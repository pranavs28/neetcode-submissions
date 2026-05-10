class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        elif n == 1:
            return cost[0]
        elif n == 2:
            return min(cost[0], cost[1])
        
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0
        dp[2] = min(cost[0], cost[1])
        i = 3
        while i < n + 1:
            dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])
            i+=1
        
        # [1,2,1,2,1,1,1]
        # [1,2,2,2,3,4,5]

        return dp[n]