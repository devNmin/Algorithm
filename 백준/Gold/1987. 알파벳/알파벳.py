def dfs(si, sj, count):
    global ans
    ans = max(ans, count)

    for ni, nj in [(si - 1, sj), (si + 1, sj), (si, sj - 1), (si, sj + 1)]:
        if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] not in v:
            v.add(arr[ni][nj])
            dfs(ni, nj, count + 1)
            v.remove(arr[ni][nj])


R, C = list(map(int, input().split()))
arr = [list(input()) for _ in range(R)]

ans = 0
v = set(arr[0][0])
dfs(0, 0, 1)
print(ans)
