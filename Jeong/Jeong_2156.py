import sys
input = sys.stdin.readline
n = int(input())
glass = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]
dp[0] = glass[0]

if n > 1:
    dp[1] = glass[0] + glass[1]

if n > 2:
    dp[2] = max(glass[0] + glass[1] ,glass[0] + glass[2], glass[1] + glass[2]) 

for i in range(3,n):
    #굳이 i번째 잔의 포도주를 먹을 필요는 없다. 핵심은 최대 값을 찾는 일이다.
    dp[i] = max((dp[i-3] + glass[i-1] + glass[i]), dp[i-2] + glass[i],dp[i-1])

print(dp[n-1])
