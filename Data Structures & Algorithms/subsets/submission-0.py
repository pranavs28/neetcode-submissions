class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        else:
            res = self.subsets(nums[1:])
            return res + [[nums[0]] + s for s in res]