from heapq import heappush, heappop

N, E = map(int, input().split())

arr = [[] for i in range(N+1)]

def Dijkstra(start):
    global arr

    res = [float("inf") for i in range(N+1)] 
    pq = []
    heappush(pq, (0, start))
    res[start] = 0

    while pq:
        dist, vertex = heappop(pq)
        
        if res[vertex]<dist:
            continue

        for next_vert, d in arr[vertex]:
            next_dist = d + res[vertex]

            if next_dist < res[next_vert]:
                res[next_vert] = next_dist
                heappush(pq, (next_dist, next_vert))

    return res


for i in range(E):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

v1, v2 = map(int, input().split())

from1 = Dijkstra(1)
fromv1 = Dijkstra(v1)
fromv2 = Dijkstra(v2)
    
temp1 = from1[v1] + fromv1[v2] + fromv2[N]
temp2 = from1[v2] + fromv2[v1] + fromv1[N]

res = min(temp1, temp2)
if(res == float("inf")):
    print(-1)
else:
    print(res)

