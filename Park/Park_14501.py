N = int(input())
arr = []

for _ in range(N):
    time, money = map(int, input().split())
    arr.append((time, money))

dp = [0] * (N+1)    # ㅋㅋ 얘가 문제였음ㅋ 와하학...^^ N+1까지 해줌으로써... 제일 마지막것까지 계산하도록...^^

for i in range(N+1):
    for j in range(i):
        dp[i] = max(dp[i], dp[j])

        if arr[j][0] + j <= i:
            dp[i] = max(dp[i], dp[j]+arr[j][1])

print(max(dp))
