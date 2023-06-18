C = int(input()) 
for tc in range(C):
    values = list(map(int,input().split()))
    N = values[0]
    avg = sum(values[1:])/N

    cnt = 0
    for i in values[1:]:
        if i > avg:
            cnt+=1
    result = cnt/N*100
    print (f"{result:.3f}%")
