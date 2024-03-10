# 백준 X보다 작은 수 브5 10871

N, X = list(map(int,input().split()))
A = list(map(int,input().split()))
result = ""
for a in A:
    if a < X:
        result += str(a) + " "
print(result)