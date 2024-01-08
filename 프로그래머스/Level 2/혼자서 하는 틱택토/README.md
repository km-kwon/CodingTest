### 혼자서 하는 틱택토

---

성공 코드

```
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
```

사용 개념

- 배열 count
- 외부 함수의 사용

---

다른 사람 코드 중 인상 깊었던 것

```
# Check if there is a winning row, column, or diagonal
def check_win(player, board):
    # Check rows
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True

    # Check columns
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def solution(board):
    num_x = sum(row.count('X') for row in board)
    num_o = sum(row.count('O') for row in board)

    if num_x - num_o > 0 or abs(num_x - num_o) > 1:
        return 0

    elif (check_win('O', board) and num_x != num_o - 1) or (check_win('X', board) and num_x != num_o):
        return 0

    return 1
```

```
def won(board, t):
    # 가로줄 판단.
    for row in board:
        if row == [t, t, t]:
            return True
        
    # 세로줄 판단.
    for col in range(3):
        if [board[row][col] for row in range(3)] == [t, t, t]:
            return True
        
    # 대각선 판단.
    if [board[0][0], board[1][1], board[2][2]] == [t, t, t]:
        return True
    if [board[2][0], board[1][1], board[0][2]] == [t, t, t]:
        return True
    
    return False
```
사용 개념

- sum 함수를 적절히 사용
- abs 함수 사용
- 각 성공에 대해 적절한 예외 처리
- 밑의 경우에는 [t,t,t] 이라는 형식을 사용하여 비교

