class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac , atl = set(),set()
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c,visit,prev):
            if ((r,c) in visit or r<0 or c<0 or r>=rows or c>=cols or heights[r][c]<prev):
                return
            visit.add((r,c))
            for dr,dc in dirs: 
                dfs(r+dr,c+dc,visit,heights[r][c])
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
        res = []

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl: 
                    res.append([r,c])
        return res 
