class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #sorted nums in ascending order 
        #find target integer within this input array 
        #return target's index else -1 if not found 

        l,h =0,len(nums)-1
        while l<=h: 
            mid = (l+h)//2
            if nums[mid]==target: 
                return mid 
            elif nums[mid]<target: 
                l=mid+1
            else:
                h=mid-1
        return -1