class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        subset = []
        def dfs(i, subset_sum):
            if subset_sum == target:
                res.append(list(subset))
                return
            if i >= len(candidates) or subset_sum > target:
                return
            
            subset.append(candidates[i])
            dfs(i + 1, subset_sum + candidates[i])
            
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, subset_sum)

        dfs(0, 0)
        return res