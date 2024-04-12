# 바이러스
def bfs(n):
    global ans
    q = [n]
    v = [0] * (N + 1)
    v[n] = 1
    while q:
        number = q.pop()
        for c in adj[number]:
            if v[c] == 0:
                v[c] = 1
                q.append(c)
                ans += 1


N = int(input())
T = int(input())
adj = [[] for _ in range(N + 1)]

for _ in range(T):
    a, b = list(map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)

ans = 0

bfs(1)
print(ans)