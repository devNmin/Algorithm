def solution(clothes):
    clothes_dict = {}
    for name, category in clothes:
        if category not in clothes_dict:
            clothes_dict[category] = [name]
        else:
            clothes_dict[category].append(name)
    answer = 1
    for _, value in clothes_dict.items():
        answer *= (len(value) + 1)
    
    return answer -1