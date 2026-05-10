class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        def rob_line(nums):
            n = len(nums)
            if n == 0:
                return 0
            if n == 1:
                return nums[0]
            if n == 2:
                return max(nums[0], nums[1])
            
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            i = 2
            while i < n:
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
                i+=1
            return dp[i-1]

        return max(rob_line(nums[1:]), rob_line(nums[:-1]))


        # [2, 9, 8, 3, 6]
        # [2, 9, ]
        