import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
res = [[0 for _ in range(m)] for _ in range(n)]
res[0][0] = 1
visited = [[False for _ in range(m)]for _ in range(n)]
visited[0][0] = True
queue = deque()
queue.append((0,0))
while queue:
    cur_y, cur_x = queue.pop()
    for y,x in zip((0,0,1,-1),(-1,1,0,0)):
        next_y,next_x = (cur_y + y, cur_x + x)
        if 0 <= next_y < n and 0 <= next_x < m:
            if arr[cur_y][cur_x] > arr[next_y][next_x]:
                if not visited[next_y][next_x]:
                    queue.append((next_y,next_x))
                    visited[next_y][next_x] = True
                res[cur_y][cur_x] += res[next_y][next_x]
print(*res)

