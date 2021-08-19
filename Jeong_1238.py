import sys
import heapq
input = sys.stdin.readline
n,m,x = map(int,input().split())
MAX = n * 1000
graph = [[] for _ in range(n)]
revers_g = [[] for _ in range(n)]

def djikstra(graph,start):
    dist = [MAX for _ in range(n)]
    min_heap = [start]; dist[start] = 0
    while min_heap:
        current = heapq.heappop(min_heap)
        for v,w in graph[current]:
            next_weight = w + dist[current]
            if next_weight < dist[v]:
                dist[v] = next_weight
                heapq.heappush(min_heap,v)
    return dist

for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u-1].append((v-1, w))
    revers_g[v-1].append((u-1, w))
#extend는 1차원의 형태로 연결 append는 다 차원의 형태로 연결해준다.
#n이 1000이상이면 플로이드 와샬 사용불가하다.
res = 0
for to_x, from_x in zip(djikstra(graph, x-1),djikstra(revers_g, x-1)): #시작점과 끝점이 명확하므로 두번의 다익스트라 만으로 값을 찾을 수 있다.
    res = max(res,to_x + from_x)

print(res)