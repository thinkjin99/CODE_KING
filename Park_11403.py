N = int(input())

arr = [list(map(int, input().split())) for i in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if arr[j][i] and arr[i][k]:
                arr[j][k] = 1

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=" ")
    print()
