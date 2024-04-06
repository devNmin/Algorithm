M, N = list(map(int, input().split()))

# (1 ≤ M ≤ N ≤ 1,000,000)

for n in range(M, N + 1):
    if n == 1:
        continue
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:  # 소수가아님
            break
    else:  # 소수임
        print(n)
