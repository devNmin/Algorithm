from collections import deque

import sys
input = sys.stdin.readline

n = int(input())
maps = [ list(map(int,input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

d = [[1,0],[0,1]] #아래, 오른쪽

queue = deque()
queue.append([0,0])

flag = False

while(queue):
    r, c = queue.popleft()

    move = maps[r][c] #현재위치에서 무조건 이동해야하는 칸수
    
    if move == 0:
        continue
    if move == -1:
        flag = True
        break

    for i in range(2):
        dr = r+ d[i][0] * move
        dc = c+ d[i][1] * move
        
        if(0>dr or dr >= n or 0>dc or dc >= n):
            continue
        
        queue.append([dr,dc])


if flag: print("HaruHaru")
else : print("Hing")