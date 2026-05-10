class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((temp, i))
        return res



        