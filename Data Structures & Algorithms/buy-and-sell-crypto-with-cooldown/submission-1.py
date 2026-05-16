class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo= {}
        def dfs(i,holding):
            if i>=len(prices):
                return 0 
            if (i,holding) in memo: 
                return memo[(i,holding)]
            cooldown = dfs(i+1,holding)

            if holding: 
                sell = dfs(i+2,False)+prices[i]
                memo[(i,holding)]=max(cooldown,sell)
            else: 
                buy = dfs(i+1,True)-prices[i]
                memo[(i,holding)]=max(cooldown,buy)
            return memo[(i,holding)]

        return dfs(0,False)