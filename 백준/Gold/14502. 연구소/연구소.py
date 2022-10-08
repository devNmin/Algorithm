from collections import deque
from itertools import combinations
from copy import deepcopy
que = deque()

N, M = list(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(N)]

hubo = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            que.append((i, j))
        elif arr[i][j] == 0:
            hubo.append((i, j))
 # x1,y1 / x2, y2
direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]


combs = combinations(hubo,3)
max_cnt = -1000
for comb in combs: # 벽 후보들
    arr2 = deepcopy(arr)
    que_c = deepcopy(que)
    visited = []
    cnt = 0

    for wx,wy in comb: # 벽 1 추가
        arr2[wx][wy] = 1

    while que_c:
        x, y = que_c.popleft()
        for dx, dy in direct:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < N and 0 <= ny < M and arr2[nx][ny] == 0:
                if (nx, ny) not in visited:
                    arr2[nx][ny] = 2
                    que_c.append((nx, ny))
                    visited.append((nx, ny))
    for i in range(N):
        for j in range(M):
            if arr2[i][j] == 0:
                cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
print(max_cnt)
#
