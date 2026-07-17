"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #start<=end guaranteed 
        #need to find min no. of rooms to schedule all meetings 
        #maintain a min heap - earliest end times at the front of heap
        #is intervals sorted? 

        #empty input returns 0 
        if not intervals: 
            return 0 
        intervals.sort(key=lambda x:x.start)
        rooms = []

        for interval in intervals: 
            if rooms and rooms[0]<=interval.start: 
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval.end)
        return len(rooms)