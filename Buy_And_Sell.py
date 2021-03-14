class Solution:
    def maxProfit(self, prices):
        minVal=prices[0]
        maxVal=0

        for i in range(0,len(prices)):
            if prices[i]-minVal<0:
                minVal=prices[i]
            if prices[i]-minVal>maxVal:
                maxVal=prices[i]-minVal
                
        return maxVal



a=Solution()
print(a.maxProfit([10,63,12,32]))