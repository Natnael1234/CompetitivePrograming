class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str1 = ''
        str2 = ''
        for i in s:
            if i in str2:
                if len(str1) < len(str2):
                    str1 = str2
                str2 = str2[str2.index(i) + 1:]
            str2 += i
        if len(str1) < len(str2):
            str1 = str2
        return len(str1)
