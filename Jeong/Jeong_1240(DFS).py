import sys
def dfs(current,target,distance):
    if current == target:
        return distance
    visit[current] = True
    for v,w in graph[current]:
        if not visit[v]:
            res = dfs(v,target,distance + w)
            if res:
                return res
                
n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    start,end,weight = map(int,sys.stdin.readline().split())
    graph[start].append((end,weight))
    graph[end].append((start,weight))


for _ in range(m):
    visit = [False for _ in range(n+1)]
    current,target = map(int,sys.stdin.readline().split())
    print(dfs(current,target,0))


