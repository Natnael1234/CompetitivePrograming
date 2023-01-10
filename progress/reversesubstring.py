class Solution:
    def reverseParentheses(self, s: str) -> str:
        Stack = [] 
        i = 0
        while i < len(s): 
            if s[i] == "(":
                Stack.append(i)
            elif s[i] == ")":
                if len(Stack) > 0:
                    start = Stack.pop()
                    print (start)
                    s = s[:start] + s[i-1: start: -1] + s[i+1:]
                    i -=2
            i += 1
        return s
