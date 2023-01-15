class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        num = len(arr)
        ans = []
        
        for i in range(num):
            MAX = max(arr[:num-i])
            max_index = arr.index(MAX)+1
            arr[:max_index] = reversed(arr[:max_index])
            ans.append(max_index)
            
            arr[:num-i] = reversed(arr[:num-i])
            ans.append(num-i)
            
        return ans 
