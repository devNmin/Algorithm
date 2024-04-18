N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def bfs(si, sj):
    q = []
    q.append((si, sj))
    narr[si][sj] = 0
    while q:
        ci, cj = q.pop(0)

        for ni, nj in [(ci - 1, cj), (ci + 1, cj), (ci, cj - 1), (ci, cj + 1)]:
            if 0 <= ni < N and 0 <= nj < N and narr[ni][nj] == 1:
                narr[ni][nj] = 0
                q.append((ni, nj))


ans = -1
for h in range(1, 101):
    narr = [a[:] for a in arr]

    for i in range(N):
        for j in range(N):
            if narr[i][j] >= h:
                narr[i][j] = 1
            else:
                narr[i][j] = 0

    mx_value = 0
    for i in range(N):
        for j in range(N):
            if narr[i][j] == 1:
                bfs(i, j)
                mx_value += 1
    ans = max(ans, mx_value)
print(ans)