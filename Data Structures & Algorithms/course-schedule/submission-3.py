class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #input prereq - each sublist has 2 elements, 2nd element take 1st
        #1st element take second
        #make an adjacency list to visualize this 
        #total numCourses you can take at most 
        #output boolean if all courses can be taken 

        #no. of nodes = no. of courses you can take (0, numCourses-1)
        #graph - for topological sort, cycle detection, default value initialized even for node with no edges
        graph = {i:[] for i in range(numCourses)}
        for a,b in prerequisites: 
            graph[b].append(a) #to take a you have to take b first 
        
        #topo sort - provide linear ordering of DAG where every edge points forward 
        #kahn's does it with bfs and dfs does it with post order traversal 

        states = [0]*numCourses #all nodes are marked unvisited 
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