class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right = 0,0
        ones, max_ones = 0,0

        while right < len(nums):
            if nums[right] == 1:
                ones += 1
                right += 1
                max_ones = max(max_ones, ones)
            else:
                max_ones = max(max_ones, ones)
                ones = 0
                right += 1
                left = right
        


        return max_ones
        


        