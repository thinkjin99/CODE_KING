import sys
sys.setrecursionlimit(100000) #없으면 recursion error 발생

def dfs(y, x, cnt):
    arr[y][x] = 1   # 방문 처리
    for dx, dy in d:
        Y, X = y+dy, x+dx
        # 벽에 닿지 않고 방문하지 않은 곳이라면
        if(0 <= Y < M) and (0 <= X < N) and arr[Y][X] == 0:
            cnt = dfs(Y, X, cnt+1)  # 계속 방문
    return cnt


M, N, K = map(int, input().split())

arr = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

res = []

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:  # 방문하지 않은 곳에서
            res.append(dfs(i, j, 1))    # 진행

print(len(res)) # 총 몇 개의 영역
print(*sorted(res)) # 각 영역의 크기. res 배열 안에 각 영역의 크기 들어있음.
