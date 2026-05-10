class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {
            0: 0
        }
        for coin in coins:
            cache[coin] = 1
        
        for i in range(1, amount + 1):
                for coin in coins:
                    if (i - coin) in cache:
                        if i in cache:
                            cache[i] = min(cache[i], cache[i-coin] + 1)
                        else:
                            cache[i] = cache[i-coin] + 1
                    else:
                        if i not in cache:
                            cache[i] = math.inf
        print(cache)
        if cache[amount] == math.inf:
            return -1
        else:
            return cache[amount]
    
        # 1 2 3 4 5 6 7 8 9 10 11
        # 

        