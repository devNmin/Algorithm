from collections import deque

N = int(input())
lst = deque(list(range(1, N + 1)))

while True:
    if len(lst) == 1:
        print(lst[0])
        break
    # [1] 제일 위에 카드 버림
    lst.popleft()
    # [2] 제일 위의 카드를 제일 아래로 옮김
    value = lst.popleft()
    lst.append(value)
