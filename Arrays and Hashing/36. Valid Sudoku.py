import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_check = [[False for i in range(9)] for j in range(9)]
        
        col_check = [[False for i in range(9)] for j in range(9)]
        
        sub_box_check = [[False for i in range(9)] for j in range(9)]
        
        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] != '.':
                    
                    num = int(board[row][col])-1
                    
                    # fill in row_check
                    if row_check[row][num] == True:
                        # print(num+1, 'row_check', row, col)
                        return False
                    else:
                        row_check[row][num] = True
                    
                    # fill in col_check
                    if col_check[col][num] == True:
                        # print(num+1, 'col_check', row, col)
                        return False
                    else:
                        col_check[col][num] = True
                    
                    # fill in sub_box_check
                    r = math.floor(row / 3)
                    c = math.floor(col / 3)
                    
                    seq = 3*r+c
                    
                    if sub_box_check[seq][num] == True:
                        # print(num+1,'sub_box_check',row, col)
                        return False
                    else:
                        sub_box_check[seq][num] = True
            
        return True
