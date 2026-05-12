class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        x_or = n
        for i in range(n):
            x_or ^= i ^ nums[i]
        return x_or