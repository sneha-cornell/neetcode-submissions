class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[b].append(a)        # ← only this inside for loop

        states = [0] * numCourses     # ← same level as for loop
        output = []

        def dfs(node):
            if states[node] == 1:
                return False
            if states[node] == 2:
                return True
            states[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            states[node] = 2
            output.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return output[::-1]

        
