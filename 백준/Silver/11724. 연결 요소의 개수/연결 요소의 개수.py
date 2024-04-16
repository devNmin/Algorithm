N, M = list(map(int, input().split()))
adj = [[] for _ in range(N + 1)]
v = [0] * (N + 1)


def bfs(n):
    v[n] = 1
    q = [n]

    while q:
        number = q.pop(0)
        for value in adj[number]:
            if v[value] == 0:
                v[value] = 1
                q.append(value)


for _ in range(M):
    a, b = list(map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)

ans = 0
for i in range(1, N + 1):
    if v[i] == 0:
        bfs(i)
        ans += 1
print(ans)