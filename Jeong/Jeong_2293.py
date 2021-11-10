m,n = [*map(int,input().split())]
coins = [int(input()) for _ in range(m)]
dp = [0] * (n + 1)
dp[0] = 1
for i in range(m):
    for j in range(coins[i], n + 1):
        #중복 처리를 위해 coins[i]의 인덱스부터 시작한다.  
        dp[j] += dp[j-coins[i]]
print(dp[-1])

