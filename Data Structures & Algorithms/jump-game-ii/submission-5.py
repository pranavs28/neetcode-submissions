class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        steps = 0
        i = 0
        while i < n-1:
            max_jump = 0
            max_jump_index = 0
            for j in range(1, nums[i] + 1):
                if i + j == n -1:
                    return steps + 1
                if i + j < n and j + nums[i+j] > max_jump:
                    max_jump = j + nums[i+j]
                    max_jump_index = i + j
            steps += 1
            i = max_jump_index
            
        return steps
            

        