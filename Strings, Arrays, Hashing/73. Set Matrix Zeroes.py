class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_set_to_zero = set()
        cols_set_to_zero = set()
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    rows_set_to_zero.add(i)
                    cols_set_to_zero.add(j)
                    
        for i in range(0, m):
            for j in range(0, n):
                if i in rows_set_to_zero or j in cols_set_to_zero:
                    if matrix[i][j] != 0:
                        matrix[i][j] = 0
