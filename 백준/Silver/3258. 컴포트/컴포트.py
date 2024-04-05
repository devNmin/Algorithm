# 입력 받기
import sys

N, Z, M = list(map(int, sys.stdin.readline().split()))
obstacle = list(map(int, sys.stdin.readline().split()))

if Z == N:                                
    Z = 0                                      
for j in range(1, N):
    values = [(1 + j * x) % N for x in range(N)]
    for value in values:
        if value == Z:
            print(j)
            sys.exit()
        elif value in obstacle:
            break
