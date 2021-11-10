import sys
input = sys.stdin.readline
t = int(input())
dp = [[0 for _ in range(4)] for _ in range(100001)]
dp[1][1] = 1
dp[2][2] = 1
dp[3][3] = 1
dp[3][1] = 1
dp[3][2] = 1
max_last = 3
for _ in range(t):
    n = int(input())
    if n > max_last:
        for i in range(max_last + 1,n + 1):
            #각각의 수로 끝나는 경우를 고려해준 뒤 합쳐서 파악한다.
            dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % 1000000009
            dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % 1000000009
            dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % 1000000009
        max_last = n
    print(sum(dp[n]) % 1000000009)