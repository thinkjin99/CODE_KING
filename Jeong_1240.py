import sys
sys.setrecursionlimit(10**6)
def floyd_warshall(n, edges):
    # 그래프 정보를 담을 인접행렬, 거리는 무한대로 초기화
    adj = [[float('inf')] * (n+1) for _ in range(n+1)] 
    
    # 인접행렬에 그래프 정보 저장 (정점 u -> v 거리 w)
    for u, v, w in edges:
        adj[u][v] = w
    
    # k : 경유지 (각 정점들을 경유지로 설정)
    for k in range(1, n+1):
        for i in range(1, n):
            for j in range(i + 1, n+1):
            	# 정점 i -> j로 갈 때 기존 거리값과 k를 거쳐갈 때의 거리 값 중 작은 값을 저장
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
                adj[j][i] = adj[i][j]

    return adj

edges = []
n,m = map(int,sys.stdin.readline().split())
for _ in range(n - 1):
    u,v,w = map(int,sys.stdin.readline().split())
    edges.append([u,v,w])
    edges.append([v,u,w])

res = floyd_warshall(n,edges)
for _ in range(m):
    start,end = map(int,sys.stdin.readline().split())
    print(res[start][end])