class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        for a,b in prerequisites: 
            graph[b].append(a)
        
        states = [0]*numCourses 
        output = []

        def dfs(node):
            if states[node]==1:
                return False
            if states[node]==2:
                return True 
            states[node]=1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            states[node]=2
            output.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output[::-1]