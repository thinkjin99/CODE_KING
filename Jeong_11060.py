n = int(input())
jumps = [int(i) for i in input().split()]
MAX = 1001
dp = [MAX] * n
dp[0] = 0
for i in range(n):
    for j in range(1, jumps[i] + 1): #0칸 점프는 제자리 점프
        if i + j < n:
            dp[i+j] = min(dp[i+j], dp[i] + 1) #각 위치까지 도달할 수 있는 최소 점프수를 구한다.
        else: 
            break
    if dp[-1] != MAX: break #마지막 값까지 도달하는 점프 수를 구하면 종료한다.

print(-1) if dp[-1] == MAX else print(dp[-1])
