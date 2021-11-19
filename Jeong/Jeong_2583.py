import sys
from collections import deque
input = sys.stdin.readline
m,n,k = map(int,input().split())
paper = [[1 for _ in range(n)] for _ in range(m)]
def bfs(start):
    queue = deque()
    queue.append(start)
    cnt = 1
    while queue:
        cur_x, cur_y = queue.pop()
        for dx,dy in zip((0,0,1,-1),(1,-1,0,0)):
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < m and 0 <= next_y < n:
                if paper[next_x][next_y]:
                    queue.append((next_x,next_y))
                    paper[next_x][next_y] = 0
                    cnt += 1
    return cnt

res = []
area_cnt = 0
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            paper[y][x] = 0

for i in range(m):
    for j in range(n):
        if paper[i][j]:
            area_cnt += 1
            paper[i][j] = 0
            res.append(bfs((i,j)))
            
print(area_cnt)
print(*sorted(res))
