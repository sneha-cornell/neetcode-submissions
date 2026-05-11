from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid: 
            return 
        rows, cols = len(grid),len(grid[0])
        INF = float('inf')
        queue = deque()
        visit = set()
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]

        def bfs(visit, queue):
            while queue: 
                r,c = queue.popleft()
                for dr,dc in dirs: 
                    nr,nc = r+dr,c+dc
                    if nr<0 or nc<0 or nr>=rows or nc>=cols:
                        continue 
                    if (nr,nc) not in visit and grid[nr][nc]!=-1:
                        visit.add((nr,nc))
                        grid[nr][nc]=grid[r][c]+1
                        queue.append((nr,nc))
        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c]==0:
                    queue.append((r,c))
                    visit.add((r,c))
        bfs(visit,queue)
        #return grid
   
