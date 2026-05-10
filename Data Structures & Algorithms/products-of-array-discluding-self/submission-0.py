class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_mult = [1] * n
        suffix_mult = [1] * n
        for i in range(n):
            if i == 0:
                prefix_mult[i] = nums[i]
                suffix_mult[n - 1 - i] = nums[n - 1 -i]
            else:
                prefix_mult[i] = prefix_mult[i-1] * nums[i]
                suffix_mult[n-1-i] = suffix_mult[n - i] * nums[n - 1 - i]
        res = []
        print(prefix_mult, suffix_mult)
        for i in range(n):
            if i == 0:
                res.append(suffix_mult[i+1])
            elif i == (n-1):
                res.append(prefix_mult[n-2])
            else:
                res.append(prefix_mult[i-1] * suffix_mult[i+1])
        return res
        

        