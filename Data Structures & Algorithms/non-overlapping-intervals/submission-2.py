class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #need to make all intervals non -overlapping
        #return min. no of intervals to remove any overlapping with others 

        intervals.sort(key=lambda x:x[1])
        count =0
        prev_end = intervals[0][1]

        for i in range(1,len(intervals)):
            if intervals[i][0]<prev_end: 
                count+=1
            else: 
                prev_end = intervals[i][1]
        return count 