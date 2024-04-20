def bfs(si, sj):
    cnt = 1
    q = [(si, sj)]
    arr[si][sj] = 1
    while q:
        ci, cj = q.pop(0)
        for ni, nj in [(ci - 1, cj), (ci + 1, cj), (ci, cj - 1), (ci, cj + 1)]:
            if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] == 0:
                q.append((ni, nj))
                arr[ni][nj] = 1
                cnt +=1
    return cnt

M, N, K = list(map(int, input().split()))
arr = [[0] * N for i in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = list(map(int, input().split()))
    for y in range(y1, y2):
        for x in range(x1, x2):
            arr[y][x] = 1

ans = 0
lst = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            lst.append(bfs(i, j))
            ans += 1
lst.sort()
print(ans)
print(*lst)