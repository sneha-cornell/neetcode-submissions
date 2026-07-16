class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #input - 2d grid with 1s,0s
        #output - integer of no. of islands
        #diagonals too? 
        #can we modify in place 

        if not grid or not grid[0]: 
            return 0
        rows,cols = len(grid),len(grid[0])
        visit = set()
        dirs = ((1,0),(0,1),(-1,0),(0,-1))

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]=='0' or (r,c) in visit:
                return 0
            visit.add((r,c))
            for dr,dc in dirs: 
                dfs(r+dr,c+dc)
        count =0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in visit: 
                    dfs(r,c)
                    count+=1
        return count 


