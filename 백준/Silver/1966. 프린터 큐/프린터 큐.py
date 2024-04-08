T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    queue = list(range(0, len(arr)))

    ans = []
    order = 1
    # 현재 문서보다 중요도가 높은게 있으면 뒤로 배치
    i = 0
    while True:
        for j in range(i + 1, len(queue)):
            if arr[i] < arr[j]:
                value = queue.pop(0)
                queue.append(value)

                value2 = arr.pop(0)
                arr.append(value2)
                break
        else:
            check = queue.pop(0)
            arr.pop(0)
            if check == M:
                print(order)
                break
            order += 1
    # 아니라면 인쇄
