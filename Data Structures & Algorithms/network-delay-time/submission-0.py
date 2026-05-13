class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times: 
            graph[u].append((v,w))
        dist= {i:float('inf') for i in range(1,n+1)}
        dist[k]=0
        heap = [(0,k)]

        while heap: 
            cost,node = heapq.heappop(heap)
            if cost>dist[node]:
                continue
            for neighbor,weight in graph[node]:
                newcost = cost+weight
                if newcost<dist[neighbor]:
                    dist[neighbor]=newcost
                    heapq.heappush(heap,(newcost,neighbor))
        result =max(dist.values())
        return result if result!=float('inf') else -1


