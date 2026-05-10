class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        return True if len(set_nums) < len(nums) else False
        