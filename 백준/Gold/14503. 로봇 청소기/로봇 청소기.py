# 14503 로봇 청소기

N, M = list(map(int, input().split()))
r, c, d = list(map(int, input().split()))
# 동 서 남 북
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
## 북, 동, 하, 서 ( 시계방향 )
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# [1] 현재칸 청소(청소되지 않을 때)
# [2] 주변칸 청소(청소되지 않은 빈칸이 없는경우)
# 2-1: 후진 -> [1]
# 2-2: 후진시 벽이면 스탑
# [3]: 주변칸 청소(청소되지않은 빈칸이 있는경우)
# 3-1 반시계 회전
# 3-2 바라보는 방향을 기준으로 앞쪽칸이 청소되지 않은 빈칸인 경우 전진
# 3-3 -> [1]


cnt = 1
visited[r][c] = 1

while True:
    is_check = False
    for _ in range(4):
        d = (d + 3) % 4
        ny, nx = r + dy[d], c + dx[d]
        if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 0:
            if visited[ny][nx] == 0:
                visited[ny][nx] = 1
                cnt += 1
                r = ny
                c = nx
                is_check = True
                break
    if not is_check:
        if arr[r - dy[d]][c - dx[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r - dy[d], c - dx[d]
