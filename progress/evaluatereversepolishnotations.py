class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) < 1:
            output = int(tokens[0])
        stack.append(int(tokens[0]))
        output = stack[0]
        for i in range (1, len(tokens)):
            if tokens[i] == "+":
                second = stack.pop()
                first = stack.pop()
                output = first + second
                stack.append(output) 
            elif tokens[i] == "-":
                second = stack.pop()
                first = stack.pop()
                output = first - second
                stack.append(output)
            elif tokens[i] == "*":
                second = stack.pop()
                first = stack.pop()
                output = first * second
                stack.append(output)
            elif tokens[i] == "/":
                second = stack.pop()
                first = stack.pop()
                output = first / second
                stack.append(output)
            else:
                stack.append(tokens[i])
            stack = [int(x) for x in stack]
            
        return int(output)
