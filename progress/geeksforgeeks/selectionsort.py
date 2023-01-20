
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
