class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val_stack = []
        for token in tokens:
            
            if token.lstrip('-').isnumeric():
                val_stack.append(int(token))


            
            else:

                arg2 = val_stack.pop()
                arg1 = val_stack.pop()

            if token == '+':
                val_stack.append(arg1 + arg2)

            if token == '-':
                val_stack.append(arg1 - arg2)
            
            if token == '*':
                val_stack.append(arg1 * arg2)
            
            if token == '/':
                val_stack.append(math.trunc(arg1 / arg2))

        return val_stack.pop()


        