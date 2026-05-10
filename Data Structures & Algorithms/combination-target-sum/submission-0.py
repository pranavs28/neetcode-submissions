class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        subset = []
        def dfs(i, subset_sum):
            if subset_sum == target:
                res.append(list(subset))
                return
            if i >= len(nums) or subset_sum > target:
                return
            
            subset.append(nums[i])
            dfs(i, subset_sum + nums[i])
            
            subset.pop()
            dfs(i + 1, subset_sum)

        dfs(0, 0)
        return res