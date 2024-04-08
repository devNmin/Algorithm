num1, num2 = list(map(int, input().split()))

minv = min(num1, num2)
maxv = max(num1, num2)

result1 = 1
for i in range(2, minv + 1):
    if maxv % i == 0 and minv % i == 0:
        result1 = i
print(result1)
v1, v2 = num1, num2
while True:
    if v1 == v2:
        print(v1)
        break
    if v1 > v2:
        v2 += num2
    else:
        v1 += num1
