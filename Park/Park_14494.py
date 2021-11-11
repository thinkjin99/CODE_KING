n, m = map(int, input().split())

arr = [[0 for _ in range(m)] for _ in range(n)]

arr[0][0] = 1

for i in range(n):
    for j in range(m):
        if i-1>=0: # 왼쪽에서
            arr[i][j] += arr[i-1][j]
        if j-1>=0: # 위에서
            arr[i][j] += arr[i][j-1]
        if i-1>=0 and j-1>=0: # 왼쪽 위에서
            arr[i][j] += arr[i-1][j-1]

print(arr[n-1][m-1] % 1000000007)
