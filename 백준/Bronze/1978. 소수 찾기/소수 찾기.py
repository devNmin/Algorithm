N = int(input())
lst = list(map(int, input().split()))

cnt = 0
for n in lst:
    if n == 1:
        continue
    for c in range(2, int(n**0.5)+1):
        if n % c == 0:
            break
    else:
        cnt += 1
print(cnt)
