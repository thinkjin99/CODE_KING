import sys
input = sys.stdin.readline
def dfs(row):
    visited[row] = 1
    for i,v in enumerate(graph[row]):
        if v != '0':
            if visited[i] == 0: #사이클을 만드는 경우 확인
                dfs(i)
            path_set.add(i)
    return

n = int(input())
graph = [input().split() for _ in range(n)]
for r in range(n):
    path_set = set()
    visited = [0 for _ in range(n)]
    dfs(r)
    for s in path_set:
        graph[r][s] = '1'
        
for g in graph:
    print(" ".join(g))






