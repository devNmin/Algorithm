def bfs(si, sj):
    global ans

    q = []
    q.append((si, sj))

    while q:
        ci, cj = q.pop(0)
        if (ci, cj) == (N-1, M-1):
            return v[N-1][M-1]
        for ni, nj in [(ci - 1, cj), (ci + 1, cj), (ci, cj - 1), (ci, cj + 1)]:
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == "1":
                q.append((ni, nj))
                arr[ni][nj] = 0
                v[ni][nj] = v[ci][cj] + 1


N, M = list(map(int, input().split()))
v = [[1] * M for i in range(N)]
arr = [list(input()) for _ in range(N)]

print(bfs(0, 0))