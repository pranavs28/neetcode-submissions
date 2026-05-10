class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ['}', ']', ')'] and len(stack) == 0:
                return False
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
        print(stack)
        return True if len(stack) == 0 else False

        