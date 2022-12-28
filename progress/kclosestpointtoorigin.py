class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        ans = []

        def dist(a, b):
            return sqrt(a**2 + b**2)

        for p in points:
            d = dist(p[0], p[1])
            arr.append([d,p[0], p[1]])

        arr.sort()
        for i in range(k):
            ans.append(arr[i][1:])
        return ans
