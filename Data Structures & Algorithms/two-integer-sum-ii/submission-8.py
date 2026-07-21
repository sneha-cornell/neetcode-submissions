class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # seen = {}
        # for i,num in enumerate(numbers):
        #     complement =target -num
        #     if complement in seen:
        #         j = seen[complement] 
        #         return [j+1,i+1]
        #     seen[num]=i
        # return []
        low,high = 0,len(numbers)-1
        while low<high: 
            s = numbers[low]+numbers[high]
            if s==target: 
                return [low+1,high+1]
            elif s<target:
                low+=1
            else: 
                high-=1
        return []

