class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0
        rows, cols = len(grid),len(grid[0])
        visit = set()
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c):
            if r<0 or c<0 or c>=cols or r>=rows or grid[r][c]==0 or (r,c) in visit: 
                return 0
            visit.add((r,c))
            path_area = 0
            for dr,dc in dirs: 
                path_area+=dfs(r+dr,c+dc)
            return path_area+1
        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area,dfs(r,c))
        return area
