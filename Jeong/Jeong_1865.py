import sys
def update_distance(graph,distance,cycle = False):
    for u in range(1,n+1):
        for v,w in graph[u]:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                if cycle: return True

    return False

def bellman_ford(graph):
    distance = [123456789 for _ in range(n+1)]
    distance[1] = 0
    for _ in range(1,n):
        update_distance(graph,distance)

    return  update_distance(graph,distance,True)

t = int(input())
for _ in range(t):
    input = sys.stdin.readline
    n,m,h = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
        
    for _ in range(h):
        w_u,w_v,w_w = map(int,input().split()) #웜홀의 정보
        graph[w_u].append((w_v,-w_w))

    res = "YES" if (bellman_ford(graph)) else "NO"
    print(res)

