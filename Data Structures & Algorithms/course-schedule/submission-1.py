class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for a,b in prerequisites: 
            graph[b].append(a)

        states = [0]*numCourses
        def dfs(node):
            if states[node]==1:
                return False
            if states[node]==2:
                return True
            states[node]=1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            states[node]=2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True