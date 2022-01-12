def fibo(n):
    if dp[n]:
        return dp[n]
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]
n = int(input())
vip_seat = [0] + [int(input()) for _ in range(int(input()))] + [n + 1]
seat_counts = [vip_seat[i] - vip_seat[i-1] - 1 for i in range(1,len(vip_seat))]
dp = [0,1,1] + [0] * 39
fibo(max(seat_counts) + 1) #fibo problem
ans = 1
for f in map(lambda x: dp[x+1], seat_counts):
    ans *= f
print(ans)