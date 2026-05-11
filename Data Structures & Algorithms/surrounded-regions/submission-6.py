class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: 
            return 0 
        rows, cols = len(board), len(board[0])
        dirs = [(1,0),(0,1),(0,-1),(-1,0)]

        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return 
            if board[r][c]!="O":
                return
            board[r][c]="S"
            for dr, dc in dirs: 
                nr,nc = r+dr, c+dc
                dfs(nr,nc)

        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)
        for c in range(cols):
            dfs(0,c)
            dfs(rows-1,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                if board[r][c]=="S":
                    board[r][c]="O" 

                
