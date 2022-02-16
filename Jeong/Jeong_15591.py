import sys
from collections import deque
input = sys.stdin.readline
MAX = 123456789
n,m = map(int,input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u,v,w = map(int,input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

for _ in range(m):
    ans = 0
    k, start = map(int,input().split())
    visited = [False] * (n + 1)
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        visited[cur] = True
        for v,w in graph[cur]:
            if (not visited[v] and w >= k):
                queue.append(v)
                ans += 1
    print(ans)