class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range (len(l)): 
            ans = []
            ret = True
            ans = nums[l[i] : r[i]+1]
            ans.sort()
            check = ans[1] - ans[0]
            for j in range(1, len(ans)-1):
                if not (ans[j + 1] - ans[j] == check):
                    ret = False
            res.append(ret)
        return res
