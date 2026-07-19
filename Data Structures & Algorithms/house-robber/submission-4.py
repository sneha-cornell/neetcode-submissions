class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp - amount of money when reached at that house
        #are all house values non negative?  
        # if not nums: 
        #     return 0 
        # if len(nums)==1:
        #     return nums[0]
        #0th house is valid, not like amount 0 or stair 0 which is just starting point 
        # dp = [0]*len(nums)
        # dp[0]=nums[0]
        # dp[1]=max(nums[0],nums[1])
        # for i in range(2,len(nums)):
        #     dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        # return dp[-1]
        prev2,prev1 =0,0
        for num in nums: 
            curr = max(prev2+num,prev1)
            prev2 = prev1
            prev1 = curr 
        return prev1
