N, M = map(int, input().split())
# 초기에는 infinite한 값 넣ㅇㅓ둠
arr = [[float("inf") for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            # 더 작은 값 넣어주깅
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

# 자기 자신은 빼줘!
for i in range(N):
    arr[i][i] = 0

sums = []
for i in range(N):
    sums.append(sum(arr[i]))

print(sums.index(min(sums))+1)
    
