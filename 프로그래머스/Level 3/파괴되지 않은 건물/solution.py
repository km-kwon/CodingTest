def solution(board, skill):  
    visited = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    
    # type, (r1, c1)~(r2, c2) 범위, degree
    for t, r1, c1, r2, c2, degree in skill:
        visited[r1][c1] += degree if t==2 else (-1)*degree
        visited[r1][c2+1] += degree if t==1 else (-1)*degree
        visited[r2+1][c1] += degree if t==1 else (-1)*degree
        visited[r2+1][c2+1] += degree if t==2 else (-1)*degree
    
    for j in range(len(board[0])):
        for i in range(len(board)):
            visited[i+1][j] += visited[i][j]
        
    for i in range(len(board)):
        for j in range(len(board[0])):
            visited[i][j+1] += visited[i][j]
    
    answer = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += visited[i][j]
            if board[i][j] > 0: answer += 1
            
    return answer


solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],	[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]] )
solution([[1,2,3],[4,5,6],[7,8,9]]	,[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]])