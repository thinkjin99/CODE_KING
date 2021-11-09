import sys
input = sys.stdin.readline
n,w = map(int,input().split())
p = [0 for _ in range(n+1)]
for i in range(1,n+1):
    p[i] = tuple(map(int,input().split()))
    
dp = [[0 for _ in range(w+1)] for _ in range(n+1)] #w가 0인 경우도 고려해줘야 한다.
for i in range(1, n+1):
    for j in range(1, w+1):
        if j < p[i][0]: #무게 수용 능력을 초과하면 물건을 담을 수 없다.
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-p[i][0]] + p[i][1])

print(dp[n][w])

