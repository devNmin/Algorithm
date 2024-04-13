# 14889 스타트와 링크
def dfs(n,alst,blst):
    global ans

    if n == N:
        if len(alst) == len(blst):
            asm = bsm = 0
            for i in range(M):
                for j in range(M):
                    asm += arr[alst[i]][alst[j]]
                    bsm += arr[blst[i]][blst[j]]
            ans = min(ans, abs(asm - bsm))
        return
    dfs(n + 1, alst + [n], blst)  # A팀 선택
    dfs(n + 1, alst, blst + [n])  # B팀 선택

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

# 리스트중 2명씩 뽑는 함수(조합)
M = N//2
ans = 100*M*N
dfs(0,[],[])
print(ans)