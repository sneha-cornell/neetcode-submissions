class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        rank = [1]*(n+1)
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x= parent[x]
            return x
        def union(x,y):
            px,py = find(x),find(y)
            if px==py: 
                return False
            if rank[px]>rank[py]:
                parent[py]=px
            elif rank[py]>rank[px]:
                parent[px]=py
            else: 
                parent[py]=px
                rank[px]+=1
            return True
        for x,y in edges: 
            if not union(x,y):
                return [x,y] 
            
