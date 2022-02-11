import sys
from itertools import accumulate
input = sys.stdin.readline
MAX = 123456789
for _ in  range(int(input().rstrip())):
    N = int(input().rstrip())
    costs = list(map(int, input().split()))
    dp = [[MAX if i != j else 0 for j in range(N)] for i in range(N)]
    accu_sum = list(accumulate(costs))
    for length in range(1, N): #결합한 장의 수
        for start in range(N - length):#시작 위치
            end = start + length #끝나는 지점
            for k in range(start, end): #k는 분할 포인트를 말한다.
                current = accu_sum[end] - accu_sum[start] + costs[start]
                dp[start][end] = min(dp[start][end], dp[start][k] + dp[k+1][end] + current)
    print(dp[0][N-1])
''' 반복문은 대각선을 기준으로 반복한다. 그래야 점화식을 풀어내는 것이 가능키 때문이다'''