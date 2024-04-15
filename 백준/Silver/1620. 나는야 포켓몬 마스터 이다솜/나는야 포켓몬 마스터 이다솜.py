import sys
N, M = list(map(int,input().split()))

poke = {}

for i in range(1,N+1):
    idx , name = i, sys.stdin.readline().rstrip()
    poke[idx] = name
    poke[name] = idx
for _ in range(M):
    value = sys.stdin.readline().rstrip()
    if value.isdigit():
        print(poke[int(value)])
    else:
        print(poke[value])