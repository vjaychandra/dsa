def board_valid(board):

    return row_valid(board) and \
            col_valid(board) and \
            box_valid(board)


def row_valid(board):
    for row in board:
        if not unit_valid(row):
            return False
    return True

def col_valid(board):
    """
    * -> unpacks each row
    """
    
    for col in zip(*board):
        if not unit_valid(col):
            return False
    return True

def box_valid(board):

    for i in (0, 3, 6):
        for j in (0, 3, 6):
            row = [ board[x][y] for x in range(i, i+3) for y in range(j, j+3) ]
            if not unit_valid(row):
                return False
    return True


def unit_valid(row):

    row = [ i for i in row if i != "." ]
    return len(set(row)) == len(row)


board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]


print(board_valid(board))
