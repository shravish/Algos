def is_valid_sudoku(board):
    def is_valid_block(block):
        nums = [num for num in block if num != '.']
        return len(nums) == len(set(nums))

    for i in range(9):
        row = board[i]
        column = [board[j][i] for j in range(9)]
        if not is_valid_block(row) or not is_valid_block(column):
            return False

    for i in range(3):
        for j in range(3):
            block = [board[x][y] 
                     for x in range(i*3, i*3 + 3) 
                     for y in range(j*3, j*3 + 3)]
            if not is_valid_block(block):
                return False

    return True
sudoku_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(is_valid_sudoku(sudoku_board))  
# Output: True
