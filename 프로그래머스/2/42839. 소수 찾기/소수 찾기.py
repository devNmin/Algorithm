from itertools import permutations

def solution(numbers):
    answer = 0
    all_c =  []
    nums = [n for n in numbers]                   # numbers를 하나씩 자른 것
    per = []                                      
    for i in range(1, len(numbers)+1):            # numbers의 각 숫자들을 순열로 모든 경우 만들기
        permu = permutations(nums, i)
        for perm in permu:
            perm = int(''.join(perm))
            if perm not in per:
                per.append(perm)
    print(per)
    for p in per:
        if p <=1:
            answer+= 0
        else:
            for i in range(2,(p//2+1)):
                if p % i == 0:
                    break
            else:
                answer+=1
    return answer