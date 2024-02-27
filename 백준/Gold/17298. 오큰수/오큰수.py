
import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

# 미리 -1로 가득채움
result = [-1] * N
stack = []

for i in range(N):
    # 스택에 값이 있고 지금비교하는 값과 stack에 넣은 마지막값인덱스의 arr 비교 
    # stack에 마지막값은 지금 앞에서부터 돌기때문에 인덱스로 접근해서 푸는것임
    while stack and arr[i] > arr[stack[-1]]:
        result[stack[-1]] = arr[i]
        stack.pop()

    stack.append(i)

print(*result)