class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        print(set_nums)
        n = len(nums)
        max_count = 0
        for i in range(n):
            if nums[i] - 1 not in set_nums:
                count = 1
                while nums[i] + count in set_nums:
                    count += 1
                max_count = max(max_count, count)
        return max_count
                

        