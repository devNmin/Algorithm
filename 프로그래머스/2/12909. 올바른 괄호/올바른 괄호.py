def solution(s):
    answer = True
    stack = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for ss in s:
        if ss =="(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True