class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L+R) //2
            if nums[L] <= nums[R]:
                return nums[L]
            elif nums[mid] >= nums[L]:
                L = mid + 1
            else:
                R = mid