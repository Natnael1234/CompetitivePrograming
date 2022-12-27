class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)

        while len(stones)>1:
            first = heappop(stones)*-1
            second = heappop(stones)*-1
            leftover = abs(first - second)
            heappush(stones, leftover*-1)

        return -stones[0]
