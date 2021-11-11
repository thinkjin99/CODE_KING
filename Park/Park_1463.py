X = int(input())

dp = [10**6 for _ in range(X+1)]  # 모든 경우에 대해 다 구하기 

dp[0] = 0
dp[1] = 0

for i in range(2, X+1):
    temp3 = 10**6
    temp2 = 10**6
    temp1 = 10**6

    if i%3 == 0:
        temp3 = dp[i//3]+1
    if i%2 == 0:
        temp2 = dp[i//2]+1
    temp1 = dp[i-1]+1

    getMin = [temp1, temp2, temp3]
    dp[i] = min(getMin)

print(dp[X])
