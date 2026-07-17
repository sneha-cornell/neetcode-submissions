class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #peak if > than neighbors
        #return index of any one peak element
        #adjacent elememnts are not duplicates right? 


        low, high = 0, len(nums)-1
        while low<high: 
            mid = (low+high)//2
            #peak at mid or left
            if nums[mid]>nums[mid+1]:
                high =mid
            else: 
                low = mid +1
        return low
