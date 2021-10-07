n = int(input())
dp = [1,3,5]
fibo = lambda x: [x[1], x[2], 2 * x[1] + x[2]]
for i in range(4,n+1):
    dp = fibo(dp)
if n <= 3:
    print(dp[n-1])
else: print(dp[-1])