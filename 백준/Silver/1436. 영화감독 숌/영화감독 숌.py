
N = int(input())
count = value = 0
while True:
    if count == N:
        break
    if str(666) in str(value):
        count+=1
    value +=1
print(value-1)
