# 백준 ACM호텔 브3 10250

T = int(input())

for _ in range(T):
    H, W, N = list(map(int,input().split()))

    floor = N % H 
    room_line = (N // H) + 1
    if floor == 0:
        floor = H
        room_line -= 1
    
    print(floor * 100 + room_line)