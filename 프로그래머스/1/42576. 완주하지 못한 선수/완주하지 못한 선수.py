def solution(participant, completion):
    answer = ''
    # 1명 제외 모두 완주
    # 참여자: participant
    # 완주한 사람 이름: completion
    participant_dict = {
        
    }
    for part in participant:
        if part not in participant_dict:
            participant_dict[part] = 1
        else:
            participant_dict[part] += 1
            
    for com in completion:
        if com in participant_dict:
            if participant_dict[com] == 1:
                del participant_dict[com]
            else:
                participant_dict[com] -= 1
    return list(participant_dict)[0]