class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #array with integers in non-descending order
        #find start,end indices of target value
        #2 binary searches - leftmost, rightmost  

        if not nums: 
            return [-1,-1]

        low,high = 0,len(nums)
        output =[]
        while low<high: 
            mid = (low+high)//2
            if nums[mid]>=target:
                high=mid
            else:
                low = mid+1
        left = low 
        #check if target exists at all 
        if left==len(nums) or nums[left]!=target:
            return [-1,-1]

        low,high =0,len(nums)
        while low<high:
            mid=(low+high)//2
            if nums[mid]>target:
                high=mid
            else:
                low=mid+1
        right = low-1
        return [left,right]
                
