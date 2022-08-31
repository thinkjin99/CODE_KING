n = int(input())
dp = [0] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

count = dp[n]
log = []

while n >= 1:
    res = dp[n - 1]
    before  = n - 1
    if n % 2 == 0: 
       if dp[n // 2] < res:
            before = n // 2
    if n % 3 == 0: 
        if dp[n // 3] < res:
            before = n // 3
    
    log.append(n)
    n = before

print(count)
for l in log:
    print(l, end=" ")
