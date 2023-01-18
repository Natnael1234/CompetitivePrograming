class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        h = 0
        i = 0
        while i < len(citations): 
            if citations[i] > h:
                h += 1
            i += 1
        return h
