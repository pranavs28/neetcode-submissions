class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s,(target - p)/s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)
        stack = []
        print(pair)
        for car in pair:
            if not stack:
                stack.append(car)
                continue
            if stack and car[2] > stack[-1][2]:
                stack.append(car)

        return len(stack)
        



        