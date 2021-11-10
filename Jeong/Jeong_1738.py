import sys
input = sys.stdin.readline
n,m = map(int,input().split())
MAX = 1234567890

def print_path(s,t,path):
    if path[s][t] == MAX:
        return
    print_path(s,path[s][t],path) #s에서 t사이의 지나는 점 K까지의 경로를 출력한다.
    res.append(path[s][t])
    print_path(path[s][t],t,path) #k에서 t까지의 경로를 출력한다.

def floyd(graph):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                #경유하는 노드 까지의 경로가 존재하지 않으면 뛰어 넘는다. 
                # 만약 뛰어넘지 않으면, 해당 경로가 존재하지 않음에도 path에 경로가 존재하는 것처럼 저장된다. 
                if (graph[i][j] > graph[i][k] + graph[k][j]) and (graph[i][k] != MAX and graph[k][j] != MAX):
                    graph[i][j] = graph[i][k] + graph[k][j]
                    path[i][j] = k
            
graph = [[MAX for _ in range(n)] for _ in range(n)]
path = [[MAX for _ in range(n)] for _ in range(n)] # 거리와 똑같이 초기화 해준다.

for _ in range(m):
    u,v,w = map(int,input().split())
    #가중치를 음수로 만들어 저장한다. 최소 가중치를 구하는 것이 유리하기 때문이다.
    graph[u-1][v-1] = -w

floyd(graph)

cycles = list(filter(lambda x: x if graph[x][x] < 0 else False, range(n))) #대각 행렬의 값이 0보다 작은 노드를 검사해 사이클에 포함되는 점들을 찾는다.
is_cycle = [True for c in cycles if graph[0][c] < MAX and graph[c][n-1] < MAX] #시작점,끝점과 연결된 사이클인지 검사한다.

if graph[0][n-1] == MAX or is_cycle: #연결되지 않았거나 음의 사이클이 시작점 ,끝점 사이에 존재한다면, 돈을 줍느라 끝점에 다다르지 못한다.
    print(-1)

else: 
    res = [0] #경로를 초기화
    print_path(0,n-1,path) #시작점과 끝점을 제외한 경로를 저장해준다.
    res += [n-1] #경로에 끝점을 추가
    print(*[i+1 for i in res]) 
