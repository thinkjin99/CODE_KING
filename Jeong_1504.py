import sys
import heapq
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n)]
MAX = 1000000
def djikstra(start):
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
    graph[u-1].append((v-1,w))
    graph[v-1].append((u-1,w))

"""이미 지나온 정점이나 간선을 또 지날 수 있기 때문에 다익스트라를 분할해서 적용해주면 된다."""

v_n = [int(i)-1 for i in input().split()]
v_1_2 = djikstra(v_n[0])[v_n[1]] #V_1에서 V_2까지의 거리
res = MAX
for i in range(len(v_n)):
    v_1 = djikstra(0)[v_n[i]] #시작점에서 지나야 하는 점 중 하나인 V_1까지의 최단거리
    v_2 = djikstra(v_n[-1+i])[n-1] #V_2에서 끝점 까지의 최단거리
    if (v_1 >= MAX or v_1_2 >= MAX or v_2 >= MAX) and res == MAX:
        res = MAX
        continue
    res = min(res, v_1 + v_1_2 + v_2)

if res == MAX:
    print(-1)

else: print(res)
