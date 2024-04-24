N = int(input())
tlst = list(map(int,input().split()))

ans = 0
tlst.sort()
for i in range(N):
    ans += tlst[i]*(N-i)

print(ans)