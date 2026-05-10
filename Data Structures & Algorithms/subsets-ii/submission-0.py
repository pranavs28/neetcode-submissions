class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sets = []
        def dfs(nums):
            if not nums:
                return [[]]
            else:
                res = dfs(nums[1:])
                new_subsets = []
                for s in res:
                    new_item = [nums[0]] + s
                    new_subsets.append(new_item)
                return res + new_subsets
        
        all_subsets = dfs(nums)
        for s in all_subsets:
            if s not in sets:
                sets.append(s)
        
        return sets