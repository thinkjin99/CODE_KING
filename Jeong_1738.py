import sys
input = sys.stdin.readline
n,m = map(int,input().split())
MAX = 1234567890

def print_path(s,t,path):
    if path[s][t] == MAX:
        return
    print_path(s,path[s][t],path) #s에서 t사이의 지나는 점 K까지의 경로를 출력한다.
    print(path[s][t],end=' ')
    print_path(path[s][t],t,path) #k에서 t까지의 경로를 출력한다.

def floyd(graph):
    for k in range(n):
        for i in range(n):
            for j in range(n): 
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    path[i][j] = k
            

graph = [[MAX for _ in range(n)] for _ in range(n)]
path = [[MAX for _ in range(n)] for _ in range(n)] # 거리와 똑같이 초기화 해준다.

for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u-1][v-1] = -w

floyd(graph)
for i in graph:
    print(i)
if graph[0][n-1] == MAX:
    print(-1)
else: print_path(0,n-1,path)