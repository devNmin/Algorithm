# 분해합

N = input()
sm = 0
for n in N:
    sm +=int(n)

for n in range(int(N)):
    number = str(n)

    ch_sm = 0
    for num in number:
        ch_sm +=int(num)
    ch_sm += int(n)

    if ch_sm == int(N):
        print(n)
        break
else:
    print("0")
