class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #O(mn) - copy matrix, O(n+m) - maintain visit sets for rows and cols, O(1)- use 1st row and 1st col as marker arrays 
        rows,cols = len(matrix), len(matrix[0])

        #check if any zeros in first row and first col marker arrays
        first_row = any(matrix[0][j]==0 for j in range(cols))
        first_col = any(matrix[i][0]==0 for i in range(rows))

        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j]==0:
                    matrix[i][0]=0 #mark row i has a zero
                    matrix[0][j]=0 #mark col j has a zero 
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][0]==0 or matrix[0][j]==0: #either row or col having zero will affect
                    matrix[i][j]=0
        if first_row: 
            for j in range(cols):
                matrix[0][j]=0
        if first_col: 
            for i in range(rows):
                matrix[i][0]=0
        


        