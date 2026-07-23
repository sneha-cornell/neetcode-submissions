class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        parent= list(range(n))

        def find(x):
            while parent[x]!= x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        def union(x,y):
            px,py = find(x),find(y)
            if px==py: 
                return False
            parent[px]=py
            return True
        for x,y in edges: 
            if not union(x,y):
                return False
        return True
