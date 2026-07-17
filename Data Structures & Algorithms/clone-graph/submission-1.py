"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #graph is guaranteed connected - can I reach all nodes from starting node 
        #deep copy - new node with the same val 
        #handle cycles, self-loops, duplicates 
        if not node: 
            return None
        visit = {}

        def dfs(node):
            if node in visit: 
                return visit[node]
            clone = Node(node.val)
            visit[node]=clone
            for nei in node.neighbors: 
                clone.neighbors.append(dfs(nei))
            return clone
        return dfs(node)
