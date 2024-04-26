def bfs(ci, cj):
    q = [(ci, cj)]
    v[ci][cj] = 1
    ans[i][j] = 0
    while q:
        si, sj = q.pop(0)
        for ni, nj in [(si - 1, sj), (si + 1, sj), (si, sj - 1), (si, sj + 1)]:
            # if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and arr[ni][nj] != 0:
            #     q.append((ni, nj))
            #     v[ni][nj] = 1
            #     ans[ni][nj] = ans[si][sj] + 1
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0:
                if arr[ni][nj] == 0:
                    v[ni][nj] = 1
                    ans[ni][nj] = 0
                elif arr[ni][nj] == 1:
                    v[ni][nj] = 1
                    ans[ni][nj] = ans[si][sj] + 1
                    q.append((ni, nj))
    return


N, M = list(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(N)]

ans = [[-1] * M for _ in range(N)]
v = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            bfs(i, j)


for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(0, end = " ")
        else:
            print(ans[i][j], end = " ")
    print()