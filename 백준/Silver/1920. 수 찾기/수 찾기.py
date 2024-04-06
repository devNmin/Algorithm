# N(1 ≤ N ≤ 100,000)
# M(1 ≤ M ≤ 100,000)
import sys

N = int(sys.stdin.readline())
arr_n = set(map(int, sys.stdin.readline().split()))

M = int(input())
arr_m = list(map(int, sys.stdin.readline().split()))


for i in range(len(arr_m)):
    if arr_m[i] in arr_n:
        print(1)
    else:
        print(0)
