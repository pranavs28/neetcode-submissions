class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        perm = []
        def dfs():
            if len(perm) == len(nums):
                res.append(list(perm))
                return
            
            for i in range(len(nums)):
                if nums[i] not in perm:
                    perm.append(nums[i])
                    dfs()
                    perm.pop()

        dfs()
        return res