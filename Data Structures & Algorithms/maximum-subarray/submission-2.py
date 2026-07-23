class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #find largest sum of elements in array (must be contiguous)
        #elements can be negative ! - sliding window will not work 
        # so use kadane algorithm 
        #return sum 
        if not nums: 
            return 0
        curr_sum, max_sum = nums[0],nums[0]

        for num in nums[1:]: 
            curr_sum=max(num,curr_sum+num)
            max_sum = max(curr_sum,max_sum)
        return max_sum