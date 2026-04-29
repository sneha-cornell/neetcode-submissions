"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # count = 0
        if not intervals: 
            return 0 

        intervals.sort(key=lambda x:x.start)
        heap = []

        # for i in range(1,len(intervals)):
        #     if intervals[i].start>intervals[i-1].start and intervals[i].end<intervals[i-1].end:
        #         count+=1
        # return count 

        for interval in intervals: 
            if heap and heap[0]<=interval.start: 
                heapq.heappop(heap)
            heapq.heappush(heap,interval.end)
        return len(heap)
