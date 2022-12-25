class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortednums = sorted(nums)
        dic = {}
        result = []

        for i in range(len(sortednums)):
            if sortednums [i] not in dic:
                dic[sortednums[i]] = i
        for i in nums:
            result.append(dic[i])
        return result
