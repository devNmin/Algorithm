# 14500 테트로미노
def dfs(n, sm, tlst):
    global ans
    if n == 4:
        ans = max(ans, sm)
        return
    for si, sj in tlst:
        for ni, nj in [(si - 1, sj), (si + 1, sj), (si, sj - 1), (si, sj + 1)]:
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0:
                v[ni][nj] = 1
                dfs(n + 1, sm + arr[ni][nj], tlst + [(ni, nj)])
                v[ni][nj] = 0


N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        v[i][j] = 1
        dfs(1, arr[i][j], [(i, j)])
print(ans)