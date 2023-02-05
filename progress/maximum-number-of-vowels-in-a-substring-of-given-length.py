class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        maxCount = 0

        for i,n in enumerate(s):
            if n in "aeiou":
                count += 1
            if i >= k and s[i-k] in "aeiou":
                count -= 1
            maxCount = max(maxCount, count) 

        return maxCount 
