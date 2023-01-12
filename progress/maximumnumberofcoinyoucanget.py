class Solution(object):
    def maxCoins(self, piles):

        output = 0
        piles.sort()
 
        while len(piles) > 0:
            
            piles.pop()
            output += piles.pop()
            piles.pop(0)

        return output
