class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src,dst in sorted(tickets,reverse=True): 
            graph[src].append(dst)
        result = []
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            result.append(airport)
        dfs("JFK")
        return result[::-1]