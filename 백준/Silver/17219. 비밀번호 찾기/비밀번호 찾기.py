import sys

N, M = list(map(int, sys.stdin.readline().split()))

password_dict = {}
for _ in range(N):
    a, b = list(sys.stdin.readline().split())
    password_dict[a] = b

for _ in range(M):
    a = sys.stdin.readline().strip()
    print(password_dict[a])