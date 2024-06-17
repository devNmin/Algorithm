# 10811 바구니 뒤집기

N, M = list(map(int, input().split()))

arr = [[n] for n in range(N + 1)]

for m in range(M):
    i, j = list(map(int, input().split()))
    tmp = []
    for n in range(i, j + 1):
        tmp.append(arr[n])
    tmp.reverse()
    for idx, n in enumerate(range(i, j + 1)):
        arr[n] = tmp[idx]

for i in range(1, N + 1):
    print(arr[i][0], end=' ')