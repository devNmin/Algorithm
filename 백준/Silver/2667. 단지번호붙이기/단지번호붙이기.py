N = int(input())
arr = []

def bfs(i,j):
    q = []
    q.append((i,j))
    cnt = 1
    while q:
        ci,cj = q.pop(0)
        for ni,nj in [(ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)]:
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1:
                arr[ni][nj] = 0
                q.append((ni,nj))
                cnt+=1
    return  cnt

for _ in range(N):
    arr.append(list(map(int,input())))

ans = 0
result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            arr[i][j] = 0
            result.append(bfs(i,j))
            ans+=1
        
print(ans)
result.sort()
print(*result,sep="\n")