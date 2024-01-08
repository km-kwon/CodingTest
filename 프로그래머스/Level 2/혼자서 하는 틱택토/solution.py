
def count(board):
    num_O, num_X = 0, 0
    for line in board:
        if "O" in line:
            num_O += line.count("O")
        if "X" in line:
            num_X += line.count("X")

    return num_O, num_X


def won(board, shape):
    for i in range(3):
        if board[i][0] == shape and board[i][1] == shape and board[i][2] == shape:
            return True
    for i in range(3):
        if board[0][i] == shape and board[1][i] == shape and board[2][i] == shape:
            return True
    if board[0][0] == shape and board[1][1] == shape and board[2][2] == shape:
        return True
    if board[2][0] == shape and board[1][1] == shape and board[0][2] == shape:
        return True
    return False


def solution(board):
    answer = -1
    num_O, num_X = count(board)
    if not (num_O == num_X or num_O == num_X+1):
        return 0
    if won(board, 'O') and won(board, 'X'):
        return 0
    if won(board, 'O') and num_O != num_X+1:
        return 0
    if won(board, 'X') and num_O != num_X:
        return 0
    return 1


# solution(["O.X", ".O.", "..X"])
solution(["OOO", "...", "XXX"])
solution(["...", ".X.", "..."])
solution(["...", "...", "..."])
