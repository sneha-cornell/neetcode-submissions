class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visit = {}
        for i,num in enumerate(nums):
            diff = target-num
            if diff in visit: 
                return [visit[diff],i]
            visit[num]=i
