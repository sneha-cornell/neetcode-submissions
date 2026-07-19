class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp state - length of LIS ending in index i 
        #O(n^2) time 
        # n =len(nums)
        # dp=[1]*n
        # for i in range(1,n):
        #     for j in range(i):
        #         if nums[j]<nums[i]:
        #             dp[i]=max(dp[i],dp[j]+1)
        # return max(dp)
        tails = []
        for num in nums:
            low,high = 0, len(tails)
            while low<high: 
                mid = (low+high)//2
                if tails[mid]<num: 
                    low = mid+1
                else: 
                    high = mid
            if low==len(tails):
                tails.append(num) #extend the LIS
            else:
                tails[low]=num #keeps existing length but replaces with smaller value 
        return len(tails)