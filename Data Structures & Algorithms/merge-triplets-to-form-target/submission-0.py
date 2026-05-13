class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = [0,0,0]
        for t in triplets: 
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue
            result[0]=max(result[0],t[0])
            result[1]=max(result[1],t[1])
            result[2]=max(result[2],t[2])
        return result==target