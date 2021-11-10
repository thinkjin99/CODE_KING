import sys
input = sys.stdin.readline
n = int(input())
rgb_map = [None for _ in range(n + 1)]
dp = [[0 for _ in range(3)] for _ in range(n+1)]
for i in range(1,n + 1):
    r,g,b = map(int,input().split())
    rgb_map[i] = [r,g,b]

dp[1] = rgb_map[1][::]

for i in range(2, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb_map[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb_map[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb_map[i][2]

print(min(dp[n]))