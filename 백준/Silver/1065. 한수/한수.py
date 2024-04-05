# 1065 한수
# 한수: 어떤 양의 정수 X의 각 자리가 등차수열
# 등차수열:  연속된 두 개의 수의 차이가 일정한 수열
# 1 <= N <=1000
N = int(input())

count = 0 
if N < 100:
    print(N)
else:
    for num in range(100, N + 1):
        numbers = list(map(int, str(num)))
        if numbers[2] - numbers[1] == numbers[1] - numbers[0]:
            count +=1
    count +=99
    print(count)