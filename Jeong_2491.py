n = int(input())
arr = [int(i) for i in input().split()]
dp = [1 for _ in range(n)]
min_dp = [1 for _ in range(n)]
for i in range(n-1):
    if arr[i] <= arr[i+1]:
        dp[i+1] += dp[i]

    if arr[i] >= arr[i+1]:
        min_dp[i+1] += min_dp[i]
print(max(max(dp),max(min_dp)))