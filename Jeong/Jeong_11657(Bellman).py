import sys
input = sys.stdin.readline
n,m = map(int,input().split())
MAX = 123456789
weight = [[MAX for _ in range(n)] for _ in range(n)]
for _ in range(m):
    u,v,w = map(int,input().split())
    weight[u - 1][v - 1] = min(w, weight[u - 1][v - 1])
    
        
distance = [MAX] * (n) 
nodes = [0]
distance[0] = 0
for i in range(n):
    next_nodes = set()
    while nodes:
        current = nodes.pop()
        for v, w in enumerate(weight[current]):
            if (distance[current] + w) < distance[v]:
                if i == n - 1: 
                    print(-1)
                    exit(0)
                distance[v] = distance[current] + w
                next_nodes.add(v)
    nodes = list(next_nodes)

for r in distance[1:]:
    if r == MAX:
        print(-1)
    else:
        print(r)