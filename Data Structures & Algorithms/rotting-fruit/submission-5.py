class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #output - min no. of minutes for 0 fresh fruits 
        #return -1 if fresh can never rot or no fresh at all? 
        #multi source bfs - sequential not simultaneous at t=0
        if not grid: 
            return 0
        rows,cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        def bfs(queue,fresh):
            time =0 
            while queue: 
                r,c,t = queue.popleft()
                for dr, dc in dirs: 
                    nr = r+dr
                    nc = c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh-=1
                        time=t+1
                        queue.append((nr,nc,time))
            return time, fresh



        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c,0))
                elif grid[r][c]==1:
                    fresh+=1
        if fresh==0:
            return 0 
        time, fresh = bfs(queue,fresh)
        return time if fresh==0 else -1
