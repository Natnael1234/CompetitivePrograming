class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dec = {}
        for i in range(len(nums)):
            if nums[i] in dec:
                dec[nums[i]].append(i)
            else:
                dec[nums[i]] = [i]
        res = 0
        for key, values in dec.items():
            if len(values) >= 2:
                n = len(values)
                res += n*(n-1)/2
        return int(res)
