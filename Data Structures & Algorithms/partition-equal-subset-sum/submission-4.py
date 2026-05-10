class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 1 2 3 4 5 5
        n = len(nums)
        arr_sum = sum(nums)
        if n == 1 or arr_sum % 2 == 1:
            return False
        def dfs(i, cursum, targetsum):
            if i > n - 1:
                return False
            if cursum == targetsum:
                return True
            if cursum > targetsum:
                return False
            
            if dfs(i + 1, cursum + nums[i], targetsum):
                return True
            if dfs(i + 1, cursum, targetsum):
                return True
            return False
        
        return dfs(0, 0, arr_sum // 2)

        
        

            
        return False

        