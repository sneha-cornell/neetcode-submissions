class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps,curr_end,farthest = 0,0,0

        for i in range(n-1):
            farthest = max(farthest,i+nums[i])
            if i==curr_end:
                jumps+=1
                curr_end = farthest
                if curr_end>=len(nums)-1:
                    break
        return jumps