import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline
# code reference: https://deep-learning-study.tistory.com/596
def prim(graph, start_node):
    visited[start_node] = True # 방문 갱신
    candidate = graph[start_node] # 인접 간선 추출
    heapq.heapify(candidate) # 우선순위 큐 생성
    edge_cnt, mst_weight = 0,0 # 전체 가중치
    min_weights = [float('inf') for _ in range(n+1)]
    min_weights[1] = 0
    while candidate:
        weight, _, v = heapq.heappop(candidate) # 가중치가 가장 적은 간선 추출
        if not visited[v]: # 방문하지 않았다면
            visited[v] = True # 방문 갱신
            mst_weight += weight # 전체 가중치 갱신
            edge_cnt += 1

            for w,u,v in graph[v]: # 다음 인접 간선 탐색
                if visited[v] == 0 and min_weights[v] > w: # 방문한 노드가 아니라면, (순환 방지)
                    heapq.heappush(candidate, (w,u,v)) # 우선순위 큐에 edge 삽입
                    min_weights[v] = w
        
        if edge_cnt == n - 1: break
    return mst_weight

while True:
    n, m = map(int,input().split()) # 노드 수, 간선 수
    if (n,m) == (0,0): break
    graph = defaultdict(list) # 빈 그래프 생성
    visited = [0] * (n+1) # 노드의 방문 정보 초기화
    total_weight = 0

    # 무방향 그래프 생성
    for i in range(m): # 간성 정보 입력 받기
        u, v, weight = map(int,input().split())
        graph[u].append((weight, u, v))
        graph[v].append((weight, v, u))
        total_weight += weight

    print(total_weight - prim(graph,1))