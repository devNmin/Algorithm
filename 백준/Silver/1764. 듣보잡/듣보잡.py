N, M = list(map(int, input().split()))
alst = set()
blst = set()
for i in range(N):
    alst.add(input())

for j in range(M):
    blst.add(input())

ans = list(alst & blst)
ans.sort()
print(len(ans))
print(*ans, sep="\n")
