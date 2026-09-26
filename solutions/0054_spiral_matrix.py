class Solution: 
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]: 
        row = len(matrix) 
        col = len(matrix[0]) 
        arr = [] 
        start_row,start_col = 0,0 
        end_row,end_col = len(matrix)-1,len(matrix[0])-1 
 
        while start_row <= end_row and start_col <= end_col: 
            for i  in range(start_col,end_col+1): 
                arr.append(matrix[start_row][i]) 
            for j in range(start_row+1,end_row+1): 
                arr.append(matrix[j][end_col]) 
            for i in range(end_col-1,start_col-1,-1): 
                if start_row == end_row: 
                    break 
                arr.append(matrix[end_row][i]) 
            for j in range(end_row-1, start_row, -1): 
                if start_col == end_col: 
                    break 
                arr.append(matrix[j][start_col]) 
            start_row += 1 
            start_col += 1 
            end_row -= 1 
            end_col -= 1 
        return arr 
