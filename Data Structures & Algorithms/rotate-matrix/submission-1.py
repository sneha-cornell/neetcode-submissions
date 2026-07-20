class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
      #transpose and reverse each row 

      n = len(matrix)
      for i in range(n):
        for j in range(i+1,n): #so you don't swap twice and make no change 
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
      for i in range(n):
        matrix[i].reverse()

     