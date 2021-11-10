import sys
from collections import deque
def bfs(vertax):
    visited = [False for _ in range(n+1)]
    queue = deque()
    queue.append(vertax)
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
                if kevin[vertax][v] == 0:
                    kevin[vertax][v] = kevin[vertax][u] + 1
        visited[u] = True

input = sys.stdin.readline
n,m = map(int,input().split())
kevin = [[0 for _ in range(n+1)] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n):
    if graph[i]:
        bfs(i)

res = float('inf')
ans = 0

for i,s in enumerate(list(map(sum,kevin))):
    if res > s and s != 0:
        res = s
        ans = i
print(ans)




