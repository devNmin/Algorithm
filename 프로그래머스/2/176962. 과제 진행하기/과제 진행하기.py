def time_to_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes

def solution(plans):
    # 시간 순서대로 정렬
    plans.sort(key=lambda x: time_to_minutes(x[1]))
    
    result = []
    stack = []
    current_time = time_to_minutes(plans[0][1])
    
    for i in range(len(plans)):
        name, start_time, duration = plans[i]
        start_time = time_to_minutes(start_time)
        duration = int(duration)
        
        # 만약 새로운 과제 시작 시간이 현재 시간보다 크다면, 중간에 멈춘 과제를 완료할 시간을 가질 수 있음
        while stack and current_time < start_time:
            last_task_name, last_task_remaining_time = stack.pop()
            if current_time + last_task_remaining_time <= start_time:
                current_time += last_task_remaining_time
                result.append(last_task_name)
            else:
                stack.append((last_task_name, last_task_remaining_time - (start_time - current_time)))
                current_time = start_time
        
        # 현재 과제를 진행
        current_time = start_time + duration
        result.append(name)
        
        # 다음 과제를 고려하기 위해 마지막 과제는 스택에 저장
        if i < len(plans) - 1:
            next_start_time = time_to_minutes(plans[i + 1][1])
            if current_time > next_start_time:
                stack.append((name, current_time - next_start_time))
                result.pop()  # 완료한 과제에서 제거, 스택에서 꺼내는 순간에 추가할 것임

    # 스택에 남아있는 과제들을 완료
    while stack:
        result.append(stack.pop()[0])
    
    return result
