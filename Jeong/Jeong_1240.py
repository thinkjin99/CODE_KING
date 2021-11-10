import heapq  # 우선순위 큐 구현을 위함
import sys
def dijkstra(graph, start):
    node_distances = [987654321 for _ in range(n+1)]  # start로 부터의 거리 값을 저장하기 위함
    node_distances[start] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue,(start,node_distances[start]))  # 시작 노드부터 탐색 시작 하기 위함.

    while queue: 
        current_destination,current_distance = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.
        if node_distances[current_destination] < current_distance: continue # 기존에 있는 거리보다 길다면, 볼 필요도 없음
        for new_destination, new_distance in graph[current_destination]:
            distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리 
            if distance < node_distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                node_distances[new_destination] = distance #경유해서 이동하는 것이 더 빠를 경우 업데이트 해준다
                heapq.heappush(queue,(new_destination,distance))  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    
    return node_distances

n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append((v,w))    
    graph[v].append((u,w)) #연결관계를 명확히 나태줘야 하기에 양방향 그래프로 생성한다.


res = []
for i in range(n + 1):
    res.append(dijkstra(graph,i))

for _ in range(m):
    start,end = map(int,sys.stdin.readline().split())
    print(res[start][end])

