class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 1 2 3 4 5 5
        n = len(nums)
        arr_sum = sum(nums)
        if n == 1 or arr_sum % 2 == 1:
            return False
    
        def dfs(i, cursum, targetsum, cache):
            if i == n:
                return False
            if cursum > targetsum:
                return False
            if cache[i][cursum] != -1:
                return True if cache[i][cursum] == 1 else False
            if cursum == targetsum:
                cache[i][cursum] = 1
                return True
            
            
            outcome = dfs(i + 1, cursum + nums[i], targetsum, cache)
            if outcome:
                # cache[i+1][cursum + nums[i]] = 1
                cache[i][cursum] = 1
                return True
            outcome = dfs(i + 1, cursum, targetsum, cache)
            if outcome:
                # cache[i+1][cursum + nums[i]] = 1
                cache[i][cursum] = 1
                return True
            
            cache[i][cursum] = 0
            return False
        
        return dfs(0, 0, arr_sum // 2, [[-1] * (arr_sum + 1) for _ in range (n+1)])

        
        

            
        return False

        