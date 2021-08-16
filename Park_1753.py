from heapq import heappush, heappop
# 시간 줄이기 위해서...
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

arr = [[] for i in range(V+1)]  # 입력받은 내용 저장할 배열

for i in range(E):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))   # 인접 리스트 형식? a 자리에 (end vertex, distance) 형태로 저장
    
res = [int(1e9) for i in range(V+1)]    # 큰 값으로 최종 계산한 거리 배열 초기화
pq = []
heappush(pq, (0, K))    # python에서의 최소힙에 (distance, vertex) 형태로 저장

res[K] = 0  # 나!는 최단거리가 0이지~
while pq:
    dist, vertex = heappop(pq)  # 힙에서 하나씩 빼오기

    if res[vertex] < dist:  # 만약 저장된 거리가 충분히 작으면 걍 넘김
        continue

    for next_vert, d in arr[vertex]:    # 그 다음의 vertex와 거리 받아오기
        next_dist = d + res[vertex] # 새로운 거리 계산. 이전에 저장된 내용에 새로운 거리 더해서 새로운 루트? 만들어냄

        if next_dist < res[next_vert]:  # 새로 만든 방법? 루트가 더 짧으면
            res[next_vert] = next_dist  # update 시켜주고
            heappush(pq, (next_dist, next_vert))    # heap에 넣어줌

# 출력
for i in range(1, V+1):
    if res[i] == int(1e9):
        print("INF")
    else:
        print(res[i])
