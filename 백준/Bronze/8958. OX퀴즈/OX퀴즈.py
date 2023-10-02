T = int(input())

for tc in range(T):
    OX = input()
    score = 0
    total = 0
    for ele in OX:
        if ele =="O":
            score += 1
            total +=score
        else:
            score = 0
    print(total)