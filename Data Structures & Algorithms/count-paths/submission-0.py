class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # 21 15 10 6 3 1
        # 6   5  4 3 2 1
        # 1   1  1 1 1 1
        
        #knapsack bottom up
        if m == 1 and n == 1:
            return 1
        
        dp = [[0] * n for _ in range(m)]

        for col in range(n):
            dp[m-1][col] = 1
        
        for row in range(m-2, -1, -1):
            dp[row][n-1] = 1

            for col in range(n-2, -1, -1):
                dp[row][col] = dp[row + 1][col] + dp[row][col + 1]
        print(dp)
        return dp[0][0]

