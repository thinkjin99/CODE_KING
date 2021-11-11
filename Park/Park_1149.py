N = int(input())

arr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)

calc = [[0] * 3 for _ in range(N)]  # 각각 그다음을 R, G, B로 택했을 때의 arr. 3xN차원.
for i in range(3):
    calc[0][i] = arr[0][i]  # 첫 번째 값 넣어줌

for i in range(1, N):   # 이전 거에서 더 작은 값 + arr에서 뽑아오는 각 값
    calc[i][0] = min(calc[i-1][1], calc[i-1][2]) + arr[i][0]
    calc[i][1] = min(calc[i-1][0], calc[i-1][2]) + arr[i][1]
    calc[i][2] = min(calc[i-1][0], calc[i-1][1]) + arr[i][2]
    
minn = min(calc[N-1][0], calc[N-1][1])
minn = min(minn, calc[N-1][2])
print(minn)
