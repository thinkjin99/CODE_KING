from collections import deque
import sys
MAX = 25001
input = sys.stdin.readline
n,m = map(int,input().split())
adj_graph = [[MAX for _ in range(n)] for _ in range(n)]

for _ in range(m):
    u,v = map(int,input().split())
    adj_graph[u-1][v-1] = 1

def bfs(start):
    queue = deque([start])
    visited = [False for _ in range(n)]
    while queue:
        u = queue.popleft()
        for i,v in enumerate(adj_graph[u]):
            if not visited[i] and v != MAX:
                queue.append(i)
                visited[i] = True
    
    for i,v_ in enumerate(visited):
        if v_:
            adj_graph[start][i] = 1

for i in range(n):
    bfs(i)

res = 0
for i in range(n):
    is_possible = True
    for j in range(n):
        if adj_graph[i][j] ==  MAX and i != j:
            if adj_graph[j][i] == MAX:
                is_possible = False
                break
    res = res + 1 if is_possible else res
print(res)


    