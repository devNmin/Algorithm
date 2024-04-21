def bfs(si, sj, lst, value):
    q = [(si, sj)]
    lst[si][sj] = 0
    while q:
        ci, cj = q.pop(0)
        for ni, nj in [(ci - 1, cj), (ci + 1, cj), (ci, cj - 1), (ci, cj + 1)]:
            if 0 <= ni < N and 0 <= nj < N and lst[ni][nj] == value and lst[ni][nj] != 0:
                q.append((ni, nj))
                lst[ni][nj] = 0


N = int(input())
arr = [list(input()) for i in range(N)]

narr = [a[:] for a in arr]

ans = [0, 0]

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            bfs(i, j, arr, arr[i][j])
            ans[0] += 1

ans2 = 0
for i in range(N):
    for j in range(N):
        if narr[i][j] == "R":
            narr[i][j] = "G"

for i in range(N):
    for j in range(N):
        if narr[i][j] != 0:
            bfs(i, j, narr, narr[i][j])
            ans[1] += 1
print(*ans)