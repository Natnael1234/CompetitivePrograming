class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        left = 0
        output = 0
        
        for right in range(len(nums)):
            k += nums[right]
            
            if k < nums[right] * (right - left + 1):
                k -= nums[left]
                left += 1
        output = right - left +1
        return output
