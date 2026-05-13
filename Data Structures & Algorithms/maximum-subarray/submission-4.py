class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        n = len(nums)

        L = 0
        curr_sum = 0
        for R in range(n):
            curr_sum += nums[R]
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
                L = R + 1
                
                
            
                
        return max_sum
        