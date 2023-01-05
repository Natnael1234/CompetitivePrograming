class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:     
        
        res = [-1] * len(nums1)
        
        for i in range (0, len(nums1)):
            if nums1[i] == nums2[len(nums2)-1]:
                    res[i] = -1
            
            for j in range (0, len(nums2)-1):
                
                if nums2[j] == nums1[i]:
                    for n in range (j+1, len(nums2)):
                        
                        if nums2[j] < nums2[n]:
                            res[i] = nums2[n]  
                            break
                        elif nums2[j]>nums2[n]:
                            continue
                        n+=1
                j+=1
            i+=1
        return res
