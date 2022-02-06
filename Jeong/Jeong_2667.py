import sys
input = sys.stdin.readline
n = int(input())
map_ = [list(map(int, input().rstrip())) for _ in range(n)]
def dfs(row, col, cnt):
    map_[row][col] = 0
    for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        nr, nc = row + dr, col + dc
        if (0 <= nr < n) and (0 <= nc < n):
            if map_[nr][nc]:
                cnt = dfs(nr, nc, cnt + 1)
    return cnt
town_cnts = []
for i in range(n):
    for j in range(n):
        if map_[i][j]:
            town_cnts.append(dfs(i,j,1))
print(len(town_cnts))
for cnt in sorted(town_cnts):
    print(cnt)
