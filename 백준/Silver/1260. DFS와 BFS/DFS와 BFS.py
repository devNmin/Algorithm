# 1260 DFS와 BFS

def dfs(n):
    v[n] = 1
    ans_dfs.append(n)
    for i in adj[n]:
        if v[i] == 0:
            dfs(i)


def bfs(n):
    q = []
    q.append(n)
    ans_bfs.append(n)
    v[n] = 1
    while q:
        c = q.pop(0)
        for i in adj[c]:
            if v[i] == 0:
                v[i] = 1
                q.append(i)
                ans_bfs.append(i)


N, M, V = list(map(int, input().split()))
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = list(map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)

for a in adj:
    a.sort()
v = [0] * (N + 1)
ans_dfs = []
ans_bfs = []
dfs(V)

v = [0] * (N + 1)
bfs(V)
print(*ans_dfs)
print(*ans_bfs)