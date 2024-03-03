def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]  # 프로세스와 우선순위를 튜플로 묶어서 관리
    execution_order = 0  # 실행 순서

    while True:
        current = queue.pop(0)  # 현재 프로세스와 우선순위
        if any(current[1] < other[1] for other in queue):  # 우선순위가 더 높은 프로세스가 있다면
            queue.append(current)  # 다시 큐의 맨 끝으로
        else:
            execution_order += 1  # 실행 순서 증가
            if current[0] == location:  # 사용자가 지정한 위치의 프로세스라면
                return execution_order  # 현재 실행 순서 반환
