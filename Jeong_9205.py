import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
def bfs(graph):
    visited = [False for _ in range(n + 2)]
    queue = deque([0])
    visited[0] = True
    while queue:
        r = queue.pop()
        for c,w in enumerate(graph[r]):
            if w and not visited[c]:
                if c == n - 1: return 'happy'
                queue.append(c)
                visited[c] = True
    return 'sad'
    
for _ in range(t):
    n = int(input()) + 2
    graph = [[0 for _ in range(n)] for _ in range(n)]
    nodes = [tuple(map(int,input().split())) for _ in range(n)]
    for row,(i_x, i_y) in enumerate(nodes):
        for col,(j_x, j_y) in enumerate(nodes):
            if i_x == j_x and i_y == j_y: continue #자기 자신인 경우 continue
            if abs(i_x - j_x) + abs(i_y - j_y) <= 1000:
                graph[row][col] = 1
    print(bfs(graph))
  

