class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        Sum = sum(chalk)
        remainingSum = k % Sum
        
        for i in range(len(chalk)):
            remainingSum -= chalk[i]
            if remainingSum < 0:            
                return i
