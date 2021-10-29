import sys
import heapq
input = sys.stdin.readline
n,m = map(int,input().split())
INF = float('inf')
graph = [[] for _ in range(n)]
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u-1].append((v-1,w))
    graph[v-1].append((u-1,w))

cur = 0
res = 0
dist = [(0,0)]
node_included = [False] * n
max_edge = 0
for _ in range(n):
    while dist != None:
        w,v = heapq.heappop(dist) #가중치를 기준으로 정렬해야 한다.
        if not node_included[v]: #포함하고 있지 않은 노드 중에서 최소 값을 탐색한다.
            res += w
            cur = v
            node_included[v] = True #포함 처리를 해준다.
            max_edge = max(max_edge,w)
            break #최소 값을 찾았다면 더 이상 반복을 수행할 필요없다.

    for v_,w_ in graph[cur]: #새롭게 연결된 간선들을 초기화 해준다.
        heapq.heappush(dist,(w_,v_))
print(res-max_edge)