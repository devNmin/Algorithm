def solution(name, yearning, photo):
    
    answer = []
    name_yearning = {
        
    }
    for i in range(len(name)):
        name_yearning[name[i]] = yearning[i]
    
    for pho in photo:
        sum = 0
        for name in pho:
            sum += name_yearning.get(name,0)
        answer.append(sum)
    return answer