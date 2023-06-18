n = int(input()) 
values = list(map(int,input().split()))
maxV = max(values)
sum = 0
for i in range(n):
    sum += values[i]/maxV*100
print(sum/n)