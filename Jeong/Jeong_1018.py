import sys
input = sys.stdin.readline
n, m = map(int,input().split())
chess_map = [[s for s in input().rstrip()] for _ in range(n)]
res = 999999
for i in range(n - 7):
    for j in range(m - 7):
        wb_cnt, bw_cnt = (0, 0)
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if chess_map[k][l] != 'W' : wb_cnt += 1
                    if chess_map[k][l] != 'B' : bw_cnt += 1
                else:
                    if chess_map[k][l] != 'B': wb_cnt += 1
                    if chess_map[k][l] != 'W': bw_cnt += 1
        min_temp = min(wb_cnt, bw_cnt)
        res = min_temp if min_temp < res else res
print(res)