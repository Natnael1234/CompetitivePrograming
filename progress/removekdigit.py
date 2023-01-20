class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and stack[-1] > i and k:
                stack.pop()
                k -= 1
            stack.append(i)
        while stack and k:
            stack.pop()
            k -= 1
        if not stack:
            return '0'
        return str(int(''.join(stack)))
