class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #input - array containing only 0s,1s, k integer
        #output - max number integer 

        l=0
        zeros =0

        for r in range(len(nums)):
            if nums[r]==0:
                zeros+=1
            if zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
        return len(nums)-l
