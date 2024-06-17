# 10813 공 바꾸기

N, M = list(map(int, input().split()))

arr = [[n] for n in range(N + 1)]

for m in range(M):
    i, j = list(map(int, input().split()))
    arr[j], arr[i] = arr[i], arr[j]

for i in range(1, N+1):
    print(arr[i][0], end=' ')