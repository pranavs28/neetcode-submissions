class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        


        #                .
        #           2              -2
        #       2      -2       2     -2
        #     2  -2   2  -2    2 -2   2 -2
        #     F   T   T  F     T  F   F  F

        #perform dfs with i, target
        # base cases: 
        #  - past end of list, return 0. 
        #  - end of list: if target = 0, return 1 else 0
        # dfs(i, sum) = dfs(i + 1, sum + target[i]) + dfs(i + 1, sum - target[i])
        # dfs(0, target)

        n = len(nums)
        cache = {}
        self.cache_use = 0
        def dfs(i, target_sum):
            if i == n: 
                if target_sum == 0:
                    return 1
                return 0
            
            if (i, target_sum) in cache:
                self.cache_use += 1
                return cache[(i, target_sum)]
            
            cache[(i, target_sum)] = dfs(i + 1, target_sum + nums[i]) + dfs(i + 1, target_sum - nums[i])
            return cache[(i, target_sum)]
        
        res = dfs(0, target)
        print(self.cache_use)
        return res
                
            

            

            