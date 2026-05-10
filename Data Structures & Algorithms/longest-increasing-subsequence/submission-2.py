class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1
        
        dp = [1] * n
        i = 1
        while i < n:
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            i += 1
        return max(dp)

        # 1 3 6 7 9 4 10 5 6
        # 1 2 3 4 5 5 6  6 7

        