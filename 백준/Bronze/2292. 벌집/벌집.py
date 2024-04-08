# 벌집

N = int(input())

if N == 1:
    print("1")
elif N <= 7:
    print("2")
else:
    arr = list(range(8, 19 + 1))
    cnt = 3

    while True:
        if N in arr:
            print(cnt)
            break
        arr = list(range(arr[0] + 6 * (cnt - 1), (arr[-1] + 6 * cnt) + 1))
        cnt += 1
