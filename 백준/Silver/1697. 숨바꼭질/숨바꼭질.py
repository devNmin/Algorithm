def bfs(s, e):
    # [1] queue, visited array create
    q = []
    v = [0] * 200001

    # [2] 초기 데이터 삽입, v[] 초기화화
    q.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        if c == e:
            return v[e] - 1
        for n in (c - 1, c + 1, c * 2):
            if 0 <= n <= 200000 and v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1

    return -1


# N(0 ≤ N ≤ 100,000)
N, K = list(map(int, input().split()))

# -1, +1, *2
ans = bfs(N, K)
print(ans)
