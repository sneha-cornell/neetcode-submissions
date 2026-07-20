class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #recurse on permutations 
        #dfs (check neighbors) + backtrack (let other paths use them)

        rows, cols = len(board), len(board[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r,c,i):
            if i==len(word):
                return True
            if (r<0) or (r>=rows) or (c<0) or (c>=cols) or board[r][c]!=word[i]:
                return False
            board[r][c]='#' #mark visited 
            for dr,dc in dirs: 
                if dfs(r+dr,c+dc,i+1): 
                    return True
            board[r][c]=word[i]
                
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False
