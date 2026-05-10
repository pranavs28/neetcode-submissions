class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i in range(len(heights)):
            new_index = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                area = height * (i - index)
                max_area = max(area, max_area)
                new_index = min(new_index, index)
            stack.append((new_index, heights[i]))
        while stack:
            index, height = stack.pop()
            area = height * (len(heights) - index)
            max_area = max(area, max_area)

        return max_area




        