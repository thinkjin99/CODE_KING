import sys
N, M = map(int, sys.stdin.readline().split())

dp = []

for i in range(N):
    usr = list(map(int, sys.stdin.readline().split()))
    mid = 0
    tmpList = []
    for u in usr:
        mid += u
        tmpList.append(mid)
    dp.append(tmpList)  # dp의 각 행에는 이전 열부터 현재 열까지의 sum값 저장됨


for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    res = 0
    for x in range(x1-1, x2):
        res += dp[x][y2-1]
        if y1-2 >= 0:   # y1-2 < 0인 경우는 한 행을 다 쓰는 거임
            res -= dp[x][y1-2]

    print(res)
