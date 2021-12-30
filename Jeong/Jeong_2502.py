import sys
input = sys.stdin.readline
dp = [0,1,1] + [0] * 28
def fibo(n):
    if dp[n]:
        return dp[n]
    if n > 2:
        dp[n] = (fibo(n-1) + fibo(n-2))
        return dp[n]
N,m = map(int,input().split())
fibo(N)
a, b = dp[N-2], dp[N-1] #a는 b보다 클 수 없다.
i = 1
while True:
    k = (m - i * a)
    if k % b == 0:
        j = k // b
        print(f'{i}\n{j}')
        break
    i += 1