class MinStack:

    def __init__(self):
        self.stack = []
        self.min = math.inf
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            self.min = min(self.min, val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val < 0:
            self.min = self.min - val
        return
        

    def top(self) -> int:
        val = self.stack[-1]
        if val > 0:
            return val + self.min
        else:
            return self.min
        


    def getMin(self) -> int:
        return self.min
        
