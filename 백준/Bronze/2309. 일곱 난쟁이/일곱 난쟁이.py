# 일곱난쟁이 2309 백준
from itertools import combinations
friends = []
for _ in range(9):
    friends.append(int(input()))

n = 7
combinations_list = list(combinations(friends, 7))

for comb in combinations_list:
    if sum(comb) == 100:
        comb = sorted(comb)
        comb = list(map(str,comb))
        print('\n'.join(comb))
        break
