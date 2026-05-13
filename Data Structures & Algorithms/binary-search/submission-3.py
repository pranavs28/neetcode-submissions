class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1
        
        L, R = 0, n-1

        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1
        
        return -1