def solution(citations):
    number_cit = range(1,len(citations)+1)
    max_h = 0
    for number in number_cit:
        answer = 0
        for citation in citations:
            if number <= citation:
                answer += 1
        if number <= answer:
            if max_h < number:
                max_h = number
    return max_h
