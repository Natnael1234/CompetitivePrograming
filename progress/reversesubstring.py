class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans = [] 
        i = 0
        while i < len(s): 
            if s[i] == "(":
                ans.append(i)
            elif s[i] == ")":
                if len(ans) > 0:
                    start = ans.pop()
                    print (start)
                    s = s[:start] + s[i-1: start: -1] + s[i+1:]
                    i -=2
            i += 1
        return s
