class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.minstack.append(min(self.minTop(), val))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        return
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return math.inf
        
    def minTop(self):
        if self.minstack:
            return self.minstack[-1]
        else:
            return math.inf

    def getMin(self) -> int:
        print(self.minstack)
        return self.minstack[-1]
        
