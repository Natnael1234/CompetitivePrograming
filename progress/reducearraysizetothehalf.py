class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic = {}
        num = len(arr)//2
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        val = list(dic.values())
        val.sort(reverse = True)
        output = 0
        for i in range (0, len(val)):
            output += val[i]
            if output >= num:
                return i + 1
