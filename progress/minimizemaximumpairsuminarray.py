class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        arr = []
        output = 0
        i = 0
        j = len(nums)-1
        while i < j:
            output = nums[i] + nums [j]
            arr.append(output)
            i+=1
            j-=1
        arr.sort()
        return arr[-1]
