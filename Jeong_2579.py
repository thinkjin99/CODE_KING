import sys
input = sys.stdin.readline
n = int(input())
stairs = [int(input()) for _ in range(n)]
dp = [0 for _ in range(len(stairs))]
dp[0] = stairs[0]
if n > 1:
    dp[1] = stairs[0] + stairs[1] 
if n > 2:
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

def top_down(n):
    if n < 3 or dp[n] != 0:
        return dp[n]
    #1이 연속으로 3개 존재하는 경우를 제외하고 n번째 계단에 도착하는 경우는 두 가지이다.
    #(n-2 + n) or (n-3 + n-1 + n) 1이 연속으로 3개 존재하지 않으려면 모든 계단을 위의 식에 따라 방문해야 한다.
    #두가지 방법중 가중치가 더 큰 방법이 해당 계단을 방문하는 최선의 수가 된다.
    dp[n] = max((top_down(n - 3) + stairs[n-1] + stairs[n]),(top_down(n - 2) + stairs[n]))
    return dp[n]
top_down(n-1)
print(dp[n-1])

