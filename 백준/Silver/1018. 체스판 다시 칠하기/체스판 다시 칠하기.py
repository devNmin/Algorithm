# 백준 체스판 다시 칠하기 실4  1018

N, M = list(map(int,input().split()))

board = [list(input()) for _ in range(N)]


def check_color(board, diff_i, diff_j, result):
    # WB
    wb_count = 0
    for i in range(8):
        for j in range(8):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):

                if board[i+diff_i][j+diff_j] != "W":
                    wb_count +=1
            else:
                if board[i+diff_i][j+diff_j] != "B":
                    wb_count +=1

    if wb_count < result:
        result = wb_count  
    # BW
    bw_count = 0
    for i in range(8):
        for j in range(8):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                if board[i+diff_i][j+diff_j] != "B":
                    bw_count +=1
            else:
                if board[i+diff_i][j+diff_j] != "W":
                    bw_count +=1
    if bw_count < result:
        result = bw_count
    return result

result = 2500
max_i = N - 8
max_j = M - 8
for i in range(max_i+1):
    for j in range(max_j+1):
        result = check_color(board, i, j, result)
print(result)