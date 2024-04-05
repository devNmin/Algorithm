import sys
N = int(sys.stdin.readline())
# 1 ≤ N ≤ 1,000,000
result = []
for _ in range(N):
    result.append(int(sys.stdin.readline()))
    
result.sort(reverse=False)
for r in result:
    print(r)
