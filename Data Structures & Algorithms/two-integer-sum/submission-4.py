class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #2 pointers - i and i+1 or smallest/largest sums
        #find complements in set - handles duplicate values 
        #only integers, will fit in memory
        #how will input, output look like
        comp = {}
        for i,num in enumerate(nums):
            
            diff = target-num
            if diff in comp:
                return [comp[diff],i]
            comp[num]=i
        return []

              
