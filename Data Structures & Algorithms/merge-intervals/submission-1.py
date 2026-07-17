class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #if end of prev=start of next, it is overlapping
        #return output in any order
        #sort first
        
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]

        for start,end in intervals[1:]: 
            if start<=res[-1][1]:
                res[-1][1]=max(res[-1][1],end)
            else: 
                res.append([start,end])
        return res