from itertools import permutations
def solution(k, dungeons):

    dungeon_number = list(range(1,len(dungeons)+1))
    
    permutation = []                                      
    
    for perm in permutations(dungeon_number):
        permutation.append(list(perm))
    
    result = [0] * len(permutation)
    
    for i, permut in enumerate(permutation):
        value = k
        for per_i in permut:
            minim_value, used_value = dungeons[per_i - 1]
            if (value < minim_value):
                break
            else:
                value -= used_value

                result[i] +=1


    return max(result)