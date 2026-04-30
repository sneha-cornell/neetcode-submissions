class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x = parent[x]
            return x
        def union(x,y):
            px,py = find(x),find(y)
            if px==py: 
                return 0
             
            parent[px]=py
            return 1  
        components= n
        for a,b in edges: 
            components-=union(a,b)
        return components

