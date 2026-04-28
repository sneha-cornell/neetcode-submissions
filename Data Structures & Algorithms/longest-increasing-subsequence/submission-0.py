class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            low,high = 0,len(tails)
            while low<high: 
                mid = (low+high)//2
                if tails[mid]<num:
                    low = mid+1
                else: 
                    high = mid
            if low == len(tails):
                tails.append(num)
            else:
                tails[low]=num
        return len(tails)
