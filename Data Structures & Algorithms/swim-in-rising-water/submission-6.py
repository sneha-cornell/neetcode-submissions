class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit =set()
        heap = [(grid[0][0],0,0)]
        dirs = [(1,0),(0,1),(0,-1),(-1,0)]

        while heap: 
            t,r,c=heapq.heappop(heap)
            if (r,c) in visit: 
                continue
            visit.add((r,c))
            if r==n-1 and c==n-1: 
                return t
            for dr,dc in dirs: 
                nr,nc = r+dr, c+dc
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in visit: 
                    heapq.heappush(heap,(max(grid[nr][nc],t),nr,nc))
        return -1
