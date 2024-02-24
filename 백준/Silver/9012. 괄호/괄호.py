import sys
T = int(sys.stdin.readline())

def check_vps(arr):
    stack = []
    
    for arr_i in arr:
        if arr_i == "(":
            stack.append("(")
        elif arr_i == ")":
            if not stack:
                return "NO"
            stack.pop()
            
    if not stack:
        return "YES"
    else:
        return "NO"
# 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력
for _ in range(T):
    arr = list(sys.stdin.readline())
    print(check_vps(arr))