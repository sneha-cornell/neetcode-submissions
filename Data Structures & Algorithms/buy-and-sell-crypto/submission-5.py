class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #input array, output integer of max profit 
        #fits in memory
        #max profit is at least 0
        #sorted? neg values in input? 

        max_profit = 0
        start = prices[0]
        
        for i in range(len(prices)):
            if prices[i]>start: 
                max_profit = max(max_profit,prices[i]-start)
            start=min(start,prices[i])
        return max_profit