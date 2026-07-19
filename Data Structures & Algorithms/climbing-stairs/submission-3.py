class Solution:
    def climbStairs(self, n: int) -> int:
        #dp state - no.of ways to climb
        if n<=1:
            return 1 
        # dp = [0]*(n+1)
        # dp[0]=dp[1]=1
        # for i in range(2,n+1):
        #     dp[i]=dp[i-1]+dp[i-2] #since dp[i] only uses previous 2 values, we don't need the whole array, so optimize
        # return dp[n]
        prev2, prev1 = 1,1
        for _ in range(2,n+1):
            curr=prev1+prev2 
            prev2 = prev1
            prev1 = curr 
        return prev1  
