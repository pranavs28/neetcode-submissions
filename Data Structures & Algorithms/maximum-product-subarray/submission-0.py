class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxProduct = 1
        minProduct = 1

        for n in nums:
            temp = maxProduct
            maxProduct = max(n, maxProduct * n, minProduct * n)
            minProduct = min(n, temp * n, minProduct * n)
            res = max(res, maxProduct)
        
        return res