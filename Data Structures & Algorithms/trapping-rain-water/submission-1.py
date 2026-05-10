class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        left_max = height[left]
        right = n -1
        right_max = height[right]
        water = 0
        while left < right:
            if height[left] <= height[right]:
                water += max(0,left_max - height[left])
                left += 1
                left_max = max(left_max, height[left])
            else:
                water += max(0,right_max - height[right])
                right -= 1
                right_max = max(right_max, height[right])

        return water
        