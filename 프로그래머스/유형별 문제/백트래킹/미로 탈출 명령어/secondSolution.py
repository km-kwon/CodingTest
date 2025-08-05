import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 제한을 늘려줌
#              아래        왼       오른        위
dir_info = [('d',1,0),('l',0,-1),('r',0,1),('u',-1,0)]
path_list = []
def find(n,m, cur_x, cur_y, des_x,des_y, k, cur_str):
    if k == 0 and cur_x == des_x and cur_y == des_y:
        path_list.append(cur_str)
        return
    elif (abs(cur_x-des_x) + abs(cur_y-des_y)) > k or k<=0 or len(path_list) > 0 or abs((abs(cur_x-des_x) + abs(cur_y-des_y))-k) % 2 != 0:
        return
    else:
        for (char, dx, dy) in dir_info:
            next_x, next_y = cur_x + dx, cur_y + dy 
            if 1<=next_x<=n and 1<=next_y<=m:
                find(n,m,next_x, next_y, des_x, des_y, k-1, cur_str+char)
    return
def solution(n, m, x, y, r, c, k):
    answer = ''
    find(n,m,x,y,r,c,k,answer)
    if len(path_list) > 0:
        answer = path_list[0]
    else:
        answer = "impossible"
    return answer

solution(3,4,2,3,3,1,5)
solution(2,2,1,1,2,2,2)
solution(3,3,1,2,3,3,4)