class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l,r=0,1
        maxp=0
        while r<len(prices):
            if prices[l]<prices[r]:
                n=prices[r]-prices[l]
                maxp=max(n,maxp)
            else:
                l=r
            r+=1
        
        return maxp
        