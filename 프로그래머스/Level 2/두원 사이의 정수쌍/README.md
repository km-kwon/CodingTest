### 두 원사이의 정수 쌍

---

성공 코드

```
import math


def solution(r1, r2):
    answer = 0

    for x in range(1, r2+1):
        y = int(math.sqrt(r2*r2 - x*x))
        if x < r1:
            y1 = math.ceil(math.sqrt(r1*r1 - x*x))
        else:
            y1 = 0
        answer = answer + y - y1+1
    return answer*4
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
