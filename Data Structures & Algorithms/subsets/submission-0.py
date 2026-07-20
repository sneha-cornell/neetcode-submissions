class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #every partial path is a subset not just the leaves 
        result = []
        def backtrack(start,path):
            result.append(path[:]) #every node is a subset
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return result