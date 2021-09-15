n = int(input())
dp = [0 for _ in range(n + 1)]
dp[0] = 0; dp[1] = 1; dp[2] = 1
for i in range(6,n + 1):
    dp[i - 3] = dp[i - 4] + dp[i - 5]
    dp[i - 2] = dp[i - 3] + dp[i - 5]
    dp[i - 1] = dp[i - 3] + dp[i - 4]
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] 

print(dp)