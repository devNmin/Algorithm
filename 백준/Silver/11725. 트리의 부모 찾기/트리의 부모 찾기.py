def bfs(n):
    q = []
    q.append(n)
    while q:
        c = q.pop(0)
        for number in adj[c]:
            if v[number] == 0:
                q.append(number)
                v[number] = c


T = int(input())
adj = [[] for _ in range(T + 1)]
v = [0] * (T + 1)
for _ in range(T - 1):
    a, b = list(map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)

bfs(1)
print(*v[2::], sep="\n")