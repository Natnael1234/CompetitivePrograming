#User function Template for python3

class Solution: 
    def select(self, arr, i):
        return
            
    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            minnimum_index=i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[minnimum_index]:
                    minnimum_index=j
            if minnimum_index!=i:
                arr[i],arr[minnimum_index]=arr[minnimum_index],arr[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends