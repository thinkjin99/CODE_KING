n = int(input())
fibo_dp = [1,1,2]
LEFT_OVER = 10007
while n > 2:
    fibo_dp = [fibo_dp[1] % LEFT_OVER, fibo_dp[2] % LEFT_OVER, (fibo_dp[1] + fibo_dp[2]) % LEFT_OVER]
    n -= 1
print(1) if n < 2 else print(fibo_dp[-1])