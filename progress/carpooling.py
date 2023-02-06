class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        lst = []
        for people,start, end in trips:
            lst.append((start, people))
            lst.append((end, -people))
        lst.sort()
        current = 0
        for i in lst:
            current += i[1]
            if current > capacity:
                return False
        return True
