# 14501 퇴사
def dfs(n,sm):
    global ans
    if n >=N:
        ans = max(ans,sm)
        return

    if n + tlst[n][0]<=N:
        dfs(n+tlst[n][0],sm+tlst[n][1])

    dfs(n+1,sm)
N = int(input())
tlst = []
for _ in range(N):
    tlst.append(list(map(int, input().split())))
ans = 0

dfs(0,0)
print(ans)