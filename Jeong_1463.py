import sys
n = int(sys.stdin.readline())
MAX = 1000000
dp = [0 for _ in range(n+1)]
for i in range(2,n+1):#1의 경우 0번 연산이 필요하므로 1부터 시작한다.
    three_multiple,two_multiple = MAX,MAX
    #2와 3의 공배수가 존재할 경우 둘다 비교 해줘야만 한다. 30의 경우를 생각해보자
    if i % 3 == 0:
        three_multiple = dp[i // 3] + 1
    if i % 2 == 0:
        two_multiple = dp[i // 2] + 1
    before = dp[i-1] + 1
    #3으로 나누는 경우, 2로 나누는 경우, -1을 하는 경우 중 최선의 경우를 탐색한다.
    dp[i] = min([before,three_multiple,two_multiple])
print(dp[n])