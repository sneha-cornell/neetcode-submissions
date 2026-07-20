class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #reuse is allowed within same path so don't need visit set like in permutations 
        result = []

        def backtrack(start,combo,remaining):
            if remaining==0: 
                result.append(combo[:])
                return 
            if remaining<0: 
                return 
            for i in range(start,len(nums)):
                combo.append(nums[i])
                backtrack(i,combo,remaining-nums[i])
                combo.pop()
        backtrack(0,[],target)
        return result
            