N = int(input())
arr = list(map(int, input().split()))

dp = [float("inf")] * N

for i in range(N-1, -1, -1):    # 뒤에서부터 검색 시도
    if i + arr[i] >= N-1:   # 만약 나만 밟았는데 끝까지 도달한다 하면
        dp[i] = 1   # 한 번에 끝이니깐!
        continue

    for j in range(1, arr[i]+1):    # 내가 건너뛸 수 있는 블록 수
        if i+j >= N-1:  # 내 다음 거 밟았는데 종료지점 도달하면
            dp[i] = dp[i]+1 # 내 거 + 1만 하면 종료되잖아
            break
        dp[i] = min(dp[i+j]+1, dp[i])   # 내 다음 거 밟아봤을 때 제일 최소 구하기 위해

# 첫 번째 블록은 무조건 밟아야 하는데,
# 거기서 넘어가는 블록의 dp가 inf면 더이상 갈 길이 없다는 거니깐...~
# 그거 체크 위함. 
cnt = 0
for i in range(arr[0]):
    if dp[i] == float("inf"):
        cnt+=1

if N == 1:  # 거리가 1이면 무슨 값이 들어와도 성공임
    print(0)
elif cnt == arr[0]:
    print(-1)
else:
    print(dp[0])
