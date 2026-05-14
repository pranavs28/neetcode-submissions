class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        n = len(coins)

        def dfs(i, amount):
            if i >= n:
                return math.inf
            if amount == 0:
                return 0
            key = (i, amount)
            if key in memo:
                return memo[key]
            
            memo[key] = math.inf
            #choose the coin
            if amount - coins[i] >= 0:
                memo[key] = min(memo[key], 1 + dfs(i, amount - coins[i]))

            #dont choose
            memo[key] = min(memo[key], dfs(i+1, amount))

            return memo[key]
        res = dfs(0, amount)
        return res if res!= math.inf else -1