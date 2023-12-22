board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

import collections

def isValidSudoku(board):
    row_set = collections.defaultdict(set)
    col_set = collections.defaultdict(set)
    grid_set = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            current_el = board[r][c]
            if current_el == ".":
                continue
            if current_el in row_set[r] or \
                current_el in col_set[c] or \
                current_el in grid_set[(r//3 , c//3)]:
                return False
            
            col_set[c].add(current_el)
            row_set[r].add(current_el)
            grid_set[(r//3 , c//3)].add(current_el)
    return True
    

print(isValidSudoku(board))
