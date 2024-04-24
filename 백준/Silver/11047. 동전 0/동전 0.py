import sys

# sys.stdin = open("input.txt", "r")

N, K = list(map(int, sys.stdin.readline().split()))

coins = []
for _ in range(N):
    coins.append(int(input()))

ans = 0
while True:
    v = [0] * N
    min_value = 100000000
    min_idx = 0
    if K == 0:
        break
    for i in range(N):
        value = K // coins[i]

        v[i] = value
        if min_value > value != 0:
            min_value = value
            min_idx = i
    ans += min_value
    K -= coins[min_idx] * min_value
print(ans)