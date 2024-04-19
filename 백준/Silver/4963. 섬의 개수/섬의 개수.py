def bfs(si, sj):
    q = [(si, sj)]

    while q:
        ci, cj = q.pop(0)
        for ni, nj in [(ci - 1, cj), (ci + 1, cj), (ci, cj - 1), (ci, cj + 1), (ci + 1, cj + 1), (ci - 1, cj - 1),
                       (ci - 1, cj + 1), (ci + 1, cj - 1)]:
            if 0 <= ni < h and 0 <= nj < w and arr[ni][nj] == 1:
                q.append((ni, nj))
                arr[ni][nj] = 0

while True:
    w, h = list(map(int, input().split()))
    if not w and not h:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                arr[i][j] = 0
                bfs(i, j)
                ans += 1
    print(ans)
