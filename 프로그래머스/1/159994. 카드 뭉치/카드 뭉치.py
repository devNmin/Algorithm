def solution(cards1, cards2, goal):
    index1, index2 = 0, 0  # 각 카드 뭉치의 인덱스를 초기화
    
    for word in goal:
        # cards1에서 단어를 꺼낼 수 있는 경우
        if index1 < len(cards1) and cards1[index1] == word:
            index1 += 1
        # cards2에서 단어를 꺼낼 수 있는 경우
        elif index2 < len(cards2) and cards2[index2] == word:
            index2 += 1
        else:
            # goal 배열의 단어가 어느 카드에서도 꺼낼 수 없는 경우
            return "No"
    
    return "Yes"
