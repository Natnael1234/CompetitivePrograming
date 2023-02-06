class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrs = 0
        curr = 0

        dic = {0:1}

        for i in nums:
            curr += i
           
            if curr - k in dic:
                subarrs += dic[curr-k]

            if curr not in dic:
                dic[curr] = 1
            else:
                dic[curr]+=1
 
        return subarrs
