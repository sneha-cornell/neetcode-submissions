class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visit = set()
        min_cost = 0
        heap = [(0,0)]

        while len(visit)<n:
            cost,node = heapq.heappop(heap)
            if node in visit: 
                continue
            visit.add(node)
            min_cost+=cost
            for neighbor in range(n):
                if neighbor not in visit: 
                    dist = (abs(points[node][0]-points[neighbor][0])+abs(points[node][1]-points[neighbor][1]))
                    heapq.heappush(heap,(dist,neighbor))

        return min_cost
        