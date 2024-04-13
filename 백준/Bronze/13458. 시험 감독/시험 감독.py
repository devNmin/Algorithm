# 13458 시험감독

N = int(input())
rooms = list(map(int, input().split()))
B, C = list(map(int, input().split()))
ans = 0
for room in rooms:

    room -= B
    ans += 1
    if room <= 0:
        continue

    sub = (room + C - 1) // C
    ans += sub

print(ans)
