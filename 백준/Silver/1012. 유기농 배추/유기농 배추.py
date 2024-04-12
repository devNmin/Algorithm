import sys

# sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10000)
input = sys.stdin.readline
MAX = 50 + 10

dirR = [1, -1, 0, 0]
dirC = [0, 0, 1, -1]


def dfs(y, x):
    graph[y][x] = False
    for dirIdx in range(4):
        newY = y + dirR[dirIdx]
        newX = x + dirC[dirIdx]
        if graph[newY][newX]:
            dfs(newY, newX)


# 0. 입력 및 초기화
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[False] * MAX for _ in range(MAX)]

    # 1. 그래프 정보 입력
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y + 1][x + 1] = True

    # 2. 방문하지 않은 지점부터 dfs 돌기
    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if graph[i][j]:
                dfs(i, j)
                answer += 1
    print(answer)