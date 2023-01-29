class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i, j = 0, 0
        while j < n:
            curr = chars[j]
            count = 0
            while j < n and chars[j] == curr:
                j += 1
                count += 1
            chars[i] = curr
            i += 1
            if count > 1:
                for c in str(count):
                    chars[i] = c
                    i += 1
        return i
