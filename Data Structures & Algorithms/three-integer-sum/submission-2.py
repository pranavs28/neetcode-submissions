class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    if [nums[i], nums[left], nums[right]] not in ans:
                        ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return ans

        