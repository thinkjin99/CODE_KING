import sys
input = sys.stdin.readline
N,m = map(int,input().split())
matrix = [[int(i) for i in input().split()] for _ in range(N)]
querys = [[int(i) for i in input().split()] for _ in range(m)]
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + matrix[i][j]

for q in querys:
    s_row, s_col, e_row, e_col = q
    base = dp[e_row][e_col]
    delta = dp[s_row-1][e_col] + dp[e_row][s_col-1] - dp[s_row-1][s_col-1]
    print(base - delta)
