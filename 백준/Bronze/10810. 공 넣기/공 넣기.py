# 10810 공 넣기

N, M = list(map(int, input().split()))

arr = [[0] for _ in range(N + 1)]

for m in range(M):
    i, j, k = list(map(int, input().split()))
    for n in range(i, j + 1):
        arr[n].append(k)

for n in range(1, N + 1):
    print(arr[n][-1], end=" ")
