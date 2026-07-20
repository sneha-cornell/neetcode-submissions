class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #backtracking problem
        result = []
        used = [False]*len(nums)
        def backtrack(path):
            if len(path)==len(nums): #full permutation built 
                result.append(path[:])
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]=True 
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i]=False
        backtrack([])
        return result 