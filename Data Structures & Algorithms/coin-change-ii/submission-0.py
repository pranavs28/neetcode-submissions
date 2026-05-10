class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        cache = {}

        def dfs(i, curr_amount):
            if i == n:
                return 0
            
            if (i, curr_amount) in cache:
                return cache[(i, curr_amount)]

            if curr_amount == 0:
                return 1
            
            #use coin at i
            cache[(i, curr_amount)] = 0
            if curr_amount - i >= 0:
                cache[(i, curr_amount)] += dfs(i, curr_amount - coins[i])
            cache[(i, curr_amount)] += dfs(i + 1, curr_amount)
            return cache[(i, curr_amount)]
        
        return dfs(0,amount)


        #                   4 (0)
        #             3(0)   3(1)   4(1)
        #          2(0)



        