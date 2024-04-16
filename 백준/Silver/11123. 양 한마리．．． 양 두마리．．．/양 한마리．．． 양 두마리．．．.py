def bfs(si, sj):
    q = []
    q.append((si, sj))
    arr[si][sj] = 0
    while q:
        ci, cj = q.pop(0)
        for ni, nj in [(ci - 1, cj), (ci + 1, cj), (ci, cj - 1), (ci, cj + 1)]:
            if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] == 1:
                arr[ni][nj] = 0
                q.append((ni,nj))


def change_value(char):
    if char == "#":
        return 1
    else:
        return 0


T = int(input())
for _ in range(T):
    H, W = list(map(int, input().split()))

    arr = [list(map(change_value, input())) for _ in range(H)]
    v = [[0] * W for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 1:
                bfs(i, j)
                ans += 1
    print(ans)