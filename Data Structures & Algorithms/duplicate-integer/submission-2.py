class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #input array of integers
        #output boolean 

        #leverage set property
        # return len(set(nums))!=len(nums)

        #exit faster as soon as we find 1st duplicate
        seen = set()
        for num in nums: 
            if num in seen: 
                return True
            seen.add(num)
        return False 