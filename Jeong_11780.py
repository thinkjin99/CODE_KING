import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
MAX = 1234567890

def print_path(s,t):
    short_path = []
    via = s
    while via != t:
        short_path.append(via)
        via = path[via][t]

    return short_path + [t]
    

def floyd(graph):
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                # 경유하는 노드 까지의 경로가 존재하지 않으면 뛰어 넘는다. 
                # 만약 뛰어넘지 않으면, 해당 경로가 존재하지 않음에도 path에 경로가 존재하는 것처럼 저장된다. 
                if (graph[i][j] > graph[i][k] + graph[k][j]) and (graph[i][k] != MAX and graph[k][j] != MAX):
                    graph[i][j] = graph[i][k] + graph[k][j]
                    path[i][j] = path[i][k]
      

graph = [[MAX for _ in range(n+1)] for _ in range(n+1)]
path = [[MAX for _ in range(n+1)] for _ in range(n+1)] # 거리와 똑같이 초기화 해준다.

for _ in range(m):
    u,v,w = map(int,input().split())
    #가중치를 음수로 만들어 저장한다. 최소 가중치를 구하는 것이 유리하기 때문이다.
    graph[u][v] = min(graph[u][v],w)
    path[u][v] = v

for i in range(1,n + 1): graph[i][i] = 0

floyd(graph)

for g in graph[1:]:
    print(*list(map(lambda x: 0 if x == MAX else x, g[1:])))
            

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] != MAX and graph[i][j] != 0:
            res = print_path(i,j) 
            print(len(res),*res)
        else:
            print(0)