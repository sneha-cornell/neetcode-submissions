class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #input array of integers
        #output boolean 
        #leverage set property
        return len(set(nums))!=len(nums)