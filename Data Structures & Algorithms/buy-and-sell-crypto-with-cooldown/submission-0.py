class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        weeks = len(prices)
        memo = {}

        def dfs(i, haveCoin):
            if i >= weeks:
                return 0
            if (i, haveCoin) in memo:
                return memo[(i, haveCoin)]
            
            do_nothing = dfs(i+1, haveCoin)

            if haveCoin:
                #have coin
                sell_coin = prices[i] + dfs(i+2, False)
                res = max(do_nothing, sell_coin)
            else:
                #no coin
                buy_coin = -prices[i] + dfs(i+1, True)
                res = max(do_nothing, buy_coin)
            
            memo[(i, haveCoin)] = res
            return res
        
        return dfs(0, False)