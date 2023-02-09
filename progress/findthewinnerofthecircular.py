class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        # recursive approach
        # if(n==1):
        #     return 1    
        # return (self.findTheWinner(n-1,k)+k-1)%(n) + 1;

        nums = list(range(1,n+1))
        while len(nums)>1:
            i=(k-1)%len(nums)
            nums.pop(i)
            nums = nums[i:]+nums[:i]

        return nums[0]
