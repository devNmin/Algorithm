def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0] * 3
    result = []
    for i, answer in enumerate(answers):
        if answer == one[i % 5]:
            score[0] +=1
        if answer == two[i % 8]:
            score[1] +=1
        if answer == three[i % 10]:
            score[2] +=1
    max_score = max(score)

    for i in range(len(score)):
        if max_score == score[i]:
            result.append(i+1)

    return result