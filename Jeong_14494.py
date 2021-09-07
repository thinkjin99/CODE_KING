import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [[1 if i == 0 or j == 0 else 0 for j in range(m)] for i in range(n)]
for row in range(1,n):
    for col in range(1,m):
        arr[row][col] = arr[row - 1][col] + arr[row][col - 1] + arr[row - 1][col - 1]

print(arr[n-1][m-1] % 1000000007)


