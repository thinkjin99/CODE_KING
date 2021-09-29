from sys import stdin
n = int(stdin.readline())
dp = [0 for _ in range(n+1)]
time_money = [tuple(map(int,stdin.readline().split())) for _ in range(n)]
max_before = 0
for d in range(n):
    next_date = d + time_money[d][0]
    next_money = time_money[d][1]
    if max_before < dp[d]: #값이 초기화 되지 않는 경우 이전의 최대값이 곧 해당 값의 최대값이 된다.
        max_before = dp[d] #만약 현재의 값이 더 크다면 값을 업데이트 해준다.
    else: dp[d] = max_before
    if next_date <= n:
        dp[next_date] = max(next_money + dp[d], dp[next_date])
print(max(dp))