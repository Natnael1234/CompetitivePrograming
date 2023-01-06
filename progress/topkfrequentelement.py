import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq = dict()

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for key,val in freq.items():
            if len(ans) < k:
                heapq.heappush(ans,[val,key])
            else:
                heapq.heappushpop(ans,[val,key])
        return [key for value, key in ans]

                



        
