class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        res = []
        for i in range(0, len(nums)):
            res.append(int(nums[i]))
        res.sort()
        res.reverse()
        l = res[k-1]
        return str(l)
